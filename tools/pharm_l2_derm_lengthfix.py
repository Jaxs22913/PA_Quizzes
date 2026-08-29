"""Length-bias remediation for Pharmacology I Lecture 2, dermatology medications.

Same shape of problem as Lecture 1 and Microbiology Lecture 2: this deck is
enumerative, so correct answers come out as lists or two-part statements while
the distractors land as single short phrases. The fix is STRUCTURAL -- a
three-part answer needs three-part distractors. Padding to a character count
does not work and stalls the rate around 40%.

ONLY WRONG CHOICES ARE REWRITTEN. The applier excludes the correct option by
construction, so a rewrite cannot land on the answer, and every replacement has
to stay unambiguously false against the lecture.

(This is the opposite call from the CMS master exams, where the reference
questions Jaxon supplied have SHORT options and the fix there was to shorten
the correct answer instead. These are enumerative recall items, not five-option
vignettes, so they follow the pharmacology precedent.)
"""
FIXES = {
 2:  (1, "The drug is stored in subcutaneous fat and released during exercise, which is why activity increases absorption"),
 8:  (2, "Follicular atrophy with thinning of the ductal epidermis, reduced keratinization, fungal overgrowth of the sebaceous duct, and mast cell histamine release"),
 11: (3, "Acute disease as nodular and pustular lesions; chronic disease as open and closed comedones alone"),
 17: (2, "Wash with a high pH soap several times daily, since a raised pH increases the activity of other topical agents"),
 19: (2, "It requires an immediate switch to systemic therapy, because irritation means the topical agent has failed"),
 20: (3, "It remains unchanged in the skin and works purely by oxidising sebum within the follicle"),
 22: (2, "Conversion to benzoic acid within the stratum corneum together with a direct comedolytic peeling effect"),
 26: (2, "Converts to benzoic acid after penetration, bleaches surface pigment, and suppresses sebum production"),
 32: (2, "Mupirocin is the preferred agent for acne; bacitracin is losing efficacy to Propionibacterium acnes resistance"),
 33: (1, "It is safe in the second and third trimesters, and only the first trimester requires contraceptive cover"),
 39: (2, "Bleaching of hair and clothing, together with staining of the surrounding skin at the injection site"),
 41: (2, "Nikolsky sign, mucosal erosion at two or more sites, and fever preceding the rash by one to three days"),
 42: (2, "Frequent hot baths with a high pH soap, air drying afterwards, and occlusive dressings left on overnight"),
 47: (1, "Patient age, sex, body weight and skin type, taken together with the season in which treatment is given"),
 49: (3, "Photosensitivity, severe sunburn, desquamation, burning and stinging that decrease with continued use"),
 51: (1, "They inhibit fungal cytochrome P450 and so prevent formation of the fungal cell wall"),
 56: (1, "Eliminating vulvovaginal candidiasis in women"),
 57: (3, "It inhibits fungal ergosterol production and so prevents cell wall synthesis"),
 58: (1, "Avoid it in pregnancy and in breastfeeding, because systemic absorption through inflamed skin is teratogenic"),
 59: (2, "Dermatophytes and Candida species including tinea versicolor and cutaneous candidiasis"),
 65: (2, "Nystatin and tolnaftate, which bind fungal membrane sterols directly and cause leakage of cell contents"),
 68: (3, "Actinic keratoses and superficial basal cell carcinoma; they are topical retinoid preparations"),
 69: (2, "Acne vulgaris, rosacea, and atopic dermatitis unresponsive to steroids"),
 70: (3, "It corrects abnormal follicular keratinization, reduces bacterial counts within the follicle, and dampens the inflammatory response"),
 71: (3, "It means the applied dose is too low and the frequency should be increased until the skin clears"),
}
