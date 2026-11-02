# -*- coding: utf-8 -*-
"""Lecture 41 (Inflammatory Lung Diseases, Gray) cram topics, condensed from guide section 3.

CRITERIA: one table per criteria set, classification, staging or cut-off on the slides (memory
cram_criteria_tables), each with a labeled memory aid. Cells are the slide wording; slide conflicts are note rows.
Slides 72-74 (acute respiratory distress syndrome) are pictures; their tables are read from the images.
"""
L41C = "#5e4123"

CRITERIA = [
{"id": "crit-l41-onset", "label": "Interstitial Lung Disease: Onset Patterns", "color": L41C,
 "tag": "Classification &middot; Lecture 41 &middot; slide 22",
 "cols": ["Onset", "Time course", "Typical of"], "widths": ["20%", "26%", "54%"], "rows": [
  ("<b>Acute</b>", "Days to weeks", "<b>Allergy</b>"),
  ("<b>Subacute</b>", "Weeks to months", "Any, but most common with <b>sarcoidosis</b> and <b>drug-induced</b> disease"),
  ("<b>Chronic</b>", "Months to years", "<b>Most</b> interstitial lung diseases: idiopathic pulmonary fibrosis, sarcoidosis, pneumoconiosis, connective tissue disease"),
  ("<b>Episodic</b>", "Less common", "<b>Hypersensitivity pneumonitis</b>"),
 ], "mnemonic": {"hook": "All Sorts Come Eventually: Allergy fast, Sarcoid and drugs Sub, Chronic for most, hypersensitivity comes and goes (Episodic).",
  "key": [["A", "Acute (days to weeks): allergy"], ["S", "Subacute (weeks to months): sarcoidosis, drug-induced"],
          ["C", "Chronic (months to years): most, including idiopathic pulmonary fibrosis, sarcoidosis, pneumoconiosis, connective tissue disease"],
          ["E", "Episodic: hypersensitivity pneumonitis"]],
  "breaks": "Sarcoidosis sits in both the subacute and the chronic rows on the slide."}},

{"id": "crit-l41-imaging-pft", "label": "Reading the Film and the Pulmonary Function Tests", "color": L41C,
 "tag": "Classification &middot; Lecture 41 &middot; slides 26, 29",
 "cols": ["Finding", "Meaning"], "widths": ["42%", "58%"], "rows": [
  {"group": "RETICULAR (curvilinear) OPACITIES"},
  ("<b>Fine</b> (ground glass)", "<b>Early</b> finding"),
  ("<b>Medium</b> (honeycombing)", "<b>Late</b> finding"),
  ("<b>Coarse</b>", "<b>Cystic spaces</b>"),
  {"group": "OTHER PATTERNS"},
  ("Nodular", "Nodules"),
  ("Reticulonodular", "Reticular shadows overlapping, or with nodules (sarcoid)"),
  ("Hilar and mediastinal lymphadenopathy", "<b>Sarcoidosis, silicosis</b>"),
  {"group": "RESTRICTIVE PATTERN"},
  ("Forced expiratory volume in 1 second &divide; forced vital capacity", "<b>Normal or increased</b>"),
  ("Total lung capacity and forced vital capacity", "<b>Decreased</b>"),
 ], "mnemonic": {"hook": "Ground glass Goes first, Honeycomb Hangs on late; in restriction the Ratio is Retained while the volumes are Reduced.",
  "key": [["G", "ground glass = fine, early"], ["H", "honeycombing = medium, late"], ["Coarse", "cystic spaces"],
          ["Ratio retained", "normal or increased ratio"], ["Volumes reduced", "total lung capacity and forced vital capacity decreased"]],
  "breaks": "The other patterns (nodular, reticulonodular, hilar adenopathy in sarcoidosis and silicosis) have no letter."}},

{"id": "crit-l41-labs", "label": "Laboratory Clues in Interstitial Lung Disease", "color": L41C,
 "tag": "Classification &middot; Lecture 41 &middot; slide 25",
 "cols": ["Test", "Points to"], "widths": ["50%", "50%"], "rows": [
  ("Sedimentation rate increased", "<b>Active sarcoidosis</b>"),
  ("High antinuclear antibody", "<b>Collagen vascular disease</b>"),
  ("<b>c-ANCA</b> (cytoplasmic antineutrophil cytoplasmic antibody)", "<b>Granulomatosis with polyangiitis</b>"),
  ("Anti-glomerular and anti-alveolar basement membrane antibodies", "<b>Goodpasture syndrome</b> (glomerulonephritis + diffuse pulmonary hemorrhage, young adults)"),
  ("Elevated angiotensin-converting enzyme", "<b>Sarcoidosis</b>; the slide also writes &ldquo;hypersensitivity silicosis&rdquo;"),
  ("Eosinophilia", "Eosinophilic pneumonia, sarcoidosis, drug-induced"),
  {"note": "Slide 44: the angiotensin-converting enzyme is elevated in 40&ndash;80% of sarcoidosis patients."},
 ], "mnemonic": {"hook": "Sarcoid has the ACE (angiotensin-converting enzyme) and the Sed rate; GPA (granulomatosis with polyangiitis) is C-ANCA; Goodpasture hits the Basement (lung and kidney); ANA means Autoimmune.",
  "key": [["ACE + Sed", "sarcoidosis (active)"], ["C-ANCA", "granulomatosis with polyangiitis"], ["Basement", "anti-basement membrane: Goodpasture"],
          ["ANA", "collagen vascular (autoimmune) disease"]],
  "breaks": "Eosinophilia (three causes) and the slide&rsquo;s &ldquo;hypersensitivity silicosis&rdquo; beside the enzyme are not in the hook."}},

{"id": "crit-l41-ipf", "label": "Idiopathic Pulmonary Fibrosis Without a Biopsy", "color": L41C,
 "tag": "Criteria &middot; Lecture 41 &middot; slide 35",
 "cols": ["#", "In a patient over 65 (all four = 90% confidence, no surgical lung biopsy)"], "widths": ["10%", "90%"], "rows": [
  ("1", "<b>Idiopathic</b> disease by history, with <b>inspiratory crackles</b> on examination"),
  ("2", "<b>Restrictive</b> physiology on pulmonary function testing"),
  ("3", "Radiographic evidence of <b>progressive fibrosis over several years</b>"),
  ("4", "<b>Diffuse, patchy fibrosis with pleural-based honeycombing</b> on high-resolution CT"),
  {"note": "Corticosteroids may be used in cryptogenic organizing pneumonia, lymphoid interstitial pneumonia and nonspecific interstitial pneumonia (slide 38); for idiopathic pulmonary fibrosis nothing has improved survival and smoking cessation is critical (slide 37)."},
 ], "mnemonic": {"hook": "Over 65 and CRPH (crackles, restriction, progression, honeycomb): skip the biopsy.",
  "key": [["C", "Crackles (inspiratory) in idiopathic disease"], ["R", "Restrictive physiology"], ["P", "Progressive fibrosis over years on films"], ["H", "Honeycombing, pleural-based, on high-resolution CT"]],
  "breaks": "The age (over 65) is outside the four letters."}},

{"id": "crit-l41-sarcoid-stage", "label": "Sarcoidosis: Chest Film Stages", "color": L41C,
 "tag": "Staging &middot; Lecture 41 &middot; slides 45, 48",
 "cols": ["Stage", "Chest film"], "widths": ["16%", "84%"], "rows": [
  ("<b>I</b>", "Bilateral hilar adenopathy <b>alone</b>"),
  ("<b>II</b>", "Hilar adenopathy <b>and</b> parenchymal involvement"),
  ("<b>III</b>", "Parenchymal involvement <b>alone</b> (diffuse reticular infiltrates)"),
  ("<b>IV</b>", "<b>Advanced fibrosis</b>: honeycombing, hilar retraction, bullae, cysts, emphysema"),
  {"note": "Best prognosis with hilar adenopathy alone; parenchymal involvement is worse; 20% with lung involvement get irreversible impairment (slide 48). Biopsy whenever lymphoma or another diagnosis is possible (slide 45)."},
 ], "mnemonic": {"hook": "Nodes, Nodes + lung, Lung, Scar.",
  "key": [["I", "nodes (hilar adenopathy) alone"], ["II", "nodes + lung"], ["III", "lung alone"], ["IV", "scar (fibrosis, honeycombing)"]]}},

{"id": "crit-l41-sarcoid-steroids", "label": "Sarcoidosis: When to Give Oral Corticosteroids", "color": L41C,
 "tag": "Criteria &middot; Lecture 41 &middot; slides 46&ndash;47",
 "cols": ["Indication (slide 47)", "Organ"], "widths": ["64%", "36%"], "rows": [
  ("<b>Hypercalcemia</b>", "Calcium"),
  ("<b>Cardiac</b> involvement", "Heart"),
  ("<b>Iritis</b>, <b>uveitis</b>", "Eyes"),
  ("Granulomatous hepatitis", "Liver"),
  ("<b>Progressive pulmonary lesions</b>", "Lungs (progressive)"),
  ("Cutaneous lesions <b>other than erythema nodosum</b>", "Skin"),
  ("Arthritis", "Joints"),
  ("<b>Central nervous system</b> involvement", "Brain"),
  ("Disabling constitutional symptoms", "Constitution"),
  {"note": "About 90% respond to corticosteroids. Intolerant or refractory: methotrexate, azathioprine or infliximab (slide 46)."},
 ], "mnemonic": {"hook": "Calcium HELPS JB&rsquo;s Constitution.",
  "key": [["C", "Calcium: hypercalcemia"], ["H", "Heart: cardiac involvement"], ["E", "Eyes: iritis, uveitis"], ["L", "Liver: granulomatous hepatitis"],
          ["P", "Progressive pulmonary lesions"], ["S", "Skin lesions other than erythema nodosum"], ["J", "Joints: arthritis"],
          ["B", "Brain: central nervous system involvement"], ["Constitution", "disabling constitutional symptoms"]],
  "breaks": "Erythema nodosum alone is the skin exception: it is NOT an indication."}},

{"id": "crit-l41-dusts", "label": "The Dust Diseases Side by Side", "color": L41C,
 "tag": "Classification &middot; Lecture 41 &middot; slides 50&ndash;64",
 "cols": ["", "Coal workers&rsquo; pneumoconiosis", "Asbestosis", "Silicosis"], "widths": ["16%", "28%", "28%", "28%"], "min_width": "560px", "rows": [
  ("Exposure", "Coal dust", "<b>Insulation, demolition, shipyards, construction</b> (10&ndash;20 years; seen about 15 years later)", "<b>Mining, sandblasting, quarry, stone work</b> (crystalline silica)"),
  ("Where", "<b>Upper</b> lung fields", "<b>Bases</b>", "<b>Upper</b> lobes (lighter dust)"),
  ("Hallmark", "<b>Coal macules 2&ndash;5 mm</b>", "<b>Pleural plaques</b> (most common film finding); ferruginous bodies; <b>CT preferred</b>", "<b>Silicotic nodules 1&ndash;10 mm</b>; <b>eggshell</b> calcification of hilar nodes; milky lavage"),
  ("Function", "Restrictive, reduced diffusing capacity", "Reduced vital capacity and total lung capacity", "Reduced forced vital capacity and forced expiratory volume"),
  ("Watch for", "<b>Progressive massive fibrosis</b>", "<b>Lung cancer</b> (smokers) and <b>mesothelioma</b> (10% lifetime)", "<b>Tuberculosis</b> (skin test + current chest film), progressive massive fibrosis, scleroderma"),
  ("Treatment", "Supportive: oxygen, vaccines, rehabilitation, stop smoking; transplant", "Supportive: fibers cannot be removed", "Supportive; stop smoking"),
 ], "mnemonic": {"hook": "Coal and silica float UP, asbestos sinks DOWN; asbestos Plants Plaques and Mesothelioma, silica brings Tuberculosis and Eggshells.",
  "key": [["Up", "coal (upper fields) and silica (upper lobes)"], ["Down", "asbestos (bases)"],
          ["Plaques + mesothelioma", "asbestos"], ["Tuberculosis + eggshells", "silica"]],
  "breaks": "The hook leaves out the coal macules (2&ndash;5 mm), the silicotic nodules, progressive massive fibrosis (coal and silica), lung cancer, scleroderma, and the function and treatment rows."}},

{"id": "crit-l41-hp", "label": "Hypersensitivity Pneumonitis: Acute, Subacute, Chronic", "color": L41C,
 "tag": "Classification &middot; Lecture 41 &middot; slides 66&ndash;67",
 "cols": ["Type", "Timing", "Signs and symptoms"], "widths": ["16%", "28%", "56%"], "rows": [
  ("<b>Acute</b>", "Within 9 hours of exposure", "<b>Flu-like illness</b> (fever, chills, muscle or joint pain, headache), rales, cough"),
  ("<b>Subacute</b>", "Multiple exposures (15%)", "Rales, cough, chronic bronchitis, shortness of breath, anorexia or weight loss"),
  ("<b>Chronic</b>", "Multiple exposures (5%)", "Cough, chronic bronchitis, shortness of breath, anorexia or weight loss, <b>fatigue, lung fibrosis, clubbing</b>"),
  {"note": "Slide 66: symptoms, with nausea 4&ndash;8 hours after exposure; slide 67: acute disease within 9 hours of exposure."},
 ], "mnemonic": {"hook": "Acute is the Flu; chronic adds the three Fs: Fatigue, Fibrosis, Fingers (clubbing).",
  "key": [["Flu", "acute: flu-like illness, rales, cough"], ["Fatigue", "chronic only"], ["Fibrosis", "chronic only"], ["Fingers", "clubbing, chronic only"]],
  "breaks": "Subacute has no letter: it sits between (rales, cough, bronchitis, dyspnea, weight loss)."}},

{"id": "crit-l41-ards", "label": "Acute Respiratory Distress Syndrome: Criteria and Severity", "color": L41C,
 "tag": "Criteria &middot; Lecture 41 &middot; slide 73 (picture)",
 "cols": ["Item", "What the picture says"], "widths": ["30%", "70%"], "rows": [
  {"group": "CORE DIAGNOSTIC CRITERIA"},
  ("Acute onset", "Develops <b>within 7 days</b> of a known clinical insult"),
  ("Bilateral opacities", "New opacities <b>not explained</b> by effusion, atelectasis or nodules"),
  ("Non-cardiogenic", "Failure <b>not fully explained</b> by heart failure or fluid overload"),
  ("Oxygenation", "Arterial oxygen pressure &divide; fraction of inspired oxygen <b>under 300 mm Hg</b> (or saturation &divide; fraction under 315)"),
  {"group": "SEVERITY (arterial oxygen pressure &divide; fraction of inspired oxygen)"},
  ("<b>Mild</b>", "200&ndash;300 mm Hg"),
  ("<b>Moderate</b>", "100&ndash;200 mm Hg"),
  ("<b>Severe</b>", "Under 100 mm Hg"),
  {"note": "Example: arterial oxygen 60 mm Hg on 50% oxygen (0.5) = 120, moderate. The management picture (slide 74) gives plateau pressure &ldquo;under 50 cm H2O&rdquo;, which differs from current guidelines (see the guide note); no question keys the number."},
 ], "mnemonic": {"hook": "A-R-D-S: Acute, Radiograph, Doesn&rsquo;t come from the heart, Short of oxygen; then grade by 3-2-1 hundred.",
  "key": [["A", "Acute: within 7 days of an insult"], ["R", "Radiograph: bilateral opacities not from effusion, atelectasis, nodules"],
          ["D", "Doesn&rsquo;t come from the heart: not fully explained by heart failure or fluid overload"], ["S", "Short of oxygen: ratio under 300"],
          ["3-2-1", "mild 200&ndash;300, moderate 100&ndash;200, severe under 100"]]}},
]

TOPICS = [
{"id": "l41-emph", "label": "★ Professor Emphasized — Inflammatory Lung Disease", "color": "#b8860b", "rows": [
  ["★ History is the clue", "&ldquo;A person showing up at a place with a thing&rdquo;: <b>occupation, hobbies, exposure, timing</b>. The presentations look alike (exertional dyspnea, dry cough, crackles); the history separates them."],
  ["★ Pay attention", "The <b>laboratory clue table</b> (sedimentation rate and angiotensin-converting enzyme = sarcoid, c-ANCA = granulomatosis with polyangiitis, anti-basement membrane = Goodpasture, antinuclear antibody = collagen vascular)."],
  ["★ Board pointers", "Lupus pernio + dry cough &rarr; sarcoid; <b>ferruginous bodies &rarr; asbestos</b>; <b>milky lavage &rarr; silicosis</b>; hypersensitivity pneumonitis: <b>find the agent, avoid the agent</b>; idiopathic pulmonary fibrosis is the most common."],
  ["Not tested", "Don&rsquo;t memorize the cause/drug charts; rare subtypes (&ldquo;desquamative interstitial pneumonia on a test? No&rdquo;); few Churg-Strauss / Wegener questions; sarcoid immunology slide."],
  ["Most time", "<b>Acute respiratory distress syndrome</b> (11 of 66 minutes): a feared complication of sepsis, trauma, aspiration and more; the pictures carry AI typos (&ldquo;Chuck&rdquo; = shock)."],
]},
{"id": "l41-ild", "label": "Interstitial Lung Disease: the Common Ground", "color": L41C, "rows": [
  ["What it is", "200+ disorders of <b>scarring and/or inflammation of the parenchyma</b> (alveoli, ducts, respiratory bronchioles); <b>not malignant, not infectious</b>; stiff, restrictive lungs &rarr; <b>shortness of breath</b>."],
  ["How", "Inflammatory cells in alveolar walls &rarr; <b>alveolitis</b> &rarr; fibroblasts &rarr; <b>collagen</b> = fibrosis (permanent)."],
  ["Two groups", "<b>Inflammation and fibrosis</b> vs <b>granulomatous</b>; each known or unknown cause. Known: inorganic and organic dusts, fumes, gases. Unknown: sarcoidosis, idiopathic pulmonary fibrosis, connective tissue disease."],
  ["Drug causes", "<b>Methotrexate, amiodarone, nitrofurantoin, bleomycin</b>, chemotherapy, radiation (and the long slide 9 list)."],
  ["Symptoms", "<b>Progressive exertional dyspnea</b> or <b>persistent nonproductive cough</b>; hemoptysis, wheeze, chest pain, tachypnea, anorexia; later dyspnea at rest."],
  ["Exam", "Small lung volumes, <b>bibasilar dry rales (inspiratory crackles)</b>, <b>clubbing</b>, right heart failure late; <b>may be normal early</b>."],
]},
{"id": "l41-iip", "label": "Idiopathic Interstitial Pneumonia &amp; Pulmonary Fibrosis", "color": "#2f5d6b", "rows": [
  ["Subtypes", "Idiopathic pulmonary fibrosis (<b>most common</b>), desquamative, nonspecific, cryptogenic organizing, respiratory bronchiolitis-associated, lymphoid, acute interstitial."],
  ["Smoking", "<b>67&ndash;75%</b> of idiopathic and familial fibrosis patients have smoked; smoking is the cause in the majority; <b>cessation is critical</b>."],
  ["Picture", "<b>Insidious dry cough</b>, exertional dyspnea, fatigue; clubbing, <b>bibasilar inspiratory crackles</b>, reduced chest expansion."],
  ["Tests", "Restrictive pattern; CT <b>diffuse patchy fibrosis with pleural-based honeycombing</b>; lower-field markings; biopsy may be needed (lavage, transbronchial, surgical)."],
  ["Treatment", "<b>Controversial</b>: nothing improves survival vs no treatment; steroids only for cryptogenic organizing, lymphoid and nonspecific subtypes."],
]},
{"id": "l41-ctd", "label": "Connective Tissue &amp; Granulomatous Disease", "color": "#4a5a2a", "rows": [
  ["Connective tissue", "Lupus, rheumatoid arthritis, ankylosing spondylitis, systemic sclerosis, Sj&ouml;gren, polymyositis-dermatomyositis, scleroderma. <b>Methotrexate treats them and also causes interstitial lung disease.</b>"],
  ["Hemorrhage syndromes", "Goodpasture (anti-basement membrane), idiopathic pulmonary hemosiderosis, isolated pulmonary capillaritis."],
  ["Granulomatous", "Sarcoidosis; granulomatosis with polyangiitis (c-ANCA); Churg-Strauss; hypersensitivity pneumonitis."],
]},
{"id": "l41-sarcoid", "label": "Sarcoidosis", "color": "#7a3b2e", "rows": [
  ["Who", "Multi-organ, <b>noncaseating granulomas</b>, lungs and lymphatics most; <b>North American Black and Northern European white</b> people; <b>women</b>; <b>third and fourth decades</b>."],
  ["Picture", "Cough, insidious dyspnea, chest discomfort, malaise, fever, weight loss, <b>nontender lymphadenopathy</b>; <b>erythema nodosum</b> (painful rashes, lower legs), parotid enlargement, <b>lupus pernio</b> (painful skin sores, face), hepatosplenomegaly."],
  ["Tests", "Film: <b>symmetric bilateral hilar and right paratracheal adenopathy</b>; angiotensin-converting enzyme up in 40&ndash;80%, hypercalcemia (5%), hypercalciuria, eosinophilia, high sedimentation rate; <b>biopsy confirms</b> (transbronchial or fine-needle node)."],
  ["Treatment", "Corticosteroids (90% respond) for the listed indications; <b>methotrexate, azathioprine, infliximab</b> if intolerant or refractory."],
  ["Follow-up", "<b>Yearly</b>: exam, pulmonary function, chest film, electrocardiogram, chemistry, <b>eye exam</b>."],
]},
{"id": "l41-hp", "label": "Hypersensitivity Pneumonitis", "color": "#5a3a5e", "rows": [
  ["What", "<b>Non-atopic, non-asthmatic</b>; inhaled <b>organic</b> dust: moldy hay (farmer&rsquo;s lung), bird excreta and feathers (bird fancier&rsquo;s), cheese maker&rsquo;s lung, moldy sugarcane, infested grain."],
  ["Picture", "Malaise, chills, fever, cough, dyspnea, nausea <b>hours after exposure</b>; may mimic paroxysmal nocturnal dyspnea (worse after work at home); crackles, tachypnea, tachycardia, cyanosis."],
  ["Tests", "<b>Serum antibodies to the agent = definitive</b>; white count up with left shift; hypoxia; restrictive; small nodules <b>sparing apices and bases</b>; biopsy if subacute or chronic; noncaseating granulomas."],
  ["Treatment", "<b>Identify and avoid the agent</b>; steroids if severe; supportive; transplant. <b>Reversible if caught early.</b>"],
]},
{"id": "l41-ards", "label": "Acute Respiratory Distress Syndrome", "color": "#7a3b2e", "rows": [
  ["Causes", "Direct: <b>aspiration</b>, diffuse pneumonia, contusion, toxic gas, near-drowning, emboli. Systemic: <b>sepsis</b> (about a third of cases), pancreatitis, shock, trauma, overdoses, <b>transfusions</b>, amiodarone, nitrofurantoin."],
  ["Picture", "<b>Dyspnea 12&ndash;48 hours</b> after the insult; <b>hypoxemia refractory to oxygen</b>; tachypnea, retractions, crackles; multiorgan failure."],
  ["Imaging", "Bilateral infiltrates becoming confluent; <b>air bronchograms (about 80%)</b>; <b>normal heart size</b>, few effusions; <b>echocardiogram excludes cardiogenic edema</b> (cardiomegaly, batwing opacities)."],
  ["Management", "Treat the cause; <b>low tidal volume</b>; positive end-expiratory pressure for arterial oxygen above 60; <b>early prone positioning (moderate to severe)</b>; <b>conservative fluids</b>; <b>transfuse at 7 g/dL</b>; steroids within 14 days (conditional); avoid oscillatory ventilation and routine pulmonary artery catheters; neuromuscular blockade controversial; ECMO (extracorporeal membrane oxygenation) salvage."],
  ["Prognosis", "Mortality about <b>30%</b> (20% trauma to 80% end-stage liver disease); lung function recovers over <b>6&ndash;12 months</b>; residual diffusion deficits, weakness, fatigue."],
]},
]
