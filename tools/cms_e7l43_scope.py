# -*- coding: utf-8 -*-
"""Lecture 43 scope -- Pulmonary Nodules and Neoplasms (Gray), CMS I Exam 7 (Respiratory Block Exam II, Monday
2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 43 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Rob Gray, DMSc, PA-C, Adjunct Instructor, NSU Jacksonville (Associate Professor and Associate Program
Director, Doctor of Medical Science, Arkansas Colleges of Health Education) -- title slide; Zoom labels him "Robert
Gray". calendar-data.js lists "CMS I - LECTURE #43 - Pulmonary Nodules and Neoplasms - Dr. Gray GUEST LECTURER",
Wednesday 2026-11-04, 10 AM-12 PM (2 hours). No conflict. Deck file "Pulmonary Nodules and Neoplasms 2026.pptx",
50 slides; the deck title matches the calendar.

RECORDING: the live Zoom session, recordings/cms-l43-nodules-neoplasms-gray-2026-11-04.m4a (1:06:33), with Zoom's
speaker-labeled transcript (.zoom-transcript.txt) cross-examined against our full faster-whisper transcript
(.transcript.txt, 806 segments); every quote below was checked in both and uses the clearer wording; times are Zoom's
(faster-whisper runs 2-15 s earlier late in the hour). Where they differ: "CT people at 3, 6, 9" (Zoom "see T
people") [22:38]; "caseating granuloma" (Zoom "KZ8") [39:11]; "hamartoma" (Zoom "hematoma") [42:44]; "N3" and "M1a"
(Zoom "And three", "In 1A") [44:40, 44:53]; "If you CT them, you'd find the tumor" (Zoom "If you see Tetum") [56:18];
"Pants Pantry" = PANCE Prep Pearls, and "super supacular node" = supraclavicular, in both. 2:41-7:35 is the host (Monique
Jaquith) chatting with him before class (he had influenza and taught remotely); screen sharing 7:49-1:06:33; the title
slide sat on screen 8:00-11:30 while students were admitted; he taught 11:00-1:06:19 and let the class go early.
Every deck slide was shown. The frame matcher mislabeled three runs; corrected here: 40:00-41:30 is slide 18 (not 46),
51:30-52:45 is slide 33 (not 13), 63:45-66:15 is slide 49 (not 39). Video-frame annotations (his pen): s18 underline
under "30 pack-year smoking"; s19 underline under the multiple / high-risk / 6-8 mm cell ("CT at 3-6 months, then at
18-24 months"); s31 underline under the later signs "bone pain, weight loss"; s32 circle round the spiculated nodule;
s38 underline under "chosen due to the subset (i.e. genetic variant)"; s42 circle round the CT mass.
Time spoken sets emphasis and scope only; it never adds off-deck content.

SLIDE 49 "THINGS TO KNOW" IS HIS EXAM BLUEPRINT (title visible only in the render and video; s49 itself is excluded
from citation because it states no facts). Its nine bullets, verbatim: "the criteria for screening an asymptomatic
and at-risk patient for lung cancer" / "a benign nodule's appearance" / "what makes you concerned for a malignant
nodule" / "your lung cancer staging based on sizes, lymph involvement and metastasis (TNM)" + "Also know how this will
affect treatment (surgery plus chemo vs chemo only, for example)" / "which lung cancers present in periphery or
central locations" / "how to recognize squamous cell carcinoma from the other NSCLC" / "how to recognize small cell
lung carcinoma (SCLC)" / "which cancer receives the most benefit from radiotherapy" / "the signs and symptoms of a
paraneoplastic associated symptoms in a patient lung carcinoma (i.e. small cell)". He walked it at [1:04:16-1:05:46]:
"Criteria for screening, like, who's ... who am I worried about, who am I not worried about"; "Things that would make
me feel better about a [benign] nodule are a reasonable thing to kind of walk out of here with" (both transcripts
garble the word: "a 9 nodule" / "an eye nodule"); "What makes you worried
about what could be a malignant nodule? What word would I see in an x-ray report or a CT report and be like, ugh, you
just ruined my day? ... The spiky word, yes. Spiculated. Good. Yeah, you don't usually see a lot of benign stuff
that's described as spiculated" [1:04:30-1:05:11]; "your lung cancer staging based on sizes. Again, do we do surgery?
Do we do chemo? Is it just better for chemo? Do you need to know every circumstance? No. Like, big picture, guys"
[1:05:11]; "Which lung cancers are peripheral? Which ones are central? See, you already know the answer to that"
[1:05:24]; "How to recognize squamous cell from the others, how to recognize small cell from the others" [1:05:29];
"Which cancer benefits most from radiotherapy?" [1:05:37]; paraneoplastic "the weirdness ... maybe I accidentally find
lung cancer" [1:05:40]. Every bullet is a REQUIRED_IO and REQUIRED_VIG row below.

RECORDING SCOPE REMARKS (verbatim, [m:ss], slide on screen):
  Board pointer, repeated three times: "Couple of things I'll point out to you, just because this is stuff that comes
      up on [PANCE Prep Pearls]. Small and squamous are central ... even Dwayne Williams is gonna tell you this. So,
      small cell, squamous cell, central ... Adenocarcinoma, large cell, usually periphery ... Small cell and squamous
      are central. See, there you go, you got half of it" [48:38-49:15, s30] -> starred.
  Test-question pointer: large cell "tends to metastasize to weird places. Large cell tends to met to the gut. Small
      intestine, bowel ... And that's specific to large cell, so I would say stuff that, like, is unique to a thing
      makes a great test question" [52:02-52:24, s33] -> starred.
  "Magic number is 6. Greater than 6 millimeters, I'm suspicious ... Especially if I'm located in the upper lobes,
      hilar structures. Especially if I've got a spiculated appearance. You're gonna see this word a lot. Spiculated is
      spiky" [33:20-33:42, s16]; 6 mm again at [25:40, s12] and [41:51, s19] -> starred (6 mm, spiculated).
  Paraneoplastic origin set up early and repeated: "I'm calling the shot now, that's where it comes from" (neuroendocrine
      cells lining the bronchioles) [15:52-16:26, s6]; "Big thing to consider ... we kind of hinted at this earlier"
      [1:01:10, s46]; small cell SIADH "that's real ... that patient may show up in the ED because of the confusion and
      seizures ... oh, that's lung cancer" [1:02:59-1:03:27, s48] -> starred.
  Squamous: "Cavitation is big with that one. Strongest association with smoking. Central location originates in the
      bronchus ... Cough, wheezing, hemoptysis are huge ... it almost looks like a COPD ... constantly in exacerbation"
      [55:42-56:14, s39]; sputum "This one you might be able to catch with sputum testing ... usually we don't do sputum
      testing" [57:35, s40], set up at [31:41, s14] "sometimes it will be, and we'll talk about the exception".
      Hypercalcemia: "A lot of times, your squamous cell will make your calcium, a big deal" [1:01:39, s46].
  Small cell: "you tend to get neuroendocrine paraneoplastic syndromes ... does better with chemo and radiation than
      the other types. If the cancer's pretty limited, you can radiate it really effectively" [58:34-58:46, s41]; PCI
      "We're literally gonna radiate the brain just in case there's metastasis" [59:38-59:54, s43].
  Staging, big picture only: "I bring this up not to, like, make you memorize the charts" [44:55, s22]; "stuff that
      crosses over to the other lung is badness ... Size of the tumor is badness. Lymph node involvement, badness.
      Metastasis, worse badness" [46:21-46:41, s25]; "It gets really granular here. I don't want you to lose your
      minds about this ... there's a continuum" [47:12, s27]; "tumor, lymph node involvement, metastasis, that's how
      you stage it out" [48:24, s29]. Staging is still on s49, so it is keyed at the level the stage pictures state.
  Fleischner: "most of the places that produce chest CT reports ... literally will publish the Fleischner table in
      those reports ... don't be like, I need to know all my Fleischner rules. Don't freak out ... I don't want you
      freaking out and being like, oh god, I have to memorize this table. I mean, you can!" [41:02-41:41, s18-s19];
      subsolid table "there's rules, you're fine" [42:24, s20]. He then read the solid-nodule rows aloud [41:51-42:20].
      Fleischner is NOT on s49 and he said not to memorize it: no REQUIRED row (dropped 2026-11-06); at most two
      solid-table (s19) items in the vignette pool, never the subsolid table.
  Cuts: lymph node stations "nobody's expecting you to, like, number these" [15:14, s5] -> s5 excluded; malignancy
      probability tables "Don't lose sleep over that, just know you're gonna work it up" [22:34, s11]; genes "don't go
      crazy about details on this" [53:41, s36]; "I do not expect you to know absolutely specific drugs for, like, this
      marker, this drug ... you're not doing oncology. Your job as a primary care PA ... is be able to screen and figure
      out risk for that patient, and then refer" [54:16-54:26, s37]; SCLC follow-up schedule "don't memorize that"
      [59:25, s43].
  Asides with nothing keyable: pre-class chat [2:41-7:35]; the Pope's nodule and lobectomy [24:30-25:25, 32:46-33:15];
      cavitation causes from chat (abscess, empyema, tuberculosis: not on the slides) [35:31-36:38]; his own PET-positive
      aortopulmonary-window node that proved a caseating granuloma [38:19-39:51] (the keyable point is s17's: inflammation
      can take up the tracer); his recurrent laryngeal nerve [56:44-57:05]; "monoclonal is Latin for really, really
      expensive" [55:12]; schedule chat [1:03:49-1:04:12]. "That's why you do that on the exam" [47:35] means the PHYSICAL
      exam (feeling for a supraclavicular node), not the test.

MINUTES (timeline, corrected as above; minus off-content time): epidemiology, risk factors and spread 7.5 (s5 and s7
dropped as excluded); incidental nodules and presenting symptoms 7.1 (Pope 0.9 off); diagnostic workup and biopsy
4.25 (Pope 0.5 off); benign versus concerning nodules 4.25 (cavitation chat 1.0 and his own work-up story 1.5 off);
screening and follow-up 3.25; staging 5.25; central versus peripheral 1.0; adenocarcinoma 2.0; large cell 1.75;
non-small cell treatment 1.5 (s36-s37 dropped: "don't go crazy" / "I do not expect you to know specific drugs");
squamous 2.2 (his nerve story 0.35 off); small cell and radiotherapy 3.0; paraneoplastic 2.5. The s49 recap (2.5 min)
is not added to any topic; REQUIRED rows carry it.

WHERE HE AND THE SLIDES DIFFER (slides win; he corrected NO slide out loud):
  s18 screening: he read the slide's criteria exactly ("55 and 80 ... at least a 30-pack year smoking history, who
      currently smoke. Or, if they quit in the last 15 years ... every year with a low-dose chest CT" [40:07-40:21]).
      No correction, so 55-80 / 30 pack-years / quit within 15 years is keyed. He did not mention Medicare 55-77.
  s22: "T4 is huge, 7 centimeters" [44:09] (slide: > 7 cm); he skipped N2 ("Ipsilateral for N1. N3 ... contralateral"
      [44:31]); "1B, 3 to 4, no lymph nodes" [45:30] matches. Slide wins.
  s24: stage II "or cancer's really small, but it's in the peribronchial nodes" [45:56] (slide: no more than 5 cm).
  s9: "metastases are four major places, liver, lungs, bone, and brain, LLBB" [18:39-18:47]: the lung as a site that
      catches other cancers' metastases is his; s9 and s41 give lung cancer's own spread as liver, brain and bone.
  s39/s40: "squamous cell is central, but squamous cell is often very bronchial" [56:19]; "It's generally central, but
      it doesn't have to be" [57:19]. Slide: "Central location and often originates in the bronchus". Key central.
  s45: he adds atrial fibrillation after chest radiation [1:00:42]: not on the slide, never keyed.
  s14: he explains alkaline phosphatase as a liver (biliary) or bone marker [29:44-31:22]; the slide only lists it in
      the lab workup. Key "part of the lab workup"; the liver/bone reasoning may sit in an explanation as his teaching,
      never as a key.

SLIDE CONFLICTS (never keyed one way or the other; the guide notes each):
  Adenocarcinoma share: s4 "35-40%", s31 "30-40%". Key "most common lung cancer" only (both percentages banned).
  Treatment by stage (s35, text vs its own table): text "Surgical resection (I-IIIB)" and "Chemo and radiation are only
      an adjunct to surgery or if the patient is stage IV"; table IIIA "Chemoradiotherapy, surgical resection in
      selected patients", IIIB "Chemoradiotherapy". Key: stage 1-2 = surgical resection (both agree); stage 4 =
      chemotherapy, surgery only for a solitary metastasis with a resectable primary (table); never ask surgery
      versus chemoradiotherapy for stage 3A or 3B.
  Squamous and immunotherapy: s37/s38 titles "NSCLC (excluding squamous cell)" targeted therapy / immunotherapy vs s40
      "Management is a combination of surgery, chemotherapy, immunotherapy (as it is a NSCLC), and radiation". Never
      ask whether squamous cell receives immunotherapy. Gene-marker-directed (targeted) therapy is for non-squamous
      disease (s37 title; "Non-small cells, except for squamous. Squamous is its own thing" [53:59]).
  Neurologic paraneoplastic labels: s46 "Lambert-Eaton myasthenic syndrome (autoimmune) - central" and "Cerebellar
      degeneration or brain encephalitis (autoimmune) - peripheral" vs s47 Lambert-Eaton = immune attack on calcium
      channels at nerve endings, at the neuromuscular junction. The s46 labels are also reversed against standard
      teaching. Never key central/peripheral for these syndromes (banned).
  Pleura: s16 "Close to a fissure or the pleura indicates something usually benign" vs s32 a peripheral spiculated
      nodule "that involved the pleura; identified later as an invasive adenocarcinoma" (and adenocarcinoma "may invade
      the pleura"). Key "adjacent to a fissure = usually benign" only (s16 + s21 minor-fissure picture); never key
      pleural contact as reassuring.
  Cavitation: concerning feature (s16) and seen in large cell (s33, s34), squamous (s39 "frequent cavitation") and small
      cell (s41 "high cavitation rate" once large). Never make cavitation the sole clue to one cell type.
  Hilum: s9 "Most of them form a mass in or near the hilum"; s30 puts adenocarcinoma (the most common type) and
      large cell in the periphery. Never ask where most lung cancers form (found by the objective-pool writer).
  Small cell and immunotherapy: s41 "Immunotherapy is less effective on small cell ... but is becoming an option" vs
      s43 "Two adjunct immunotherapies are also approved for SCLC". Not a contradiction; never key "no role".
  s31 "metastatic (T4M1 or 2)": there is no M2 on s22's table (banned).
  s13 lists adrenal insufficiency under the heading "Kidneys": key the adrenal finding, never "kidney metastasis".

DECK VERSUS CURRENT GUIDELINES (slides keyed; one line each for the guide):
  Screening (s18): the 2021 USPSTF update is ages 50-80 with a 20 pack-year history (still current smokers or quit
      within 15 years); Medicare now covers 50-77. Writers avoid the gap: screening patients are eligible under BOTH
      versions (55-80, at least 30 pack-years, smoking now or quit within 15 years) or ineligible under BOTH (younger than
      50, older than 80, under 20 pack-years, quit more than 15 years ago, or symptomatic); never a patient aged 50-54 or
      with 20-29 pack-years. The 2021 numbers are banned so they never appear as options.
  Mortality (s3): the slide ranks lung cancer second in women behind breast cancer; current US data rank it first in
      women too (the phrase is banned; key the men's "highest mortality" fact instead).
  Staging (s22-s29) is the eighth edition; the ninth edition (2024) splits N2 and M1c. Key the slides.
  Large cell carcinoma (s33): current classification has shrunk this group (marker-positive tumors are reclassified as
      adenocarcinoma or squamous). Key the slides.

PICTURE SLIDES (content that lives only in pictures; OCR in l43_ocr.txt checked against the renders and video frames):
  s4 pie of cell-type shares by smoking; s6 neuroendocrine cells lining the bronchioles; s8 type I pneumocytes (thin,
  ~95% of alveolar surface, gas exchange) and type II (cuboidal, ~5%, secrete surfactant); s10 growth sequence
  (genetically altered cell, hyperplasia, dysplasia, in situ cancer, malignant tumor invading blood and lymph,
  metastases); s11 the 8-30 mm solid nodule algorithm; s15 the fit-for-surgery biopsy algorithm; s16 calcification
  patterns (benign: diffuse, central, popcorn, concentric; malignant: ground-glass [stippled], eccentric) and the chest
  film; s19-s20 the Fleischner tables; s22 the TNM table; s23-s29 the stage pictures; s30 the location table; s35 the
  stage-treatment table and resection diagram; s37 the targeted-therapy flowchart (cut); s38 checkpoint pictures;
  s42 small cell histology caption; s43 the NCCN small cell flowchart; s47 Lambert-Eaton infographic; s48 carcinoid
  syndrome body diagram (heart: pulmonic and tricuspid valve thickening and stenosis, endocardial fibrosis; skin:
  cutaneous flushes, apparent cyanosis; respiratory: cough, wheezing, dyspnea; liver: hepatomegaly; gastrointestinal:
  diarrhea, cramps, nausea, vomiting; retroperitoneal and pelvic fibrosis). The s19 picture carrying "These
  recommendations do not apply to lung cancer screening, patients with immunosuppression, or patients with known
  primary cancer" is hidden behind the table (not visible in the render or the video): never keyed.

SYLLABUS ITEMS AND WHAT THE DECK ACTUALLY COVERS (gaps are never filled from outside):
  Lung neuroendocrine (carcinoid) tumors: s4 names "Carcinoid tumors" among the mixed and rare types; s48 "Carcinoid
      syndromes (for lung causes it's mainly only from a bronchial carcinoid). Exogenous release of serotonin from
      cancer cells leads to multiple other symptoms" + the body diagram. Spoken [1:02:40-1:02:56]: flushes, valve
      thickening, diarrhea, cramps, nausea, vomiting. GAP: no carcinoid epidemiology, imaging, diagnostic test,
      management or prognosis (5-HIAA, octreotide, somatostatin, chromogranin banned).
  SIADH: s46 (endocrine paraneoplastic); s48 small cell -> neuroendocrine cells -> excess antidiuretic hormone
      (vasopressin) -> water retention -> hyponatremia and decreased serum osmolality -> confusion, seizures, ataxia,
      other neurologic dysfunction, but no peripheral or pulmonary edema (insidious). GAP: no diagnostic criteria
      (urine studies) and no treatment (fluid restriction, hypertonic saline, vaptans, demeclocycline banned).
  Hypercalcemia: s46 "Hypercalcemia (particularly squamous cell)"; s14 "CMP incl calcium" in the lab workup. GAP: no
      symptoms, mechanism (PTHrP banned) or treatment (bisphosphonates, calcitonin banned).
  "Discuss relationship between small cell lung cancer and paraneoplastic syndromes": s4 (paraneoplastic syndromes are
      consequences of a growing tumor, "typically the small cell type"); s6 (neuroendocrine cells in the bronchioles);
      s41 (neuroendocrine paraneoplastic symptoms if the carcinoma develops from the APUD cells that secrete
      polypeptide hormones); s48 (small cell -> SIADH); s49. Well covered -> IO_SCLC.
  Adult and elderly: s3 (most >50 years old, about 4% under 40), s18 (screening ages and annual low-dose CT; upside and
      downside), s35 (must tolerate surgery: survive and recover), s15 (unfit -> segmentectomy or image-guided biopsy ->
      radiotherapy), s45 (radiotherapy effects). -> IO_POP.

EXCLUDED_SLIDES (never cited):
  1, 2      title, objectives
  5         lymph node station map: "nobody's expecting you to, like, number these" [15:14]
  7         labeled histology of bronchus and alveolus, no teaching text, 15 s on screen
  49        "Things to Know" (the blueprint; it states no facts: cite the content slides)
  50        "Any questions?" (awareness ribbon)

=====================================================================================================================
WRITING PLAN (two IO writers and two vignette writers; ~72 IO and ~74 vignette items; targets per topic as IO/VIG)
=====================================================================================================================
General: four options, key first (c=0), misconception tag on every distractor, numeric options ascending. Write stage
labels with ARABIC numerals ("stage 3A", "stage 1B", "stage 4"): the acronym guard rejects "IIIA", "IIB", "IA", "IVB"
(plain "stage I-IV" passes). Expand every acronym at first use in each field: "computed tomography (CT)" is the
reverse order the guard wants, so write "CT (computed tomography)" or just the words; same for PET, SCLC, NSCLC,
SIADH, TNM, PCI, ALP. Named findings in vignette stems carry their slide description (NAMED below). Cite the slide that
SHOWS the fact (C(n) / CS(a, b)). Vignettes: DX_CAP is 6 of 30, so at most ~18 of 74 vignettes may ask the diagnosis;
"classify" = the stage from the stem's tumor size, nodes and spread. Every REQUIRED row: write at least 4 per pool.
Multi-comorbidity / "what instead" items the slides support are marked [WI].

T_EPI "Epidemiology, risk factors and spread" (s3-s10; s5, s7 excluded) -- 9/6
  s3: >30% of cancer deaths in men (highest mortality of all cancers in men); five-year survival 17-18% in the US;
  smoking in 85-90% of cases (second-hand smoke 20%); packs per day and years compound the risk (5x to 10x to 20x);
  other risks: radiation and radon, air pollution, environmental and chemical toxins, tuberculosis or HIV infection,
  genetics, diet, alcohol; >200,000 new US cases a year, 2 million worldwide; most >50 years old (about 4% under 40:
  "You can't take it off entirely from your differentials" [13:30]). s4: two main types, small cell (15-20%, oat cell)
  and non-small cell (adenocarcinoma, squamous 20-30%, large cell 9-10%); rare types: carcinoid, bronchial gland,
  sarcomatoid, Pancoast; paraneoplastic syndromes typically from the small cell type. s6: neuroendocrine cells line the
  bronchioles. s8: type II pneumocytes are more numerous (60% of alveolar cells) but cover only 3-5% of the surface and
  secrete surfactant; type I are thin and do gas exchange. s9: carcinogens activate oncogenes and inactivate tumor
  suppressor genes; most masses form in or near the hilum, some in the periphery (hard to diagnose); spread to regional
  nodes, then liver, brain and bone, through angiogenesis and loss of differentiation. s10: hyperplasia -> dysplasia ->
  in situ -> invasive malignancy entering blood and lymph -> metastases. Leads: risk factors, education (smoking
  dose), complication (metastatic sites). Traps: no adenocarcinoma percentage; no women's mortality rank; no s10
  research diagram (Siglec, sRAGE).

T_PRESENT "Incidental nodules and presenting symptoms" (s11-s13) -- 9/10
  s11 algorithm for a NEW SOLID nodule 8-30 mm: assess clinical probability of malignancy (judgment or a validated
  model) -> very low (<5%): CT surveillance at 3-6, 9-12 and 18-24 months (low-dose, thin-section, noncontrast);
  low/moderate (5-65%): FDG-PET -> negative or mild uptake = the same CT surveillance; moderate or intense uptake =
  nonsurgical biopsy (transthoracic needle or endoscopic) or video-assisted thoracoscopic surgery with resection; high
  (>65%): standard stage evaluation (with or without FDG-PET) -> no metastases -> video-assisted thoracoscopic surgery
  with resection. Footnote: referral to a pulmonologist, thoracic surgeon, interventional radiologist or oncologist is
  recommended for high probability and for moderate/intense uptake (referral lead). Do not ask the probability
  percentages as numbers ("don't lose sleep") -- give the class in words or a clear clinical picture and ask the step.
  s12: nodules are found incidentally on a chest film or CT done for another reason; first estimate size (<6 mm
  generally not concerning unless high risk); solitary nodules on a chest film = "coin lesions"; most are benign
  (granuloma [inflammatory] or hamartoma [connective tissue growth]) but high-risk patients are worked up to exclude
  malignancy; symptomatic presentation: persistent cough, hemoptysis, dysphagia, wheezing or shortness of breath,
  systemic symptoms (weight loss, fever or fatigue, bone or chest pain, endocrine disorders); lung cancer is deadly
  because symptoms appear only when advanced or metastatic. s13 metastatic presentations with no respiratory
  symptoms: brain (headaches, vision changes, nausea, vomiting, syncope, seizures; papilledema with raised intracranial
  pressure; cranial nerve findings near the midbrain/pons), liver (dull right upper quadrant ache, firm hepatomegaly,
  poor appetite, jaundice, hepatic failure), bone (pain, fractures without falls -- a cough can fracture the spine,
  spinal cord compression), adrenal insufficiency (fatigue, weight loss, dizziness, hypotension, hyponatremia with
  hyperkalemia). Leads: next step, test, referral, diagnosis (metastatic site), complication. [WI] a COPD patient whose
  "exacerbations" never settle (spoken framing) -> image, do not just treat the exacerbation. Trap: hyponatremia WITH
  hyperkalemia and hypotension = adrenal metastasis (s13), not SIADH (s48).

T_WORKUP "Diagnostic workup and biopsy" (s14-s15) -- 6/6
  s14: chest film "is not a good tool here" (may find the nodule; otherwise rules out other pathology); standard =
  CT with contrast of the chest and upper abdomen, then biopsy or intervention; bronchoscopy, transthoracic or
  thoracoscopic biopsy depending on the nodule's location (can be CT-guided, can involve excision); PET; genetic
  testing; additional: CBC with differential, CMP including calcium, alkaline phosphatase, pulmonary function tests,
  sputum cytology (not sensitive). s15: excision or non-surgical treatment considered -> PET-CT for staging if not
  done -> fit for surgery? YES: wedge resection with on-table frozen section -> completion lobectomy under the same
  anesthetic; or image-guided biopsy -> malignancy confirmed -> lobectomy (or anatomical segmentectomy if unfit for
  lobectomy); not confirmed -> repeat biopsy or proceed if a false negative is feared. NO: image-guided biopsy if
  possible and safe -> confirmed -> stereotactic ablative radiotherapy, radiofrequency ablation or conventional radical
  radiotherapy; biopsy not possible or not safe -> straight to those treatments. [WI] unfit for lobectomy ->
  segmentectomy; unfit for surgery -> radiotherapy; biopsy unsafe -> treat without it. Leads: test, next step,
  treatment, avoid (a chest film to work up a known suspicious nodule; sputum cytology as the screen of choice).

T_CONCERN "Benign versus concerning nodules" (s16-s17) -- 7/7
  s16 concerning: >6 mm; upper lobes or hilar structures; spiculated (spikes, deviations or lobulations in the border);
  more than 3 nodules; enlarging over time; contrast-enhancing on CT; cavitated or nonsolid; patient at high risk.
  Benign: well-defined borders, fat (hamartoma), calcification (popcorn = hamartoma); near a fissure usually benign.
  Calcification patterns (picture): benign diffuse, central, popcorn, concentric; malignant ground-glass (stippled)
  and eccentric. s17: FDG-PET -- highly metabolic cells take up the sugar, suggesting malignancy; low or normal uptake
  is a good sign; uptake does not rule out inflammatory conditions (they may also take it up). Leads: next step, test,
  diagnosis (hamartoma / granuloma from the picture), education. [WI] a PET-avid nodule in a patient with an active
  granulomatous process -> still needs tissue (biopsy), PET alone does not prove cancer. Trap: no pleural-contact
  reassurance; cavitation is concerning but not diagnostic of a cell type.

T_SCREEN "Screening and nodule follow-up" (s18-s21) -- 6/7
  s18 (bold on the slide, "30 pack-year" underlined in class): USPSTF screening is for high-risk people WITHOUT symptoms
  or a known nodule: adults 55-80 with at least 30 pack-years who smoke now or quit within the last 15 years; annual
  low-dose chest CT (less radiation than a standard chest CT; works because air and nodules contrast well); upside
  early detection -> earlier intervention, better prognosis; downside many false positives -> unnecessary workup with
  complications (such as a biopsy). Fleischner guidelines (2017) track incidental nodules. s19 SOLID nodules (the only
  Fleischner table keyed): single, low risk: <6 mm no routine follow-up; 6-8 mm CT at 6-12 months, then consider CT at
  18-24 months; >8 mm consider CT at 3 months, PET/CT or tissue sampling. Single, high risk: <6 mm optional CT at 12
  months; 6-8 mm CT at 6-12 months, then CT at 18-24 months; >8 mm consider CT at 3 months, PET/CT or tissue sampling.
  Multiple, low risk: <6 mm no routine follow-up; 6-8 mm and >8 mm CT at 3-6 months, then consider CT at 18-24 months.
  Multiple, high risk: <6 mm optional CT at 12 months; 6-8 mm and >8 mm CT at 3-6 months, then at 18-24 months (the
  6-8 mm cell underlined in class). s20 subsolid table: at most 2 IO items, plain rows only (ground glass <6 mm no
  follow-up; >=6 mm CT at 6-12 months then every 2 years to 5 years; part solid >=6 mm CT at 3-6 months; persistent
  part-solid with a solid part >=6 mm highly suspicious). s21 benign CT pictures: smoothly marginated solid nodule
  with internal fat and calcification = hamartoma; smoothly marginated solid nodule with central calcification = healed
  granuloma; nodular opacity next to the minor fissure = linear scar or lymphoid tissue. Leads: next step (screen or
  not, follow-up interval), education (false positives, radiation), diagnosis (s21 picture), avoid (screening a
  symptomatic patient -> diagnostic workup instead [WI]; screening someone who quit 20 years ago). Traps: the 2021
  numbers (banned); Medicare (banned); volumes and recommendation grades (banned).

T_STAGE "Lung cancer staging" (s22-s29) -- 8/9
  s22: staged once CT (location and size), PET (lymph involvement) and biopsy (tumor type) are back; TNM. T: T1 <=3 cm
  (1a <=1, 1b >1-2, 1c >2-3); T2 >3-5 cm or main bronchus (not carina), visceral pleura, or atelectasis/post-
  obstructive pneumonitis to the hilum (2a >3-4, 2b >4-5); T3 >5-7 cm or chest wall, pericardium, phrenic nerve, or
  satellite nodules in the same lobe; T4 >7 cm or mediastinum, diaphragm, heart, great vessels, recurrent laryngeal
  nerve, carina, trachea, esophagus, spine, or a separate tumor in another lobe of the same lung. N1 ipsilateral
  peribronchial/hilar/intrapulmonary; N2 ipsilateral mediastinal/subcarinal; N3 contralateral mediastinal or hilar,
  or any scalene/supraclavicular. M1a contralateral lung, pleural/pericardial nodule or malignant effusion; M1b single
  extrathoracic metastasis; M1c multiple extrathoracic metastases. Stages (s23-s29): 1A <=3 cm, no nodes; 1B >3-4 cm,
  no nodes; 2A >4-5 cm, no nodes; 2B >5-7 cm no nodes (or chest wall / phrenic / heart lining / same-lobe nodule) OR
  <=5 cm with peribronchial or hilar nodes; 3A >7 cm (or diaphragm, mediastinum, great vessels, etc.) with no nodes, OR
  >5 cm with peribronchial/hilar nodes plus invasion, OR <=5 cm with mediastinal/subcarinal nodes; 3B >5 cm with
  mediastinal nodes, OR <=5 cm with contralateral, supraclavicular or scalene nodes; 3C >5 cm with contralateral,
  supraclavicular or scalene nodes; 4A other lung, pleural or pericardial nodules or fluid, or ONE site outside the
  chest (adrenal); 4B multiple sites outside the chest (adrenal and bone). s25: stages 1-3 are M0; N2 or N3 moves it to
  stage 3. Score-from-the-vignette items ("classify"): give size, node location and spread plainly; prefer the clean
  cells (1A, 1B, 2A, 2B, 3A via mediastinal nodes, 3B via supraclavicular node with a small tumor, 4A, 4B); no edge
  cases at an exact boundary. He wants the "badness" logic: crossing to the other lung, bigger tumor, more nodes,
  metastasis.

T_LOCATION "Central versus peripheral cancers" (s30) -- 3/3 (plus location items inside each cell-type topic)
  s30 table: small cell central, usually metastatic by diagnosis; adenocarcinoma periphery (not amenable to early
  detection); squamous central bronchi, diagnosable by sputum cytology; large cell periphery (not amenable to early
  detection). Mixed types exist (adenosquamous, combined small cell). Mnemonic he gave: "Small and squamous are central"
  (S and S central; the other two peripheral). Leads: diagnosis from a central/peripheral mass, test (sputum cytology
  for a central squamous lesion).

T_ADENO "Adenocarcinoma" (s31-s32) -- 4/4
  s31: most common; mid-lung and periphery; first metastasizes to lymphatics before leaving the lungs; associated with
  peripheral scars; noninvasive, minimally invasive or invasive; usually >50 with smoking history, but smoking is not
  always associated; persistent cough and shortness of breath without infection; 2/3 present advanced (T2+ with N1-3)
  or metastatic; mostly asymptomatic early; respiratory symptoms first (cough, shortness of breath, chest tightness or
  pain, hemoptysis, fatigue); later bone pain, weight loss, systemic (paraneoplastic) issues (underlined in class).
  s32: from type II pneumocytes via atypical adenomatous hyperplasia, in situ first; lepidic growth along the alveolar
  lining or stromal invasion (minimally invasive); later pleura and vessels (invasive); mucicarmine stain shows mucin
  (adenocarcinoma) -- negative may point to large cell; CT: peripheral spiculated nodule involving the pleura =
  invasive adenocarcinoma. Mnemonic: "adeno = gland" (type II pneumocytes are glandular, make surfactant) [50:32].
  Leads: diagnosis (peripheral nodule in a nonsmoker or a scarred lung), test (mucicarmine), complication.

T_LARGE "Large cell carcinoma" (s33-s34) -- 3/3
  s33: no specific genetic or histologic marker -- a diagnosis of exclusion among non-small cell types; anaplastic,
  undifferentiated, pleomorphic; cells about 3x larger (kept apart from small cell because treatments differ); subtypes
  giant-cell (sarcomatoid), basaloid, rhabdoid, neuroendocrine; periphery; necrosis and hemorrhage more readily than
  other non-small cell types; large cavitated peripheral mass on CT (biopsy still required); metastasis to unusual
  sites: SMALL INTESTINE AND BOWEL (starred: "unique to a thing makes a great test question"); no standardized
  treatment. s34: peripheral cavitating tumor with its own blood supply; histology confirms anaplastic tissue.
  Leads: diagnosis (peripheral cavitating mass + bowel metastasis), complication, test (biopsy; mucicarmine negative).

T_NSCLC_TX "Non-small cell treatment and targeted therapy" (s35-s38) -- 3/4
  s35: resection by size and nodes -- wedge/segment resection or lobectomy (open or thoracoscopic), pneumonectomy;
  patient must tolerate surgery (survive and recover); chemotherapy and radiation are adjuncts, or for stage 4, because
  non-small cell cancers respond poorly to them; chemotherapy and immunotherapy can now be targeted to genetic and
  protein markers. Table: stage 1-2 surgical resection; stage 4 chemotherapy, surgery only for a solitary metastasis
  with a resectable primary. Resection diagram: wedge = small part of a lobe, segment = larger part, lobectomy = whole
  lobe, pneumonectomy = whole lung. s36-s38 (keep to ONE or two items): tumor genetic testing lets the oncologist tailor
  therapy; TP53 is a tumor suppressor gene; checkpoint-inhibitor monoclonal antibodies ("-mab") are immunotherapy used
  with or after chemotherapy, for non-surgical candidates, or by marker. Never a marker-to-drug pairing, never which
  drug is approved for which stage (he cut it), no brand names. [WI] stage 1 adenocarcinoma in a patient who cannot
  tolerate surgery -> radiotherapy route (s15); stage 4 -> chemotherapy, not resection. Referral lead: primary care
  screens, judges risk and refers ([54:26]).

T_SQUAMOUS "Squamous cell carcinoma" (s39-s40) -- 4/4
  s39: second most common (20-30%); STRONGEST association with smoking; frequent cavitation and obstruction; central,
  often arises in a bronchus; silent until it obstructs the bronchus -> cough, wheezing, hemoptysis; large obstruction
  -> atelectasis and pneumonia risk; spreads by local invasion -> dysphagia, voice change (laryngeal nerves). s40:
  lymphangitic spread to hilar nodes; CAN be caught by sputum testing (unlike the others); management = surgery,
  chemotherapy, immunotherapy, radiation; CT: large cavitated spiculated lesion with nodular inner margins and
  lymphangitic spread. s46: hypercalcemia particularly squamous. Leads: diagnosis (central cavitating mass in a heavy
  smoker, hemoptysis, high calcium), test (sputum cytology), complication (post-obstructive pneumonia, hoarseness,
  dysphagia, hypercalcemia). Trap: do not ask whether squamous gets immunotherapy.

T_SMALL "Small cell carcinoma and radiotherapy" (s41-s45) -- 5/5
  s41: limited (one area, only local nodes), extensive (spread beyond), combined (mixed with non-small cell); central,
  infiltrates the mucosa; insidious -> >70% metastatic (liver, bone, brain) before detection; neuroendocrine
  paraneoplastic symptoms (APUD cells secreting polypeptide hormones); high cavitation rate once large; RESPONDS BETTER
  TO CHEMOTHERAPY AND RADIATION than the three non-small cell types; radiation works best in LIMITED stage; immunotherapy
  less effective (genetic variability) but becoming an option; short arm of chromosome 3. s42: fragile, crushed at
  biopsy; small cells, no nucleoli, high nuclear-to-cytoplasm ratio. s43: after initial therapy with a complete or
  partial response, limited stage -> prophylactic cranial irradiation (radiate the brain because brain metastasis is so
  likely); extensive stage -> consider it with or without thoracic radiotherapy; brain MRI preferred over CT; PCI not
  recommended with poor performance status or impaired neurocognitive function (at most one [WI] item); two adjunct
  immunotherapies approved. s44: linear accelerator beams focus radiation on the target. s45 radiotherapy effects:
  acute -- localized skin, mucosa and tissue changes (erythema, hyperpigmentation, ulceration risk), inflammation, hair
  loss, little nausea or vomiting (less systemic than chemotherapy); chronic -- pulmonary fibrosis and scarring,
  cardiovascular fibrosis (coronary disease, valve disease, cardiomyopathy), localized hair loss, lymphedema and fluid
  retention (think axillary), neuropathy. Leads: diagnosis, treatment, next step (PCI), complication (radiation
  effects), education, avoid ([WI] PCI in a patient with dementia). Oat cell is an older name (say so if used).

T_PARA "Paraneoplastic syndromes" (s46-s48) -- 5/6
  s46: hormonal or cytokine effects of tumor tissue (primary or metastasis): endocrine -- SIADH, hypercalcemia
  (particularly squamous); neurologic -- Lambert-Eaton myasthenic syndrome, cerebellar degeneration or encephalitis
  (autoimmune); dermatologic -- acanthosis nigricans, dermatomyositis; hematologic (no example given: never keyed).
  s47: Lambert-Eaton = autoimmune attack on calcium channels at nerve endings -> less acetylcholine released -> muscles
  cannot contract properly -> progressive weakness, particularly the legs; rare (about 3000 patients a year). s48:
  carcinoid syndrome from a bronchial carcinoid (serotonin; flushing, apparent cyanosis, pulmonic and tricuspid valve
  thickening/stenosis, endocardial fibrosis, wheeze, cough, dyspnea, hepatomegaly, diarrhea, cramps, nausea, vomiting,
  retroperitoneal and pelvic fibrosis); small cell -> neuroendocrine cells -> excess antidiuretic hormone ->
  hyponatremia, low serum osmolality, confusion, seizures, ataxia, NO edema. Use IO_SCLC for the small cell link (s4,
  s6, s41, s48). Leads: diagnosis (which cancer / which syndrome), test (serum sodium, calcium), complication.
  Attribution rules: hypercalcemia -> squamous; SIADH -> small cell; carcinoid syndrome -> bronchial carcinoid; other
  paraneoplastic pictures -> small cell as "most likely" (s4 "typically"), never "only".

IO tags: IO_A for most items; IO_SCLC for the small cell / paraneoplastic link (at least 6 IO items); IO_POP for
adult/elderly care (age bands for screening, most cases over 50 but 4% under 40, surgical fitness, unfit -> segment-
ectomy or radiotherapy, radiotherapy effects) (at least 6 IO items). The IO partition wants every IO in every form.
"""

DECK = "Pulmonary Nodules and Neoplasms 2026.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following pulmonary neoplasms: 2. Pulmonary nodule 3. Lung cancer (bronchogenic "
        "carcinoma) a. Non-small-cell lung cancer (NSCLC) b. Small-cell lung cancer (SCLC) c. Lung neuroendocrine "
        "(carcinoid) tumors 4. Paraneoplastic Neoplasm Associated Syndromes a. SIADH b. Hypercalcemia")
IO_SCLC = "Discuss relationship between small cell lung cancer and paraneoplastic syndromes."
IO_POP = ("Identify medical care strategies for pulmonary nodules and neoplasms in the lecture topic list for the "
          "following populations. 7. adult 8. elderly")
IOS = [IO_A, IO_SCLC, IO_POP]

# Topic constants (quiz chips). Each is one contiguous slide range.
T_EPI = "Epidemiology, risk factors and spread"
T_PRESENT = "Incidental nodules and presenting symptoms"
T_WORKUP = "Diagnostic workup and biopsy"
T_CONCERN = "Benign versus concerning nodules"
T_SCREEN = "Screening and nodule follow-up"
T_STAGE = "Lung cancer staging"
T_LOCATION = "Central versus peripheral cancers"
T_ADENO = "Adenocarcinoma"
T_LARGE = "Large cell carcinoma"
T_NSCLC_TX = "Non-small cell treatment and targeted therapy"
T_SQUAMOUS = "Squamous cell carcinoma"
T_SMALL = "Small cell carcinoma and radiotherapy"
T_PARA = "Paraneoplastic syndromes"

TOPIC_SLIDES = {
    T_EPI: (3, 10),
    T_PRESENT: (11, 13),
    T_WORKUP: (14, 15),
    T_CONCERN: (16, 17),
    T_SCREEN: (18, 21),
    T_STAGE: (22, 29),
    T_LOCATION: (30, 30),
    T_ADENO: (31, 32),
    T_LARGE: (33, 34),
    T_NSCLC_TX: (35, 38),
    T_SQUAMOUS: (39, 40),
    T_SMALL: (41, 45),
    T_PARA: (46, 48),
}

# Writing targets per topic: (IO pool, vignette pool). Not read by the partition.
POOL_TARGETS = {
    T_EPI: (9, 6), T_PRESENT: (9, 10), T_WORKUP: (6, 6), T_CONCERN: (7, 7), T_SCREEN: (6, 7),
    T_STAGE: (8, 9), T_LOCATION: (3, 3), T_ADENO: (4, 4), T_LARGE: (3, 3), T_NSCLC_TX: (3, 4),
    T_SQUAMOUS: (4, 4), T_SMALL: (5, 5), T_PARA: (5, 6),
}

EXCLUDED_SLIDES = {1, 2, 5, 7, 49, 50}

SCOPE_BANNED = [
    # brand names the partition's brand guard does not list
    r"\b(?:Opdivo|Keytruda|Tecentriq|Yervoy)\b",
    # marker-specific regimens and markers ("I do not expect you to know absolutely specific drugs" [54:16])
    r"osimertinib|crizotinib|ceritinib|alectinib|brigatinib|afatinib|erlotinib|gefitinib|pemetrexed|docetaxel"
    r"|nintedanib|carboplatin|cisplatin|ciplatin|platinum doublet|T790M|\bROS-?1\b|ipilimumab",
    r"\b(?:KRAS|EGFR|ALK)\b[^.?]{0,15}\d+ ?%|\d+ ?%[^.?]{0,15}\b(?:KRAS|EGFR|ALK)\b|\bPD-?L1\b[^.?]{0,40}(?:<|>|≥|less than|greater than|at least|\d+ ?%)",
    # Fleischner volumes and recommendation grades
    r"mm3|mm³|\b(?:100|250) ?mm\b|recommendation [1-5][A-C]\b",
    # small cell surveillance schedule ("don't memorize that" [59:25])
    r"every (?:2|3|3-4|3 to 4|6) (?:mo|months) during|oncology follow-up visits",
    # stage-by-stage survival column (s35, never narrated, unlabeled)
    r"\b(?:75|55|50|40|10-35|10 to 35) ?%[^.?]{0,40}surviv|surviv[^.?]{0,40}\b(?:75|55|50|40|10-35|10 to 35) ?%",
    # screening: the 2021 numbers never appear (patients are eligible or ineligible under both versions); no Medicare
    r"\b20[- ]pack[- ]years?\b|\b50 ?(?:-|to|and) ?80\b|\bages? 50\b|Medicare",
    # conflicting adenocarcinoma share (s4 vs s31); nonexistent M2 (s31)
    r"\b(?:35-40|35 to 40|30-40|30 to 40) ?%|\bM2\b",
    # women's mortality rank (deck vs current data)
    r"second[- ]highest (?:cancer )?mortality|behind breast|after breast cancer|secondary to breast",
    # node station numbers (s5 cut), research diagram on s10
    r"\bstations?\b|Siglec|sRAGE|osteoblast activation|neutrophil-driven",
    # off-deck paraneoplastic and carcinoid workup, treatment and classic signs (syllabus gaps)
    r"5-HIAA|hydroxyindoleacetic|octreotide|somatostatin|chromogranin|PTHrP|parathyroid hormone[- ]related"
    r"|bisphosphonate|zoledron|calcitonin|demeclocycline|tolvaptan|conivaptan|vaptan|hypertonic saline"
    r"|fluid restriction|Cushing|ACTH|adrenocorticotropic|Horner|superior vena cava|clubbing"
    r"|hypertrophic (?:pulmonary )?osteoarthropathy|anti-?Hu\b|voltage-gated|Trousseau",
    # s46 central/peripheral labels on the neurologic syndromes (contradicted by s47)
    r"(?:Lambert|myasthenic|cerebellar|encephalitis)[^.?]{0,30}\b(?:central|peripheral)\b",
    # outside sources
    r"StatPearls|UpToDate|Harrison|Gemini|Lecturio|Dwayne|PANCE|National Comprehensive Cancer Network|NCCN|Mayo Clinic",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "coin lesion": "solitary",          # s12: solitary nodules seen on a chest film are sometimes called coin lesions
    "spiculated": "spik",               # s16: spiculated appearance (spikes or deviations or lobulations in border)
    "popcorn": "calcif",                # s16: calcifications (popcorn looking = hamartoma)
    "lepidic": "alveolar lining",       # s32: lepidic growth across the alveolar lining
    "lambert": "weakness",              # s47: progressive, debilitating muscle weakness, particularly in the legs
}

# Minutes on screen per pool topic (timeline, corrected; minus off-content time; see MINUTES above).
TOPIC_MINUTES = {
    T_EPI: 7.5,
    T_PRESENT: 7.1,
    T_WORKUP: 4.25,
    T_CONCERN: 4.25,
    T_SCREEN: 3.25,
    T_STAGE: 5.25,
    T_LOCATION: 1.0,
    T_ADENO: 2.0,
    T_LARGE: 1.75,
    T_NSCLC_TX: 1.5,
    T_SQUAMOUS: 2.2,
    T_SMALL: 3.0,
    T_PARA: 2.5,
}

# Slide 49 ("Things to Know") is the blueprint: every bullet is a row in BOTH sets, at least 1 per form (write >= 4
# per pool). Stage labels in keys use Arabic numerals ("Stage 3A").
_SCLC_KEY = r"(?<!non-)(?<!non )\bsmall[- ]cell|oat cell"
_SCREEN_STEM = r"(?<!genetic )(?<!molecular )\bscreen"
_BENIGN = (r"benign|reassur|hamartoma|granuloma|calcif|smooth|well[- ]defined|fissure|\bfat",
           r"hamartoma|granuloma|benign|popcorn|smooth|well[- ]defined|calcif|\bfat|fissure|scar|lymphoid")
_STAGE = (r"\bstag(?:e|ing)\b", r"^(?:stage|T[0-4]|N[0-3]|M[01])\b")
_STAGE_TX = (r"\bstage|lymph|\bnod(?:e|es|al)\b|metasta",
             r"resection|lobectomy|wedge|segmentectomy|pneumonectomy|surg|chemo|radiation|radiotherapy")
_LOCATION = (r"\bcentral|peripher", r"squamous|(?<!non-)(?<!non )\bsmall[- ]cell|oat cell|adenocarcinoma|large[- ]cell|central|peripher")
_RADIO = (r"radiat|radiotherapy|irradiat", _SCLC_KEY + r"|limited|prophylactic cranial")
_PARA = (r"paraneoplastic|hyponatremi|sodium|antidiuretic|osmolal|hypercalc|Lambert|myasthenic|cerebellar|encephalitis"
         r"|acanthosis|dermatomyositis|carcinoid|serotonin|flush", r".")

REQUIRED_IO = [
    ("Screening criteria", _SCREEN_STEM, r".", 1),
    ("Benign nodule appearance", _BENIGN[0], _BENIGN[1], 1),
    ("Concerning nodule features", r"concern|suspicio|malignan|worrisome",
     r"spicul|spik|upper lobe|hilar|enlarg|grow|contrast|cavit|nonsolid|non-solid|more than (?:three|3)"
     r"|(?:greater|larger|more) than 6|uptake|high risk", 1),
    ("Stage from tumor, node and metastasis findings", _STAGE[0], _STAGE[1], 1),
    ("Stage decides treatment", _STAGE_TX[0], _STAGE_TX[1], 1),
    ("Central versus peripheral location", _LOCATION[0], _LOCATION[1], 1),
    ("Squamous cell carcinoma recognized", r".", r"squamous", 1),
    ("Small cell carcinoma recognized", r".", _SCLC_KEY, 1),
    ("Cancer that benefits most from radiotherapy", _RADIO[0], _RADIO[1], 1),
    ("Paraneoplastic signs", _PARA[0], _PARA[1], 1),
]

REQUIRED_VIG = [
    ("Screening criteria from the vignette", _SCREEN_STEM, r".", 1),
    ("Benign nodule appearance", _BENIGN[0], _BENIGN[1], 1),
    ("Concerning nodule in the stem", r"spicul|enlarg|grew|grown|contrast[- ]enhanc|uptake|nonsolid"
     r"|more than (?:three|3) nodules", r".", 1),
    ("Stage from the vignette", _STAGE[0], _STAGE[1], 1),
    ("Stage decides treatment", _STAGE_TX[0], _STAGE_TX[1], 1),
    ("Central versus peripheral location", _LOCATION[0], _LOCATION[1], 1),
    ("Squamous cell carcinoma recognized", r".", r"squamous", 1),
    ("Small cell carcinoma recognized", r".", _SCLC_KEY, 1),
    ("Cancer that benefits most from radiotherapy", _RADIO[0], _RADIO[1], 1),
    ("Paraneoplastic signs", _PARA[0], _PARA[1], 1),
    # Fleischner (s19) is NOT required (session owner, 2026-11-06): he said not to memorize the table [33:20 area],
    # so at most two Fleischner solid-nodule items in the whole vignette pool, none in the objective pool.
]
