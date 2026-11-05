# -*- coding: utf-8 -*-
"""Lecture 41 scope -- Inflammatory Lung Diseases (Gray), CMS I Exam 7 (Respiratory Block Exam II, Monday
2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 41 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Rob Gray, DMSc, PA-C, Adjunct Instructor, NSU Jacksonville (Associate Professor and Associate Program
Director, Arkansas Colleges of Health Education) -- title slide (the deck's title reads "Pulmonary Inflammatory
Disease"). calendar-data.js lists "CMS I - LECTURE #41 - Inflammatory Lung Diseases - Dr. Gray GUEST LECTURER",
Monday 2026-11-02, 1-3 PM (2 hours). No conflict. Deck file "Inflammatory Lung Disease 2026.pptx", 74 slides.

RECORDING: his own narrated copy of the deck ("... With Narration.pptx", 75 slides, 71 narrated clips, 66.1 min),
extracted to recordings/cms-l41-inflammatory-lung-gray-narration-slideNN.m4a; transcript (faster-whisper medium.en,
one machine transcription, no second opinion) cms-l41-inflammatory-lung-gray-narration.transcript.txt. Clip numbers
are the NARRATED deck's: narrated 1-71 = plain 1-71; narrated 72 is an extra slide ("Acute Respiratory Distress
Syndrome / StatPearls: ARDS Article (excellent resource!)") NOT in the plain deck; narrated 73-75 = plain 72-74.
It sets emphasis and scope only (time spoken never adds off-deck content). Timestamps below are [narrated slide m:ss].

NARRATION SCOPE REMARKS (what he says is / is not tested):
  The charts: "do not memorize the charts, but they're there for your reference" [s3 0:23]; the drug and cause
      tables (s9-10) "do not challenge yourself by trying to memorize this ... there's a lot of drugs that can
      ... trigger interstitial lung disease ... built up over time" [s9 0:08]; s15-16 "please don't get into like
      memorizing every chart" [s16 0:01]. Drug causes are keyed only from the short lists he repeats (s12 treatment
      related: radiation, methotrexate, amiodarone, nitrofurantoin, chemotherapy; s18 methotrexate; s72
      chemotherapy, amiodarone, nitrofurantoin), never from the long s9 list alone.
  Rare idiopathic subtypes: "Am I gonna go like hey, is that desquamative interstitial pneumonia on a test? No"
      [s12 1:36]; s38 steroid subtypes "pretty rare ... Don't find your way too far down the rabbit hole" [s38 0:30].
      IPF "is kind of the most common thing" [s12 1:22].
  Granulomatous vasculitis: "you're not gonna get like a lot of Churg-Strauss and Wegener's questions ...
      Sarcoid, you could see questions about" [s21 0:31].
  Sarcoid pathophysiology (s41): "I'm not spending a lot of time on this" [s41 0:24]: never keyed.
  Lab clues (s25): "I would pay attention to this slide a little bit, because these are some things we can start
      differentiating" [s25 0:01] -> starred.
  History is the clue, repeated five times: "every board question is going to have a thing where it's a person
      showing up at a place with a thing ... What's their occupation? ... hobbies" [s3 2:16]; [s32 0:45], [s52 0:21],
      [s68 0:01], [s75 3:06] "The presentation may be same, but their history will be your indicator."
  Board pointers: lupus pernio with a dry cough = "red flag for like hey consider sarcoid" [s43 0:47]; ferruginous
      bodies -> "ah, asbestos" [s55 1:50]; milky lavage "usually confirmatory of like a silicosis" [s62 0:18].
  ARDS pictures (s72-74): "I use some AI resources here ... do not lose your minds ... shock, they literally say
      Chuck ... I'll be specific about it where it's important" [narrated s72 1:41]. He says nothing about the s74
      plateau pressure ("under 50 cm H2O"): no correction, so the number stays unkeyed.

MINUTES (clip durations): ARDS 11.3 (17%, the most), ILD definition and causes 12.1 (of it 2.1 on the
"don't memorize" charts s9, s15, s16), sarcoidosis 8.1, presentation and workup 7.8, IIP/IPF 7.0, asbestosis and
mesothelioma 4.6, hypersensitivity pneumonitis 4.1, coal workers' pneumoconiosis 3.7, connective tissue and other
unknown-cause 3.7, silicosis 3.4. TOPIC_MINUTES below drops the don't-memorize slides (9, 15, 16), the picture-only
excluded slides (8, 28, 36) and s41.

WHERE HE AND THE SLIDES DIFFER (slides win; none is a correction of a slide):
  s44: he says the ACE is elevated "in about half to 80%" [s44 0:25]; the slide says 40-80%.
  s51/s53: he gives the upper-lung location of coal macules first to "the weight of the coal dust" [s51 0:45], then
      to the dust being "pretty light" [s53 0:19]; the slides give the location (upper lung fields) without a
      reason for coal, and "lighter dust" for silica (s60). The reason is keyed for silica only.
  s75 (plain s74): "Steroids are gonna be huge, usually within the first 14 days" [s75 1:11]; the picture says
      guidelines "conditionally support" corticosteroids within 14 days. Keyed as the picture says.

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
  Hypersensitivity pneumonitis timing: s66 "Nausea 4-8 hours after exposure"; s67 "Acute within 9 hours" (the first
      sits inside the second; an independent check found no real conflict). Either figure is keyable as stated.

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

# Minutes spoken per pool topic (narration clip durations; see MINUTES above), for cms_e7_partition.py.
TOPIC_MINUTES = {
    "Interstitial lung disease: definition and causes": 10.0,
    "Connective tissue and other unknown-cause disease": 3.7,
    "Interstitial lung disease: presentation and workup": 6.8,
    "Idiopathic interstitial pneumonia and pulmonary fibrosis": 6.6,
    "Sarcoidosis": 7.5,
    "Coal workers' pneumoconiosis": 3.7,
    "Asbestosis and mesothelioma": 4.6,
    "Silicosis": 3.4,
    "Hypersensitivity pneumonitis": 4.1,
    "Acute respiratory distress syndrome": 11.3,
}

# Every form carries at least one acute respiratory distress syndrome item that works from the arterial oxygen to
# inspired oxygen ratio (s73): the severity class or the threshold.
REQUIRED = [
    ("ARDS oxygenation ratio", r"fraction of inspired oxygen|inspired oxygen fraction", r".", 1),
]
