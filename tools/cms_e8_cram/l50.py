# -*- coding: utf-8 -*-
"""Lecture 50 (Hematologic Malignancies Part II, Gannon) cram topics, condensed from the slides.

CRITERIA: one table per criteria set, staging system, cut-off or classification on the slides (memory
cram_criteria_tables), each with a labeled memory aid. Cells are the slide wording; slide conflicts are note rows
(tools/cms_e8l50_scope.py: s47 picture ">= 60%" against s57 "10-60%", s57 "AND", s52 "by definition symptomatic"
against s47 SLiM, s50 "beta-2 macroglobulin" against s51 "beta2-microglobulin", s41 titled "Management of NHL" but
teaching Hodgkin, the s26 picture titled non-Hodgkin and reused for Hodgkin on s40). The Rai (s10) and R-ISS (s51)
tables are pictures on the slides, read from the 1920 px renders.

The gold card leads with what Ms. Gannon flagged out loud (recording 2026-11-18, part 3 onward), then the slides' own
visual emphasis (bold, underline). Spoken correction (flags file): the slides 30/34 "50% cured" for aggressive lymphoma and diffuse large B-cell lymphoma was corrected out loud to about 70%, so no cure percentage is keyed; it appears only in a note row with her correction.
Slide typos corrected: hairy cell (s9), Hodgkin (s21), pruritus (s22, s24, s38), arrhythmia (s28), dacarbazine
(s41), may require (s42), proteasome (s53), beta-2 microglobulin (s50).
"""
L50C = "#46491c"

CRITERIA = [
{"id": "crit-l50-rai", "label": "Rai Staging: Chronic Lymphocytic Leukemia", "color": L50C,
 "tag": "Staging &middot; Lecture 50 &middot; slide 10",
 "cols": ["Rai stage", "Findings"], "widths": ["18%", "82%"], "rows": [
  ("<b>0</b>", "Asymptomatic lymphocytosis"),
  ("<b>I</b>", "Lymphocytosis and <b>lymphadenopathy</b>"),
  ("<b>II</b>", "Lymphocytosis, lymphadenopathy, <b>organomegaly*</b>"),
  ("<b>III</b>", "Lymphocytosis and <b>anemia</b>, with or without lymphadenopathy and/or organomegaly"),
  ("<b>IV</b>", "Lymphocytosis and <b>thrombocytopenia</b>, with or without lymphadenopathy, organomegaly, and/or anemia"),
  {"note": "*Organomegaly = hepatomegaly and/or splenomegaly. Rai is historical, describes <b>prognostic groups</b>, needs <b>no advanced imaging</b> (physical exam and labs), and may set the indication for treatment (symptomatic disease or rapid progression). The contemporary tool is the CLL International Prognostic Index, named on the slide without its items."},
 ], "mnemonic": {"hook": "Count down the body from the blood: 0 Lymphs, I Lumps, II Liver or spleen, III Low red cells, IV Low platelets.",
  "key": [["0 Lymphs", "lymphocytosis only"], ["I Lumps", "+ lymphadenopathy"], ["II Liver or spleen", "+ organomegaly (hepatomegaly and/or splenomegaly)"],
          ["III Low red cells", "+ anemia (nodes and organs optional)"], ["IV Low platelets", "+ thrombocytopenia (anything else optional)"]],
  "breaks": "Stages III and IV do not need the nodes or organs: anemia alone makes III, thrombocytopenia alone makes IV."}},

{"id": "crit-l50-cll-mbl", "label": "Chronic Lymphocytic Leukemia vs Monoclonal B Lymphocytosis", "color": L50C,
 "tag": "Cut-off &middot; Lecture 50 &middot; slides 7&ndash;9",
 "cols": ["", "Chronic lymphocytic leukemia", "Monoclonal B lymphocytosis"], "widths": ["26%", "40%", "34%"], "rows": [
  ("Absolute lymphocyte count", "<b>&gt; 5K x 3 months</b>, or <b>&lt; 5K with lymphadenopathy or other symptoms</b>; labs: &ldquo;must be &gt;5K; often &gt;100K&rdquo;", "Elevated but <b>&lt;5K</b> lymphocytes"),
  ("Nodes, organs, cytopenias, symptoms", "May be present", "<b>Absent</b> (no lymphadenopathy, organomegaly, cytopenias, or other symptoms)"),
  ("Confirm with", "<b>Flow cytometry</b>: clonal B cells; <b>coexpression of CD19 and CD5</b>; bone marrow biopsy usually not needed", "&mdash;"),
  ("Course", "Rai 0&ndash;IV; Richter transformation risk", "<b>Progresses to chronic lymphocytic leukemia at 1&ndash;2% per year</b>"),
  {"note": "Neither slide says where exactly 5,000 falls; slide 7&rsquo;s &ldquo;must be &gt;5K&rdquo; sits against slide 8&rsquo;s &ldquo;&lt; 5K with lymphadenopathy&rdquo;. Other differentials (slide 9): atypical lymphocytosis with infections (pertussis); Waldenstr&ouml;m macroglobulinemia, hairy cell leukemia, lymphomas in leukemic phase (told apart by morphology and immunophenotype)."},
 ], "mnemonic": {"hook": "Five thousand for three months, or Under five with a Finding (nodes or symptoms); no Finding under five is just MBL, which turns 1&ndash;2 a year.",
  "key": [["Five thousand x three months", "ALC &gt;5K for 3 months = chronic lymphocytic leukemia"], ["Under five with a Finding", "ALC &lt;5K with lymphadenopathy or other symptoms = chronic lymphocytic leukemia"],
          ["No Finding under five", "monoclonal B lymphocytosis"], ["1&ndash;2 a year", "progression to chronic lymphocytic leukemia 1&ndash;2% per year"]],
  "breaks": "Flow cytometry, CD19 and CD5 coexpression and the 100K figure are not in the hook."}},

{"id": "crit-l50-lugano", "label": "Lymphoma Staging: Lugano (Modified Ann Arbor)", "color": L50C,
 "tag": "Staging &middot; Lecture 50 &middot; slides 26, 40 (picture)",
 "cols": ["Stage", "Picture caption"], "widths": ["16%", "84%"], "rows": [
  ("<b>1</b>", "Localized disease; <b>single lymph node region or single organ</b>"),
  ("<b>2</b>", "Two or more lymph node regions on the <b>same side of the diaphragm</b>"),
  ("<b>3</b>", "Two or more lymph node regions <b>above and below the diaphragm</b>"),
  ("<b>4</b>", "<b>Widespread disease; multiple organs</b>, with or without lymph node involvement"),
  {"note": "The picture is titled &ldquo;Stages of Non-Hodgkin&rsquo;s Lymphoma&rdquo; and is reused for Hodgkin lymphoma on slide 40: the same four stages apply to both. Staging needs imaging (usually CT or PET, slide 25). The Hodgkin treatment slide (41) adds &ldquo;IIA&rdquo;, &ldquo;B symptoms&rdquo; and &ldquo;bulky&rdquo;."},
 ], "mnemonic": {"hook": "The diaphragm is the equator: One spot; Two on one side; Three on both sides; Four in the organs.",
  "key": [["One spot", "single node region or single organ"], ["One side", "2+ regions, same side of the diaphragm"],
          ["Both sides", "2+ regions above and below the diaphragm"], ["Organs", "widespread, multiple organs, with or without nodes"]],
  "breaks": "Nothing on the picture is left out; the IIA, B-symptom and bulky labels come from the Hodgkin treatment slide."}},

{"id": "crit-l50-nhl-tx", "label": "Non-Hodgkin Lymphoma: Treatment by Type", "color": L50C,
 "tag": "Treatment step &middot; Lecture 50 &middot; slide 27",
 "cols": ["Presentation", "Treatment"], "widths": ["34%", "66%"], "rows": [
  ("<b>Single node, non-aggressive</b>", "<b>Radiation</b>"),
  ("<b>Low-grade B-cell lymphomas</b>", "<b>Rituximab</b> (anti-CD20 monoclonal antibody) if treatment required, &plusmn; chemotherapy if extensive"),
  ("<b>Aggressive B-cell lymphomas</b>", "Multi-drug chemotherapy, e.g. <b>R-CHOP</b>: rituximab, cyclophosphamide, vincristine, doxorubicin, prednisone; some get more aggressive regimens"),
  ("<b>T-cell lymphomas</b>", "Similar regimens (<b>CHOP</b>) <b>minus rituximab</b>: <b>no CD20 on T cells</b>"),
  {"note": "&ldquo;Highly dependent on subtype and presentation.&rdquo; Follicular lymphoma: frequently watch and wait, intermittent low-intensity therapy if symptomatic (slide 16)."},
 ], "mnemonic": {"hook": "R-CHOP is Really Cooking Very Dangerous Pasta; T cells skip the R.",
  "key": [["Really", "rituximab"], ["Cooking", "cyclophosphamide"], ["Very", "vincristine"], ["Dangerous", "doxorubicin"], ["Pasta", "prednisone"],
          ["T cells skip the R", "T-cell lymphomas: CHOP without rituximab (no CD20)"]],
  "breaks": "The hook follows the slide&rsquo;s list order, not the letters of CHOP (in CHOP, H is doxorubicin and O is vincristine). Radiation for a single non-aggressive node and rituximab alone for low-grade B-cell lymphoma are not in the hook."}},

{"id": "crit-l50-nhl-prognosis", "label": "Non-Hodgkin Lymphoma: Poor-Prognosis Factors", "color": L50C,
 "tag": "Prognostic factors &middot; Lecture 50 &middot; slide 30",
 "cols": ["Factor", "Slide wording"], "widths": ["30%", "70%"], "rows": [
  ("Age", "<b>Age &gt; 60</b>"),
  ("Spread", "<b>Extranodal sites</b>"),
  ("Performance status", "<b>Poor (&gt;2) performance status, ECOG</b> (Eastern Cooperative Oncology Group)"),
  ("Stage", "<b>Stage III or IV</b>"),
  ("Lab", "<b>Elevated LDH</b> (lactate dehydrogenase)"),
  {"note": "Same slide: indolent lymphomas incurable but survival often 10&ndash;15+ years (risk of progression to aggressive lymphoma); aggressive lymphomas often treatable and curable with chemotherapy (the slide&rsquo;s &ldquo;50% cured&rdquo; was corrected out loud: &ldquo;more closely to 70%&rdquo;), 5-year survival 60&ndash;70%; T-cell lymphomas respond less well than B-cell."},
 ], "mnemonic": {"hook": "A-E-P-S-L: an Aged patient, Extranodal, Poorly performing, Stage III-IV, with a high LDH.",
  "key": [["Aged", "age &gt; 60"], ["Extranodal", "extranodal sites"], ["Poorly performing", "ECOG &gt; 2"], ["Stage", "III or IV"], ["LDH", "elevated"]],
  "breaks": "The survival figures in the note row are not in the hook."}},

{"id": "crit-l50-genes", "label": "Lymphoid Cancers: Genes, Translocations and Infections", "color": L50C,
 "tag": "Classification &middot; Lecture 50 &middot; slides 5, 8, 16&ndash;18, 20&ndash;21, 31&ndash;32, 37, 39",
 "cols": ["Marker", "Disease", "Slide wording"], "widths": ["28%", "30%", "42%"], "rows": [
  ("<b>t(14;18)</b>, BCL-2", "<b>Follicular</b> lymphoma", "BCL-2 placed on chromosome 14, preventing cell death (slide 16)"),
  ("<b>Cyclin D1, t(11;14)</b>", "<b>Mantle cell</b> lymphoma", "Identifies the subtype (slide 20)"),
  ("<b>MYC</b> upregulation", "<b>Burkitt</b> lymphoma", "Stimulated cell growth and division (slide 31)"),
  ("<b>MYD88</b> mutation (~90%)", "<b>Lymphoplasmacytic</b> (Waldenstr&ouml;m)", "Excess IgM &rarr; hyperviscosity (slide 18)"),
  ("Del 13q, del 11q, trisomy 12, del 17p", "Chronic lymphocytic leukemia", "80% of cases (slide 5)"),
  ("<b>CD19 + CD5</b>", "Chronic lymphocytic leukemia", "Coexpressed on the lymphocytes (slide 8)"),
  ("<b>CD15 + CD30</b>", "<b>Classical Hodgkin</b> lymphoma", "Expressed (slide 39)"),
  ("<i>H. pylori</i>", "Gastric MALT lymphoma", "2/3 of cases (slide 17)"),
  ("Hepatitis C", "Splenic marginal zone", "Associated (slide 17)"),
  ("HTLV-1", "Adult T-cell leukemia/lymphoma", "Very aggressive; Caribbean, Central and South America (slide 21)"),
  ("Epstein-Barr virus", "Endemic Burkitt; Hodgkin", "Endemic Burkitt strongly associated (slide 32); Hodgkin 40&ndash;50% (slide 37)"),
  ("HIV/AIDS", "Immunodeficiency-associated Burkitt", "Associated (slide 32)"),
 ], "mnemonic": {"hook": "Follicles at Fourteen-Eighteen keep cells alive (BCL-2); the Mantle is Eleven-Fourteen with a Crown (cyclin D1); Burkitt's MYC Makes You Climb fast; Waldenstr&ouml;m's MYD88 makes IgM Mud (hyperviscosity).",
  "key": [["Fourteen-Eighteen", "follicular, t(14;18), BCL-2 blocks cell death"], ["Eleven-Fourteen + Crown", "mantle cell, t(11;14), cyclin D1"],
          ["Makes You Climb", "Burkitt, MYC upregulation"], ["Mud", "lymphoplasmacytic, MYD88, IgM hyperviscosity"]],
  "breaks": "The CD markers, the chronic lymphocytic leukemia deletions and the infection rows are not in the hook."}},

{"id": "crit-l50-hl-tx", "label": "Hodgkin Lymphoma: Treatment by Stage", "color": L50C,
 "tag": "Treatment step &middot; Lecture 50 &middot; slide 41",
 "cols": ["Stage", "Treatment"], "widths": ["42%", "58%"], "rows": [
  ("<b>Early stage I and IIA</b>", "<b>Short course of chemotherapy</b> (ABVD historically)"),
  ("<b>Bulky stage I or II disease, or B symptoms</b>", "<b>Chemotherapy + radiation</b>"),
  ("<b>Stage III or IV</b>", "<b>Chemotherapy</b>"),
  ("ABVD", "<b>Adriamycin (doxorubicin), bleomycin, vinblastine, dacarbazine</b>; new agents are replacing <b>bleomycin</b> because of <b>pulmonary toxicities</b>"),
  {"note": "Slide 41 is titled &ldquo;Management of NHL&rdquo; but sits in the Hodgkin section and teaches Hodgkin treatment. Relapse after first line: allogeneic stem cell transplant (slide 42)."},
 ], "mnemonic": {"hook": "Small and quiet: short chemo. Big or Burning (bulky or B symptoms): chemo plus Beams. Spread (III-IV): chemo. ABVD: A Big Vine Drops; Bleomycin hurts the lungs.",
  "key": [["Small and quiet", "I and IIA: short chemotherapy"], ["Big or Burning", "bulky I-II or B symptoms: chemotherapy + radiation"],
          ["Spread", "III or IV: chemotherapy"], ["A Big Vine Drops", "doxorubicin (Adriamycin), bleomycin, vinblastine, dacarbazine"]],
  "breaks": "The transplant-at-relapse line (slide 42) is not in the hook."}},

{"id": "crit-l50-tls", "label": "Tumor Lysis Syndrome", "color": L50C,
 "tag": "Emergency &middot; Lecture 50 &middot; slides 28, 33&ndash;34",
 "cols": ["", "Slide wording"], "widths": ["24%", "76%"], "rows": [
  ("What", "<b>Medical emergency</b>: rapid tumor breakdown releases <b>potassium, phosphorus, uric acid</b>"),
  ("Kidney", "Acute renal failure from <b>uric acid and calcium phosphate crystals</b> in the renal tubules"),
  ("Biggest risk", "<b>Hyperkalemia &rarr; arrhythmia</b> and potential death"),
  ("Who", "Spontaneously in highly aggressive lymphoma (<b>Burkitt</b>); also acute lymphoblastic and acute myeloid leukemia with marked leukocytosis"),
  ("Treat", "<b>Aggressive IV fluid hydration</b>"),
  ("Prevent", "Anticipate in aggressive lymphoma: <b>allopurinol</b> (hypouricemic agent) and <b>fluids in advance</b>; &ldquo;drink plenty of fluids and take allopurinol!&rdquo; (slide 34)"),
 ], "mnemonic": {"hook": "Tumor lysis spills a PUP: Potassium, Uric acid, Phosphorus. Potassium Stops the heart, the crystals Stop the kidney; Flush and Fix with fluids and allopurinol.",
  "key": [["PUP", "potassium, uric acid, phosphorus released"], ["Stops the heart", "hyperkalemia &rarr; arrhythmia (largest risk)"],
          ["Stops the kidney", "uric acid and calcium phosphate crystals &rarr; acute renal failure"], ["Flush and Fix", "aggressive IV fluids; allopurinol ahead of time"]],
  "breaks": "Who gets it (Burkitt spontaneously; acute leukemias with marked leukocytosis) is not in the hook."}},

{"id": "crit-l50-crab-slim", "label": "Multiple Myeloma: CRAB and SLiM", "color": L50C,
 "tag": "Criteria &middot; Lecture 50 &middot; slides 47, 48, 50, 52 &#9733;",
 "cols": ["Letter", "Finding", "Slide wording"], "widths": ["12%", "30%", "58%"], "rows": [
  ("<b>C</b>", "Calcium (<b>hypercalcemia</b>)", "Constipation, increased thirst, urinary frequency, nausea"),
  ("<b>R</b>", "<b>Renal insufficiency</b>", "Swelling"),
  ("<b>A</b>", "<b>Anemia</b>", "Fatigue, shortness of breath"),
  ("<b>B</b>", "<b>Bone lesions/pain</b>", "Often back, chest, or pelvis; osteolytic &ldquo;punched out&rdquo; lesions (slide 48)"),
  ("<b>S</b>", "Bone marrow plasma cells", "Picture: &ldquo;Bone marrow &ge; Sixty (60%) plasmacytosis&rdquo;"),
  ("<b>Li</b>", "Abnormal light chain ratio", "Picture: &ldquo;Light chains &gt;100:1&rdquo;"),
  ("<b>M</b>", "MRI lesion", "Picture: &ldquo;MRI: &ge;2 lesions&rdquo;"),
  {"note": "Diagnosis (slide 50): <b>&ge; 10% bone marrow plasma cells or biopsy-proven plasmacytoma + 1 or more CRAB feature</b>. SLiM = &ldquo;may be asymptomatic with certain lab findings&rdquo; (slide 47), while slide 52 says myeloma is &ldquo;by definition a symptomatic condition&rdquo;. The picture also lists amyloidosis, hyperviscosity, polyneuropathies; higher risk of infections."},
 ], "mnemonic": {"hook": "The CRAB is SLiM: CRAB pinches the body (Calcium, Renal, Anemia, Bone); SLiM shows on the labs (Sixty percent, Light chains 100 to 1, MRI 2 lesions).",
  "key": [["C", "hypercalcemia"], ["R", "renal insufficiency"], ["A", "anemia"], ["B", "bone lesions"],
          ["Sixty", "&ge;60% marrow plasma cells"], ["Light 100", "light chain ratio &gt;100:1"], ["MRI 2", "&ge;2 MRI lesions"]],
  "breaks": "The symptoms under each CRAB letter and the &ldquo;also&rdquo; list (amyloidosis, hyperviscosity, polyneuropathies) are not in the hook."}},

{"id": "crit-l50-plasma-spectrum", "label": "MGUS vs Smoldering Myeloma vs Multiple Myeloma", "color": L50C,
 "tag": "Cut-offs &middot; Lecture 50 &middot; slides 44, 50, 53, 56, 57 &#9733;",
 "cols": ["", "MGUS", "Smoldering myeloma", "Multiple myeloma"], "widths": ["19%", "25%", "28%", "28%"], "rows": [
  ("M-protein", "<b>&lt; 3 g/dL</b>", "<b>&gt; 3 g/dL</b> AND", "Monoclonal protein on serum protein electrophoresis (characteristic)"),
  ("Bone marrow plasma cells", "Clonal <b>&lt; 10%</b>", "<b>10&ndash;60%</b>", "<b>&ge; 10%</b> or biopsy-proven plasmacytoma"),
  ("Myeloma-defining events", "<b>None</b>; asymptomatic by definition", "<b>None</b> (anemia, bone lesions, renal failure, etc.)", "<b>+ 1 or more CRAB feature</b>"),
  ("Progression", "<b>~1% per year</b>", "<b>~10% per year</b>; some high-risk groups &gt;50% within 2 years", "Relapsing; incurable"),
  ("Treatment", "&mdash;", "Typically none; early intervention for some subgroups", "3- or 4-drug regimen; autologous transplant if a candidate"),
  {"note": "Neither slide says where exactly 3 g/dL or 10% falls. Smoldering &ldquo;10&ndash;60%&rdquo; (slide 57) meets the SLiM picture&rsquo;s &ldquo;&ge; 60%&rdquo; (slide 47) at 60%. Slide 57&rsquo;s &ldquo;AND&rdquo; is the slide&rsquo;s (current International Myeloma Working Group wording: &ge;3 g/dL <i>or</i> 10&ndash;60%). MGUS is printed &ldquo;of unknown significance&rdquo; on slide 56 (&ldquo;undetermined&rdquo; on the slide 44 picture)."},
 ], "mnemonic": {"hook": "Three and Ten are the gates, and the speed goes up by ten: under 3 and under 10 = MGUS, creeping 1% a year; over 3 and 10&ndash;60 = smoldering, 10% a year; 10 or more plus a CRAB = myeloma.",
  "key": [["Under 3, under 10", "MGUS: M-protein &lt;3 g/dL, plasma cells &lt;10%"], ["1% a year", "MGUS progression"],
          ["Over 3, 10&ndash;60", "smoldering: M-protein &gt;3 g/dL and 10&ndash;60% plasma cells"], ["10% a year", "smoldering progression"],
          ["10 + CRAB", "myeloma: &ge;10% plasma cells (or plasmacytoma) + 1 CRAB feature"]],
  "breaks": "The high-risk smoldering group (&gt;50% within 2 years) and the treatment row are not in the hook."}},

{"id": "crit-l50-riss", "label": "R-ISS Staging: Multiple Myeloma", "color": L50C,
 "tag": "Staging &middot; Lecture 50 &middot; slide 51 (table picture)",
 "cols": ["Stage", "Criteria", "Survival (mo)"], "widths": ["12%", "70%", "18%"], "rows": [
  ("<b>I</b>", "&beta;2-microglobulin <b>&lt;3.5 mg/L</b>; albumin <b>&ge;3.5 g/dL</b> <i>and</i> standard-risk chromosomal abnormalities <i>and</i> normal LDH (defined as less than ULN)", "82"),
  ("<b>II</b>", "<b>Not R-ISS stage I or III</b>", "62"),
  ("<b>III</b>", "&beta;2-microglobulin <b>&ge;5.5 mg/L</b> regardless of albumin levels <i>and</i> high-risk chromosomal abnormalities: <b>del 17p, t(4;14) or t(14;16)</b> <i>and</i> high LDH (defined as higher than ULN)", "40"),
  {"note": "R-ISS = Revised International Staging System; LDH = lactate dehydrogenase; ULN = upper limit of normal. Prognostic only: &ldquo;does not impact treatment decisions broadly&rdquo;. Slide 50 prints the test as &ldquo;beta-2 macroglobulin&rdquo;; it is beta-2 microglobulin. (Current guideline note: published stage III is &beta;2-microglobulin &ge;5.5 with high-risk abnormalities <i>or</i> high LDH; the slide prints &ldquo;and&rdquo;.)"},
 ], "mnemonic": {"hook": "3.5 and 3.5 is stage one; 5.5 with bad chromosomes and high LDH is stage three; everything in between is two.",
  "key": [["3.5 and 3.5", "stage I: &beta;2-microglobulin &lt;3.5 mg/L, albumin &ge;3.5 g/dL, standard risk, normal LDH"],
          ["5.5 + bad chromosomes", "stage III: &beta;2-microglobulin &ge;5.5, del 17p, t(4;14) or t(14;16), high LDH"], ["In between", "stage II: not I or III"]],
  "breaks": "The survival months (82, 62, 40) are not in the hook."}},
]

TOPICS = [
{"id": "l50-emph", "label": "★ Emphasized — Hematologic Malignancies Part II", "color": "#b8860b", "rows": [
  ["★ Said: CRAB", "&ldquo;You absolutely need to know this ... it will <b>100% be on a test</b>&rdquo;: <b>hypercalcemia, renal insufficiency, anemia, bone lesions</b> (slide 47)."],
  ["★ Said: 10% plasma cells", "Myeloma needs only <b>&ge;10% marrow plasma cells</b> (+ 1 CRAB), unlike the 20% blasts of acute leukemia: &ldquo;remember that for your test&rdquo; (slide 50). Remember <b>Bence Jones protein</b>."],
  ["★ Said: Burkitt", "&ldquo;Starry sky, you think Burkitt&rsquo;s ... you&rsquo;ll definitely see that on a test&rdquo;; endemic = <b>sub-Saharan Africa</b>, &ldquo;strongly, strongly, strongly associated with <b>EBV</b>&rdquo; (slide 32)."],
  ["★ Said: Hodgkin", "<b>Reed-Sternberg cells</b> = &ldquo;automatically think of Hodgkin&rsquo;s&rdquo; (slide 36); <b>ABVD</b> = Hodgkin (slide 41); node <b>pain after alcohol</b> (slide 38)."],
  ["★ Said: tumor lysis", "&ldquo;A medical emergency ... you need to recognize it for your testing&rdquo;: <b>high potassium, phosphorus, uric acid</b> (she added low calcium); fluids + allopurinol (slide 28)."],
  ["★ Said: CLL", "<b>High white count + painless nodes</b> = think CLL; <b>flow cytometry</b> is the key test, <b>CD19 + CD5</b> pathognomonic, so no marrow biopsy (slides 7&ndash;8); <b>Richter transformation</b> (slide 12); &ldquo;an isolated white count alone does not equal treatment&rdquo;."],
  ["★ Said: lymphoma", "Infections to know: <b>HIV, EBV, HTLV-1, <i>H. pylori</i></b> (slide 23); <b>excisional biopsy</b>, never trust a negative fine needle aspiration; <b>LDH</b> on every lymphoma (slide 25); stage by the <b>diaphragm</b> (slide 26); <b>T cells worse than B cells</b> (slide 30)."],
  ["Played down", "CD numbers beyond CD19/CD5; follicular t(14;18)/BCL-2; nodal and splenic marginal zone; mantle cell; Lyme and HHV-8; myeloma staging. Still on the slides."],
  ["★ Chronic lymphocytic leukemia", "<b>Mature B cells</b> (slide 4); <b>frequently diagnosed while asymptomatic</b>, <b>painless lymphadenopathy</b>, <b>lymphocytosis &gt;5K</b> (slide 7); <b>confirmed by <u>flow cytometry</u></b>, no marrow biopsy usually (slide 8); <b>watch and wait</b> (slide 11); <b>Richter transformation</b> (slide 12)."],
  ["★ Non-Hodgkin", "<b>85% B-cell</b>, aggressive to indolent (slide 15); <b>excisional biopsy</b> and <b>CT or PET</b> (slide 25); <b>tumor lysis syndrome: emergency, aggressive IV fluids</b> (slide 28); <b>poor-prognosis factors</b> (slide 30)."],
  ["★ Burkitt", "<b>&ldquo;Starry sky&rdquo;</b> (slide 32); <b>prompt treatment, emergent referral</b>; <u>excellent prognosis if found early</u>; <b>tumor lysis</b> (slide 33)."],
  ["★ Hodgkin", "<b>Reed-Sternberg cells</b> (slide 36); <b>bimodal</b>, <b>Epstein-Barr virus 40&ndash;50%</b> (slide 37); <b>painless cervical nodes (70%)</b>, <b>pain with alcohol</b> (slide 38); treatment by stage (slide 41); <b>&gt;90% alive at 5 years</b> (slide 42)."],
  ["★ Myeloma", "<b>CRAB</b> (slide 47); <b>&ge;10% plasma cells or plasmacytoma + 1 CRAB</b> (slide 50); goal = <b>prolonged remissions</b> (slide 52); <b>3- or 4-drug regimen</b>, <b>most relapse</b> (slide 53); <b>shorter remissions each line, incurable</b> (slide 54); smoldering <b>10% per year</b> (slide 57)."],
]},
{"id": "l50-cll", "label": "Chronic Lymphocytic Leukemia", "color": "#2f5d6b", "rows": [
  ["What", "Proliferative leukemia of <b>mature B-cell lymphocytes</b> in blood, marrow, nodes, spleen (same disease as small lymphocytic lymphoma); 1% of United States cancers. Mature T-cell form: T-cell prolymphocytic leukemia."],
  ["Genes", "80%: <b>del 13q, del 11q, trisomy 12, del 17p</b>."],
  ["Who", "<b>Median age 70</b>; <b>2&times; males</b>; Eastern European and Jewish descent; <b>no known occupational or environmental risk factors</b>."],
  ["Picture", "Often <b>asymptomatic, routine labs</b>; <b>painless</b> firm mobile nodes (50&ndash;90%); B symptoms 5&ndash;10%; fatigue, bruising, infections; <b>splenomegaly ~40%</b>."],
  ["Diagnosis", "<b>Flow cytometry</b>; ALC &gt;5K x 3 months (or &lt;5K with nodes/symptoms); <b>CD19 + CD5</b>; cytogenetics for prognosis; marrow biopsy usually not needed; <b>Rai</b> stage."],
  ["Treat", "<b>Watch and wait</b> until lymphocyte doubling &lt;6 months or symptoms. <b>BTK inhibitors</b> (Bruton tyrosine kinase: ibrutinib, acalabrutinib, zanubrutinib; continuous); <b>venetoclax</b> (BCL-2) + antibody (fixed duration); <b>rituximab, obinutuzumab, ofatumumab</b>."],
  ["Outlook", "5-year relative survival ~88%; <b>Richter transformation</b> to aggressive B-cell lymphoma; many <b>die with it, not from it</b>; hematology/oncology, outpatient, pill (indefinite) or infusion + pill (time-limited)."],
]},
{"id": "l50-nhl", "label": "Non-Hodgkin Lymphoma: Types", "color": "#5a3a5e", "rows": [
  ["Group", "Lymphoid malignancy of B (85%), T or NK cells; 4% of United States cancers; very aggressive (Burkitt, diffuse large B-cell, T-cell leukemia/lymphoma) to indolent (follicular, marginal zone, chronic lymphocytic leukemia)."],
  ["Follicular", "<b>Most common indolent</b>; <b>waxing and waning painless nodes</b>; <b>t(14;18) BCL-2</b>; packed follicles; often watch and wait; incurable."],
  ["Marginal zone", "5&ndash;17%; <b>MALT most common</b> (gut, eyes, lungs); <b>gastric MALT 2/3 <i>H. pylori</i></b>; splenic = <b>hepatitis C</b>; older adults."],
  ["Lymphoplasmacytic", "= <b>Waldenstr&ouml;m macroglobulinemia</b>; <b>MYD88</b> ~90%; <b>IgM &rarr; hyperviscosity</b> (blurred vision, headache, rarely stroke); 5-year 78%; familial, farming, pesticides."],
  ["Diffuse large B-cell", "<b>Most common non-Hodgkin lymphoma in adults</b>; fast-growing mass and/or B symptoms; often curable (slide 34&rsquo;s cure figure corrected out loud upward)."],
  ["Mantle cell", "Rare (5%); <b>cyclin D1 t(11;14)</b>; aggressive; men 60&ndash;70; survival &lt;2 to &gt;9 years."],
  ["T-cell", "Peripheral T-cell, not otherwise specified = most common (1/3); <b>adult T-cell leukemia/lymphoma: HTLV-1</b>, Caribbean, Central and South America; <b>NK/T-cell: nasal</b>."],
  ["Mycosis fungoides", "Skin lesions <b>like a fungal infection</b> &rarr; nodules that may ulcerate; <b>S&eacute;zary syndrome = erythroderma</b> with severe itch; treat the skin."],
]},
{"id": "l50-nhl-care", "label": "Non-Hodgkin Lymphoma: Work-up &amp; Care", "color": "#5a3a5e", "rows": [
  ["Risk", "White, developed countries, <b>male</b>; immunosuppression, transplant; lupus, Sj&ouml;gren, celiac, Crohn&rsquo;s; DDT (farming); <i>H. pylori</i>, HTLV-1, hepatitis C, HIV, Epstein-Barr virus, Lyme, HHV-8; family history."],
  ["Picture", "<b>Peripheral nodes &gt;2/3</b>; <b>B symptoms</b>; pruritus, rash; <b>extranodal in about half</b> (CNS lymphoma: headache, neuro deficits); mediastinal B-cell: mass, cough, abnormal chest X-ray."],
  ["Diagnosis", "<b>Excisional lymph node biopsy</b> (2 cm, persistent, growing); <b>not fine needle aspiration</b> (architecture); <b>CT or PET</b>; CBC, chemistries (tumor lysis), LDH; marrow biopsy; <b>lumbar puncture for high-grade incl. Burkitt</b>."],
  ["Chemo harms", "Infections, bleeding, anemia, electrolyte abnormalities, diarrhea (all agents)."],
  ["Teach", "Hematologist, ideally a lymphoma expert; outpatient unless aggressive with electrolyte problems; <b>Burkitt: rapid transfer</b>; <b>fluids + allopurinol</b>."],
]},
{"id": "l50-burkitt", "label": "Burkitt Lymphoma", "color": "#7a3b2e", "rows": [
  ["What", "<b>Very aggressive</b>; <b>MYC</b> upregulation; very rapidly growing, often painless swelling (visible change within a day); B symptoms."],
  ["Three types", "<b>Endemic</b>: sub-Saharan Africa, New Guinea, <b>Epstein-Barr virus</b>. <b>Sporadic</b>: United States, Western Europe, males, <b>almost always &lt;35</b>. <b>Immunodeficiency</b>: HIV/AIDS."],
  ["Pathology", "<b>&ldquo;Starry sky&rdquo;</b>: sheets of lymphoma with benign macrophages clearing dying cells."],
  ["Act", "<b>Prompt treatment, emergent hematology referral</b>; doubling within 24 hours; multi-agent chemotherapy; watch for <b>tumor lysis</b>; lumbar puncture in work-up."],
  ["Outlook", "Excellent if early: <b>&gt;90% children</b>, 50&ndash;90% adults."],
]},
{"id": "l50-hodgkin", "label": "Hodgkin Lymphoma", "color": "#2f5d6b", "rows": [
  ["What", "B-cell lymphoma: few <b>Reed-Sternberg cells</b> (binucleated, neoplastic B cells) among many immune cells; <b>contiguous, orderly spread</b>; 10&ndash;15% of lymphomas."],
  ["Who", "<b>Bimodal: 20s and &gt;60</b>; same-sex sibling <b>10&times;</b>; <b>Epstein-Barr virus 40&ndash;50%</b>; HIV, HHV-6, tuberculosis."],
  ["Picture", "<b>Painless asymptomatic nodes (70%), usually cervical</b> (supraclavicular, mediastinal); <b>pain with alcohol</b>; mediastinal mass on chest X-ray; splenomegaly ~30%; intense pruritus."],
  ["Diagnosis", "<b>Excisional biopsy</b>, not fine needle aspiration; <b>CD15 and CD30</b>; chest X-ray; CBC, chemistries, LDH; marrow biopsy; Lugano stage."],
  ["Outlook", "<b>&gt;90% alive at 5 years</b>; relapse &rarr; allogeneic stem cell transplant; worse: older, bulky, lymphocyte-depleted or mixed cellularity; late myelodysplastic syndrome, secondary leukemia, other cancers."],
]},
{"id": "l50-myeloma", "label": "Multiple Myeloma", "color": "#5e4123", "rows": [
  ["What", "Plasma cell (terminally differentiated B cell) clone making <b>one antibody, most commonly IgG</b>; <b>10% of hematologic malignancies</b>; spectrum MGUS &rarr; smoldering &rarr; myeloma."],
  ["Mechanism", "<b>Osteoclast activation &rarr; calcium release</b>; kidney injury from <b>light chain and calcium phosphate deposition</b>; anemia from kidney and marrow."],
  ["Who", "<b>Most over 65</b>; <b>African Americans</b> higher risk; family history; <b>prior MGUS or smoldering myeloma</b>; radiation, chemical, occupational."],
  ["Picture", "<b>CRAB</b>; infections; skull <b>&ldquo;punched out&rdquo; lytic lesions</b>."],
  ["Differential", "Smoldering myeloma, MGUS; Waldenstr&ouml;m (<b>IgM</b>); chronic lymphocytic leukemia, non-Hodgkin lymphoma, amyloidosis; reactive hypergammaglobulinemia (cirrhosis, inflammation)."],
  ["Work-up", "<b>M-protein on serum protein electrophoresis</b>; urine <b>Bence Jones protein</b>; CBC, metabolic panel; 24-hour urine protein electrophoresis; <b>marrow biopsy with flow</b>; <b>kappa/lambda ratio</b>; beta-2 microglobulin; <b>whole-body CT</b>."],
  ["Treat", "Goal: <b>prolonged remissions</b>, survival, quality of life. <b>Proteasome inhibitor + immunomodulatory drug + steroid</b> (3&ndash;4 drugs); <b>autologous transplant</b> + maintenance if a candidate; continuous therapy at relapse; CAR-T, bispecifics for relapse."],
  ["Outlook", "5-year relative survival ~60%; shorter remission each line; <b>incurable</b>; may exceed 10 years today; lifelong follow-up with a myeloma expert."],
]},
]
