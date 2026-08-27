# -*- coding: utf-8 -*-
# CMS I Lecture 9 -- pool G. CORRECTIVE POOL.
#
# WHY THIS EXISTS. check_slot_coverage.py --floors was run AFTER partitioning
# rather than before, which is the standing rule for this class, and it found
# Lecture 9 under floor on nine slots -- including `avoid` at ZERO. Pools A to F
# had covered the front half of the fact frame (what is it, what does it look
# like, how is it treated) and thinned out across the back half: what to avoid,
# what to tell the patient, what goes wrong.
#
# The deck was not thin there. It carries a dedicated "Referral, Education &
# Prognosis" slide for EVERY condition, and re-reading those slides turned up
# content that had been missed entirely -- most importantly KAPOSI SARCOMA
# IMMUNE RECONSTITUTION INFLAMMATORY SYNDROME, which is a way treatment itself
# makes the disease worse, and the nail unit's explicit warning against repeated
# empiric antifungal or wart treatment.
#
# IT ALSO CORRECTED A CONFLATION OF MINE. The deck lists the BCC subtypes TWICE
# and they are not the same list: CLINICAL is superficial, nodular, pigmented,
# morpheaform; HISTOLOGIC is superficial, nodular, micronodular, infiltrative.
# It is the HISTOLOGIC subtype that determines behaviour. Earlier questions and
# the guide had presented the clinical list as though it were the histologic one.
#
# Weighted deliberately to the thin slots rather than spread evenly.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO = "1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"

POOL_G = [
 # ---------------- avoid (was 0) ----------------
 dict(topic="Nail unit neoplasms", io=IO, slot="avoid",
   q="A single nail abnormality has persisted despite treatment. What does the deck say to avoid?",
   opts=[
     ["Repeated empiric antifungal, antibiotic or wart treatment",
      "Correct — repeating empiric therapy on a solitary persistent nail lesion is how diagnostic delay happens."],
     ["Photographing the nail before referral",
      "Photography is encouraged, so long as it does not delay referral."],
     ["Examining the other nine nails",
      "Every nail should be examined, not avoided."],
     ["Removing the nail polish before examination",
      "Removing polish is required, not avoided."]],
   c=0, cite=c(95)),

 dict(topic="Nail unit neoplasms", io=IO, slot="avoid",
   q="The deck says to photograph a concerning pigmented band. What caution comes with that?",
   opts=[
     ["Do not let photographing it delay referral",
      "Correct — documentation is for tracking change, not for postponing the specialist."],
     ["Do not photograph it, because pigment renders inaccurately",
      "The deck recommends photographing it."],
     ["Do not photograph it until the polish has regrown",
      "Polish is removed for examination, and this is not a stated caution."],
     ["Do not photograph more than one nail at a time",
      "No such restriction is given."]],
   c=0, cite=c(95)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="avoid",
   q="What harm does the deck attribute to overly aggressive cutaneous T-cell lymphoma therapy?",
   opts=[
     ["Complications and premature death",
      "Correct — and early aggressive treatment has not been proven to cure disease or prevent progression."],
     ["Accelerated transformation to systemic lymphoma",
      "Not the harm the deck names."],
     ["Permanent phototherapy intolerance",
      "Not a harm the deck states."],
     ["Loss of eligibility for a cutaneous lymphoma centre",
      "Not a claim the deck makes."]],
   c=0, cite=c(76)),

 dict(topic="Kaposi sarcoma", io=IO, slot="avoid",
   q="Why must oedema severity not be used to judge Kaposi sarcoma burden?",
   opts=[
     ["Marked oedema may occur with few or no visible skin lesions",
      "Correct — the deck says explicitly not to use oedema severity alone."],
     ["Oedema in Kaposi sarcoma is always caused by the antiretroviral therapy",
      "Not a claim the deck makes."],
     ["Oedema only appears once visceral disease is established",
      "The deck does not tie oedema to visceral disease this way."],
     ["Oedema resolves within days of starting treatment",
      "Not stated, and it would not make severity a valid gauge."]],
   c=0, cite=c(60)),

 dict(topic="Actinic keratosis", io=IO, slot="avoid",
   q="A course of field therapy has cleared a patient's actinic keratoses. What must not be assumed?",
   opts=[
     ["That surveillance can stop, because the surrounding field remains at risk",
      "Correct — ongoing surveillance remains necessary despite successful therapy."],
     ["That the treatment reactions of erythema and crusting were abnormal",
      "Those are expected local reactions the patient is warned about."],
     ["That daily sun protection is still required",
      "Sun protection remains part of the education, so this is not the false assumption."],
     ["That a nonhealing lesion should be reviewed promptly",
      "Prompt review of a nonhealing or changing lesion is exactly what is advised."]],
   c=0, cite=c(15)),

 # ---------------- complication (was 1) ----------------
 dict(topic="Kaposi sarcoma", io=IO, slot="complication",
   q="What is Kaposi sarcoma immune reconstitution inflammatory syndrome?",
   opts=[
     ["Kaposi sarcoma present when antiretroviral therapy begins can worsen as the immune system recovers",
      "Correct — the treatment itself can make the disease worse before it improves."],
     ["Kaposi sarcoma appearing for the first time years after antiretroviral therapy begins",
      "The syndrome concerns disease already present when therapy starts."],
     ["Kaposi sarcoma that fails to respond to antiretroviral therapy at all",
      "Non-response is not what this syndrome describes."],
     ["An allergic reaction to liposomal doxorubicin",
      "It is an immune phenomenon related to starting antiretroviral therapy."]],
   c=0, cite=c(63)),

 dict(topic="Kaposi sarcoma", io=IO, slot="complication",
   q="In which patients is Kaposi sarcoma immune reconstitution inflammatory syndrome especially dangerous?",
   opts=[
     ["Those with visceral disease",
      "Correct — endemic or visceral disease and this syndrome can be aggressive and rapidly fatal."],
     ["Those with classic Kaposi sarcoma",
      "Classic disease is usually indolent and rarely fatal."],
     ["Those with only oral lesions",
      "The deck singles out visceral disease."],
     ["Those over seventy years old",
      "Age is not the risk the deck names here."]],
   c=0, cite=c(63)),

 dict(topic="Basal cell carcinoma", io=IO, slot="complication",
   q="Where does the morbidity of basal cell carcinoma come from?",
   opts=[
     ["Local destruction, recurrence, delayed diagnosis and anatomically complex sites",
      "Correct — metastatic disease is rare but serious, and hedgehog inhibitor therapy exists for it."],
     ["Nodal metastasis in three to seven per cent of cases",
      "That figure belongs to actinically induced squamous cell carcinoma."],
     ["Perineural spread to the skull base in most cases",
      "Not the stated source of morbidity."],
     ["Transformation into squamous cell carcinoma",
      "The deck does not describe this transformation."]],
   c=0, cite=c(38)),

 dict(topic="Nail unit neoplasms", io=IO, slot="complication",
   q="What increases recurrence and functional morbidity in nail unit squamous cell carcinoma?",
   opts=[
     ["Incomplete excision, immunosuppression, delayed diagnosis and bone invasion",
      "Correct — it is often curable with complete surgery, which is why incompleteness matters."],
     ["Complete margin-controlled surgery",
      "That is the treatment that reduces recurrence."],
     ["Photographing the lesion before referral",
      "Documentation does not affect recurrence."],
     ["A negative human papillomavirus result",
      "Not a factor the deck names."]],
   c=0, cite=c(95)),

 # ---------------- education (was 2) ----------------
 dict(topic="Kaposi sarcoma", io=IO, slot="education",
   q="What must a patient starting antiretroviral therapy for Kaposi sarcoma be told?",
   opts=[
     ["That the lesions may worsen early, as immune reconstitution inflammatory syndrome",
      "Correct — warning them beforehand stops early worsening being read as treatment failure."],
     ["That the lesions will always improve within two weeks",
      "The deck warns of possible early worsening instead."],
     ["That antiretroviral therapy should be stopped if lesions enlarge",
      "Stopping therapy is not what the deck advises."],
     ["That oral lesions never respond to therapy",
      "Not a claim the deck makes."]],
   c=0, cite=c(67)),

 dict(topic="Melanoma", io=IO, slot="education",
   q="Which melanoma subtype does the deck say is frequently delayed in diagnosis, making early reporting critical?",
   opts=[
     ["Acral lentiginous melanoma",
      "Correct — which is why patients are told to report new pigment, widening bands or periungual pigment promptly."],
     ["Superficial spreading melanoma",
      "The commonest subtype, but not the one flagged for diagnostic delay."],
     ["Lentigo maligna melanoma",
      "Not the subtype flagged here."],
     ["Nodular melanoma",
      "Nodular melanoma is flagged for rapid growth and lacking classic features, not for reporting delay."]],
   c=0, cite=c(56)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="education",
   q="What does the deck say patients should be told about establishing the cutaneous T-cell lymphoma diagnosis?",
   opts=[
     ["It may require repeated biopsies, and the disease is usually chronic",
      "Correct — setting that expectation early matters, because the diagnosis is often slow to confirm."],
     ["A single biopsy is definitive in nearly all cases",
      "The deck says repeated biopsies may be needed."],
     ["The diagnosis is made clinically and biopsy is unnecessary",
      "Biopsy is central to the diagnosis."],
     ["Blood testing establishes the diagnosis before any biopsy",
      "Not what the deck states."]],
   c=0, cite=c(76)),

 dict(topic="Basal cell carcinoma", io=IO, slot="education",
   q="Which two things must a patient on topical therapy for basal cell carcinoma understand?",
   opts=[
     ["That local inflammation is expected, and that clearance has to be confirmed afterwards",
      "Correct — the inflammation is not a reason to stop, and clearing visibly is not the same as being clear."],
     ["That inflammation means the drug has failed, and treatment should stop",
      "Inflammation is an expected reaction."],
     ["That clearance is assumed once the lesion is no longer visible",
      "The deck requires clearance to be confirmed."],
     ["That sun protection is unnecessary once treatment begins",
      "Sun protection remains part of the education."]],
   c=0, cite=c(38)),

 dict(topic="Actinic keratosis", io=IO, slot="education",
   q="Which local reactions should an actinic keratosis patient be warned to expect from field therapy?",
   opts=[
     ["Erythema and crusting, alongside adherence to the full treatment duration",
      "Correct — patients who are not warned stop the course early."],
     ["Permanent hypopigmentation at every treated site",
      "Not the expected reaction the deck names."],
     ["Blistering that requires the course to be abandoned",
      "The deck emphasises adherence to the duration."],
     ["No visible reaction at all if the therapy is working",
      "A local reaction is expected."]],
   c=0, cite=c(15)),

 # ---------------- initial test / gold standard ----------------
 dict(topic="Basal cell carcinoma", io=IO, slot="gold standard",
   q="Which basal cell carcinoma subtype list determines behaviour and treatment?",
   opts=[
     ["The HISTOLOGIC list: superficial, nodular, micronodular and infiltrative",
      "Correct — and note it differs from the CLINICAL list, which is superficial, nodular, pigmented and morpheaform."],
     ["The CLINICAL list: superficial, nodular, pigmented and morpheaform",
      "That is what you see; the deck says the histologic subtype dictates treatment selection."],
     ["Either list, since the two are identical",
      "They are not identical: pigmented and morpheaform are clinical, micronodular and infiltrative histologic."],
     ["Neither, since size determines treatment",
      "The deck attributes it to histologic subtype."]],
   c=0, cite=c(33)),

 dict(topic="Basal cell carcinoma", io=IO, slot="initial test",
   q="What must be assessed when planning basal cell carcinoma treatment?",
   opts=[
     ["Whether it is low-risk versus morpheaform, micronodular, infiltrative, recurrent, or in a tissue-sensitive site",
      "Correct — the deck says this directly changes treatment selection."],
     ["Whether the patient has had nicotinamide previously",
      "Chemoprevention is separate from treatment selection."],
     ["Whether the lesion is pigmented or not",
      "Pigmentation is a clinical descriptor rather than the risk stratifier."],
     ["Whether the patient can tolerate hedgehog inhibitors",
      "Those are reserved for advanced disease."]],
   c=0, cite=c(28)),

 dict(topic="Actinic keratosis", io=IO, slot="initial test",
   q="Which lesion features make early squamous cell carcinoma the distinction to exclude in an actinic keratosis?",
   opts=[
     ["Thick, indurated, ulcerated, enlarging, painful, bleeding, persistent or recurrent",
      "Correct — the deck's full list of features that shift the concern to carcinoma."],
     ["Rough, flat, flesh-coloured and better felt than seen",
      "That is a typical actinic keratosis."],
     ["Pearly, translucent, with telangiectasias",
      "That describes nodular basal cell carcinoma."],
     ["Scaly, symmetric and under two millimetres",
      "Nothing in that combination raises the concern."]],
   c=0, cite=c(13)),

 # ---------------- etiology / risk factors ----------------
 dict(topic="Squamous cell carcinoma", io=IO, slot="risk factors",
   q="Besides sun exposure and immunosuppression, which risk factors does the deck list for squamous cell carcinoma?",
   opts=[
     ["Chronic wounds, scars or prior radiation fields; certain genetic diseases; and mucosal or genital disease",
      "Correct — the three additional categories as listed."],
     ["Tanning beds, fair skin and male sex only",
      "Those fall under the sun-exposure and population description."],
     ["Chronic lymphocytic leukaemia and human immunodeficiency virus only",
      "Those are named under immunosuppression."],
     ["Red tattoo ink, laser treatment and cryotherapy",
      "Those are keratoacanthoma risk factors from Lecture 7."]],
   c=0, cite=c(21)),

 dict(topic="Basal cell carcinoma", io=IO, slot="risk factors",
   q="In which three immunosuppressed groups is basal cell carcinoma more common and more likely to recur?",
   opts=[
     ["Non-Hodgkin lymphoma, solid-organ transplant, and allogeneic stem cell transplant",
      "Correct — the three groups named on the risk factor slide."],
     ["Chronic lymphocytic leukaemia, human immunodeficiency virus, and transplant",
      "That trio is the one given for squamous cell carcinoma."],
     ["Diabetes, chronic kidney disease and cirrhosis",
      "None of these is named."],
     ["Pregnancy, and long-term oral contraceptive or corticosteroid use",
      "Not the groups the deck names."]],
   c=0, cite=c(33)),

 # ---------------- prognosis / differential ----------------
 dict(topic="Actinic keratosis", io=IO, slot="prognosis",
   q="What are the four possible fates of an individual actinic keratosis?",
   opts=[
     ["It may persist, involute, recur, or progress",
      "Correct — including involution, which is why individual lesion behaviour is unpredictable."],
     ["It may persist, progress, metastasise, or recur",
      "Actinic keratoses do not metastasise; involution is the missing fourth."],
     ["It may only persist or progress",
      "That leaves out involution and recurrence."],
     ["It will always progress if left untreated",
      "About one in a thousand per year progresses; most do not."]],
   c=0, cite=c(15)),

 dict(topic="Cutaneous T-cell lymphoma", io=IO, slot="prognosis",
   q="Which cutaneous T-cell lymphoma features worsen prognosis, and which carries the best?",
   opts=[
     ["Tumours, erythroderma and lymphadenopathy worsen it; limited patch disease does not reduce survival",
      "Correct — survival is not reduced in limited patch-stage disease."],
     ["Patch and plaque disease worsen it; tumour-stage disease carries the best prognosis",
      "That reverses the deck entirely."],
     ["Only lymphadenopathy worsens it; skin findings do not affect prognosis",
      "Tumours and erythroderma also worsen it."],
     ["Prognosis is uniformly poor regardless of stage",
      "The deck describes it as usually slowly progressive over decades."]],
   c=0, cite=c(76)),

 dict(topic="Kaposi sarcoma", io=IO, slot="prognosis",
   q="Which Kaposi sarcoma form may REGRESS, and what makes it do so?",
   opts=[
     ["Iatrogenic disease, which may regress when immunosuppression is reduced",
      "Correct — which is why the transplant team is consulted before any reduction."],
     ["Classic disease, which regresses with local radiation",
      "Classic disease is indolent and managed palliatively, not described as regressing this way."],
     ["Endemic disease, which regresses with antiretroviral therapy",
      "Endemic disease is often aggressive and can be rapidly fatal."],
     ["Epidemic disease, which regresses once chemotherapy stops",
      "Epidemic disease responds to immune restoration, not to stopping chemotherapy."]],
   c=0, cite=c(67)),

 dict(topic="Kaposi sarcoma", io=IO, slot="referral",
   q="Which team must be involved BEFORE immunosuppression is reduced in iatrogenic Kaposi sarcoma?",
   opts=[
     ["The transplant team",
      "Correct — the deck lists them explicitly as a referral before reducing immunosuppression."],
     ["Medical oncology",
      "Oncology is for systemic disease."],
     ["Palliative care",
      "Palliative care is for high symptom burden."],
     ["Pulmonology or gastroenterology",
      "Those are for symptomatic visceral evaluation."]],
   c=0, cite=c(67)),

 dict(topic="Squamous cell carcinoma", io=IO, slot="first-line",
   q="How often should a patient treated for squamous cell carcinoma be examined, and how does immunosuppression change it?",
   opts=[
     ["At least annual skin and lymph-node examination, with closer intervals if high-risk or immunosuppressed",
      "Correct — the interval tightens rather than the examination changing."],
     ["At least annual skin examination only, unchanged by immunosuppression",
      "Lymph nodes are included, and the interval does change."],
     ["Every three months for life in all patients",
      "The deck's baseline is at least annual."],
     ["Only when the patient reports a new lesion",
      "Scheduled surveillance is required."]],
   c=0, cite=c(26)),
]
