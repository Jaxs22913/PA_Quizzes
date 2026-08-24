# -*- coding: utf-8 -*-
# CMS I Lecture 9 -- pool H. DIAGNOSTIC TESTING, the question she said she would write.
#
# WHY THIS EXISTS. In the 24 August lecture Professor Jaquith repeatedly stopped
# to say she was going to set "how do you diagnose this?" questions -- on
# squamous cell carcinoma ("what's our diagnostic testing? We're biopsying it
# ... I should definitely give you a question on that"), on melanoma ("Biopsy,
# great. I'm totally gonna write a question for that. I haven't done these
# questions yet"), and on cutaneous T-cell lymphoma ("you guys know that
# question for everyone for this lecture at least ... do a biopsy is how you're
# gonna diagnose this").
#
# Measured against the pools, Lecture 9 had the THINNEST diagnostic-test
# coverage of any lecture in the exam -- 2 questions in 108, 1.9%. Only actinic
# keratosis and melanoma had one at all. Squamous cell, basal cell, Kaposi
# sarcoma and cutaneous T-cell lymphoma had none, even though the deck carries a
# dedicated "Differential Diagnosis & Diagnostic Testing" slide for every one of
# them naming the specific technique.
#
# THE ANSWER IS NOT SIMPLY "BIOPSY" AND THAT IS THE POINT. Each condition names
# a different technique or a different caveat: shave or punch for basal cell,
# depth sufficient to separate in situ from invasive for squamous cell, a
# representative lesion with human herpesvirus 8 findings for Kaposi, and for
# cutaneous T-cell lymphoma untreated lesions, possibly several, with a single
# negative biopsy not excluding the disease. Questions that accept a bare
# "biopsy" would not test what the slides actually say.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"

POOL_H = [
 dict(topic="Squamous cell carcinoma", io=IO, slot="initial test",
   q="How is a suspected squamous cell carcinoma diagnosed, and what must the sample achieve?",
   opts=[
     ["Shave, punch or excisional biopsy sampling sufficient depth to separate in situ from invasive disease",
      "Correct — depth is the point, because in situ and invasive carry different treatment, margins and risk."],
     ["Shave biopsy only, since deeper sampling risks seeding the tumour",
      "The deck offers three techniques and says nothing about seeding."],
     ["Clinical diagnosis alone, with biopsy reserved for recurrence",
      "That is closer to the actinic keratosis rule, not squamous cell carcinoma."],
     ["Dermoscopy, with biopsy only if dermoscopy is inconclusive",
      "Dermoscopy supports recognition of actinic keratosis; it is not the squamous cell pathway."]],
   c=0, cite=c(23)),

 dict(topic="Squamous cell carcinoma", io=IO, slot="test finding",
   q="Which five features should the pathology report identify in a squamous cell carcinoma?",
   opts=[
     ["Differentiation grade, depth or thickness, perineural or perivascular invasion, margin status, and aggressive subtype",
      "Correct — all five, and each of them feeds the decision about Mohs and about follow-up."],
     ["Differentiation grade, Breslow thickness, ulceration, mitotic rate, and margin status",
      "Breslow thickness, ulceration and mitotic rate belong to melanoma reporting."],
     ["Histopathologic subtype alone, since that dictates treatment selection",
      "Subtype alone is the basal cell carcinoma emphasis."],
     ["Human herpesvirus 8 findings, immune status, and margin status",
      "Those relate to Kaposi sarcoma."]],
   c=0, cite=c(23)),

 dict(topic="Squamous cell carcinoma", io=IO, slot="initial test",
   q="What regional assessment does the deck require alongside biopsy of a squamous cell carcinoma?",
   opts=[
     ["Palpate the draining lymph-node basins, considering imaging or nodal evaluation for high-risk tumours",
      "Correct — the nodes are examined at diagnosis, not only at follow-up."],
     ["Routine computed tomography of the chest, abdomen and pelvis in every case",
      "Routine staging imaging is not required for typical disease."],
     ["Sentinel lymph node biopsy in every case over one centimetre",
      "Sentinel node biopsy is a melanoma pathway in this deck."],
     ["No regional assessment, since actinically induced disease rarely spreads",
      "The metastatic rate is three to seven per cent, and the nodes are examined."]],
   c=0, cite=c(23)),

 dict(topic="Basal cell carcinoma", io=IO, slot="initial test",
   q="How should a suspected basal cell carcinoma be sampled?",
   opts=[
     ["With a shave or punch biopsy, to confirm the diagnosis",
      "Correct — and the pathology then determines the histologic subtype, which dictates treatment."],
     ["With an excisional biopsy taken to below the lesion, to preserve depth",
      "That depth requirement belongs to the melanoma rule."],
     ["With a deep shave sampling sufficient depth to separate in situ from invasive disease",
      "That is the squamous cell carcinoma requirement."],
     ["It is a clinical diagnosis and biopsy is not usually required",
      "The deck says suspected basal cell carcinoma should be sampled."]],
   c=0, cite=c(36)),

 dict(topic="Basal cell carcinoma", io=IO, slot="avoid",
   q="What does the deck say about imaging in typical localized basal cell carcinoma?",
   opts=[
     ["Routine imaging is not needed; it is reserved for advanced, deeply invasive or metastatic disease",
      "Correct — and that specialist-directed workup is the exception rather than the rule."],
     ["Routine imaging of the affected region is required before any excision",
      "The deck states routine imaging is not needed."],
     ["Magnetic resonance imaging is required whenever the lesion is on the face",
      "Facial site drives Mohs selection, not routine imaging."],
     ["Imaging replaces biopsy when the lesion is in a tissue-sensitive site",
      "Biopsy is still what confirms the diagnosis."]],
   c=0, cite=c(36)),

 dict(topic="Kaposi sarcoma", io=IO, slot="initial test",
   q="How is Kaposi sarcoma confirmed, and what supports the diagnosis on histology?",
   opts=[
     ["Biopsy of a representative lesion, with human herpesvirus 8-associated findings supporting it",
      "Correct — the virus links the histology back to the cause."],
     ["Biopsy of the largest lesion, with Epstein-Barr virus findings supporting it",
      "The virus is human herpesvirus 8, and the lesion should be representative rather than largest."],
     ["Clinical appearance alone, since the violaceous colour is characteristic",
      "The deck says explicitly to discriminate by more than colour alone."],
     ["Human immunodeficiency virus testing alone, since that establishes the context",
      "Immune context is assessed, but biopsy confirms the diagnosis."]],
   c=0, cite=c(65)),

 dict(topic="Kaposi sarcoma", io=IO, slot="differential",
   q="Which features does the deck say to use when discriminating Kaposi sarcoma from its lookalikes?",
   opts=[
     ["Immune status, distribution, oral lesions, oedema, visceral symptoms and biopsy — not colour alone",
      "Correct — the warning against relying on colour is the point of the list."],
     ["Colour, size and symmetry of the lesions",
      "Colour alone is exactly what the deck warns against."],
     ["Breslow thickness, ulceration and mitotic rate",
      "Those are melanoma pathology variables."],
     ["Chronicity, treatment resistance and follicular hair loss",
      "Those are the cutaneous T-cell lymphoma discriminators."]],
   c=0, cite=c(65)),

 dict(topic="Kaposi sarcoma", io=IO, slot="initial test",
   q="How does the deck define the immune context once Kaposi sarcoma is suspected?",
   opts=[
     ["Test for human immunodeficiency virus if status is unknown; if known, assess CD4 count, viral load, antiretroviral history and adherence",
      "Correct — knowing the status is not enough, the degree of immune suppression matters."],
     ["Test for human immunodeficiency virus only if the patient reports risk factors",
      "The deck tests when status is unknown, not only on reported risk."],
     ["Assess CD4 count alone, since it determines prognosis",
      "Viral load, therapy history and adherence are assessed too."],
     ["No immune assessment is needed once biopsy confirms the diagnosis",
      "Defining the immune context is a listed step."]],
   c=0, cite=c(65)),

 dict(topic="Kaposi sarcoma", io=IO, slot="escalation",
   q="Which directed procedures does the deck reserve for symptomatic Kaposi sarcoma rather than performing routinely?",
   opts=[
     ["Bronchoscopy for suspected pulmonary disease, and endoscopy driven by symptoms or management rather than routinely in asymptomatic patients",
      "Correct — a chest radiograph is used when pulmonary involvement is possible, but scoping is not routine."],
     ["Bronchoscopy and endoscopy in every newly diagnosed patient",
      "The deck states endoscopy is not routine in asymptomatic patients."],
     ["Computed tomography of the chest in every newly diagnosed patient",
      "A chest radiograph is what the deck names, and only when pulmonary involvement is possible."],
     ["No further evaluation once the skin lesions are biopsied",
      "A complete extent assessment is required."]],
   c=0, cite=c(65)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="initial test",
   q="Which lesion should be selected for skin biopsy in suspected cutaneous T-cell lymphoma?",
   opts=[
     ["An active, representative, UNTREATED lesion, coordinating with dermatopathology",
      "Correct — treating a lesion first can obscure the very histology you are trying to read."],
     ["The oldest and most heavily treated lesion, since it is most established",
      "Treatment alters the histology; the deck specifies untreated."],
     ["Any lesion, since the histology is uniform across the disease",
      "The deck asks for an active, representative lesion specifically."],
     ["A lymph node rather than skin, since staging matters more",
      "Node biopsy is for advanced disease; skin biopsy gives the histologic diagnosis."]],
   c=0, cite=c(74)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="avoid",
   q="A biopsy for suspected cutaneous T-cell lymphoma comes back nondiagnostic, but the clinical picture still fits. What does the deck say?",
   opts=[
     ["A single nondiagnostic biopsy does not exclude the disease; correlate clinically and reassess over time",
      "Correct — and numerous biopsies may be needed, which is why patients are warned in advance."],
     ["The diagnosis is excluded and an alternative should be pursued",
      "The deck states the opposite explicitly."],
     ["Proceed directly to systemic therapy on clinical grounds alone",
      "Skin-directed, stage-guided care follows a diagnosis, not a nondiagnostic biopsy."],
     ["Repeat the biopsy from the same site after treating it topically first",
      "Lesions selected for biopsy should be untreated."]],
   c=0, cite=c(74)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="escalation",
   q="Which blood tests does the deck list for ADVANCED cutaneous T-cell lymphoma?",
   opts=[
     ["Complete blood count with differential, eosinophilia, circulating Sezary cells, T-cell gene-rearrangement testing and specialist flow cytometry",
      "Correct — these belong to advanced disease rather than to the initial skin diagnosis."],
     ["Complete blood count alone, repeated at every visit",
      "The deck lists a fuller panel for advanced disease."],
     ["Human herpesvirus 8 serology and CD4 count",
      "Those belong to Kaposi sarcoma."],
     ["Serum lead level and ferritin",
      "Neither is part of this workup."]],
   c=0, cite=c(74)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="differential",
   q="Which discriminators separate cutaneous T-cell lymphoma from psoriasis, eczema and tinea?",
   opts=[
     ["Chronicity, treatment resistance, large or oddly distributed patches, severe pruritus, follicular hair loss, tumours or erythroderma, nodes, and histology over time",
      "Correct — no single one settles it, which is why longitudinal reassessment is stressed."],
     ["The colour and symmetry of the lesions alone",
      "That is the reasoning the Kaposi slide warns against."],
     ["A positive potassium hydroxide preparation",
      "That would point to tinea, and is not the discriminator list given."],
     ["Response to a two-week course of topical corticosteroid",
      "Treatment RESISTANCE is a discriminator, but a steroid trial is not the listed method."]],
   c=0, cite=c(74)),

 dict(topic="Actinic keratosis", io=IO, slot="initial test",
   q="What triggers a biopsy of an actinic keratosis, and which technique is used?",
   opts=[
     ["Morphology or behaviour raising concern for squamous cell carcinoma, or persistence or recurrence after therapy; shave or punch biopsy",
      "Correct — both triggers and the technique, from the same slide."],
     ["Any actinic keratosis on the face, using an excisional biopsy",
      "Site alone is not the trigger, and excision is not the named technique."],
     ["Failure of a single cryotherapy treatment, using a deep shave",
      "Persistence or recurrence after therapy is the trigger, not a single treatment failure specifically."],
     ["Any lesion over one centimetre, using a punch biopsy",
      "No size threshold is given."]],
   c=0, cite=c(13)),

 dict(topic="Actinic keratosis", io=IO, slot="test finding",
   q="What must the pathologist distinguish when an actinic keratosis is biopsied, and why does it matter?",
   opts=[
     ["Actinic keratosis versus squamous cell carcinoma in situ versus invasive squamous cell carcinoma, because invasion changes treatment, margins and risk substantially",
      "Correct — three possibilities, not two, and the consequence is what makes it worth asking."],
     ["Actinic keratosis versus seborrhoeic keratosis, because the treatments differ",
      "Seborrhoeic keratosis is on the differential but is not the interpretation question."],
     ["Hypertrophic versus atrophic actinic keratosis, because that guides field therapy",
      "The deck does not divide it this way."],
     ["Whether the lesion is on a field-cancerized site, because that guides surveillance",
      "Field cancerization matters, but it is not what the pathologist distinguishes."]],
   c=0, cite=c(13)),

 dict(topic="Nail unit neoplasms", io=IO, slot="referral",
   q="What does the deck require of a biopsy for a suspicious nail lesion?",
   opts=[
     ["Prompt referral to a dermatologist experienced in nail-unit biopsy, with the biopsy sampling the correct site",
      "Correct — the referral is to someone experienced in the nail unit specifically."],
     ["A shave biopsy of the nail plate itself, taken in primary care",
      "The nail plate is not the target and the deck asks for experienced referral."],
     ["Observation with photographs for three months before any biopsy",
      "Photography is encouraged but must not delay referral."],
     ["Removal of the entire digit for histologic assessment",
      "Amputation is reserved for deep, extensive or bone-involving disease."]],
   c=0, cite=c(93)),
]
