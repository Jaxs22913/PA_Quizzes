# -*- coding: utf-8 -*-
"""Lecture 41 scope -- Inflammatory Lung Diseases (Gray), CMS I Exam 7 (Respiratory Block Exam II, Monday
2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 41 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Rob Gray, DMSc, PA-C, Adjunct Instructor, NSU Jacksonville (Associate Professor and Associate Program
Director, Arkansas Colleges of Health Education) -- title slide (the deck's title reads "Pulmonary Inflammatory
Disease"). calendar-data.js lists "CMS I - LECTURE #41 - Inflammatory Lung Diseases - Dr. Gray GUEST LECTURER",
Monday 2026-11-02, 1-3 PM (2 hours). No conflict. Deck file "Inflammatory Lung Disease 2026.pptx", 74 slides.

RECORDING: his own narrated copy of the deck ("... With Narration.pptx", 75 slides, 71 narrated clips, 66 min),
extracted to recordings/cms-l41-inflammatory-lung-gray-narration-slideNN.m4a. Clip numbers are the NARRATED
deck's: narrated 1-71 = plain 1-71; narrated 72 is an extra slide ("Acute Respiratory Distress Syndrome /
StatPearls: ARDS Article (excellent resource!)") NOT in the plain deck; narrated 73-75 = plain 72-74. It sets
emphasis and scope only (time spoken never adds off-deck content). Folded in when the transcript lands.

SLIDES 72-74 ARE PICTURES (three generated infographics on acute respiratory distress syndrome, no slide text):
72 etiology, epidemiology and risk factors; 73 presentation, diagnosis and differentials (the four "core
diagnostic criteria" and the oxygenation severity classes); 74 management and recovery. Read from the images
(they carry typos: "chuck" for shock, "trioyclie" for tricyclic, "protomine" for protamine, "AROS" for ARDS).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf pp. 19-20, "Inflammatory Lung Diseases"), the
leading number dropped and the syllabus's own sub-numbering kept (it numbers the disease list 2-9 and the
population list 11-12, and prints "Acute respiratory disease syndrome" for acute respiratory DISTRESS syndrome).

SLIDE CONFLICTS (never keyed one way or the other; the guide notes each):
  ARDS plateau pressure: s74 says low tidal volumes "Constrain ventilatory plateau pressures under 50 cm H2O"; the
      usual ceiling is 30. Plateau pressure numbers are never keyed (SCOPE_BANNED).
  Connective tissue disease: s12 (Harrison classification) files connective tissue disease under ILD of KNOWN
      cause (systemic disease); s18 titles it "Pulmonary Fibrosis of Unknown Etiology" and the syllabus lists it
      under unknown etiology. Never ask whether it is known or unknown.
  How common: s3 "Largely due to occupational and environmental exposure"; s15 and s31 make idiopathic pulmonary
      fibrosis / idiopathic interstitial pneumonia the most common diagnosis. Key "most common" only as s31/s32
      state it (idiopathic pulmonary fibrosis is the most common subtype); s15 percentages are never keyed.
  Silicosis: s60 "Simple disease state usually asymptomatic"; s61 "Rapid onset of symptoms". Never ask the onset
      speed of silicosis.
  s54 (coal workers' pneumoconiosis management) says "Corticosteroids may relieve the chronic alveolitis in
      silicosis": keyed for neither disease.
  s25 "Elevated ACE level: sarcoidosis, hypersensitivity silicosis": ACE is keyed for sarcoidosis only (s25, s44).
  s9 drug list: the notes say "pay attention" (notes do not count); drug causes are keyed from the slide's table
      and the s12 "treatment related" box only.
  Hypersensitivity pneumonitis timing: s66 "Nausea 4-8 hours after exposure"; s67 "Acute within 9 hours". Items
      say "hours after exposure" without choosing between them.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15).

EXCLUDED_SLIDES (never cited):
  1, 2            title, objectives
  8               gross pathology and histology photographs (honeycomb lung), no text
  28, 36          example films (sarcoid adenopathy film, honeycombing CT) without teaching text
  30, 49          section title slides
"""

DECK = "Inflammatory Lung Disease 2026.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following inflammatory lung diseases: 2. Interstitial lung disease of unknown etiology: "
        "a. Sarcoidosis b. Idiopathic pulmonary fibrosis (IPF) c. Pulmonary fibrosis associated with connective "
        "tissue disorders (CTD) 3. Interstitial lung disease of known etiology: a. Occupational lung diseases "
        "4. Hypersensitivity pneumonitis 5. Pneumoconiosis 6. Asbestosis 7. Silicosis 8. Idiopathic interstitial "
        "pneumonia 9. Acute respiratory disease syndrome (ARDS)")
IO_POP = ("Identify medical care strategies for inflammatory lung disease in the lecture topic list for the "
          "following populations. 11. adult 12. elderly")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {1, 2, 8, 28, 30, 36, 49}

SCOPE_BANNED = [
    r"plateau pressure.{0,40}\d|\b50 cm|\b30 cm",
    r"relative frequency|\b55 ?%|\b26 ?%",
    r"StatPearls|Harrison|Merck|Gemini|UpToDate|Lecturio|Papadakis",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "lupus pernio": "skin sores",          # s43 picture: lupus pernio (painful skin sores on face)
    "erythema nodosum": "lower legs",      # s43 picture: erythema nodosum (itchy and painful rashes on the lower legs and ankles)
    "eggshell": "hilar",                   # s63: "Eggshell" calcification of the periphery of the hilar lymph nodes
    "ferruginous bod": "dust",             # s55: a result of inorganic dust inhalation
    "progressive massive fibrosis": "upper",  # s51/s54: conglomeration (and contraction) in the upper lung fields
}

# Every form carries at least one acute respiratory distress syndrome item that works from the arterial oxygen to
# inspired oxygen ratio (s73): the severity class or the threshold.
REQUIRED = [
    ("ARDS oxygenation ratio", r"fraction of inspired oxygen|inspired oxygen fraction", r".", 1),
]
