# -*- coding: utf-8 -*-
"""CMS I Lecture 9 — pool F. Content that exists ONLY as pictures.

Three slides in this deck extract as empty and carry real, examinable content
in the image alone:

  Slide 50  the LEVEL OF INVASION diagram, levels I-V against epidermis,
            papillary dermis, reticular dermis and subcutaneous tissue. NOTE the
            deck labels these only "Level I" to "Level V" -- the word "Clark"
            appears NOWHERE in the deck, not on the slide and not inside the
            figure. It is the conventional name and is given in parentheses so
            students recognise it elsewhere, but the questions lead with the
            deck's own wording, because that is what an exam written from this
            deck will use.
  Slide 53  the "Stages of Melanoma" diagram, stage 0 through stage IV
  Slide 54  the full TNM MELANOMA STAGING OVERVIEW table

Pools A-E were written from the extracted text and therefore had zero coverage
of any of it -- "TNM", "Clark", "stage IV", "N0" and "M0" all returned no hits.
This is the image-only-slides failure exactly: a text extraction reporting a
slide as empty is not evidence the slide is empty.

SCOPE JUDGEMENT. The TNM table is titled an "Overview" and its lower rows are
oncology-staging minutiae (IIIB: T0, T1a/b or T2a, N1b or N1c...). Questions here
cover what the axes MEAN and the anchor stages -- 0 and IV -- rather than asking
anyone to reproduce the grid. Contrast the Clin Path Lecture 3 build, where a
cancer-specific TNM table was deliberately NOT used because it appeared there
only as an illustration; here the lecture IS about melanoma, so its own staging
is on topic.

Correct answer first (c=0); distractors written to the answer's shape.
"""
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"

POOL_F = [
 dict(topic="Malignant melanoma", io=IOA, slot="test finding",
   q="Slide 50's diagram maps levels I to V against skin anatomy (this is the system conventionally called the Clark level). Which layers do they correspond to?",
   opts=[
     ["I confined to the epidermis; II into the papillary dermis; III filling the papillary dermis; IV into the reticular dermis; V into the subcutaneous tissue",
      "Correct — the level of invasion is an ANATOMIC layer, unlike Breslow thickness which is a measurement."],
     ["I confined to the epidermis; II into the reticular dermis; III filling the reticular dermis; IV into the papillary dermis; V into the subcutaneous tissue",
      "The papillary and reticular dermis are the wrong way round."],
     ["I into the papillary dermis; II into the reticular dermis; III into subcutaneous tissue; IV into muscle; V into bone",
      "Level I is confined to the epidermis, and the scale stops at subcutaneous tissue."],
     ["I confined to the stratum corneum; II into the epidermis; III into the papillary dermis; IV into the reticular dermis; V into the dermis-subcutaneous junction",
      "Level I is the whole epidermis, not the stratum corneum alone."]],
   c=0, cite=c(50)),

 dict(topic="Malignant melanoma", io=IOA, slot="test finding",
   q="How does the level of invasion (Clark) differ from Breslow thickness, and which does the deck call the dominant prognostic variable?",
   opts=[
     ["The level of invasion is the anatomic layer reached; Breslow thickness is a measured depth, and Breslow is the dominant prognostic variable",
      "Correct — Breslow is measured in millimetres and drives margins and staging. Note the deck labels these only \u201cLevel I\u201d to \u201cLevel V\u201d and never uses the word Clark; that is the conventional outside name for the same system."],
     ["The level of invasion is a measured depth; Breslow thickness is the anatomic layer reached, and the level is the dominant prognostic variable",
      "The two definitions are swapped, and Breslow dominates."],
     ["Both describe the same measurement on different scales, and either may be used as the dominant prognostic variable",
      "They are different concepts."],
     ["The level of invasion is the anatomic layer reached; Breslow thickness is a measured depth, and the level is the dominant prognostic variable",
      "The definitions are right but the deck names Breslow as dominant."]],
   c=0, cite=c(55)),

 dict(topic="Malignant melanoma", io=IOA, slot="test finding",
   q="In the TNM melanoma staging overview, what do the three letters denote?",
   opts=[
     ["T is primary tumour thickness; N is the number of tumour-involved regional lymph nodes; M is the number of metastases at a distant site",
      "Correct — the footnote of the staging table defines all three."],
     ["T is the tumour's anatomic level; N is the number of naevi present; M is the number of mitoses per high-power field",
      "None of the three is defined that way."],
     ["T is the time since onset; N is the number of tumour-involved regional lymph nodes; M is the number of distant metastases",
      "T is primary tumour thickness, not duration."],
     ["T is primary tumour thickness; N is the nodal diameter in centimetres; M is the mitotic rate",
      "N counts involved nodes and M counts distant metastases."]],
   c=0, cite=c(54)),

 dict(topic="Malignant melanoma", io=IOA, slot="test finding",
   q="Which TNM combination defines stage 0 melanoma?",
   opts=[
     ["Tis, N0, M0", "Correct — carcinoma in situ with no nodal or distant disease."],
     ["T1a, N0, M0", "That combination is stage IA."],
     ["Tis, N1a, M0", "Nodal involvement takes it out of stage 0."],
     ["T0, N0, M1", "Distant metastasis is stage IV."]],
   c=0, cite=c(54)),

 dict(topic="Malignant melanoma", io=IOA, slot="test finding",
   q="What defines stage IV melanoma in the staging overview?",
   opts=[
     ["Any T, any N, with M1 — that is, distant metastasis present whatever the primary or nodal status",
      "Correct — M1 alone determines it."],
     ["T4b, N3a/b/c, with M0 — the deepest primary with extensive nodal disease but no distant spread",
      "That combination is stage IIID."],
     ["Any T with N0 and M0 — a thick primary with no nodal or distant disease",
      "Without nodal or distant disease it cannot be stage IV."],
     ["Tis with any N and any M — in situ disease with any degree of spread",
      "Stage IV is defined by M1."]],
   c=0, cite=c(54)),

 dict(topic="Malignant melanoma", io=IOA, slot="prognosis",
   q="In the Stages of Melanoma diagram, what distinguishes stage III from stage IV?",
   opts=[
     ["Stage III is spread to the lymph nodes; stage IV is spread to other organs",
      "Correct — nodal against distant spread."],
     ["Stage III is spread to other organs; stage IV is spread to the lymph nodes",
      "The two are the wrong way round."],
     ["Stage III is localised disease thicker than stage II; stage IV is spread to the lymph nodes",
      "Localised thicker disease is stage II."],
     ["Stage III is melanoma confined to the epidermis; stage IV is localised disease in the skin",
      "Epidermis-confined disease is stage 0."]],
   c=0, cite=c(53)),

 dict(topic="Malignant melanoma", io=IOA, slot="prognosis",
   q="In the Stages of Melanoma diagram, what are stage 0, stage I and stage II?",
   opts=[
     ["Stage 0 is melanoma confined to the epidermal region of the skin; stage I is localised disease, only in skin and very thin; stage II is localised disease thicker than stage I",
      "Correct — 0, I and II are all still local."],
     ["Stage 0 is localised disease only in the skin and very thin; stage I is melanoma confined to the epidermal region; stage II is disease that has spread to the lymph nodes",
      "Stage 0 is the epidermis-confined disease and stage II remains localised."],
     ["Stage 0 is disease that has spread to the lymph nodes; stage I is melanoma confined to the epidermal region; stage II is localised disease that is very thin",
      "Nodal spread is stage III."],
     ["Stage 0 is localised disease thicker than stage I; stage I is melanoma confined to the epidermal region; stage II is disease that has spread to other organs",
      "Distant spread is stage IV."]],
   c=0, cite=c(53)),
]
