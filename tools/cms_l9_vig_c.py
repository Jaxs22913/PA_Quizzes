# -*- coding: utf-8 -*-
# CMS I Lecture 9 — SET 2, vignette pool C. Kaposi sarcoma, cutaneous T-cell
# lymphoma, nail unit neoplasms.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

VIG_C = [
 dict(topic="Kaposi sarcoma", io=IOA, lead="diagnosis",
   q="A 34-year-old man newly diagnosed with human immunodeficiency virus has several red-purple plaques on his legs. Which examination is called essential, and what might you find?",
   opts=[
     ["Oral examination — hard palate lesions are common and may be the presenting site",
      "Correct — the mouth may declare the disease before anywhere else."],
     ["Nail examination — subungual lesions are common and may be the presenting site",
      "Mucosal involvement is common and the hard palate is a frequent presenting site, so it is the mouth rather than the nails that must be examined."],
     ["Ocular examination — eyelid lesions are common and may be the presenting site",
      "Eyelid lesions occur but are not the essential examination; the oral mucosa, and the hard palate in particular, is the site that must be inspected."],
     ["Scalp examination — follicular lesions are common and may be the presenting site",
      "Follicular involvement is a cutaneous T-cell lymphoma clue."]],
   c=0, cite=c(64)),

 dict(topic="Kaposi sarcoma", io=IOB, lead="treatment",
   q="A 34-year-old man newly diagnosed with human immunodeficiency virus has several red-purple plaques on his legs and is not yet on antiretroviral therapy. Which is the first priority in his Kaposi sarcoma management?",
   opts=[
     ["Begin or optimise antiretroviral therapy, since immune restoration is the cornerstone of treatment for epidemic disease",
      "Correct — antiretroviral therapy comes before local or systemic cancer treatment."],
     ["Begin liposomal doxorubicin and paclitaxel, since systemic chemotherapy is the cornerstone of epidemic disease",
      "Chemotherapy is added for advanced disease after antiretroviral therapy."],
     ["Begin intralesional vinblastine to each plaque, since local palliation is the cornerstone of epidemic disease",
      "That is the approach in classic disease of older adults."],
     ["Reduce his immunosuppressive medication doses, since dose reduction is the cornerstone of epidemic disease",
      "That applies to the iatrogenic form."]],
   c=0, cite=c(66)),

 dict(topic="Kaposi sarcoma", io=IOA, lead="test",
   q="A patient with known Kaposi sarcoma has marked lower limb oedema but only three visible skin lesions. How should the oedema be interpreted?",
   opts=[
     ["Marked oedema can occur even with few or no visible lesions, so its severity must not be used to gauge disease burden",
      "Correct — the skin can look almost clear while disease is extensive."],
     ["Marked oedema indicates a correspondingly low disease burden, consistent with the small number of visible skin lesions",
      "Oedema severity does not track lesion count."],
     ["Marked oedema is not a feature of Kaposi sarcoma at any stage and points instead to venous thrombosis",
      "It is an explicit feature of the disease."],
     ["Marked oedema indicates the classic rather than the epidemic form, and its severity gauges the disease burden",
      "No such form-specific rule is given."]],
   c=0, cite=c(64)),

 dict(topic="Kaposi sarcoma", io=IOB, lead="next step",
   q="A 61-year-old kidney transplant recipient develops Kaposi sarcoma. Which is the most appropriate management step, and what caution applies?",
   opts=[
     ["Reduce immunosuppressive medication doses where clinically feasible, coordinating with the transplant team before making any change",
      "Correct — the transplant team must be involved before doses change."],
     ["Reduce immunosuppressive medication doses immediately without involving the transplant team, since the malignancy takes priority",
      "Reducing immunosuppression may clear the tumour but risks rejecting the graft, so that trade-off is decided with the team managing the transplant."],
     ["Begin or optimise antiretroviral therapy, since immune restoration is the cornerstone of treatment",
      "That applies to epidemic, acquired immunodeficiency-associated disease."],
     ["Begin liposomal doxorubicin and paclitaxel first, since iatrogenic disease does not respond to dose reduction",
      "Dose reduction is the first step for the iatrogenic form."]],
   c=0, cite=c(66)),

 dict(topic="Cutaneous T-cell lymphoma", io=IOA, lead="diagnosis",
   q="A 57-year-old has had itchy scaly plaques on the trunk for four years, several larger than 5 cm. They have been treated as eczema and then as psoriasis without lasting response, and he has patchy hair loss within some plaques. Which is the most likely diagnosis?",
   opts=[
     ["Cutaneous T-cell lymphoma", "Correct — chronicity, treatment resistance and follicular involvement together."],
     ["Psoriasis", "It is a named mimic, but it would not resist treatment for years with follicular hair loss."],
     ["Eczematous dermatitis", "It is a named mimic, but the folliculotropic hair loss discriminates against it."],
     ["Tinea corporis", "It is a named mimic, but potassium hydroxide and treatment response would separate it."]],
   c=0, cite=c(74)),

 dict(topic="Cutaneous T-cell lymphoma", io=IOA, lead="test",
   q="A 62-year-old man has a chronic pruritic eruption that has not settled on treatment. Which two clinical clues should raise suspicion of cutaneous T-cell lymphoma?",
   opts=[
     ["Itch out of proportion to the apparent inflammatory activity, and follicular involvement with hair loss",
      "Correct — folliculotropism discriminates from routine eczema or psoriasis."],
     ["Complete absence of itch, and sparing of the hair follicles throughout the eruption",
      "Pruritus is common and may be severe, and follicular involvement is the clue."],
     ["Rapid complete response to a topical corticosteroid, and sharply demarcated silvery scale",
      "Treatment resistance rather than rapid response is the discriminator."],
     ["Annular plaques with central clearing, and a positive potassium hydroxide preparation from the border",
      "That describes tinea, one of the mimics."]],
   c=0, cite=c(70)),

 dict(topic="Cutaneous T-cell lymphoma", io=IOA, lead="treatment",
   q="A patient with early-stage cutaneous T-cell lymphoma asks whether aggressive chemotherapy now would cure it. Which is the most appropriate response?",
   opts=[
     ["Early aggressive treatment has not been proven to cure the disease or prevent progression, and may itself cause harm",
      "Correct — overly aggressive therapy may cause complications and premature death, so a stage-directed, skin-first approach suits most early disease. Aggression is a harm here rather than a virtue."],
     ["Early aggressive systemic chemotherapy reliably cures the disease and prevents progression, so it should begin immediately",
      "Early aggressive chemotherapy has not been shown to cure the disease or prevent progression, and its complications can shorten a life that would otherwise run for decades."],
     ["No treatment of any kind alters the course, so observation alone is appropriate at every stage",
      "Skin-directed therapy is offered for early disease."],
     ["Total-skin electron-beam treatment should be given first to every patient regardless of stage",
      "That is reserved for progressive disease."]],
   c=0, cite=c(75)),

 dict(topic="Nail unit neoplasms", io=IOA, lead="diagnosis",
   q="A 55-year-old has a brown band running the length of the left thumbnail. Over eight months it has widened, the lines within it vary in colour and spacing, and pigment now extends onto the skin of the proximal nail fold. Which finding is most concerning, and what is it called?",
   opts=[
     ["The pigment extending onto the proximal nail fold — the Hutchinson sign, highly concerning for nail unit melanoma",
      "Correct — it should prompt urgent expert evaluation regardless of other features."],
     ["The widening of the band — the Hutchinson sign, highly concerning for nail unit melanoma",
      "Widening is concerning, but the Hutchinson sign is the periungual pigment."],
     ["The variation in line colour and spacing — the Hutchinson sign, concerning for a benign melanonychia",
      "That variation is concerning, but it is not the Hutchinson sign."],
     ["The eight-month duration — the Hutchinson sign, concerning for a subungual haematoma",
      "Duration is not the sign, and a haematoma would grow out."]],
   c=0, cite=c(84)),

 dict(topic="Nail unit neoplasms", io=IOA, lead="next step",
   q="A 48-year-old has a red, eroded, mass-like lesion under one fingernail with no pigment at all. It has progressed over five months. Which is the most appropriate next step?",
   opts=[
     ["Consider biopsy — amelanotic nail melanoma can look red, pink, eroded or mass-like",
      "Correct — the absence of pigment does not exclude melanoma, so biopsy any unexplained, progressive single-nail lesion."],
     ["Reassure, because the complete absence of a pigmented band reliably excludes melanoma",
      "A proportion of nail melanomas produce no pigment at all, appearing as a red or eroded mass, so absence of a dark band cannot exclude the diagnosis."],
     ["Treat empirically for onychomycosis and review in six months",
      "Treating empirically for fungus and reviewing in six months is how nail melanoma is missed; a progressive destructive nail lesion needs sampling."],
     ["Treat as a chronic paronychia with oral antibiotics and review in six weeks",
      "Labelling it a chronic paronychia delays diagnosis in exactly the way that costs digits; a progressive mass-like nail lesion is biopsied."]],
   c=0, cite=c(84)),

 dict(topic="Nail unit neoplasms", io=IOA, lead="diagnosis",
   q="A 41-year-old describes severe stabbing pain under one fingernail, worse in cold water, with an exquisitely tender point. The nail itself looks almost normal, with a small red-blue spot beneath it. Which is the most likely diagnosis?",
   opts=[
     ["Glomus tumour", "Correct — the triad of paroxysmal pain, point tenderness and cold sensitivity."],
     ["Nail unit melanoma", "That presents with pigment change or a mass rather than this pain triad."],
     ["Nail unit squamous cell carcinoma", "That is a chronic verrucous periungual plaque with hyperkeratosis."],
     ["Subungual haematoma", "That follows trauma and grows out with the nail."]],
   c=0, cite=c(86)),

 dict(topic="Nail unit neoplasms", io=IOA, lead="diagnosis",
   q="A 67-year-old has had a warty plaque beside one fingernail for two years. It has been treated repeatedly as a wart and once as a fungal infection, and now oozes and bleeds with nail plate destruction. Which is the most likely diagnosis?",
   opts=[
     ["Nail unit squamous cell carcinoma",
      "Correct — this is the commonest malignant nail tumour, called Bowen disease while confined to the epithelium, and a lesion repeatedly relabelled wart, paronychia or fungus is the classic history."],
     ["Nail unit melanoma",
      "Nail unit melanoma occurs but is far less common, and it more often presents as a pigmented band or an amelanotic eroded mass than as a warty plaque."],
     ["Nail unit basal cell carcinoma",
      "Nail unit basal cell carcinoma is exceptionally uncommon, since the nail unit receives little ultraviolet exposure; squamous cell carcinoma is the common malignant nail tumour."],
     ["Onychomatricoma",
      "Onychomatricoma is a benign tumour of the nail matrix, producing a thickened yellow nail with longitudinal ridging rather than destruction and bleeding."]],
   c=0, cite=c(79)),

 dict(topic="Nail unit neoplasms", io=IOB, lead="education",
   q="A patient with a confirmed nail unit melanoma asks whether she will lose the finger. Which is the most appropriate response?",
   opts=[
     ["Amputation is not automatic — digit-sparing wide excision or Mohs with immunostaining is contemporary care",
      "Correct — amputation is reserved for deep, extensive or bone-involving disease, and the digit is preserved where margins can be reliably assessed."],
     ["Amputation is the automatic first treatment for any nail unit melanoma, whatever the depth or extent",
      "Margins can be assessed in the nail unit using Mohs with immunostaining, so digit-sparing excision is standard and amputation is reserved for deep or bone-involving disease."],
     ["Amputation is never performed for nail unit melanoma at any depth or extent",
      "It is reserved for deep, extensive or bone-involving disease."],
     ["Amputation is decided by the number of digits involved rather than by depth or bone involvement",
      "Depth, extent and bone involvement are the criteria."]],
   c=0, cite=c(94)),
]
