# -*- coding: utf-8 -*-
"""Lecture 42 scope -- Pulmonary Vascular Disorders (Gray), CMS I Exam 7 (Respiratory Block Exam II, Monday
2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 42 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Rob Gray, DMSc, PA-C, Adjunct Instructor, NSU Jacksonville (Associate Professor and Associate Program
Director, Doctor of Medical Science, Arkansas Colleges of Health Education) -- title slide. calendar-data.js lists
"CMS I - LECTURE #42 - Pulmonary Vascular Disease - Dr. Gray GUEST LECTURER", Wednesday 2026-11-04, 8-10 AM (2
hours). No conflict (the deck says "Disorders", the calendar "Disease"). Deck file "Pulmonary Vascular Disorders
2026 - Gray.pptx", 62 slides. Same guest lecturer and same day as Lectures 43 and 44. He taught remotely ("I popped
positive for flu" [8:37]).

RECORDING: the live Zoom class, recordings/cms-l42-pulmonary-vascular-gray-2026-11-04.m4a (1:46:17), with Zoom's own
speaker-labeled transcript (.zoom-transcript.txt). Zoom transcript only; the faster-whisper cross-examination is
pending (Zoom's ASR garbles terms: "core pulmonary" = cor pulmonale, "wealth score"/"welt" = Wells, "perk" = PERC,
"Tedalafil", "Vapamil", "Arnies", "cigarettes" = SGLT2 inhibitors, "Curly B lines", "Palisine" = Palla, "Eloquus").
Host chat 4:14-8:37; screen sharing 5:41-1:12:21 and 1:12:25-1:38:45; the title slide sat on screen 6:15-12:30 while
students were admitted; content 12:30 (slide 2) to 1:38:45 (slide 62); break [1:12:02]-[1:12:29] (recording
paused); Q&A in gallery view [1:38:38]-[1:46:11], both student questions on Wells and PERC. Timestamps below are
recording time [m:ss]; the slide on screen comes from E/timeline_l42.txt (Zoom frames matched to the deck, 15 s
steps). Every slide 2-62 was shown; slide 18 only about 10 s (not in the timeline file, unread). Flags file:
recordings/cms-l42-pulmonary-vascular-gray-2026-11-04.flags.md.

SCOPE REMARKS FROM THE RECORDING (verbatim, [m:ss], slide on screen):
  Test markers (starred in the guide):
    Dyspnea trap, the top emphasis: "Here's the problem. Don't rely on shortness of breath." [1:16:59] s50; "Because
      about a quarter of people with, like, giant PEs don't have dyspnea." [1:17:35]; "If you walk away with nothing
      else from this lecture today, y'all, walk away with that." [1:17:58]; again in the summary "Remember, 25% of
      patients don't have dyspnea." [1:37:33] s62. (Also [1:17:18] "Test questions will throw you like textbook
      PEs": stems will usually give dyspnea; the 25% fact is the slide's.)
    S1Q3T3: "A classic finding, the one they tell you, oh, it's a board question, is S1Q3T3." [1:19:00] s51;
      "S1Q3T3 is a pattern for… Right ventricular strain." [1:19:42]-[1:19:50].
    Classic chest film signs: "Classic… classical signs, great for board questions." [1:21:14] s51.
    Wells and PERC: "big two tools we're gonna use for PE is your wealth score and your perk." [1:22:33] s53; "4 or
      lower, PE's unlikely. Score bigger than 4? So, 5 and up, PE likely." [1:24:38]-[1:24:43]; PERC "is a rule-out
      tool ... every single one of these has to be negative." [1:25:34] s54; Q&A "wells first ... if I got wells low
      risk. Then I can use PERC to rule out. It's not an either-or." [1:43:16]-[1:43:33]. Same day, Lecture 44
      wrap-up with no slide on screen (cms-l44-pleural-disorders-gray-2026-11-04.zoom-transcript.txt [1:37:27]):
      "know your wells, know your perk, those are gonna be super, like, that's fair game." [1:37:38] "Because it's
      easy math, and the risk factors are pretty straightforward, so know how to do those things."
    Pulmonary embolism risk stratification: "this is kind of what's on the books for now, so that's what you're gonna
      learn, that's what you're gonna get on pants" [1:32:48] s58; "know the one in the middle, and you're good."
      [1:33:53] (submassive / intermediate risk).
    Pulmonary hypertension prognostic risk: "When I start having signs of RV failure, I'm automatically at high risk.
      I got higher than 10% chance of dying in the next year." [47:31] s25.
    "PDE5 inhibitors, you should know. That's your AFILs." [48:20] s26.
    "COPD is the absolute leading cause." [15:00] s5. "So that alveolar hypoxia is the most important driver of that
      pulmonary hypertension when we get into our COPD patients." [20:20] s6.
    "the visual hallmark of bad right heart pressure overload is that septal flattening ... D shape" [33:06] s14.
    "Right heart is gonna be your gold standard." [45:21] s24. CTPA: "The modern gold standard." [1:29:02] s55; "you're
      gonna use CTPA as your gold standard. If you can't use it, VQ's okay." [1:38:09] s62.
    Echocardiography in pulmonary embolism: "It's not for diagnosis, it's for stratification." [1:31:06] s56.
    Thrombolysis: "We don't really like doing it for submassive" [1:35:51] s60; "If you can't do thrombolytics, again,
      somebody's had recent surgery, active bleeding, or you got, like, a clot in transit in the right heart"
      [1:36:04] s60. CTEPH: "the optimal management for CTEPH is surgical." [1:36:58] s61.
    "Over 18 to 20 is cardiogenic type failure." [1:04:37] s38.
  Cuts:
    s20 stage diagram: "Don't worry, I don't expect you to read these charts and stuff yet" [39:27].
    s24 wedge and pressure detail: "How did we get there? Don't worry about it. It's fine. That's what… that's what the
      rest of the ICU is for." [46:02]. No pressure thresholds for mean pulmonary artery pressure or resistance are on
      the slides: never key one.
    s26 endothelin receptor antagonists and prostacyclins: "don't freak out. Like, this is specialty sorcery a little
      bit. I'm just bringing it up for completeness" [48:20] (class level only).
    s28 algorithm: "don't lose sleep about exactly, like, the circumstances." [51:15]; "this is ICU stuff. So, don't
      freak out over it ... No single variable is going to determine that therapy. This is one of those where it's
      hard to do, like, a specific test question ... You just think in terms of, like, what's my functional class,
      and do calcium channel blockers work" [52:03]-[52:14]. Key the top level only; the cardiac index rule is cut.
    s16 "There's not, like, one answer, this is just an approach kind of slide." [35:33].
    s37 film reading: "don't worry, if you don't see it yet, don't freak out" [1:03:18] (the descriptions count).
    s41 "it's just a good refresher for you ... I'm not gonna beat it up too much." [1:07:30]-[1:07:57]; s42 "Don't
      lose too much sleep" [1:08:04]; s44 "don't go crazy on this one" [1:09:41]; s52 "Don't worry, don't freak out
      about that, just, you may see it called that." [1:22:26].
    Lecture 44 [1:37:44]: "Do I want you to memorize the entire flow chart for things? Absolutely not" -- key the
      decision points of s57 and s61, never every box.
  Advice and mnemonics (guide only): "When you're studying for pants, and you've got 3 things, remember the one in the
  middle." [46:51] s25; S3 = "big floppy left ventricle", S4 = "stiffened" [41:49]-[42:17] s22; "your prostaglandins
  generally have PROST in the name" [50:00] s26; LMNOP "like my toolbox, not a checklist" [1:05:03]-[1:05:19] s39;
  "pipes, pumps, or filter? ... your differentials all spring from the answer to that question" [58:36]-[58:47] s33;
  "I don't need 15 risk factors, I just need a couple of good ones." [1:15:51] s49; "What gets you in trouble is
  your failure to imagine the differential." [1:14:11] s48; "Don't be that guy where it's like, well, that was
  misspelled, so I get free points." [12:12] (typos in the AI pictures).

MINUTES (timeline minutes on screen, minus off-content stretches; see the flags file):
  cor pulmonale definition 3.75 (s4-5 plus s3, where he defined it); cor pulmonale pathophysiology 10.75 (11.25 less
  the test-prep aside [21:30]-[21:57]); cor pulmonale diagnosis and management 7.75 (8.25 less a chat question
  [35:37]-[36:10]); pulmonary hypertension classification 3.5 (s17 divider, s18 about 10 s, s19-20); presentation
  4.75; diagnosis and prognosis 3.1 (Mayo aside [45:41]-[46:04]); treatment 5.4 (6.5 less the off-slide
  nitroglycerin chat quiz [49:24]-[49:45], candy, "Prost", a family story [53:44]-[54:01]); pulmonary edema
  mechanism 4.75; presentation and diagnosis 5.15 (wilderness aside [1:00:06]-[1:00:42]); management 5.8 (off-slide
  thoracentesis story [1:10:47]-[1:11:30]); pulmonary embolism risk factors and presentation 7.5 (attorney aside,
  off-slide sinus tachycardia [1:19:07]-[1:19:42]); diagnosis 9.4 (off-slide D-dimer list [1:26:45]-[1:27:28],
  coworker story [1:27:39]-[1:28:46]); risk stratification and treatment 6.0. Total 77.6 of 84.0 timeline minutes.
  Not counted: the Q&A [1:40:04]-[1:45:49] (about 5.75 minutes, all Wells and PERC), which REQUIRED covers instead.

WHERE HE AND THE SLIDES DIFFER (no out-loud correction of any slide; the slide wins every time):
  Wells malignancy: Q&A "Any malignancy? ... I had Mohs, that still puts me on the radar ... Malignancy is malignancy
    is malignancy." [1:40:17]-[1:41:09]. Slide 53: "Malignancy (on treatment, treated in last 6 months, or
    palliative)", which he read at [1:24:13]-[1:24:33]. Key the slide; vignettes avoid skin cancer and remote cancer.
  PERC trauma: "even lowercase t trauma counts" [1:42:11]. Slide 54: "No surgery/trauma" (unqualified) -- the same
    thing; vignettes avoid minor-trauma ambiguity.
  PERC order: "If I get a single positive, I jump to Wells" [1:25:37]. Slide 57 runs Wells first, then PERC when PE is
    unlikely; he restates that order at [1:31:24]-[1:31:56] and [1:43:16]. Key slide 57.
  Prior DVT/PE: "Don't get me started on this one, because this is the same weight" [1:23:56] -- the slide files it
    under "Lower Weight Criteria" at +1.5. Key the points; never key the high/lower label for that row.
  "4 or higher… 4 or lower, PE's unlikely" [1:24:38]: a slip he fixed at once; matches the slide.
  Positive pressure: "I need to give oncotic pressure, and the best way to do that is air pushing in" [1:06:20] -- a
    slip; slide 40 says positive pressure stents alveoli and lowers preload and afterload. Never key "oncotic" here.
  Off-slide, never keyed: sinus tachycardia as "The most common EKG finding in pulmonary embolism" ("I didn't put this
    on a slide" [1:19:07]-[1:19:18], again [1:23:32], [1:37:49]) -- it reaches the exam only as Wells heart rate
    >100 (+1.5); phosphodiesterase-5 inhibitor plus nitroglycerin ("what do I not need to give ... Nitro" [49:29]);
    amlodipine and verapamil as the calcium channel blockers [51:30]; flash pulmonary edema after aggressive
    thoracentesis [1:10:47]; D-dimer raised by bruises, lacerations, pregnancy, COVID [1:27:07]-[1:27:24]; apixaban
    ("Eloquus" [1:33:24]). The slides name no anticoagulant or thrombolytic drug.

SLIDE CONFLICTS (slide vs slide; never keyed one way or the other):
  "Gold standard": s14 calls echocardiography "The Gold Standard" (cor pulmonale); s24 calls right heart
    catheterization "The mandatory gold standard" (pulmonary hypertension; he said so out loud [45:21]); s36 calls
    transthoracic echo the "Gold Standard for Structural Assessment" (pulmonary edema); s55 calls CTPA "The Modern Gold
    Standard" (pulmonary embolism). Key: echo = "the most useful initial test" / screening (s24); right heart
    catheterization confirms pre-capillary pulmonary hypertension by measuring mean pulmonary artery pressure, wedge
    pressure and resistance (s24); CTPA = first-line imaging and gold standard for PE (s55, s62). Never write "gold
    standard" next to echocardiography (banned).
  Wedge pressure cut-offs: <=15 = pre-capillary pulmonary hypertension and cor pulmonale, >15 = left heart failure
    (s12, s23); cardiogenic pulmonary edema >18-20 and noncardiogenic <=18 (s33, s38), >18 (s45). A wedge of 16-18
    is "elevated" on s23 but "noncardiogenic" on s33: vignettes give <=12 or >=22 only (values 15-18 banned).
  Nitrates: "immediate preload and afterload reduction via venodilation" (s39, and he said "We reduce preload and
    afterload" [1:05:38]) vs "Use IV nitrates to rapidly reduce afterload" (s46). Key s39; never key "afterload only"
    or "preload, not afterload".
  Echo vs right heart catheterization on s12 ("Step 3: RHC & Echo"): fine together; s24 decides which does what.
  s44 repeats its stage D "Marked symptoms" bullet (layout duplicate, no conflict).

DECK VS CURRENT GUIDELINES (slides keyed; one line each for the guide):
  s22 "Elevated JVP (>8 cm above the left atrium)": jugular venous pressure is measured from the sternal angle (right
    atrium reference); never key the number or the chamber (banned).
  s27 "pneumococcal (23-valent and 13-valent)": the current adult schedule uses PCV20 or PCV21 (or PCV15 then PPSV23);
    key "annual influenza and pneumococcal immunization" only (valencies banned).
  s41 "MRA ... per the 2024 FINEARTS-HF trial": FINEARTS-HF tested finerenone (nonsteroidal); the trial name is banned.
  s58 submassive/intermediate risk: the 2019 European Society of Cardiology scheme splits intermediate-high and
    intermediate-low; he said "They're starting to rethink the stratification now" [1:32:48]. Key the slide's three.
  s53 Wells immobilization ">3 days": the published rule reads "3 days or more"; vignettes avoid exactly 3 days.
  s54 PERC "O2 >94%" equals the published "saturation 95% or more"; "No surgery/trauma" (the published rule adds
    "within 4 weeks, needing hospitalization"); vignettes avoid boundary values.
  s39 morphine "use with caution": current heart failure guidelines advise against routine morphine; the slide's
    caution is what is keyed.
  s61 CTEPH: balloon pulmonary angioplasty and riociguat exist for inoperable disease (not on the slide; never keyed).

PICTURE SLIDES: slides 3-62 are single AI-made infographic pictures (watermark "Gemini Notebook"); every fact lives
only in a picture, so E/l42_deck.txt is OCR evidence and every render (render/l42vascular_hi/s003-s062.png) was
viewed. Decorative monitor readouts on s49-s62 (heart rate 145/180/100, saturation 95/90, blood pressure 100/72,
"D-Dimer 0.3", "Impact" bars) and the s38 wedge graph values (8, 12, 22) and the s31 gauge (75) are decoration:
never key them. s51 carries a drawn EKG strip (deep S in lead I; Q and inverted T in lead III) and a chest film with
circles 1-3 labeled Westermark, Hampton's hump, Palla. s56 carries a "D-Shaped Septum" drawing. s3 states "driving up
to 20% of all hospital admissions" (unread, unsupported, banned). AI typos ("reles", "causs", "nonadhorence",
"loprost") are spelling only.

EXCLUDED_SLIDES:
  1    title (Rob Gray)
  2    objectives (deck wording, not the syllabus)
  3    section title picture ("The Right Heart's Burden"; its only claim is the 20% admissions figure)
  17   section divider ("Cor Pulmonale & Pulmonary Hypertension")
  30   section divider ("Pulmonary Edema / The Drowning Lung")
  31   decorative "The Drowning Lung" picture (garbled labels, 75 gauge)
  47   section divider ("Pulmonary Embolism")
  Slide 18 stays citable (definition; "the most common cause of RV failure overall is Left Ventricular (LV)
  failure") although it was on screen only about 10 s: use it at most once per pool.

WRITING PLAN (each pool set needs ~70+ items for the two 30-item forms; the partition weights by TOPIC_MINUTES;
counts are IO pool / vignette pool; "*" = he flagged it; spell out every abbreviation: "PERC (Pulmonary Embolism
Rule-out Criteria)", "World Health Organization group 3", "CTPA (computed tomographic pulmonary angiography)" or just
the words; no mechanism-of-action stems -- ask which class fits a situation, never how a drug works):

T_CP_DEF "Cor pulmonale: definition and causes" s4-5, 4 / 3.
  Definition: alteration in right ventricular structure and function (enlargement, hypertrophy, dilation) caused
  EXCLUSIVELY by a primary disorder of the respiratory system or pulmonary vasculature; elevated mean pulmonary artery
  pressure with NORMAL wedge pressure; "Group 2 PH: Left Heart Failure. This is NOT Cor Pulmonale."; elevated
  left-sided filling pressures must be excluded first (s4). s18: most common cause of right ventricular failure
  overall is left ventricular failure. Causes (s5): parenchymal, primarily chronic -- *COPD "The absolute leading
  cause", present in >50% of COPD; interstitial lung disease (fibrotic destruction); sleep-disordered breathing
  (chronic nocturnal alveolar hypoventilation). Vascular, acute and chronic -- acute PE (sudden macroscopic
  occlusion); primary pulmonary arterial hypertension (idiopathic remodeling, Group 1); CTEPH (unresolved clot
  burden, Group 4). Leads: diagnosis (left heart failure vs cor pulmonale by wedge pressure), classify (cause
  category), test. Trap: right heart failure from left heart failure is NOT cor pulmonale.

T_CP_PATHO "Cor pulmonale: pathophysiology and hemodynamics" s6-11, 10 / 9.
  s6: healthy lung -- localized hypoxia gives focused vasoconstriction that shunts blood and optimizes ventilation-
  perfusion matching; chronic lung disease (COPD "Blue Bloaters") -- global alveolar hypoxia and hypercapnia give
  diffuse vasoconstriction, a massive rise in pulmonary vascular resistance and relentless right ventricular
  afterload; *"Alveolar hypoxia is the single most important driver of pulmonary hypertension in COPD." s7: structural
  effacement (emphysema, fibrosis, PE) makes the resistance anatomical, not just functional; loss of total
  cross-sectional area; compounding factor polycythemia (from chronic hypoxia) raises blood viscosity. s8: acute
  crash (massive PE) -- pressure outpaces adaptation, wall tension rises instantly: acute dilation, stretch,
  microinfarction; chronic burden (COPD, ILD) -- gradual rise, compensatory hypertrophy until exhaustion; the right
  ventricle is thin-walled, high-compliance, low-pressure, highly sensitive to sudden afterload change. s9 matrix:
    Acute   | massive PE            | minutes to hours | sudden dilation and dysfunction | severe sudden dyspnea,
            |                       |                  |                                 | sweating, rapid pulse,
            |                       |                  |                                 | pallor, syncope
            | threat: decreased left ventricular filling, immediate cardiovascular collapse (shock)
    Chronic | COPD, ILD, PAH        | months to years  | concentric hypertrophy, then    | unproductive cough,
            |                       |                  | late dilation                   | progressive exertional
            |                       |                  |                                 | dyspnea, "Blue Bloater"
            | threat: progressive volume overload, hypoxemia, right heart failure
  s10 acute chain: right ventricular wall tension spikes -> acute dilation -> septum bows LEFTWARD into the left
  ventricle -> left ventricular diastolic distensibility and filling fall -> output plummets, systemic hypotension,
  collapse; signs: distended neck veins, tricuspid regurgitation murmur (stretched annulus), tachycardia, pallor.
  s11 chronic decompensation: right ventricular heave (parasternal lift, left sternal border), intensified P2,
  tricuspid regurgitation systolic murmur; tender hepatomegaly, ascites, dependent pitting edema. Leads: diagnosis
  (acute vs chronic), classify (acute vs chronic), complication (shock from septal shift; polycythemia), test.
  Trap: hypertrophy needs time -- acute = dilation.

T_CP_DXTX "Cor pulmonale: diagnosis and management" s12-16, 7 / 7.
  s12 funnel: Step 1 chest x-ray (interstitial markings = ILD, hyperinflation = COPD, vs clear fields) and pulmonary
  function tests (obstructive vs restrictive) -> Group 3; Step 2 ventilation-perfusion scan or CTPA to exclude
  segmental defects (CTEPH, PE) -> Group 4; Step 3 right heart catheterization and echo: elevated mean pulmonary
  artery pressure with wedge <=15 mmHg -> Group 1. s13: obstructive (COPD) = reduced FEV1/FVC (spell out), "The most
  common cause"; restrictive (ILD) = reduced total lung capacity, "Crucial for classifying Group 3"; chest film:
  flattened diaphragms (COPD hyperinflation), enlarged central pulmonary arteries; in PAH or PE the peripheral fields
  may look deceptively clear. s14: EKG peaked P waves (right atrial enlargement), tall R in V1 (right ventricular
  hypertrophy), abnormal in 70% of acute PE, severe right axis deviation in chronic cor pulmonale; echo: right
  ventricular enlargement, estimates pulmonary artery systolic pressure, *systolic septal flattening = D-shaped left
  ventricle. s15: prime directive -- treat the underlying lung disease; "Oxygen is a Drug" -- continuous supplemental
  oxygen is paramount in Group 3 (COPD, ILD) and reverses alveolar hypoxic vasoconstriction; COPD bronchodilators and
  aggressive treatment of respiratory infections; acute PE thrombolytics and anticoagulation (expand blood volume if
  hypotensive); Group 1 PAH phosphodiesterase-5 inhibitors, endothelin receptor antagonists, prostacyclins. s16 fluid
  balance: too much = hepatic congestion and severe edema; too little = decreased left ventricular filling and a
  catastrophic output drop; diuretics (loop, spironolactone) for retention; the damaged right ventricle relies on
  elevated filling pressures (preload); over-diuresis starves the left ventricle; hypokalemia can trigger lethal
  arrhythmias. "What instead": avoid aggressive diuresis in right ventricular failure (s16, s27); watch potassium on
  loop diuretics (s16); oxygen as therapy for the COPD patient (s15). Leads: test, next step, treatment, avoid,
  complication, classify (group from the workup).

T_PH_CLASS "Pulmonary hypertension: classification and pathophysiology" s18-20, 4 / 4.
  s19 World Health Organization groups (FULL table; REQUIRED_VIG "group from the vignette"):
    Pre-capillary  Group 1 (PAH)                  obliterative/proliferative  idiopathic, connective tissue disease,
                                                                              HIV (spell out), schistosomiasis
                   Group 3 (lung disease/hypoxia) [mechanism word banned]     COPD, interstitial lung disease, sleep
                                                                              apnea
                   Group 4 (CTEPH)                obstructive                 chronic thromboembolic occlusion
    Post-capillary Group 2 (left heart disease)   passive                     obstruction to pulmonary venous
                                                                              outflow (HFrEF, HFpEF, mitral stenosis)
                   Group 5 (unclear/multifactorial) complex                   hematologic, systemic, metabolic
                                                                              (e.g., sarcoidosis)
  Spoken [38:10]: "Group 1… Arterial ... Group 3, lung disease ... Group 4 is clots. Group 2 is left heart failure."
  s20 (sequence only, "Don't worry ... these charts"): stage 1 compensatory hypertrophy; stage 2 dilation and failure
  (Frank-Starling fails, end-diastolic volume rises); stage 3 ventricular interdependence (septum bows into the left
  ventricle) -> impaired left ventricular diastolic filling -> reduced output -> exertional syncope despite normal
  left ventricular contractility. Leads: classify (group), diagnosis, complication (exertional syncope).

T_PH_PRES "Pulmonary hypertension: presentation and examination" s21-23, 5 / 5.
  s21 (percentages banned): exertional dyspnea and fatigue -- often the only early symptom, frequently misattributed
  to deconditioning = Early/Mild (World Health Organization class I-II); dizziness/lightheadedness, marked limitation
  = Moderate (class III); syncope/presyncope = ominous, a fixed low output that cannot rise with exertion; end-stage
  abdominal bloating, early satiety, edema, present at rest = Severe (class IV). s22: elevated jugular venous pressure
  with large a waves (early) or regurgitant v waves (tricuspid insufficiency) [no number, no chamber]; parasternal
  lift (right ventricular heave); accentuated P2; right ventricular S3 gallop (right ventricular dysfunction);
  hepatojugular reflux (sustained moderate pressure on the liver raises the venous pressure by >1 cm; elevated
  right-sided filling pressures); edema up to hips and sacrum when severe; cool extremities (low output, peripheral
  vasoconstriction). s23 table:
    Left heart failure: orthopnea, paroxysmal nocturnal dyspnea; bibasilar crackles, wheezing, Kerley B lines, pleural
      effusions; wedge >15 mmHg.
    Right heart failure / cor pulmonale: abdominal bloating, early satiety, profound fatigue, exertional syncope; lungs
      typically clear; film shows enlarged central pulmonary arteries with peripheral pruning; normal/low wedge (<=15)
      with elevated mean pulmonary artery pressure.
  Leads: diagnosis (left vs right failure), classify (functional class from symptoms), complication, test.

T_PH_DX "Pulmonary hypertension: diagnosis and prognosis" s24-25, 4 / 4.
  s24: echo = screening, "the most useful initial test" (right ventricular size, TAPSE (spell out), pulmonary
  pressures; finds left-sided valvular or myocardial mimics); ventilation-perfusion scan = "Essential test to exclude
  CTEPH"; pearl: do not rely solely on CT angiography -- a high-probability mismatch sends the patient down a
  surgical pathway (thromboendarterectomy) (*[45:04]); right heart catheterization = the mandatory confirmation,
  measures mean pulmonary artery pressure, wedge pressure and pulmonary vascular resistance to confirm pre-capillary
  pulmonary hypertension (*[45:21]). s25 prognostic risk (estimated 1-year mortality; REQUIRED_VIG):
    Low (<5%)            RV failure signs absent   progression slow      no syncope          class I or II  walk >440 m
    Intermediate (5-10%) RV failure signs absent   progression moderate  occasional syncope  class III      165-440 m
    High (>10%)          RV failure signs PRESENT  progression rapid     repeated syncope    class IV       <165 m
  (*"When I start having signs of RV failure, I'm automatically at high risk" [47:31].) Six-minute walk distances are
  on the slide and keyable. Leads: test (initial vs confirm vs exclude CTEPH), next step, classify (risk), complication
  (prognosis). Mixed-feature vignettes: make the classifying feature decisive (right ventricular failure signs ->
  high), not a tie.

T_PH_TX "Pulmonary hypertension: treatment" s26-29, 5 / 5.
  s26 classes (no mechanism-of-action stems): endothelin receptor antagonists (ambrisentan, bosentan, macitentan);
  *phosphodiesterase-5 inhibitors (sildenafil, tadalafil -- "your AFILs"); prostacyclins / IP receptor agonists
  (epoprostenol, treprostinil, iloprost, selexipag) = "most potent class for vasodilation and anti-platelet
  aggregation; essential for severe disease". s27: careful diuresis is central (IV loop diuretics venodilate before
  they diurese; avoid aggressive over-diuresis -- it drops preload and crashes output); keep PaO2 >60 mmHg, oxygen
  especially during sleep or exertion (hypoxia is a potent pulmonary vasoconstrictor); avoid strict bedrest --
  supervised steady aerobic rehabilitation is safe, prevents deconditioning, improves fatigue; annual influenza and
  pneumococcal immunizations mandatory (no valencies). s28 top level only: vasoreactive -> high-dose oral calcium
  channel blockers (no drug names); not vasoreactive -> stratify: low/intermediate (class II/III) -> oral combination
  (endothelin receptor antagonist + phosphodiesterase-5 inhibitor), early combination beats sequential monotherapy;
  high risk (class IV or rapid decline) -> continuous IV or subcutaneous parenteral prostanoids (epoprostenol). s29:
  advance directives and early palliative care (sudden death or lethal syncope may be the first sign of
  progression); about 6% survival at 90 days after CPR (spell out) in PAH; lung transplantation is the only
  definitive option for refractory disease (or pulmonary veno-occlusive disease), IV support as a bridge. "What
  instead": no strict bedrest (s27); no aggressive diuresis (s27); calcium channel blockers only when vasoreactive
  (s28). Leads: treatment, next step, avoid, education, referral (transplant, palliative care).

T_EDEMA_MECH "Pulmonary edema: mechanism and causes" s32-34, 5 / 4.
  s32: outward force = elevated capillary hydrostatic pressure, "the engine of cardiogenic edema"; inward = plasma
  oncotic pressure, the failing counterbalance; barrier = semi-permeable capillary membrane, intact but overwhelmed;
  *edema when hydrostatic exceeds oncotic, or the barrier shatters [57:01]. s33: cardiogenic = pressure problem
  (intact capillaries under hydrostatic backup; wedge >18-20 mmHg; "the pump is failing"); noncardiogenic =
  permeability problem (shattered endothelium leaking protein-rich fluid; wedge <=18; "the pipe is leaking"). s34
  causes -- cardiogenic: systolic dysfunction (ischemic, reduced ejection fraction), diastolic (stiffening and aging,
  preserved ejection fraction), valvular (chronic aortic/mitral regurgitation, severe stenosis); noncardiogenic: ARDS
  (spell out; inflammatory capillary destruction), sepsis (systemic vasodilation and endothelial leak), toxins
  (inhaled chemical injury). Leads: classify (cardiogenic vs noncardiogenic), diagnosis, test.

T_EDEMA_DX "Pulmonary edema: presentation and diagnosis" s35-38 and s43, 5 / 6.
  s35: pink frothy sputum (alveolar fluid shift with microvascular hemorrhage; "by the time I'm, like, coughing up
  pink frothy stuff, I am late in the game" [59:58]); bilateral rales/crackles and wheezing (fluid-filled airways,
  peribronchial cuffing); S3 gallop (overloaded failing ventricle); acute dyspnea, diaphoresis, tripoding
  (catecholamine surge). s36: B-type natriuretic peptide proves ventricular stretch -- substantial elevation separates
  cardiogenic dyspnea from pulmonary mimics; transthoracic echo = best test for structural assessment (ventricular
  size, ejection fraction, valves) [never write "gold standard" beside echo]; pulmonary artery catheter / right heart
  catheterization = the "ultimate hemodynamic arbiter" when the cause is uncertain. s37: batwing opacities (central
  perihilar alveolar edema); peribronchial cuffing (edema thickening bronchiole walls, blurring); Kerley B lines
  (horizontal peripheral lines, fluid in the interlobular septa); bilateral pleural effusions. s38: the balloon wedge
  "looks forward" to measure left atrial pressure; >18-20 mmHg confirms cardiogenic hydrostatic failure. s43 mimics
  (shared: dyspnea, hypoxemia, tachycardia): heart failure = highly elevated natriuretic peptide, echo abnormalities,
  Kerley B lines; PE = clear lungs on film, natriuretic peptide normal initially, S1Q3T3 or right ventricular strain;
  COPD exacerbation = wheezing/hyperinflation, hypercapnia, natriuretic peptide usually normal. Leads: diagnosis,
  test, classify.

T_EDEMA_TX "Pulmonary edema: management and prognosis" s39-42, s44-46, 6 / 6.
  s39 LMNOP (toolbox, not checklist): Loop diuretics IV (furosemide, bumetanide, torsemide); Morphine -- use with
  caution (venodilation/anxiolysis vs respiratory depression); Nitrates IV -- immediate preload AND afterload
  reduction via venodilation; Oxygen and upright positioning (gravity reduces venous return); Positive airway
  pressure (noninvasive ventilation: alveolar stenting, preload reduction). s40: positive pressure stents alveoli,
  pushes fluid back, lowers intrathoracic preload and afterload; nitrate venodilation shifts volume into venous
  capacitance, lowering capillary hydrostatic pressure. s41 (refresher, 1-2 items): quadruple therapy -- ARNI
  (sacubitril-valsartan; spell out), beta-blockers, mineralocorticoid receptor antagonists (reduced and preserved/
  mildly reduced ejection fraction), SGLT-2 inhibitors (spell out; newest); greatest mortality reduction in reduced
  ejection fraction. s42 POPULATIONS: adult (reduced ejection fraction; ischemia-driven; higher reserve; tolerates
  aggressive diuresis) vs elderly (preserved ejection fraction; age-related stiffening; elevated end-diastolic
  pressure; extreme preload sensitivity; narrow margin; gentle, precise diuresis; over-diuresis -> precipitous
  hypotension; under-diuresis -> recurrent flooding). s44 stages: A and B prevention and risk focus; C quadruple
  therapy; D marked symptoms at rest despite maximal therapy, frequent hospitalizations -> referral for heart
  transplant, mechanical circulatory support (LVAD, spell out), or palliative/hospice care. s45: synthesis (phase 2
  wedge >18 mmHg). s46 flash pulmonary edema: triggers acute MI, severe ischemia, severe hypertension; chronic heart
  failure exacerbation (nonadherence, excess salt, rapid arrhythmias); signs severe dyspnea, cyanosis, diaphoresis,
  pink frothy sputum; diffuse bilateral rales, rhonchi, expiratory wheezing; film "butterfly pattern edema and
  vascular blurring"; elevated natriuretic peptide, elevated wedge, hypoxemia; table cardiogenic (wedge elevated;
  acute MI, severe hypertension, chronic heart failure decompensation; cardiac enlargement/dysfunction common) vs
  noncardiac (wedge normal or low; ARDS, high altitude, sepsis, toxins; cardiac function typically normal);
  interventions upright with legs dangling, oxygen or noninvasive ventilation, IV furosemide (immediate venodilation
  and diuresis), IV nitrates; transition: temporarily hold outpatient therapy during acute kidney injury; CONTINUE
  oral beta-blockers unless the patient is in shock; cautious morphine (eases anxiety, risks severe ventilatory-drive
  reduction). Multi-comorbidity "what instead": flash edema on a home beta-blocker -> continue it (stop only in
  shock); flash edema with acute kidney injury -> hold outpatient therapy; hypercapnic COPD patient in pulmonary
  edema -> morphine is the agent to avoid; elderly preserved-ejection-fraction patient -> gentle diuresis, never
  aggressive. Leads: treatment, next step, avoid, referral (stage D), complication, classify (stage).

T_PE_RISK "Pulmonary embolism: risk factors and presentation" s48-51, 7 / 7.
  s48: DVT and PE are one continuum; asymptomatic to hemodynamic collapse and death. s49 Virchow's triad:
  hypercoagulability (malignancy, estrogen therapy, pregnancy, genetic thrombophilias, sepsis); venous stasis
  (prolonged immobilization >8 hr flights, bed rest, paralysis, heart failure New York Heart Association III/IV);
  endothelial injury (recent surgery, central venous catheters, pacemaker wires, pelvic/lower limb trauma); "Inability
  to identify a known clinical predisposition should never dissuade an objective evaluation if the presentation is
  consistent with embolism." s50 three syndromes: isolated dyspnea (sudden over minutes to hours, at rest or only with
  exertion); pleuritic pain and hemoptysis (distal pleural-based infarction, localized friction rub); circulatory
  collapse (syncope, severe hypotension, obstructive shock = massive proximal occlusion); *THE DYSPNEA TRAP:
  approximately 25% of proven PE completely lack dyspnea (REQUIRED_IO). s51: *S1Q3T3 (deep S in lead I, Q wave and
  inverted T in lead III) "Suggests severe RV strain, not purely PE. Highly specific, but low sensitivity."; *chest
  film: Westermark sign (focal peripheral oligemia, decreased vascularity), Hampton's hump (wedge-shaped pleural-based
  opacity = infarction), Palla sign (enlarged right descending pulmonary artery); most PE films are abnormal but
  nonspecific (atelectasis, effusion); classic signs highly suggestive but infrequent. Leads: diagnosis, test (what
  the EKG or film shows), complication, classify (which syndrome). Traps: no "most common EKG finding" item (banned);
  S1Q3T3 = right ventricular strain, highly specific, low sensitivity -- never "sensitive" or "PE only".

T_PE_DX "Pulmonary embolism: diagnosis" s52-57, 9 / 10.
  s52: Bayesian -- the pre-test probability (Wells) is set independently of any test and decides which test and how
  to read it; tests = D-dimer, CTPA, ventilation-perfusion scan. s53 *Wells (FULL table; REQUIRED_IO and _VIG):
    +3.0 clinical signs and symptoms of DVT            +1.5 previous DVT or PE
    +3.0 PE is the #1 diagnosis (more likely than      +1.0 hemoptysis
         alternatives)                                 +1.0 malignancy (on treatment, treated in last 6 months,
    +1.5 heart rate >100 bpm                                or palliative)
    +1.5 immobilization (>3 days) or surgery in previous 4 weeks
    Score <=4 = PE unlikely; >4 = PE likely; decides biomarker (D-dimer) vs direct imaging (CTPA).
  s54 *PERC (FULL; REQUIRED_IO and _VIG), all eight must be true to stop: age <50; heart rate <100; oxygen saturation
  >94%; no hemoptysis; no exogenous estrogen; no prior VTE (spell out); no surgery/trauma; no unilateral leg swelling;
  "For very low clinical gestalt (<15%). If all true, STOP workup." D-dimer: for low/intermediate probability
  patients who FAIL PERC; high sensitivity, low specificity; a negative ELISA (spell out) D-dimer safely excludes PE;
  positive -> imaging; these tools rule OUT disease in outpatients; D-dimer has limited utility in inpatients
  (universally high false-positive rates). s55: CTPA = "The Modern Gold Standard", first-line for almost all
  patients; limits: IV iodinated contrast, radiation, overdiagnosis of clinically insignificant subsegmental PE.
  Ventilation-perfusion scan: frequently nondiagnostic with underlying cardiopulmonary disease (COPD, severe heart
  failure); best for renal dysfunction, severe contrast allergy, critically ill (portable bedside perfusion scan); a
  completely negative scan excludes PE with the same certainty as a negative pulmonary angiogram. s56: massive PE ->
  acute right ventricular pressure overload -> septum bows into the left ventricle -> lower left ventricular
  end-diastolic volume -> crashed output and collapse; *transthoracic echo has poor sensitivity (~50%) for acute PE
  but very high specificity for right ventricular strain: risk stratification, NOT diagnosis. s57 algorithm: Wells
  <=4 -> PERC: pass -> stop; fail -> D-dimer: negative -> ruled out; positive -> CTPA. Wells >4 -> bypass D-dimer,
  direct CTPA (or ventilation-perfusion scan if contrast is contraindicated). Positive CTPA / high-probability scan ->
  confirmed -> assess hemodynamic stability and right ventricular strain. Multi-comorbidity "what instead": PE likely
  plus severe contrast allergy or renal dysfunction -> ventilation-perfusion scan (REQUIRED_VIG); PE likely plus
  severe COPD or heart failure (normal kidneys, no allergy) -> CTPA, because the scan is often nondiagnostic; Wells >4
  -> skip the D-dimer; hospitalized patient -> D-dimer of limited use. Leads: next step, test, classify (Wells total,
  PERC pass/fail), avoid. Vignette rules for scoring items: state every Wells and PERC element explicitly (say
  outright whether PE is judged the most likely diagnosis; give heart rate, saturation, age, estrogen use, prior
  clots, recent surgery or trauma, leg swelling, hemoptysis, cancer status); avoid boundary values (heart rate 100,
  saturation 94-95%, immobilized exactly 3 days, surgery exactly 4 weeks ago, cancer treated exactly 6 months ago,
  skin cancer); a total of exactly 4 is allowed and keys "unlikely".

T_PE_TX "Pulmonary embolism: risk stratification and treatment" s58-62, 6 / 7.
  s58 risk stratification (FULL table; REQUIRED_IO and _VIG; *"know the one in the middle"):
    Low-risk                    normotensive, NO right ventricular dysfunction, negative cardiac biomarkers ->
                                excellent prognosis, standard anticoagulation
    Submassive / intermediate   normotensive (systolic >90) BUT right ventricular dysfunction (echo or CTPA) or
                                myocardial necrosis (elevated troponin or natriuretic peptide) -> high risk of sudden
                                deterioration
    Massive / high-risk         sustained hypotension (systolic <90 for >15 min), pulselessness, or profound
                                bradycardia; circulatory collapse -> high mortality, immediate advanced intervention
  (no systolic of exactly 90; no hypotension of exactly 15 minutes). s59: phase 1 immediate anticoagulation on a
  confirmed diagnosis (or high clinical suspicion while awaiting imaging); phase 2 the 3-month decision --
  transient/provoked (recent surgery, trauma, hospitalization, estrogen therapy) -> consider stopping after 3 months;
  persistent/unprovoked (active malignancy, hypercoagulable states, no identifiable risk factor) -> indefinite
  anticoagulation; DVT and PE are managed identically; goal = halt propagation and allow endogenous fibrinolysis.
  s60: systemic and catheter-directed thrombolysis = "the gold standard for Massive PE (hemodynamically unstable)";
  "Highly controversial in Submassive PE" (bleeding and intracranial hemorrhage risk); mechanical thrombectomy and
  surgical embolectomy = reserved for massive PE with absolute contraindications to thrombolytics (e.g., recent
  surgery, active bleeding) or a right heart "clot in transit". s61 CTEPH: screen for persistent or worsening dyspnea
  after 3 months of anticoagulation; none -> length of anticoagulation by recurrence risk; persistent -> ventilation-
  perfusion scan: normal -> back to the length decision; abnormal -> transthoracic echo, right heart catheterization,
  pulmonary angiogram, refer to an expert center, continue anticoagulation; risk factors: unprovoked PE, delay in
  diagnosis >2 weeks, right ventricular dysfunction on the first CTPA, recurrent PE; *optimal treatment surgical
  (pulmonary thromboendarterectomy). s62 summary: suspect (Virchow, 25% without dyspnea, S1Q3T3), calculate (Wells
  <=4 -> PERC and D-dimer; >4 -> imaging), locate (CTPA; ventilation-perfusion for renal failure or allergy; echo
  D-shaped septum), stratify (massive = obstructive shock; submassive = right ventricular strain or biomarkers;
  low-risk = stable), treat (anticoagulate all; thrombolyze or thrombectomize the unstable; screen for CTEPH at 3
  months). Multi-comorbidity "what instead": massive PE plus recent surgery, active bleeding or a right heart clot in
  transit -> mechanical thrombectomy or surgical embolectomy (REQUIRED_VIG); submassive PE -> anticoagulation, with
  thrombolysis controversial; post-operative (provoked) PE -> consider stopping at 3 months, active cancer ->
  indefinite; persistent dyspnea at 3 months -> ventilation-perfusion scan. No anticoagulant or thrombolytic drug
  names (none on the slides; banned). Leads: classify, treatment, next step, avoid, education (duration), referral
  (expert center), complication (CTEPH).

POPULATIONS (IO_POP): slide 42 is the adult vs elderly slide (gentle diuresis in the elderly, preserved ejection
fraction, narrow margin); also s54 (age <50 in PERC: an older patient cannot be PERC-negative), s49 (pregnancy,
estrogen), s27 (avoid bedrest; rehabilitation), s29 (advance directives), s21 (early symptoms misread as
deconditioning). Put at least 4 IO_POP items in the objective pool and 2 in the vignette pool so both forms can carry
one.
"""

DECK = "Pulmonary Vascular Disorders 2026 - Gray.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

# Syllabus objectives (CMS syllabus p. 20, "Pulmonary Vascular Disease"), verbatim; the leading "1." dropped and the
# syllabus's own sub-numbering kept (it numbers the diseases 2-5, the population objective 6, the populations 7-8).
IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following pulmonary vascular diseases: 2. Cor pulmonale 3. Pulmonary embolism "
        "4. Pulmonary hypertension 5. Pulmonary edema")
IO_POP = ("Identify medical care strategies for pulmonary vascular disease in the lecture topic list for the "
          "following populations. 7. adult 8. elderly")
IOS = [IO_A, IO_POP]

# Topic names the pools use (quiz chips) and their slide ranges.
T_CP_DEF = "Cor pulmonale: definition and causes"
T_CP_PATHO = "Cor pulmonale: pathophysiology and hemodynamics"
T_CP_DXTX = "Cor pulmonale: diagnosis and management"
T_PH_CLASS = "Pulmonary hypertension: classification and pathophysiology"
T_PH_PRES = "Pulmonary hypertension: presentation and examination"
T_PH_DX = "Pulmonary hypertension: diagnosis and prognosis"
T_PH_TX = "Pulmonary hypertension: treatment"
T_EDEMA_MECH = "Pulmonary edema: mechanism and causes"
T_EDEMA_DX = "Pulmonary edema: presentation and diagnosis"
T_EDEMA_TX = "Pulmonary edema: management and prognosis"
T_PE_RISK = "Pulmonary embolism: risk factors and presentation"
T_PE_DX = "Pulmonary embolism: diagnosis"
T_PE_TX = "Pulmonary embolism: risk stratification and treatment"

TOPIC_SLIDES = {
    T_CP_DEF: (4, 5),         # s3 (excluded) is where he defined it out loud
    T_CP_PATHO: (6, 11),
    T_CP_DXTX: (12, 16),
    T_PH_CLASS: (18, 20),
    T_PH_PRES: (21, 23),
    T_PH_DX: (24, 25),
    T_PH_TX: (26, 29),
    T_EDEMA_MECH: (32, 34),
    T_EDEMA_DX: (35, 38),     # plus s43 (the mimics table)
    T_EDEMA_TX: (39, 46),     # without s43, which belongs to T_EDEMA_DX
    T_PE_RISK: (48, 51),
    T_PE_DX: (52, 57),
    T_PE_TX: (58, 62),
}

EXCLUDED_SLIDES = {1, 2, 3, 17, 30, 31, 47}

SCOPE_BANNED = [
    # outside sources, the picture tool, trial names (s39 "DOSE trial", s41 "2024 FINEARTS-HF trial")
    r"Gemini|Notebook ?LM|StatPearls|UpToDate|Harrison|Merck|Lecturio|Papadakis|Tintinalli|Mayo|DOSE trial|FINEARTS",
    # decoration and unsupported claims: s3 admissions figure, s31 gauge, s49 trauma-fracture rate, s61 odds ratio,
    # s55 scanner trivia, s27 vaccine valencies
    r"hospital admissions|\b75 ?mm|\b56 ?%|odds ratio|\b3\.2\b|64-(?:section|slice)|(?:6th|sixth)[- ]generation"
    r"|\b(?:13|23)-valent",
    # s21 / s22 symptom and sign percentages (the 15% dizziness figure only beside dizziness: PERC's <15% stays)
    r"\b(?:86|27|17|21|23) ?%|(?<![\d.])4 ?%|(?:dizz|lightheaded)\w*[^.?]{0,40}\b15 ?%|\b15 ?%[^.?]{0,40}(?:dizz|lightheaded)",
    # s22 venous pressure reference error
    r"above the left atri|\b8 ?(?:cm|centimet)",
    # cut out loud: s28 cardiac index rule ("this is ICU stuff"); no pressure or resistance thresholds on any slide;
    # s19's AI mechanism word for Group 3
    r"cardiac index|\b2\.5 ?L|Wood units?|venoconstrict"
    r"|(?:pulmonary arter\w* pressure|mPAP)[^.?]{0,40}(?:>|greater than|above|over|exceed\w*|at least) ?(?:20|25)\b",
    # gold-standard conflict: s14 echo vs s24 catheterization vs s36 echo (never "gold standard" beside echo)
    r"echocardiogra\w*[^.?]{0,40}\bgold standard|\bgold standard[^.?]{0,25}echocardiogra",
    # wedge values that fall between the s23 (15) and s33 (18) cut-offs
    r"(?:wedge|occlusion) pressure\)?(?: \([^)]*\))?(?: of| is| was| measures| measured at| reads)? 1[5-8]\b",
    # off-slide content he spoke: sinus tachycardia as the most common EKG finding, the nitroglycerin interaction,
    # calcium channel blocker names, thoracentesis flash edema, anticoagulant and thrombolytic names, skin cancer
    r"most common (?:EKG|ECG|electrocardiogra\w*) (?:finding|abnormality|change)"
    r"|(?:sildenafil|tadalafil|phosphodiesterase)[^.?]{0,80}nitroglycerin|nitroglycerin[^.?]{0,80}(?:sildenafil|tadalafil|phosphodiesterase)"
    r"|amlodipine|verapamil|nifedipine|diltiazem|re-?expansion|thoracentesis"
    r"|apixaban|rivaroxaban|dabigatran|edoxaban|warfarin|heparin|enoxaparin|alteplase|tenecteplase|Eliquis"
    r"|\bMohs\b|basal cell|skin cancer",
    # score boundary values (Wells, PERC, s58): heart rate 100, saturation 94-95%, exactly 3 days, 4 weeks, 6 months,
    # systolic exactly 90, hypotension of exactly 15 minutes
    r"(?:heart rate|pulse)(?: \([^)]*\))?(?: is| was| of)? 100\b|(?:saturation|oximetry)(?: \([^)]*\))?(?: of| is| was| at)? 9[45] ?%"
    r"|(?:immobiliz\w*|bed ?rest|bedbound|bedridden|in bed)[^.?]{0,30}(?:for|after|of) (?:3|three) days"
    r"|(?:surgery|operation|procedure|replacement|repair|ectomy)[^.?]{0,40}(?:4|four) weeks ago"
    r"|(?:cancer|carcinoma|malignan|chemotherapy|radiation|lymphoma|leukemia|tumor)[^.?]{0,60}(?:6|six) months ago"
    r"|\b90/\d{2,3}\b|systolic[^.?]{0,30}\bof 90\b|(?:for|lasting) (?:15|fifteen) min",
]

# Named findings in vignette stems carry their description, taken from the slide that describes them.
NAMED = {
    "westermark": "oligemia",            # s51: focal peripheral oligemia (decreased vascularity)
    "hampton": "wedge",                  # s51: wedge-shaped, pleural-based opacity indicating infarction
    "palla": "descending",               # s51: enlarged right descending pulmonary artery
    "s1q3t3": "lead",                    # s51: deep S wave in lead I, Q wave and inverted T wave in lead III
    "kerley": "septa",                   # s37: horizontal peripheral lines, fluid in the interlobular septa
    "batwing": "perihilar",              # s37: central, perihilar distribution of alveolar edema
    "butterfly": "blurring",             # s46: butterfly pattern edema and vascular blurring
    "peribronchial cuffing": "bronchiol",  # s37: edema thickening the walls of the bronchioles
    "hepatojugular": "liver",            # s22: sustained moderate pressure on the liver raises the venous pressure
    "d-shaped": "sept",                  # s14 / s56: systolic septal flattening, the D-shaped septum
    "heave": "parasternal",              # s11 / s22: parasternal lift along the left sternal border
    "clot in transit": "right heart",    # s60: right heart "clot in transit"
    "blue bloater": "hypercapni",        # s6: global alveolar hypoxia and hypercapnia in COPD
}

# Minutes taught per pool topic (timeline minutes on screen less off-content stretches; see MINUTES above).
TOPIC_MINUTES = {
    T_CP_DEF: 3.75,
    T_CP_PATHO: 10.75,
    T_CP_DXTX: 7.75,
    T_PH_CLASS: 3.5,
    T_PH_PRES: 4.75,
    T_PH_DX: 3.1,
    T_PH_TX: 5.4,
    T_EDEMA_MECH: 4.75,
    T_EDEMA_DX: 5.15,
    T_EDEMA_TX: 5.8,
    T_PE_RISK: 7.5,
    T_PE_DX: 9.4,
    T_PE_TX: 6.0,
}

# (label, stem regex, key regex, minimum per form). The pool must hold at least twice the minimum of each.
REQUIRED_IO = [
    # "big two tools ... your wealth score and your perk" [1:22:33]; Lecture 44 [1:37:27] "that's fair game"
    ("Wells score", r"\bWells\b", r".", 1),
    ("PERC rule", r"Rule-out Criteria|\bPERC\b", r".", 1),
    # "If you walk away with nothing else from this lecture today" [1:17:58] (s50)
    ("Pulmonary embolism without dyspnea", r"dyspnea|shortness of breath",
     r"\b25\b|quarter|one in four|lack|without|absent|rely", 1),
    # "oh, it's a board question, is S1Q3T3" [1:19:00]; "great for board questions" [1:21:14] (s51)
    ("S1Q3T3 or a classic chest film sign", r"S1Q3T3|Westermark|Hampton|Palla|lead III", r".", 1),
    # "that's what you're gonna get on pants ... know the one in the middle" [1:32:48]-[1:33:53] (s58)
    ("Pulmonary embolism risk category",
     r"massive|embol[\s\S]{0,160}(?:intermediate[- ]risk|risk categor|stratif)"
     r"|(?:intermediate[- ]risk|risk categor|stratif)[\s\S]{0,160}embol",
     r"massive|submassive|intermediate|low[- ]risk|high[- ]risk|normotens|hypotens|right ventric|troponin", 1),
]
REQUIRED_VIG = [
    # score-from-the-vignette items, one row per full criteria set on the slides
    ("Wells score from the vignette (s53)", r"\bWells\b", r".", 1),
    ("PERC from the vignette (s54)", r"Rule-out Criteria|\bPERC\b", r".", 1),
    ("Pulmonary embolism risk category from the vignette (s58)",
     r"^(?=[\s\S]*embol)(?=[\s\S]*(?:massive|risk|stratif|classif|categor))",
     r"massive|submassive|intermediate|low[- ]risk|high[- ]risk", 1),
    ("Pulmonary hypertension prognostic risk from the vignette (s25)",
     r"walk(?:ing)? distance|six-minute walk|6-minute walk",
     r"\b(?:low|intermediate|high)\b", 1),
    ("Pulmonary hypertension group from the vignette (s19)", r"World Health Organization|\bgroup\b", r"\bgroup\b", 1),
    # contraindication / "what instead" items the slides state
    ("Thrombolysis contraindicated: thrombectomy or embolectomy instead (s60)",
     r"recent (?:\w+ )?surgery|recent operation|active(?:ly)? bleed|hemorrhag|clot in transit",
     r"thrombectomy|embolectomy", 1),
    ("Contrast contraindicated: ventilation-perfusion scan instead (s55, s57)",
     r"kidney|renal|creatinine|contrast", r"ventilation|perfusion scan|V/Q", 1),
]
