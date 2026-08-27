# -*- coding: utf-8 -*-
"""Cutaneous Bacterial Infections -- question pool for the Updated CMS derm master exams."""
DECK = "4.  Cutaneous Bacterial Infections.pptx"
IO_A = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing, management, referrals, patient education and prognosis "
        "of cutaneous bacterial infections")
IO_B = ("b — Discuss unique considerations of methicillin-resistant Staphylococcus aureus skin infections, "
        "including risk factors, presentation, and treatment")

def Q(topic, q, opts, c, slide, io=IO_A):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Acne vulgaris",
  "A 15-year-old boy presents with facial lesions. Examination shows open and closed comedones across the forehead "
  "and nose with no papules, pustules, or nodules. What is the most appropriate first-line treatment?",
  [["A topical retinoid",
    "Correct. For comedonal, non-inflammatory acne the guideline is a topical retinoid, which is comedolytic and "
    "anti-inflammatory and normalises the follicular hyperkeratinisation. If it is not tolerated, azelaic acid or "
    "salicylic acid may be substituted."],
   ["A topical retinoid combined with an oral antibiotic",
    "Adding an oral antibiotic is the regimen for moderate papulopustular and mixed acne, and requires inflammatory "
    "lesions to justify it. This patient has none, so the antibiotic has no inflammatory target and adds resistance "
    "risk."],
   ["Oral isotretinoin as monotherapy",
    "Isotretinoin monotherapy is reserved for severe nodular acne or resistant mild disease. It is a potent teratogen "
    "requiring mandatory pregnancy testing and prescriber registration, which is a substantial burden for untreated "
    "comedonal acne."],
   ["Topical benzoyl peroxide alone",
    "Benzoyl peroxide is a first-line drug especially for mild acne and suppresses Cutibacterium acnes, but its role "
    "is antimicrobial and keratolytic rather than primarily comedolytic. The retinoid is the agent named for "
    "comedonal disease."],
   ["An oral contraceptive pill",
    "Oral contraceptives are considered for patients with hyperandrogenism or when acne is unresponsive to both "
    "topical retinoids and antibiotics. They are also not an option for a male patient."]],
  0, 32),

Q("Acne vulgaris",
  "A 17-year-old girl has moderate papulopustular and mixed acne of the face and upper back that has not responded to "
  "eight weeks of a topical antimicrobial. What regimen is recommended?",
  [["A topical retinoid together with an oral antibiotic and topical benzoyl peroxide",
    "Correct. Moderate papulopustular and mixed acne is treated with a topical retinoid and an oral antibiotic and "
    "topical benzoyl peroxide. Benzoyl peroxide is specifically added whenever an antibiotic is used, to reduce the "
    "risk of bacterial resistance."],
   ["A topical retinoid together with an oral antibiotic, without benzoyl peroxide",
    "Two-thirds correct, and the missing third matters: benzoyl peroxide is recommended alongside antibiotic therapy "
    "to reduce resistance. Omitting it is the commonest way a correct-looking regimen goes wrong."],
   ["An oral antibiotic alone continued indefinitely",
    "Oral antibiotics should be prescribed for the shortest time necessary, and monotherapy without benzoyl peroxide "
    "invites resistance in Cutibacterium acnes. It also leaves the follicular hyperkeratinisation untreated."],
   ["A topical retinoid alone",
    "A topical retinoid alone is the regimen for comedonal disease. Moderate inflammatory acne that has already "
    "failed topical therapy needs systemic treatment added."],
   ["Oral isotretinoin as monotherapy",
    "Isotretinoin monotherapy sits alongside the triple regimen for severe nodular acne. Moving to it before trying "
    "the recommended combination escalates past an effective and much safer option."]],
  0, 33),

Q("Acne vulgaris",
  "A 19-year-old woman is to begin oral isotretinoin for recalcitrant nodular acne. What safety requirements apply?",
  [["Negative pregnancy tests are mandatory before starting, monthly during treatment, and five weeks after "
    "completion, with only one month dispensed at a time",
    "Correct. Isotretinoin is a potent teratogen. Negative pregnancy tests are mandatory prior to initiation, "
    "monthly, and 5 weeks post treatment, only one month is dispensed at a time, and providers must be registered."],
   ["A negative pregnancy test before starting only, with no further testing required",
    "A single baseline test leaves the entire treatment course and the washout period unmonitored, which is exactly "
    "the window the monthly and post-treatment testing exists to cover."],
   ["Monthly liver function tests, with no pregnancy testing required",
    "Laboratory monitoring accompanies isotretinoin, but omitting pregnancy testing removes the single most important "
    "safeguard for a potent teratogen in a woman of childbearing age."],
   ["A negative pregnancy test before starting and one week after completion",
    "The post-treatment interval is wrong. Testing is required 5 weeks after treatment, and shortening it to a week "
    "would clear a patient while the drug's teratogenic risk persists."],
   ["No specific requirements, since isotretinoin is used as monotherapy",
    "Monotherapy describes how the drug is combined with others, not how it is monitored. Isotretinoin carries the "
    "strictest prescribing requirements of any acne agent."]],
  0, 30),

Q("Acne vulgaris",
  "A patient starting topical tretinoin and benzoyl peroxide asks how to use them. What education should be given?",
  [["Do not apply the two together; wait at least three hours between them because of the risk of skin irritation",
    "Correct. Topical tretinoin and benzoyl peroxide should not be applied together because of the risk of skin "
    "irritation, and at least three hours should separate them."],
   ["Apply the two together to improve penetration and speed the response",
    "Applying them simultaneously produces the irritation the separation is designed to avoid, and irritation is the "
    "main reason patients abandon topical acne therapy."],
   ["Apply the two together but wash the face vigorously between applications",
    "Vigorous washing is itself discouraged; the advice is to wash no more than twice daily with a gentle cleanser "
    "and warm rather than hot water. This compounds irritation instead of preventing it."],
   ["Use only one of the two, since they cannot be used in the same regimen",
    "They can and often should both be used, just not applied at the same time. Discarding one removes a component of "
    "the recommended regimen."],
   ["Apply both twice daily and expect clearance within one week",
    "Improvement takes 4 to 6 weeks, clinical response is measured by new lesion counts after 6 to 8 weeks, and the "
    "back and chest may take 3 to 4 months. A one-week expectation guarantees perceived failure."]],
  0, 35),

Q("Acne vulgaris",
  "A 24-year-old woman has persistent acne, hirsutism, and irregular menses. What differential diagnosis should be "
  "considered?",
  [["Polycystic ovary syndrome, indicating androgen hypersecretion",
    "Correct. Persistent acne in a hirsute woman with irregular or absent menses indicates androgen hypersecretion, "
    "and polycystic ovary syndrome is the named differential. Signs of hyperandrogenism should be sought during "
    "pre-treatment assessment."],
   ["Rosacea",
    "Rosacea is on the differential but is identified by papules and pustules in the middle third of the face with "
    "telangiectasias, flushing, and an absence of comedones. It does not cause hirsutism or menstrual irregularity."],
   ["Anabolic steroid use",
    "Anabolic steroid use is a recognised cause of acne and should be asked about in the medication history. It would "
    "not typically produce irregular menses with hirsutism in the way endogenous androgen excess does."],
   ["Acne mechanica",
    "Acne mechanica follows pressure on the skin from shoulder pads, orthopaedic casts, or helmets occluding the "
    "pilosebaceous follicle. It is localised to the pressure site and has no endocrine features."],
   ["Perioral dermatitis",
    "Perioral dermatitis produces monomorphic papules around the mouth with sparing of the vermilion border and is "
    "associated with topical corticosteroid use. It has no androgenic association."]],
  0, 17),

Q("Folliculitis",
  "A 28-year-old man presents with an abrupt eruption of small pustules on the thighs and buttocks. Each pustule sits "
  "on an erythematous base and is pierced by a central hair. He is afebrile with no systemic symptoms. He has type 2 "
  "diabetes and wears occlusive workout clothing. What is the most likely causative organism?",
  [["Staphylococcus aureus",
    "Correct. Bacterial folliculitis is most commonly caused by Staphylococcus aureus. His diabetes and occlusive "
    "clothing are both listed risk factors, alongside obesity, poor hygiene, heat and humidity, immunocompromise, "
    "corticosteroids, and nasal carriage."],
   ["Pseudomonas aeruginosa",
    "Pseudomonas aeruginosa causes folliculitis occasionally, classically after exposure to inadequately chlorinated "
    "whirlpools, hot tubs, or water slides. No such exposure is described, and Staphylococcus aureus remains the "
    "commonest cause overall."],
   ["Streptococcus pyogenes",
    "Streptococcus pyogenes is the most common organism in erysipelas and a cause of impetigo and cellulitis. It is "
    "not the characteristic organism of follicular pustules."],
   ["Corynebacterium minutissimum",
    "Corynebacterium minutissimum causes erythrasma, a chronic superficial infection of intertriginous skin that "
    "fluoresces coral-red under a Wood's lamp. It does not produce follicular pustules."],
   ["Candida albicans",
    "Candida albicans is the most common pathogen in chronic paronychia and causes cutaneous candidiasis in moist "
    "occluded sites. A pustule pierced by a central hair is a bacterial follicular lesion."]],
  0, 39),

Q("Pseudomonas folliculitis",
  "A 31-year-old woman develops an itchy pustular eruption two days after using a hotel hot tub. Examination shows "
  "follicular papules and pustules over the trunk, buttocks, and proximal limbs, sparing the face, neck, palms, and "
  "soles. She is afebrile. What is the most appropriate management?",
  [["Reassurance and supportive care, since most cases resolve without specific treatment in 2 to 10 days",
    "Correct. Pseudomonas folliculitis is usually self-limiting and most cases resolve without specific treatment, "
    "clearing in 2 to 10 days. A wet dressing of 5 percent acetic acid may be applied for 20 minutes 2 to 4 times "
    "daily for symptom relief."],
   ["Oral ciprofloxacin for all patients",
    "Ciprofloxacin is reserved for widespread or resistant cases. Prescribing it routinely for a self-limiting "
    "eruption exposes the patient to a fluoroquinolone with no benefit over observation."],
   ["Oral trimethoprim-sulfamethoxazole for probable methicillin-resistant Staphylococcus aureus",
    "That regimen targets methicillin-resistant Staphylococcus aureus, whereas the organism here is a gram-negative "
    "rod acquired from contaminated water. The antibiotic would not cover it."],
   ["Topical mupirocin applied three times daily",
    "Mupirocin is a topical antistaphylococcal agent used for mild bacterial folliculitis and impetigo. It does not "
    "cover Pseudomonas aeruginosa."],
   ["Advise that showering immediately after hot tub use prevents recurrence",
    "Showering after contact with contaminated water specifically does not prevent infection. Prevention depends on "
    "continuous water filtration, frequent monitoring of chlorine levels, and frequent water changes."]],
  0, 52),

Q("Pseudofolliculitis barbae",
  "A 26-year-old Black man reports tender bumps on his neck and jawline that appear after shaving. Examination shows "
  "erythematous papules, several with a visible central hair shaft curving back into the skin. What is the underlying "
  "process?",
  [["A foreign body reaction to hair that has curved back into the follicular wall and re-entered the skin",
    "Correct. Pseudofolliculitis barbae is a foreign body reaction to hair in any shaved area. The cut hair curves "
    "into the follicular wall and penetrates the skin to form a tender red papule or pustule, and it occurs commonly "
    "in Black men because of tightly curled facial hair together with keratin gene variations."],
   ["Bacterial infection of the follicle by Staphylococcus aureus",
    "True bacterial folliculitis is a distinct condition, though secondary infection can complicate "
    "pseudofolliculitis barbae and lead to pustules and abscess formation. The primary process here is mechanical "
    "rather than infective."],
   ["An allergic reaction to shaving products",
    "Allergic contact dermatitis would produce a well-demarcated eruption over the whole area of product contact "
    "rather than discrete papules each containing a re-entrant hair shaft."],
   ["Occlusion of apocrine glands with secondary inflammation",
    "Apocrine gland involvement describes hidradenitis suppurativa, which affects the axilla, groin, breasts, and "
    "perineum with recurrent nodules and sinus tracts rather than the shaved beard area."],
   ["Follicular hyperkeratinisation with increased sebum production",
    "Follicular hyperkeratinisation and increased sebum are two of the four factors in acne vulgaris, whose hallmark "
    "lesion is the comedone. There is no comedone in pseudofolliculitis barbae."]],
  0, 55),

Q("Pseudofolliculitis barbae",
  "What advice about shaving technique is most appropriate for a patient with pseudofolliculitis barbae who cannot "
  "stop shaving entirely?",
  [["Avoid lift-and-cut razor systems and use a single or at most double blade with a mild razor angle",
    "Correct. Patients should avoid lift-and-cut razor systems and look for mild razor angles with single or at most "
    "double blades, because those systems cut the hair below the skin surface where it can re-enter the follicular "
    "wall."],
   ["Use a multi-blade lift-and-cut razor for the closest possible shave",
    "This is precisely the system to avoid. The closer the cut sits below the surface, the more readily the hair "
    "re-enters the skin, which is the mechanism of the disease."],
   ["Shave daily against the direction of hair growth to prevent ingrowth",
    "Shaving against the grain cuts the hair below the surface and worsens the problem. Stopping shaving where "
    "possible is the first recommendation."],
   ["Continue shaving as usual and rely on a topical corticosteroid to control the papules",
    "Mild corticosteroids reduce inflammation and are part of treatment, but relying on them while continuing the "
    "provoking technique treats the consequence and leaves the cause."],
   ["Use a chemical depilatory daily on freshly shaved skin",
    "Chemical depilatories are a shaving alternative rather than an addition, and applying one to freshly shaved "
    "irritated skin increases the irritant burden."]],
  0, 57),

Q("Furuncles and carbuncles",
  "A 40-year-old man has a painful fluctuant nodule 4 mm across on the back of the neck. He is afebrile and it is a "
  "single lesion. What is the most appropriate management?",
  [["Warm compresses without antibiotics",
    "Correct. Warm compresses are usually sufficient for small furuncles, and no antibiotics are given if the patient "
    "is afebrile with a single lesion under 5 mm."],
   ["Warm compresses plus oral cephalexin",
    "Oral antibiotics are indicated if a lesion under 5 mm fails to resolve with drainage, if the lesion is over "
    "5 mm, if cellulitis is expanding, or if the patient is immunocompromised. None of those applies yet, which makes "
    "this the most tempting overtreatment."],
   ["Immediate incision and drainage",
    "Incision and drainage is for large furuncles, with the material cultured to evaluate for methicillin-resistant "
    "Staphylococcus aureus. A 4 mm lesion does not require it as a first step."],
   ["Oral trimethoprim-sulfamethoxazole for presumed methicillin-resistant Staphylococcus aureus",
    "Coverage for methicillin-resistant Staphylococcus aureus is used when it is cultured or suspected. Presuming it "
    "in an afebrile patient with a single small lesion that needs no antibiotic at all is two steps too far."],
   ["Squeezing the lesion to express its contents",
    "Patients are specifically instructed not to squeeze pustules. Doing so risks deeper inoculation and spread."]],
  0, 65),

Q("Furuncles and carbuncles",
  "A 55-year-old man with diabetes presents with an extremely painful lesion on the back of the neck. Examination "
  "shows a deep, indurated plaque with several separate openings draining pus. He has malaise, chills, and a fever of "
  "38.4 degrees Celsius. What is the lesion, and what is the mainstay of therapy?",
  [["A carbuncle, whose mainstay of therapy is incision and drainage",
    "Correct. A carbuncle is two or more confluent furuncles with separate heads, arising in several hair follicles, "
    "and systemic symptoms are more common with a carbuncle than a furuncle. Incision and drainage is the mainstay, "
    "supported by oral antibiotics."],
   ["A furuncle, whose mainstay of therapy is incision and drainage",
    "A furuncle is a deep-seated abscess of a single hair follicle and adjacent subcutaneous tissue, presenting as a "
    "firm tender nodule with a single opening. The multiple separate heads here define a carbuncle."],
   ["A carbuncle, whose mainstay of therapy is oral antibiotics alone",
    "The lesion is identified correctly but antibiotics alone leave the collection undrained. Incision and drainage "
    "is the mainstay, with antibiotics as an adjunct."],
   ["An abscess, whose mainstay of therapy is warm soaks",
    "An abscess arises from traumatic inoculation of bacteria rather than from hair follicles, and warm soaks apply "
    "when a lesion has already drained spontaneously. This lesion arises from confluent follicles."],
   ["Hidradenitis suppurativa, whose mainstay of therapy is topical clindamycin",
    "Hidradenitis suppurativa affects apocrine-bearing skin of the axilla, groin, breasts, and perineum with "
    "recurrence more than twice in six months. The posterior neck is not an apocrine site and this is an acute single "
    "episode."]],
  0, 67),

Q("Hidradenitis suppurativa",
  "A 34-year-old man presents with recurrent painful red nodules and draining lesions in both axillae and the groin. "
  "He has had four such episodes in the past six months and two lesions previously drained. He is obese and smokes. "
  "Examination shows inflamed nodules and several sinus tracts. What three elements establish the diagnosis?",
  [["Typical lesions, characteristic distribution in the axilla and groin, and recurrence more than twice in six "
    "months",
    "Correct. Hidradenitis suppurativa is primarily a clinical diagnosis requiring three key elements: typical "
    "lesions, characteristic distribution in the axilla and groin, and recurrence more than twice in six months. "
    "Biopsy is not usually required."],
   ["Typical lesions, characteristic distribution, and a positive bacterial culture",
    "The first two elements are right, which makes this the closest wrong answer, but the third is recurrence rather "
    "than culture. Hidradenitis suppurativa is an inflammatory process of the apocrine glands rather than a primary "
    "infection, and culture is not part of the diagnostic triad."],
   ["Typical lesions, characteristic distribution, and a biopsy showing follicular occlusion",
    "Biopsy would show follicular occlusion by keratinous material, but it is explicitly not usually required. "
    "Requiring it would make a clinical diagnosis unnecessarily invasive."],
   ["Fever, leukocytosis, and a draining sinus",
    "These are markers of acute infection rather than the diagnostic elements of a chronic recurrent apocrine "
    "inflammatory disease."],
   ["A single episode of axillary abscess with a positive family history",
    "One episode cannot satisfy the recurrence criterion, which is what separates this condition from an isolated "
    "furuncle or abscess."]],
  0, 74),

Q("Hidradenitis suppurativa",
  "A patient with hidradenitis suppurativa asks what she can do herself to reduce flares. Which measure is described "
  "as essential?",
  [["Smoking cessation",
    "Correct. Smoking cessation is described as essential among the preventive measures, alongside avoiding heat "
    "exposure, daily cleansing with an antibacterial soap or chlorhexidine or benzoyl peroxide wash, weight loss if "
    "obese, and avoiding constrictive clothing and frictional trauma."],
   ["Daily vigorous scrubbing of the affected areas",
    "Daily cleansing with an antibacterial soap is recommended, but frictional trauma is specifically to be avoided. "
    "Vigorous scrubbing supplies exactly the friction that provokes lesions."],
   ["Wearing tight-fitting garments to support the affected areas",
    "Constrictive clothing and frictional trauma are among the exposures to avoid. Tight garments worsen the "
    "mechanical component of the disease."],
   ["Applying heat to the axillae daily",
    "Avoiding heat exposure is a listed preventive measure, and hot weather with excessive perspiration is a "
    "predisposing factor."],
   ["Shaving the affected areas daily with a multi-blade razor",
    "Laser hair removal appears among the preventive options, but daily razor shaving of inflamed apocrine-bearing "
    "skin adds trauma rather than reducing it."]],
  0, 75),

Q("Erythrasma",
  "A 58-year-old man with diabetes has an asymptomatic brownish patch in the crural region and scaling between the "
  "fourth and fifth toes. Under a Wood's lamp the affected skin fluoresces coral-red. What is the causative "
  "organism, and what is first-line treatment for localised disease?",
  [["Corynebacterium minutissimum, treated with topical erythromycin or clindamycin",
    "Correct. Erythrasma is a chronic superficial infection of intertriginous skin caused by Corynebacterium "
    "minutissimum invading the upper third of the stratum corneum. Coral-red fluorescence under a Wood's lamp is "
    "diagnostic, and first-line treatment for localised disease is topical erythromycin or clindamycin."],
   ["Corynebacterium minutissimum, treated with oral erythromycin or clarithromycin",
    "The organism is right but oral therapy is reserved for widespread disease. Localised disease is treated "
    "topically, so this over-treats."],
   ["A dermatophyte, treated with topical terbinafine",
    "Tinea cruris and tinea pedis are on the differential and occupy the same sites, which is what makes this "
    "tempting. But dermatophytes do not fluoresce coral-red, and that finding is what settles the diagnosis."],
   ["Candida albicans, treated with topical miconazole",
    "Cutaneous candidiasis is on the differential, and an antifungal cream such as miconazole is added if yeast is "
    "also present. But candidiasis does not produce coral-red fluorescence."],
   ["Staphylococcus aureus, treated with topical mupirocin",
    "Staphylococcus aureus causes folliculitis, furuncles, and impetigo. It does not produce a chronic asymptomatic "
    "intertriginous patch with coral-red fluorescence."]],
  0, 84),

Q("Impetigo",
  "A 5-year-old boy has several lesions around the nose and mouth. Examination shows golden-yellow adherent crusts "
  "over shallow erosions, with palpable regional lymphadenopathy. He is afebrile and there are only four lesions. "
  "What is the most appropriate treatment?",
  [["Topical mupirocin ointment, with crusts removed before application",
    "Correct. Topical therapy is used for a single or limited number of non-bullous lesions, and mupirocin ointment "
    "is adequate for most cases of impetigo and as effective as oral therapy with fewer side effects. Crusts should "
    "be removed before applying it."],
   ["Topical mupirocin ointment applied over the intact crusts",
    "The agent and route are right but the technique is wrong, and it matters: crusts must be removed first or the "
    "ointment cannot reach the infected erosion beneath."],
   ["Oral cephalexin",
    "Cephalexin is the oral drug of choice for children, but oral therapy is reserved for more extensive disease. "
    "Four lesions is a limited number, so topical treatment is preferred and carries fewer side effects."],
   ["Oral trimethoprim-sulfamethoxazole for presumed methicillin-resistant Staphylococcus aureus",
    "Coverage for methicillin-resistant Staphylococcus aureus is used when it is cultured or suspected, and cultures "
    "are obtained for high-risk patients such as healthcare workers or teachers. Nothing here suggests that risk."],
   ["Oral penicillin V",
    "Treatment should cover both staphylococci and streptococci, and penicillin V does not cover Staphylococcus "
    "aureus. Penicillin V is the drug for erysipelas, where group A streptococcus is the organism."]],
  0, 94),

Q("Impetigo",
  "A 6-year-old girl had impetigo three weeks ago. She now presents with facial oedema, tea-coloured urine, and "
  "hypertension. Her mother asks whether the antibiotics failed. What is the most accurate explanation?",
  [["This is acute post-streptococcal glomerulonephritis, and antibiotics do not prevent it because the immune "
    "response usually precedes treatment",
    "Correct. Acute post-streptococcal glomerulonephritis may follow impetigo, especially in 3 to 7 year olds, and "
    "is characterised by sudden oedema, haematuria, and hypertension. Antibiotics do not prevent it because "
    "activation of the immune response most often precedes antibiotic treatment."],
   ["This is acute post-streptococcal glomerulonephritis, which would have been prevented by earlier antibiotics",
    "The diagnosis is right but the causal claim is wrong, and it wrongly assigns blame to the treatment. The immune "
    "activation precedes antibiotics, which is exactly why they do not prevent it."],
   ["This represents treatment failure requiring a change of antibiotic",
    "The skin infection has resolved; this is a delayed immune-mediated renal complication rather than persistent "
    "bacterial infection. Changing antibiotics would not address it."],
   ["This is rheumatic fever following the skin infection",
    "Acute post-streptococcal glomerulonephritis is the complication named as following impetigo, and its features "
    "are renal rather than cardiac or articular."],
   ["This is an allergic reaction to the antibiotic used for the impetigo",
    "A drug reaction would not produce haematuria with hypertension and oedema three weeks after treatment in this "
    "characteristic pattern."]],
  0, 97),

Q("Impetigo",
  "A 3-year-old has several tense, clear-to-cloudy blisters on the trunk arising on intact skin. Some have ruptured, "
  "leaving shallow moist erosions ringed by a collarette of scale. There is no lymphadenopathy. What organism and "
  "mechanism are responsible?",
  [["Staphylococcus aureus exclusively, releasing epidermolytic toxins that cause epidermal splitting",
    "Correct. Bullous impetigo is caused exclusively by Staphylococcus aureus, which releases epidermolytic toxins "
    "producing epidermal splitting. Bullae occur on intact skin, rupture to leave collarettes, and lymphadenopathy is "
    "uncommon — in contrast to non-bullous disease, where it is common."],
   ["Staphylococcus aureus or Streptococcus pyogenes, invading through a break in the skin",
    "That description belongs to non-bullous impetigo, which is the more common form and follows a break in the "
    "skin. Bullous disease is exclusively staphylococcal and arises on intact skin."],
   ["Streptococcus pyogenes exclusively, through direct dermal invasion",
    "Streptococcus pyogenes contributes to non-bullous impetigo and is the main organism in erysipelas, but bullous "
    "impetigo is exclusively staphylococcal."],
   ["Corynebacterium minutissimum invading the stratum corneum",
    "Corynebacterium minutissimum causes erythrasma, an asymptomatic intertriginous patch with coral-red "
    "fluorescence. It does not produce bullae."],
   ["An autoimmune antibody against the epithelial basement membrane",
    "Antibodies against the basement membrane produce bullous pemphigoid, a disease of adults over 60 with tense "
    "1 to 3 cm bullae. This is a toxin-mediated infection in a young child."]],
  0, 89),

Q("Impetigo",
  "A patient has a lesion that began as a pustule over inflamed skin and deepened into a dermal ulceration covered by "
  "a thick grey-yellow crust. He has diabetes and a recent insect bite at the site. What form of impetigo is this?",
  [["Ecthyma",
    "Correct. Ecthyma is uncommon and is predisposed to by pre-existing tissue damage such as bites and by "
    "immunocompromised states such as diabetes. It begins as a vesicle or pustule over inflamed skin that deepens "
    "into dermal ulceration with a thicker grey-yellow crust."],
   ["Non-bullous impetigo",
    "Non-bullous impetigo is the more common form and produces a superficial honey-coloured crust over an erosion "
    "rather than a deeper dermal ulceration with a thick grey-yellow crust."],
   ["Bullous impetigo",
    "Bullous impetigo produces fragile superficial bullae on intact skin that rupture leaving collarettes. It is "
    "superficial rather than ulcerative."],
   ["Erysipelas",
    "Erysipelas involves the upper dermis and superficial lymphatics, producing a raised plaque with a clear line of "
    "demarcation and high fever. It is not a crusted ulcer at a bite site."],
   ["Cellulitis",
    "Cellulitis involves the deeper dermis and subcutaneous tissue with poorly defined borders and the four cardinal "
    "signs of inflammation. It does not produce a discrete crusted dermal ulcer."]],
  0, 91),

Q("Erysipelas",
  "A 62-year-old woman presents with sudden onset of fever to 39.1 degrees Celsius, chills, and myalgias, followed "
  "within a day by a painful red area on her left shin. Examination shows a brightly erythematous plaque raised above "
  "the surrounding skin with a sharply defined border, and red streaks extending proximally. She has tinea pedis. "
  "What is the most likely organism and the drug of choice?",
  [["Streptococcus pyogenes, treated with penicillin V",
    "Correct. Group A streptococcus is the most common organism in erysipelas, which involves the upper dermis and "
    "superficial cutaneous lymphatics. Penicillin V is the pharmacotherapy, with clindamycin if the patient is "
    "penicillin allergic. Tinea pedis is a listed risk factor."],
   ["Staphylococcus aureus, treated with cephalexin",
    "Staphylococcus aureus is a cause of cellulitis, which is the deeper process with indistinct borders. The raised "
    "plaque with a clear line of demarcation and the lymphatic streaking identify erysipelas instead."],
   ["Streptococcus pyogenes, treated with trimethoprim-sulfamethoxazole",
    "The organism is right but the drug is aimed at methicillin-resistant Staphylococcus aureus and has poor "
    "streptococcal activity. Penicillin V is the named agent."],
   ["Pseudomonas aeruginosa, treated with ciprofloxacin",
    "Pseudomonas aeruginosa causes hot tub folliculitis after contaminated water exposure. It is not the organism of "
    "a febrile demarcated leg plaque."],
   ["Corynebacterium minutissimum, treated with topical erythromycin",
    "Corynebacterium minutissimum causes erythrasma, which is chronic, asymptomatic, and non-febrile. Sudden high "
    "fever with a rapidly spreading plaque excludes it."]],
  0, 104),

Q("Cellulitis",
  "A 49-year-old man has a warm, tender, erythematous area on the right lower leg with indistinct borders and "
  "surrounding oedema. What feature most reliably distinguishes cellulitis from erysipelas?",
  [["Cellulitis has indistinct borders that are not raised, whereas erysipelas is raised with a clear line of "
    "demarcation",
    "Correct. Erysipelas involves the upper dermis and superficial lymphatics, producing a plaque raised above the "
    "surrounding skin with a clear line of demarcation. Cellulitis involves the deeper dermis and subcutaneous tissue "
    "and therefore has borders that are indistinct and not raised."],
   ["Cellulitis is bilateral whereas erysipelas is unilateral",
    "Cellulitis most commonly affects the lower leg and is almost never bilateral. Bilateral leg redness should "
    "prompt consideration of stasis dermatitis rather than either infection."],
   ["Only cellulitis produces fever",
    "Fever occurs in both, and erysipelas characteristically produces high fever of 38 to 40 degrees Celsius with "
    "sudden onset within 48 hours of the skin changes."],
   ["Only erysipelas is caused by Streptococcus pyogenes",
    "Streptococcus pyogenes is the most common erysipelas organism, but group A beta-haemolytic streptococci also "
    "cause cellulitis alongside Staphylococcus aureus. The organism does not separate them reliably."],
   ["Only cellulitis follows a portal of entry",
    "Both follow a portal of entry such as tinea pedis, trauma, or an open lesion, and in erysipelas the inciting "
    "event is often not recalled at all."]],
  0, 107),

Q("Cellulitis",
  "A patient with non-purulent cellulitis of the leg is started on cephalexin. Forty-eight hours later he still has "
  "fever and the area has extended. What should be considered?",
  [["Necrotizing fasciitis, which is deeper and much more virulent and should be considered if there is no response "
    "within 48 hours",
    "Correct. The differential specifically states that necrotizing fasciitis should be considered if there is no "
    "response to antibiotics within 48 hours. It may initially be diagnosed as cellulitis, with the patient sent home "
    "and returning worse."],
   ["Normal treatment response, since cellulitis often looks worse during the first day",
    "Cellulitis may look and feel worse during the first day as destroyed pathogens release enzymes that increase "
    "local inflammation, which makes this genuinely true at 24 hours. But fever usually resolves within 24 hours of "
    "antibiotics, and persistence beyond 48 hours demands reassessment."],
   ["Contact dermatitis, given the failure to respond to antibiotics",
    "Contact dermatitis is on the differential but is identified by itching, vesicles, and absence of fever. This "
    "patient is febrile with spreading erythema."],
   ["Deep vein thrombosis as the sole explanation",
    "Deep vein thrombosis is on the differential and should be considered, but it would not explain fever with "
    "expanding erythema, and it does not carry the surgical urgency of the correct answer."],
   ["Allergy to cephalexin",
    "A drug allergy would produce a new pruritic eruption or systemic hypersensitivity features rather than extension "
    "of the original infected area with continuing fever."]],
  0, 108),

Q("Cellulitis",
  "A patient with cellulitis of the leg has an area that is tense, cyanotic, and bronzed with blanching. What is the "
  "significance of this finding?",
  [["The tissue is devitalised and will not be perfused, so antibiotics cannot reach it and surgical debridement is "
    "needed",
    "Correct. Devitalised tissue that is tense, cyanotic, necrotic, bronzed, and blanched will not be perfused, so "
    "antibiotics will not get to the site. Surgical debridement is required."],
   ["This is the expected appearance of resolving cellulitis",
    "Resolving cellulitis fades from erythema without becoming tense, cyanotic, or bronzed. Mistaking necrosis for "
    "improvement is the error that delays the surgery this patient needs."],
   ["This indicates a drug reaction to the antibiotic",
    "A drug reaction would not produce localised bronzed, cyanotic, non-perfused tissue within the area of "
    "infection."],
   ["This indicates deep vein thrombosis and anticoagulation should be started",
    "Deep vein thrombosis produces swelling and pain but not bronzed necrotic skin, and anticoagulation would not "
    "address non-perfused devitalised tissue."],
   ["The antibiotic dose should be increased and the area observed",
    "Increasing the dose does not solve the problem, which is that no blood is reaching the tissue to carry any dose "
    "of any antibiotic there."]],
  0, 111),

Q("Necrotizing fasciitis",
  "A 47-year-old man with alcohol use disorder presents with severe leg pain following a minor injury. Over hours the "
  "skin changes from red-purple to blue-grey, bullae with thick purple fluid appear, and the area that was exquisitely "
  "tender becomes numb. He is febrile and tachycardic. What is the most appropriate immediate action?",
  [["Immediate surgical consultation for aggressive debridement, without waiting for imaging or laboratory results",
    "Correct. Necrotizing fasciitis is a surgical emergency with high mortality, and laboratory tests and imaging "
    "studies should not delay surgical intervention. Loss of tenderness reflects destruction of superficial nerves "
    "and is an ominous sign."],
   ["Obtain magnetic resonance imaging to localise the site and depth before consulting surgery",
    "Magnetic resonance imaging and computed tomography do localise the site and depth of infection, which makes this "
    "sound reasonable. But imaging must not delay surgical intervention, and the time it takes is time the infection "
    "continues to advance."],
   ["Start broad-spectrum antibiotics and reassess in 24 hours",
    "Broad-based antibiotics covering aerobic gram-positive and gram-negative organisms are given, but they are an "
    "adjunct to surgery rather than a substitute. Waiting 24 hours in a rapidly progressive necrotising infection is "
    "not survivable management."],
   ["Admit for observation and elevate the limb",
    "Observation is exactly what leads to the described pattern of patients being diagnosed with cellulitis, sent "
    "home, and returning with worsening disease."],
   ["Perform bedside incision and drainage in the emergency department",
    "This condition requires aggressive operative debridement of necrotic tissue in theatre with admission to a "
    "surgical intensive care unit, not a bedside drainage procedure."]],
  0, 128),

Q("Necrotizing fasciitis",
  "Computed tomography of a patient with suspected necrotizing fasciitis shows gas in the soft tissue fascial planes. "
  "What does this indicate about the likely organism?",
  [["Gas may be present with Clostridium perfringens infection and is not present with group A streptococcal "
    "infection",
    "Correct. Gas may be present with Clostridium perfringens infection but is not present with group A streptococcal "
    "infection. Ultrasound is also useful for demonstrating air bubbles in soft tissue."],
   ["Gas is present with group A streptococcal infection and absent with Clostridium perfringens",
    "The two organisms are reversed. A clinician using this rule would exclude clostridial infection on the very "
    "finding that suggests it."],
   ["Gas is present in all cases of necrotizing fasciitis regardless of organism",
    "Absence of gas does not exclude necrotizing fasciitis, and group A streptococcal disease specifically does not "
    "produce it. Requiring gas for the diagnosis would miss the common streptococcal form."],
   ["Gas indicates the infection is superficial rather than involving deep fascia",
    "Gas in the fascial planes indicates deep involvement. Necrotizing fasciitis involves the tissue surrounding "
    "muscles, nerves, fat, and blood vessels."],
   ["Gas indicates a fungal rather than bacterial cause",
    "Necrotizing fasciitis is a bacterial infection that may be polymicrobial with aerobic, anaerobic, or mixed "
    "flora. Gas points to a gas-forming bacterium rather than a fungus."]],
  0, 129),

Q("Acute paronychia",
  "A 22-year-old woman presents three days after a manicure with rapid onset of redness, swelling, and tenderness of "
  "the tissue around her right index fingernail. Purulent fluid has collected under the skin of the nail fold. What "
  "is the most appropriate management?",
  [["Incision and drainage, with cultures where appropriate and oral antibiotics",
    "Correct. Acute paronychia starts as cellulitis and progresses to abscess. Severe cases with a purulent "
    "collection require incision and drainage, cultures where appropriate to rule out methicillin-resistant "
    "Staphylococcus aureus, and oral antibiotics such as amoxicillin-clavulanate or cephalexin."],
   ["Warm water soaks for 20 minutes three times daily alone",
    "Warm soaks are the treatment for mild cases without a collection. Once purulent fluid has collected, soaks alone "
    "leave an abscess undrained."],
   ["A broad-spectrum topical antifungal and keeping the hands dry",
    "That is the approach to chronic paronychia, where Candida albicans is the most common pathogen and the cause is "
    "prolonged immersion or chemical exposure. This is an acute bacterial process following trauma."],
   ["Oral acyclovir for probable herpetic whitlow",
    "Herpetic whitlow is on the differential and a Tzanck smear is used to rule it out, but it produces grouped "
    "painful vesicles rather than a purulent collection following a manicure."],
   ["Nail plate removal in all cases",
    "Nail removal is not the described management. Incision and drainage of the collection is what is required."]],
  0, 119),

Q("Chronic paronychia",
  "A 45-year-old dishwasher has had swollen, tender nail folds on several fingers for four months, without "
  "fluctuance. The nail plates are thickened and discoloured and the cuticles have separated from the nail plate. "
  "What is the most common pathogen, and what is the key patient instruction?",
  [["Candida albicans, and the patient should keep the hands as dry as possible",
    "Correct. Chronic paronychia is an inflammatory reaction of the proximal nail fold to irritants and allergens, "
    "and Candida albicans is the most common pathogen. Predisposing occupations include dishwashers, bartenders, "
    "cleaners, and cooks, and patients should be instructed to keep the hands as dry as possible."],
   ["Staphylococcus aureus, and the patient should keep the hands as dry as possible",
    "The instruction is right but the organism belongs to acute paronychia, which follows trauma such as a manicure "
    "or nail biting and produces rapid onset with a purulent collection."],
   ["Candida albicans, and the patient should soak the hands three times daily",
    "The organism is right but the advice is the opposite of what is needed. Continuous immersion is the cause, so "
    "prescribing soaks perpetuates the condition."],
   ["Pseudomonas aeruginosa, and the nail should be removed",
    "Pseudomonal nail infection appears on the differential, but Candida albicans is the most common pathogen and "
    "nail removal is not the described treatment."],
   ["A dermatophyte, treated with oral terbinafine",
    "Onychomycosis is on the differential, and the thickened discoloured nail plates make it worth excluding. But the "
    "primary process here is inflammation of the proximal nail fold from chronic wet work."]],
  0, 123),

Q("MRSA considerations",
  "A furuncle is incised and drained and the culture grows methicillin-resistant Staphylococcus aureus. Which oral "
  "regimens are appropriate?",
  [["Trimethoprim-sulfamethoxazole, doxycycline, or clindamycin",
    "Correct. When methicillin-resistant Staphylococcus aureus is cultured or suspected, the oral options given are "
    "trimethoprim-sulfamethoxazole, doxycycline, and clindamycin."],
   ["Dicloxacillin or cephalexin",
    "Dicloxacillin and cephalexin are the empiric oral agents for ordinary staphylococcal furuncles and carbuncles, "
    "and they are beta-lactams — precisely the class methicillin resistance defeats."],
   ["Penicillin V or amoxicillin",
    "Penicillin V is the drug for erysipelas, where group A streptococcus is the organism. Neither agent covers "
    "methicillin-resistant Staphylococcus aureus."],
   ["Ciprofloxacin or acetic acid soaks",
    "Ciprofloxacin and dilute acetic acid soaks belong to Pseudomonas folliculitis acquired from contaminated water."],
   ["Topical mupirocin alone",
    "Mupirocin ointment applied to the nares is used to address the Staphylococcus aureus carrier state in recurrent "
    "folliculitis. It is not adequate treatment for a drained methicillin-resistant abscess."]],
  0, 66, IO_B),

Q("MRSA considerations",
  "In which patient with impetigo should a culture be obtained rather than relying on clinical appearance alone?",
  [["A healthcare worker or teacher, who is at high risk for methicillin-resistant Staphylococcus aureus",
    "Correct. Cultures are obtained if the patient is at high risk for methicillin-resistant Staphylococcus aureus "
    "infection, with healthcare workers and teachers given as the examples, or if acute post-streptococcal "
    "glomerulonephritis is a concern."],
   ["Any child under five years of age",
    "Impetigo is common in infants and children and is most often diagnosed by clinical appearance. Age alone does "
    "not create the resistance risk that prompts culture."],
   ["Any patient with honey-coloured crusting",
    "Honey-coloured adherent crust is the classic appearance of non-bullous impetigo and is what allows a clinical "
    "diagnosis. It is a reason not to culture rather than a reason to."],
   ["Any patient being treated with topical mupirocin",
    "Mupirocin is adequate for most cases of limited non-bullous impetigo and as effective as oral therapy. Its use "
    "does not itself indicate culture."],
   ["Only patients who have already failed oral antibiotics",
    "Waiting for treatment failure delays identification in exactly the high-risk groups where resistance is "
    "anticipated in advance."]],
  0, 93, IO_B),
]

QUESTIONS += [

Q("Acne vulgaris",
  "What are the four factors involved in the pathogenesis of acne vulgaris?",
  [["Follicular hyperkeratinisation, increased sebum production, Cutibacterium acnes proliferation, and inflammation",
    "Correct. Acne involves follicular hyperkeratinisation with excess keratin in the follicle, increased sebum "
    "production providing a growth medium, proliferation of Cutibacterium acnes, and inflammation. The temporal "
    "sequence among them is not fully understood."],
   ["Follicular hyperkeratinisation, decreased sebum production, bacterial proliferation, and inflammation",
    "Sebum production is increased rather than decreased — the sebum provides the growth medium the bacteria need. "
    "Reversing it removes the link between the sebaceous gland and the organism."],
   ["Apocrine gland occlusion, bacterial proliferation, sinus tract formation, and scarring",
    "Apocrine occlusion with sinus tracts describes hidradenitis suppurativa, which is called acne inversa because it "
    "resembles acne vulgaris but affects different glands."],
   ["Neurovascular dysregulation, innate immune dysfunction, Demodex overgrowth, and microbiome alteration",
    "That is the pathogenesis of rosacea, which is distinguished from acne by the absence of comedones and the "
    "presence of persistent flushing."],
   ["Autoimmune follicular inflammation, androgen excess, and impaired barrier function",
    "Androgens do stimulate sebaceous growth and secretion at puberty, but acne is not an autoimmune follicular "
    "disease and barrier impairment belongs to atopic dermatitis."]],
  0, 6),

Q("Acne vulgaris",
  "What is the hallmark lesion of acne vulgaris, and why does it matter diagnostically?",
  [["The comedone, whose absence argues against acne and toward rosacea",
    "Correct. Comedones are the hallmark of acne vulgaris, and the differential specifically distinguishes rosacea by "
    "papules and pustules in the middle third of the face with telangiectasias, flushing, and an absence of "
    "comedones."],
   ["The pustule, whose absence argues against acne",
    "Pustules are among the inflammatory lesions of acne but are shared with rosacea, folliculitis, and perioral "
    "dermatitis. They cannot serve as the distinguishing lesion."],
   ["The nodule, whose presence defines the diagnosis",
    "Nodules occur in severe acne and drive the decision to use isotretinoin, but they are a severity marker rather "
    "than the hallmark that identifies the disease."],
   ["The telangiectasia, whose presence confirms acne",
    "Telangiectasias belong to rosacea. Their presence argues against acne rather than for it."],
   ["The papule, which is unique to acne among facial eruptions",
    "Papules occur across acne, rosacea, perioral dermatitis, and folliculitis. Acne is described as polymorphic, "
    "with several lesion types present at once."]],
  0, 13),

Q("Acne vulgaris",
  "Why is benzoyl peroxide recommended alongside topical or oral antibiotic therapy for acne?",
  [["It suppresses Cutibacterium acnes and reduces the risk of bacterial resistance",
    "Correct. Benzoyl peroxide is keratolytic and anti-inflammatory and suppresses Cutibacterium acnes. It is "
    "recommended alongside antimicrobials specifically to reduce the risk of bacterial resistance, and combination "
    "products exist for that purpose."],
   ["It is comedolytic and normalises follicular hyperkeratinisation",
    "Comedolysis and normalisation of hyperkeratinisation describe topical retinoids. Topical antimicrobials are "
    "explicitly described as not comedolytic."],
   ["It inhibits tyrosinase and improves post-inflammatory hyperpigmentation",
    "Tyrosinase inhibition with improvement of post-inflammatory hyperpigmentation is a property of azelaic acid."],
   ["It decreases sebum excretion",
    "Decreased sebum excretion is the mechanism of isotretinoin, and oestrogen in combined oral contraceptives also "
    "decreases sebum production."],
   ["It provides ultraviolet protection to acne-prone skin",
    "Benzoyl peroxide has no photoprotective role. Photosensitivity is a consideration with topical retinoids and "
    "with doxycycline."]],
  0, 22),

Q("Acne vulgaris",
  "A patient with acne asks how quickly treatment will work. What education is accurate?",
  [["Improvement takes 4 to 6 weeks, response is judged by new lesion counts at 6 to 8 weeks, and the back and chest "
    "may take 3 to 4 months",
    "Correct. Improvement in lesions can take 4 to 6 weeks, clinical improvement is measured by the number of new "
    "lesions after 6 to 8 weeks of therapy, and areas on the back and chest are slowest to respond, taking 3 to 4 "
    "months."],
   ["Improvement takes 4 to 6 weeks and all body sites respond at the same rate",
    "The timeline is right for the face but the claim of uniform response is wrong, and it is the part that causes "
    "patients to abandon treatment for truncal acne before it has had time to work."],
   ["Improvement should be evident within one week of starting therapy",
    "A one-week expectation guarantees perceived failure and premature discontinuation of an effective regimen."],
   ["No improvement should be expected for at least six months at any site",
    "This understates the response and may prompt unnecessary escalation to systemic therapy while a working regimen "
    "is dismissed as ineffective."],
   ["Response cannot be measured objectively, so treatment should be continued indefinitely",
    "Response is measured objectively by the number of new lesions after 6 to 8 weeks, which is what allows a regimen "
    "to be judged and changed."]],
  0, 36),

Q("Acne vulgaris",
  "A 16-year-old football player develops acne confined to the shoulders and upper back under his pads. What "
  "predisposing factor does this represent?",
  [["Acne mechanica, from pressure occluding the pilosebaceous follicle",
    "Correct. Acne mechanica results from pressure on the skin — shoulder pads, orthopaedic casts, and helmets are "
    "the named examples — occluding the pilosebaceous follicle."],
   ["Drug-induced acne from an anabolic steroid",
    "Anabolic steroid use is a recognised cause and belongs in the history of any athlete, but the strictly "
    "pressure-mapped distribution under the pads points to a mechanical cause."],
   ["Endocrine acne from insulin resistance",
    "Insulin resistance is proposed to stimulate androgen production and is listed among endocrine factors, but it "
    "would produce acne in the hormonally responsive sebaceous areas rather than confined to a pressure site."],
   ["Emotional stress causing cortisol release",
    "Stress with cortisol release is listed among predisposing factors, but it would not confine the eruption to the "
    "area beneath the equipment."],
   ["Genetic predisposition, given the three-fold risk with an affected first-degree relative",
    "Genetics is a key factor with a three-fold risk if a first-degree relative is affected, but inherited "
    "susceptibility does not create a distribution that matches sports equipment."]],
  0, 9),

Q("Acne vulgaris",
  "For which patient is a combined oral contraceptive most appropriate as acne therapy?",
  [["A woman with hyperandrogenism whose acne has not responded to topical retinoids and antibiotics",
    "Correct. Oral contraceptives are considered for patients with hyperandrogenism and when acne is unresponsive to "
    "both topical retinoids and topical or oral antibiotics. Oestrogen decreases sebum production and reduces ovarian "
    "androgen production."],
   ["A woman with mild comedonal acne who has not yet used any topical therapy",
    "Mild comedonal acne is treated first with a topical retinoid. Starting systemic hormonal therapy before any "
    "topical trial reverses the treatment ladder."],
   ["A man with moderate papulopustular acne",
    "Combined oral contraceptives are not applicable to male patients, whose moderate disease is treated with a "
    "topical retinoid, an oral antibiotic, and benzoyl peroxide."],
   ["A woman planning pregnancy in the next three months",
    "A patient planning pregnancy is not an appropriate candidate for contraceptive-based therapy, and the treatment "
    "goal and the reproductive goal are in direct conflict."],
   ["Any adolescent as first-line therapy regardless of sex or severity",
    "Combined oral contraceptives sit well down the systemic treatment list and are considered for specific "
    "indications rather than used as universal first-line therapy."]],
  0, 28),

Q("Folliculitis",
  "A patient has folliculitis that has recurred repeatedly despite topical treatment. Cultures grow Staphylococcus "
  "aureus each time. What additional measure addresses the likely reservoir?",
  [["Mupirocin ointment applied to the nares to address the Staphylococcus aureus carrier state",
    "Correct. Recurrent or recalcitrant folliculitis raises the Staphylococcus aureus carrier state, and mupirocin "
    "ointment is used for it. Nasal swabs of the patient and family members are taken to evaluate carriage."],
   ["A longer course of the same topical antibiotic cream",
    "Extending a treatment that has already failed repeatedly does not address why it keeps returning, which is "
    "recolonisation from a reservoir."],
   ["Oral ciprofloxacin",
    "Ciprofloxacin is used for widespread or resistant Pseudomonas folliculitis after water exposure. It is not the "
    "agent for staphylococcal carriage."],
   ["A potassium hydroxide wet mount of a plucked hair",
    "A potassium hydroxide wet mount using a plucked hair is done to rule out dermatophyte folliculitis, which is a "
    "reasonable step in resistant cases. But the cultures have already identified the organism."],
   ["Switching to an antibacterial soap alone",
    "Antibacterial soaps such as Dial or Lever 2000 are part of general treatment along with good hygiene and loose "
    "clean clothing. They do not eradicate nasal carriage."]],
  0, 46),

Q("Folliculitis",
  "What test should be performed on a plucked hair when folliculitis fails to respond to antibacterial treatment?",
  [["A potassium hydroxide wet mount to rule out dermatophyte folliculitis",
    "Correct. In resistant cases a potassium hydroxide wet mount using a plucked hair is used to rule out fungal, "
    "specifically dermatophyte, folliculitis. Culture and Gram stain from an unroofed pustule are also performed."],
   ["A Tzanck smear to rule out herpetic infection",
    "A Tzanck smear evaluates vesicular lesions for herpesvirus changes and is used to rule out herpetic whitlow in "
    "paronychia. It is not the plucked-hair test."],
   ["A mineral oil preparation to identify mites",
    "A mineral oil preparation confirms scabies by identifying the mite, its eggs, or fecal pellets. It is a skin "
    "scraping rather than a hair test."],
   ["A Wood's lamp examination for coral-red fluorescence",
    "Coral-red fluorescence identifies erythrasma caused by Corynebacterium minutissimum. It is not performed on a "
    "plucked hair and does not detect dermatophytes."],
   ["Direct immunofluorescence for immunoglobulin deposits",
    "Direct immunofluorescence detects immune deposits in autoimmune blistering disease. Folliculitis is an "
    "infectious or irritant process."]],
  0, 44),

Q("Abscess",
  "How does a cutaneous abscess differ in origin from a furuncle?",
  [["An abscess often follows traumatic inoculation of bacteria into the skin, whereas a furuncle arises from an "
    "infected hair follicle",
    "Correct. An abscess is a collection of purulent material within the dermis and deeper tissues, often due to "
    "traumatic inoculation of bacteria into the skin, compared with furuncles, which arise from infected hair "
    "follicles."],
   ["An abscess arises from an infected hair follicle, whereas a furuncle follows traumatic inoculation",
    "The two origins are swapped. A furuncle is by definition a deep-seated infection of a hair follicle and its "
    "adjacent subcutaneous tissue."],
   ["An abscess involves apocrine glands, whereas a furuncle involves eccrine glands",
    "Apocrine gland inflammation describes hidradenitis suppurativa. Neither an abscess nor a furuncle is defined by "
    "eccrine involvement."],
   ["An abscess is superficial and a furuncle is confined to the epidermis",
    "Both are deep. An abscess involves the dermis and deeper tissues and a furuncle involves the follicle and "
    "adjacent subcutaneous tissue; epidermal infection describes impetigo."],
   ["An abscess is always sterile whereas a furuncle is always infected",
    "An abscess is a collection of purulent material from bacterial infection. A sterile neutrophilic collection "
    "would raise pyoderma gangrenosum instead."]],
  0, 113),

Q("Abscess",
  "A patient has an abscess that has not drained spontaneously. What is the appropriate management?",
  [["Surgical incision and drainage",
    "Correct. If the lesion does not spontaneously drain, surgical incision and drainage is required. If it drains "
    "spontaneously, warm soaks and broad-spectrum antibiotics with consideration of methicillin-resistant "
    "Staphylococcus aureus are used, adjusted by culture."],
   ["Warm soaks and broad-spectrum antibiotics alone",
    "That is the management once a lesion has drained spontaneously. An undrained collection will not resolve on "
    "antibiotics, because the drug does not penetrate a walled-off cavity of pus."],
   ["Oral antibiotics selected by culture of the intact skin surface",
    "A surface culture samples colonising flora rather than the organism inside the abscess, and it delays the "
    "drainage that is the definitive treatment."],
   ["Observation until the lesion drains on its own",
    "Waiting allows the collection to enlarge and risks extension into surrounding tissue. Incision and drainage is "
    "the indicated step."],
   ["Squeezing the lesion to express its contents",
    "Patients are instructed not to squeeze such lesions, which risks deeper inoculation and spread rather than "
    "controlled evacuation."]],
  0, 115),

Q("Erysipelas",
  "What laboratory and imaging approach is appropriate in a classic presentation of erysipelas?",
  [["Clinical diagnosis, with blood and tissue cultures not cost effective and imaging of low yield",
    "Correct. Erysipelas is a clinical diagnosis in a classic presentation. Leukocytosis and raised erythrocyte "
    "sedimentation rate and C-reactive protein are common, but blood and tissue cultures are not cost effective "
    "because of extremely low organism yield, and imaging studies are of low yield and not indicated."],
   ["Blood and tissue cultures in every patient before starting antibiotics",
    "Cultures have extremely low yield in erysipelas and are not cost effective. Delaying treatment for them is "
    "particularly unhelpful given that prompt treatment matters because of potentially rapid progression."],
   ["Magnetic resonance imaging to define the depth of involvement",
    "Imaging is of low yield and not indicated in a classic presentation. Depth is inferred clinically from the "
    "raised, sharply demarcated plaque."],
   ["Skin biopsy in every patient to confirm the diagnosis",
    "Biopsy is not part of the routine evaluation of a classic erysipelas presentation and would delay prompt "
    "treatment."],
   ["No laboratory testing of any kind is ever useful",
    "Leukocytosis and raised inflammatory markers are common and can support the clinical impression; it is cultures "
    "and imaging specifically that add little."]],
  0, 103),

Q("Cellulitis",
  "In which patient with cellulitis is no diagnostic workup required?",
  [["A patient with a limited area of involvement, minimal pain, no systemic signs, and no risk factor for serious "
    "illness",
    "Correct. Cellulitis is usually a clinical diagnosis, and no workup is needed when there is a limited area of "
    "involvement, minimal pain, no systemic signs, and no risk factor for serious illness such as extremes of age or "
    "immunocompromise."],
   ["Any patient whose cellulitis involves the lower leg",
    "The lower leg is the most common site, so this describes the majority of cases rather than a low-risk subset. "
    "Site does not determine whether investigation is needed."],
   ["Any patient who is afebrile at presentation",
    "Fever may be absent depending on severity, so a normal temperature alone does not establish that the patient is "
    "low risk. Extent, pain, and comorbidity all contribute."],
   ["Any patient already taking antibiotics",
    "Current antibiotic use does not remove the need for assessment, and failure to respond within 48 hours should "
    "raise necrotizing fasciitis."],
   ["Only patients under 40 years of age",
    "Extremes of age are one risk factor among several, and a single age cut-off does not capture immunocompromise, "
    "extent, or systemic signs."]],
  0, 109),

Q("Cellulitis",
  "A patient with cellulitis is warned that the area may look worse on the first day of antibiotics. What explains "
  "this, and when should therapy be reconsidered?",
  [["Sudden destruction of pathogens releases enzymes that increase local inflammation; therapy should be "
    "reconsidered if fever persists beyond 48 hours",
    "Correct. Cellulitis may look and feel worse during the first day because sudden destruction of pathogens "
    "releases potent enzymes that increase local inflammation. Fever usually resolves within 24 hours, and "
    "persistence beyond 48 hours should prompt a change in antimicrobial therapy."],
   ["Sudden destruction of pathogens releases enzymes; therapy should be reconsidered only after seven days",
    "The mechanism is right but the threshold is far too long. Waiting a week to reconsider risks missing "
    "necrotizing fasciitis, which should be considered if there is no response within 48 hours."],
   ["The antibiotic is failing and should be changed immediately on day one",
    "Changing therapy on the first day misinterprets an expected inflammatory response and abandons an appropriate "
    "antibiotic before it has been given a fair trial."],
   ["The patient has developed an allergy to the antibiotic",
    "Worsening erythema at the infected site on day one reflects the inflammatory response to bacterial killing "
    "rather than hypersensitivity, which would produce a new eruption elsewhere."],
   ["This indicates devitalised tissue requiring immediate debridement",
    "Devitalised tissue is recognised by a tense, cyanotic, bronzed, blanched appearance rather than by ordinary "
    "first-day worsening of erythema."]],
  0, 112),

Q("Necrotizing fasciitis",
  "Which set of risk factors is associated with necrotizing fasciitis?",
  [["Trauma, burns, surgery, immunosuppression, renal failure, alcoholism, odontogenic infection, and intravenous "
    "drug use, with male predominance",
    "Correct. Those are the listed risk factors, and the condition is more common in males than females."],
   ["Obesity, poor hygiene, occlusive clothing, and hot humid temperatures",
    "That set belongs to folliculitis, along with immunocompromised states, corticosteroids, diabetes, and nasal "
    "carriage of Staphylococcus aureus."],
   ["Impaired lymphatic drainage after mastectomy, athlete's foot, and obesity",
    "Those are erysipelas risk factors, where impaired lymphatic drainage and tinea pedis as a portal of entry are "
    "prominent."],
   ["Manicure, ingrown nail, hangnail, and nail biting",
    "Those are the predisposing factors for acute paronychia."],
   ["Continuous immersion of the hands in water and contact with chemicals",
    "That is the occupational history behind chronic paronychia in dishwashers, bartenders, cleaners, and cooks."]],
  0, 125),

Q("Hidradenitis suppurativa",
  "A woman with moderate hidradenitis suppurativa has not responded to topical therapy. What is the rationale for "
  "adding spironolactone?",
  [["It is an aldosterone antagonist that inhibits ovarian and adrenal androgen production",
    "Correct. Spironolactone is an aldosterone antagonist that inhibits ovarian and adrenal production of androgens. "
    "Combination birth control pills are used similarly, reducing luteinising hormone and follicle-stimulating "
    "hormone secretion."],
   ["It is an immunosuppressant that blocks tumour necrosis factor",
    "Tumour necrosis factor blockade describes infliximab, which is used for severe disease. Spironolactone works "
    "through androgen suppression instead."],
   ["It reduces the size of draining sinuses when injected into the lesion",
    "Intralesional triamcinolone acetonide is what decreases the size of draining sinuses. Spironolactone is taken "
    "orally and acts systemically."],
   ["It is a retinoid that normalises follicular keratinisation",
    "Oral retinoids such as isotretinoin are a separate treatment option. Spironolactone is not a retinoid."],
   ["It is an antibiotic that suppresses the causative organism",
    "Topical clindamycin and erythromycin and systemic antibiotics are used, but hidradenitis suppurativa is an "
    "inflammatory apocrine disease rather than a primary infection, and spironolactone has no antibacterial action."]],
  0, 78),

Q("Hidradenitis suppurativa",
  "What offers the best chance of permanent cure in hidradenitis suppurativa?",
  [["Wide excision of the affected areas",
    "Correct. Chances of permanent cure are best with wide excision of the affected areas. Large fluctuant cysts are "
    "incised and drained, but that manages an episode rather than curing the disease."],
   ["Long-term systemic antibiotics",
    "Some advocate long-term systemic antibiotics, but the long-term outcomes are described as often poor. They "
    "control rather than cure."],
   ["Incision and drainage of each cyst as it develops",
    "Incision and drainage relieves individual large fluctuant cysts. Because the disease recurs in the same apocrine "
    "regions, repeated drainage never becomes a cure."],
   ["Intralesional triamcinolone acetonide injections",
    "Intralesional triamcinolone decreases the size of draining sinuses, which is a useful symptomatic measure rather "
    "than a definitive one."],
   ["Topical clindamycin used indefinitely",
    "Mild topical steroid creams combined with topical antibiotics are favoured for mild disease, but they do not "
    "eliminate the affected apocrine-bearing tissue."]],
  0, 79),

Q("Erythrasma",
  "Where is erythrasma most commonly found, and what is the typical symptom profile?",
  [["The inner thighs, crural region, scrotum, and between the fourth and fifth toes, usually asymptomatic and "
    "sometimes pruritic",
    "Correct. The most common sites are the inner thighs, crural region, scrotum, and between the fourth and fifth "
    "toes, with the axilla, under the breasts, and intergluteal folds less common. It is usually asymptomatic and may "
    "be pruritic."],
   ["The face and lower extremity, with sudden onset of high fever",
    "The face and lower extremity with sudden high fever describes erysipelas, an acute streptococcal infection "
    "rather than a chronic asymptomatic intertriginous one."],
   ["The axilla, groin, breasts, and perineum, with recurrent painful suppurative lesions",
    "That distribution and symptom profile belong to hidradenitis suppurativa, which affects apocrine-bearing skin "
    "with recurrence more than twice in six months."],
   ["Around the nose and mouth, with honey-coloured crusting",
    "Perioral honey-coloured crusting is non-bullous impetigo, a superficial epidermal infection of children."],
   ["The scalp, thighs, trunk, axilla, and inguinal region, with follicular pustules",
    "Those are the common sites of folliculitis, whose lesions are pustules pierced by a central hair."]],
  0, 81),
]
