# -*- coding: utf-8 -*-
"""Hand-written repairs for explanations the self-containment pass broke.

Deleting an attribution subject ("the lecture", "Dr. Wood") stranded the verb
that followed it -- "Correct. says to avoid retinoids during pregnancy". Each
replacement below restores a subject rather than re-adding the attribution, so
the sentence stands on its own. Two also drop a residual "the syllabus".
"""

REPAIRS = {
 "Age is not a contraindication, and notes retinoids are useful for wrinkles and dyspigmentation.":
 "Age is not a contraindication; retinoids are in fact useful for wrinkles and dyspigmentation.",

 "Bexarotene is the retinoid links to T-cell lymphoma.":
 "Bexarotene is the retinoid used in T-cell lymphoma.",

 "Correct, and adds distracting the child, removing irritants and allergens, and maintaining hydration.":
 "Correct, along with distracting the child, removing irritants and allergens, and maintaining hydration.",

 "Correct, and notes a gel formulation is available alongside oral use.":
 "Correct, and a gel formulation is available alongside oral use.",

 "Correct, and notes it is not absorbed though it may irritate mucous membranes.":
 "Correct, and it is not absorbed, though it may irritate mucous membranes.",

 "Correct, which is why it is the agent the syllabus calls a mitotic inhibitor.":
 "Correct, which is why it is classed as a mitotic inhibitor.",

 "Correct. Note this sits outside the syllabus objectives, which name only antibacterials, antivirals and antifungals.":
 "Correct. Note this sits outside the stated objectives, which name only antibacterials, antivirals and antifungals.",

 "Correct. groups these as defecation, urination, miosis, bradycardia, bronchorrhoea, bronchospasm, emesis, lacrimation and salivation.":
 "Correct. These group as defecation, urination, miosis, bradycardia, bronchorrhoea, bronchospasm, emesis, lacrimation and salivation.",

 "Correct. notes the eruption is not seen with hydrocortisone.":
 "Correct. The eruption is not seen with hydrocortisone.",

 "Correct. notes the topoisomerase IV mechanism is poorly understood.":
 "Correct. The topoisomerase IV mechanism is poorly understood.",

 "Correct. says to avoid retinoids during pregnancy.":
 "Correct. Retinoids are avoided during pregnancy.",

 "Frames the course by duration rather than by appearance alone.":
 "The course is defined by duration rather than by appearance alone.",

 "Frames the inflammation as intrinsic to how the drug works.":
 "The inflammation is intrinsic to how the drug works.",

 "Photolability is the property assigns to tretinoin, and adapalene is the stable one.":
 "Photolability belongs to tretinoin; adapalene is the stable one.",

 "Singles out moxifloxacin as the exception.":
 "Moxifloxacin is the exception.",

 "Tazarotene is the retinoid links to both acne and psoriasis.":
 "Tazarotene is the retinoid used for both acne and psoriasis.",

 "Treats acne as a chronic disease throughout rather than splitting it this way.":
 "Acne is treated as a chronic disease rather than split this way.",

 "Treats irritation as a barrier to adherence, not as a marker of efficacy.":
 "Irritation is a barrier to adherence, not a marker of efficacy.",

 "Vancomycin is not a protein synthesis inhibitor, and notes it is not a beta-lactam.":
 "Vancomycin is not a protein synthesis inhibitor, and it is not a beta-lactam either.",
}
