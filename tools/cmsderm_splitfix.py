# -*- coding: utf-8 -*-
"""Split options that carried two different KINDS of answer at once.

Jaxon: an option should be one answer -- just the disease, or just the
treatment -- not "Ramsay Hunt syndrome; add a systemic corticosteroid". Where a
question asked for both, the option had to carry both, so the lead-in is narrowed
here and the options reduced to a single category.

NOT every semicolon is wrong. Left alone deliberately:
  * genuine contrasts, where the contrast IS the question ("Alkalis act in
    minutes; soaps over weeks", "Abscess from inoculation; furuncle from a
    follicle", the patch-versus-prick pairing);
  * same-category compounds, which the reference itself uses -- its urticaria
    item offers "Discontinue TMP-SMX; initiate a daily oral antihistamine",
    two treatment decisions rather than a diagnosis welded to a drug.

`expl` supplies an explanation only where a genuinely new option replaces one
that no longer fits the narrowed question.
"""

SPLIT = {

("l10",13): {"lead": "What is the first management priority?",
 "opts": ["Start or optimise antiretroviral therapy","Start systemic chemotherapy first",
          "Intralesional vincristine","Observation alone","Topical alitretinoin"],
 "expl": {4: "Topical therapy has a role in limited cutaneous disease but does nothing for the immunodeficiency driving it. Immune restoration through antiretroviral therapy is the cornerstone of treatment for epidemic Kaposi sarcoma."}},

("l10",18): {"lead": "Where does the tumour most often arise?",
 "opts": ["The matrix","The nail bed","The periungual skin","The hyponychium","The proximal nail fold"],
 "expl": {3: "The hyponychium lies under the free edge of the nail and is not the usual origin. Matrix tumours are what produce longitudinal plate changes such as melanonychia.",
          4: "The proximal nail fold overlies the matrix but is not itself the site of origin, which is part of why these tumours are recognised late."}},

("l2",57): {"lead": "What is the most important clinical consideration for this agent?",
 "opts": ["Caution over nephrotoxicity","Risk of cutaneous atrophy","Irritation and photosensitivity",
          "Reserve it for the face and eyelids","Second-line use alongside coal tar"]},

("l3",9): {"lead": "What should be suspected?",
 "opts": ["Urticarial vasculitis","Ordinary chronic urticaria","Hereditary angioedema","Mastocytosis","Anaphylaxis"]},

("l3",18): {"lead": "What is the appropriate first-line treatment?",
 "opts": ["Topical aluminium chloride","Botulinum toxin A injections","Endocrine investigation",
          "Topical glycopyrronium","Psychological therapy alone"]},

("l3",33): {"lead": "What course should be expected?",
 "opts": ["Benign and self-limiting","Progression to malignancy","Lifelong immunosuppression is required",
          "Invariable recurrence after clearing","Resolution within days"],
 "expl": {4: "Granuloma annulare is self-limiting but resolves over months to years rather than days, and localised disease is often simply observed."}},

("l3",40): {"lead": "What course should be expected?",
 "opts": ["Resolution in 3 to 5 days with desquamation","Resolution in 1 to 2 weeks with infection risk",
          "Blistering within 24 hours","A need for prophylactic antibiotics","A need for surgical referral"],
 "expl": {2: "Blistering marks second-degree injury with partial dermal involvement. This burn is confined to the epidermis, and the examination specifically records no blistering."}},

("l4",10): {"lead": "What is the lesion?",
 "opts": ["A carbuncle","A furuncle","A cutaneous abscess","Hidradenitis suppurativa","Folliculitis"],
 "expl": {4: "Folliculitis is superficial inflammation of the follicle producing small pustules pierced by a central hair, not a deep indurated plaque with several draining openings and systemic symptoms."}},

("l4",13): {"lead": "What is first-line treatment for localised disease?",
 "opts": ["Topical erythromycin","Oral erythromycin","Topical terbinafine","Topical miconazole","Topical mupirocin"]},

("l4",25): {"lead": "What is the most common pathogen?",
 "opts": ["Candida albicans","Staphylococcus aureus","Pseudomonas aeruginosa","A dermatophyte","Streptococcus pyogenes"],
 "expl": {4: "Streptococcus pyogenes contributes to acute paronychia and to impetigo, but chronic paronychia from prolonged wet work is most often candidal."}},

("l4",40): {"lead": "When should therapy be reconsidered?",
 "opts": ["If fever persists beyond 48 hours","Only after seven full days","Immediately, on day one",
          "Only if a new rash appears","As soon as the area looks worse"],
 "expl": {3: "A new eruption elsewhere would suggest drug hypersensitivity, but it is not the trigger for reassessing an antibiotic that is failing to control the infection itself.",
          4: "The area often looks and feels worse on the first day as destroyed pathogens release enzymes that increase local inflammation, so appearance alone on day one is the wrong trigger."}},

("l6",13): {"lead": "What is the first management step?",
 "opts": ["Stop the corticosteroid","Increase the corticosteroid potency","Patch test before anything else",
          "Apply an emollient and observe","Start calcipotriene"]},

("l6",14): {"lead": "What topical choice covers both possibilities?",
 "opts": ["A topical azole","Topical nystatin","Topical terbinafine","Topical erythromycin","Topical mupirocin"]},

("l6",24): {"lead": "What is first-line treatment?",
 "opts": ["Gabapentin or a tricyclic antidepressant","Long-term opioids","Antivirals",
          "Systemic corticosteroids","Acetaminophen alone"]},

("l6",34): {"lead": "What form is this?",
 "opts": ["Flat warts","Verruca vulgaris","Molluscum contagiosum","Plantar warts","Seborrheic keratoses"]},

("l6",36): {"lead": "What therapy is required?",
 "opts": ["Oral antifungal therapy","Oral cephalexin","A topical antifungal cream alone",
          "A change of shaving technique","A topical retinoid"]},

("l6",41): {"lead": "What treatment is added beyond antivirals?",
 "opts": ["A systemic corticosteroid","No additional treatment","Urgent ophthalmology referral",
          "A corticosteroid instead of an antiviral","Topical antibiotic drops"]},

("l7",26): {"lead": "What do they contain?",
 "opts": ["Lipid-laden macrophages","Keratin within an epithelial cyst","Eccrine duct neoplasms",
          "Dilated capillaries","Mucin extruded from a joint"],
 "expl": {4: "Mucin extruded from a joint space forms a digital mucous cyst over the distal interphalangeal joint, not a soft yellow plaque of the eyelid."}},

("l7",27): {"lead": "What is the most likely diagnosis?",
 "opts": ["Lipoma","Epidermoid cyst","Dermatofibroma","Cutaneous abscess","Liposarcoma"]},

("l8",4): {"lead": "What is this presentation?",
 "opts": ["Crusted scabies","Ordinary scabies","Post-scabietic dermatitis","Xerosis of aging","Psoriasis"],
 "expl": {1: "Ordinary scabies is defined by severe itching, and this patient has none. The absence of pruritus alongside thick scale is what marks the crusted form."}},

("l8",9): {"lead": "What organism is responsible?",
 "opts": ["Cimex lectularius","Sarcoptes scabiei","Pediculus humanus corporis","Tunga penetrans","Schistosome cercariae"]},

("l8",14): {"lead": "What is the treatment?",
 "opts": ["Oral albendazole or ivermectin","Surgical excision or cryotherapy","Topical therapy alone",
          "Excision of an embedded flea","Whole-body permethrin"]},

("l8",18): {"lead": "In which region of the United States is the hobo spider the predominant cause of necrotic arachnidism?",
 "opts": ["The Pacific Northwest","The Midwest and Southeast","The Northeast","The Southwest","The Gulf Coast"],
 "expl": {4: "The Gulf Coast is not the region associated with this spider. Hobo spiders predominate in the Pacific Northwest, where they are frequently mistaken for brown recluses."}},

("l8",21): {"lead": "What stage is this?",
 "opts": ["Stage 1, early localised infection","Stage 2, early disseminated infection",
          "Stage 3, late persistent infection","Cellulitis at the bite site","A tick-bite hypersensitivity reaction"],
 "expl": {4: "A local hypersensitivity reaction to a bite appears within hours and stays small, whereas erythema migrans expands over days to more than 5 cm with central clearing."}},

("l9",0): {"lead": "What is the inheritance pattern?",
 "opts": ["Autosomal dominant","Autosomal recessive","X-linked","A somatic mutation","Not heritable"],
 "expl": {4: "Ephelides are autosomal dominant, and the family pattern with fair skin and red hair is part of the presentation. Calling them non-heritable would discard that."}},

("l9",7): {"lead": "What additional evaluation should be considered?",
 "opts": ["Magnetic resonance imaging of the brain and spine","No imaging at any stage",
          "Complete excision in every case","Observation alone with no imaging","Genetic testing of the parents"],
 "expl": {4: "Congenital naevi arise from somatic mutations rather than inherited ones, so parental genetic testing would not inform the child's risk."}},

("l9",10): {"lead": "What are blue naevi composed of?",
 "opts": ["Deeply pigmented dermal melanocytes","Melanocytes within the epidermis","Proliferating keratinocytes",
          "Lipid-laden macrophages","Dilated dermal capillaries"]},

("l7",31): {"lead": "What is the theoretical basis for using it?",
 "opts": ["It warms the scar, raising collagenase activity","It cools the scar, reducing blood flow",
          "It induces tissue hypoxia","It delivers corticosteroid transdermally","It blocks ultraviolet light"]},

("l9",8): {"lead": "What is this lesion?",
 "opts": ["Nevus spilus","A congenital melanocytic naevus","A cafe au lait macule",
          "A dysplastic naevus","A blue nevus"],
 "expl": {1: "Congenital melanocytic naevi are evident at birth as brown patches or plaques, sometimes with a pebbly surface, but they lack the darker macules and papules scattered within a lighter background that defines nevus spilus."}},

("l6",11): {"lead": "What is the usual duration of first-line oral terbinafine for each?",
 "opts": ["Six weeks fingernails, twelve weeks toenails","Twelve weeks fingernails, six weeks toenails",
          "Two weeks for both","Six weeks for both","Lifelong therapy"]},

("l8",20): {"lead": "What is the term for the aggregate of medical effects caused by caterpillars, moths, and butterflies?",
 "opts": ["Lepidopterism","Erucism","Arachnidism","Tungiasis","Cercarial dermatitis"]},

("l6",22): {"lead": "What does that finding signify?",
 "opts": ["Hutchinson sign, which increases ocular risk",
          "Hutchinson sign, whose absence would exclude eye disease",
          "Disseminated zoster","Ramsay Hunt syndrome","Zoster sine herpete"]},
}
