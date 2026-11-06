# -*- coding: utf-8 -*-
from _pd2_pulm_osce_data import R
BATCH = {

"Pleural effusion": R(
  "urgent",
  "CMS L44 Pleural Disorders (Gray) &middot; slides 26, 41, 46, 83, 85&ndash;90, 96, 97, 99, 101, 102, 106, "
  "108, 110, 111, 113, 114 &middot; PD2 Thorax slides 30, 34, 40, 43, 52&ndash;55, 59&ndash;62",
  "Affects more than 1.5 million people a year in the United States, about 500,000 of them from congestive "
  "heart failure (slide 83), which also causes over 90% of transudates (slide 111).",
  "&ldquo;I get winded just walking to the mailbox, and I&rsquo;ve got a dry cough. There&rsquo;s a sharp "
  "pain on my right side when I breathe in deep, and it goes up into my shoulder.&rdquo; Sometimes: "
  "&ldquo;My ankles swell and I sleep propped up on pillows.&rdquo;",
  "Under 300 mL there are <b>no examination findings</b> (slide 87). Inspection: <b>asymmetric "
  "expansion</b>; the trachea shifts <b>away</b> from an effusion over 1000 mL (slide 87). Palpation: "
  "<b>decreased tactile fremitus</b>, increased toward the top of a large effusion (PD2 Thorax slide 62). "
  "Percussion: <b>dull over the fluid</b>, with a high diaphragm (PD2 Thorax slides 43, 62). Auscultation: "
  "<b>diminished or absent breath sounds</b>, bronchial toward the top, possible friction rub; voice sounds "
  "decreased to absent, increased near the top (slide 88). The slides give no vital-sign clue.",
  "Examine the back with the patient sitting, arms folded across the chest (PD2 Thorax slide 30). Inspect for "
  "<b>asymmetric expansion</b> and check that the <b>trachea is midline</b> (PD2 Thorax slide 34). Palpate "
  "<b>chest expansion</b> and <b>tactile fremitus</b> side to side (PD2 Thorax slide 40). <b>Percuss</b> "
  "down both sides to the dull level and measure <b>diaphragmatic excursion</b>, normally 3&ndash;5.5 cm "
  "(PD2 Thorax slide 43). Auscultate breath sounds and for a rub, then test <b>egophony, bronchophony and "
  "whispered pectoriloquy</b> near the top of the dullness (PD2 Thorax slides 52&ndash;55).",
  [("Lobar pneumonia", "Dull too, but <b>increased</b> fremitus, bronchial breath sounds, late inspiratory "
                       "crackles and egophony over the area, with the trachea midline (PD2 Thorax slide 60); "
                       "an infiltrate, not fluid, on the film (slide 89)"),
   ("Atelectasis", "Dull with diminished sounds too, but the trachea deviates <b>toward</b> the affected side "
                   "and the intercostal spaces narrow (PD2 Thorax slide 59)"),
   ("Pneumothorax", "Fremitus and breath sounds are lost too, but the note is <b>hyperresonant</b>, not dull "
                    "(PD2 Thorax slide 61)")],
  "<b>Upright chest X-ray</b> &rarr; blunted costophrenic angles: 75 mL of fluid blunts the posterior angle "
  "(lateral view), 175 mL the lateral angle (frontal view) (slide 90). <b>Thoracentesis with pleural fluid "
  "analysis</b> &rarr; <b>exudate</b> by Light&rsquo;s criteria if at least one is met: fluid-to-serum "
  "protein ratio &gt; 0.5, fluid-to-serum lactate dehydrogenase ratio &gt; 0.6, or fluid lactate "
  "dehydrogenase &gt; two-thirds of the upper limit of normal serum lactate dehydrogenase; none met means "
  "<b>transudate</b> (slides 101, 110). Also send white cell count, Gram stain, cytology and culture (slide 99).",
  "<b>Increased</b> fremitus, bronchial breath sounds and egophony over the dull area, with the trachea "
  "midline, mean pneumonia (PD2 Thorax slide 60), and the film shows an infiltrate, not fluid (slide 89). "
  "Dullness with the trachea pulled <b>toward</b> that side means atelectasis (PD2 Thorax slide 59). A "
  "<b>hyperresonant</b> note means pneumothorax, confirmed by a visceral pleural line on the X-ray (slide 26).",
  "<b>Treat the underlying disorder</b> (slide 113): for a heart-failure transudate, diuretic therapy first "
  "(slide 97). <b>Therapeutic thoracentesis</b> removes fluid and relieves symptoms (slide 96). <b>Chest "
  "tube</b> at the 4th or 5th intercostal space, midaxillary line (slide 41). Recurrent malignant effusion: "
  "<b>pleurodesis</b> with a sclerosant such as talc (slides 46, 113) or an <b>indwelling tunneled pleural "
  "catheter</b> drained at home (slides 113, 114). Empyema: drainage plus antibiotics (slide 108). "
  "Chylothorax: octreotide and fewer long-chain triglycerides (slide 106).",
  "URGENT &mdash; prompt upright chest X-ray, then diagnostic thoracentesis for any new "
  "effusion with no clinical cause (slide 96).",
  "Fluid has collected between the lung and the chest wall, and <b>finding its cause</b> (most often heart "
  "failure, pneumonia or cancer) guides treatment (slides 102, 111, 113). The needle sample takes "
  "50&ndash;100 mL for testing (slide 96), and draining more eases the breathlessness. Fluid that keeps "
  "coming back from cancer can be managed with pleurodesis or a catheter drained at home (slide 113). "
  "Return for worse breathlessness, fever or coughing blood (slide 86)."),

"Pleurisy": R(
  "routine",
  "CMS L44 Pleural Disorders (Gray) &middot; slides 9&ndash;14, 23 &middot; PD2 Thorax slides 13, 14, 17, "
  "40, 50 &middot; PDM 16 slides 5, 50",
  "Pleuritic pain is a symptom with many causes &mdash; viral or bacterial infection, lupus, "
  "rheumatoid arthritis, trauma, pneumothorax, pulmonary embolism, cancer and drug reactions (slides 9, 10); "
  "the slides give no prevalence figure.",
  "&ldquo;It&rsquo;s a sharp, stabbing pain right here on my side, and it catches every time I take a deep "
  "breath, cough or sneeze.&rdquo; Sometimes: &ldquo;It goes up into my shoulder and neck on the same "
  "side.&rdquo;",
  "Inspection: <b>tachypnea</b> with <b>limited expansion on the painful side</b> (slide 12), from splinting "
  "(PD2 Thorax slide 40). Palpation and percussion <b>depend on the underlying condition</b>; the slides "
  "give no finding of pleurisy&rsquo;s own (slide 12). Auscultation: a <b>pleural friction rub</b> &mdash; "
  "grating, scratching or creaking, in both phases of breathing, that <b>disappears when the breath is "
  "held</b> (slide 12), louder with firm stethoscope pressure and unchanged by coughing (PD2 Thorax slide "
  "50). The slides give no transmitted-voice-sound finding, and no vital-sign clue beyond tachypnea.",
  "Have the patient <b>point to the pain</b> and say what worsens it (PD2 Thorax slide 13). <b>Palpate the "
  "chest wall</b> for focal tenderness that reproduces the pain (PD2 Thorax slide 14). Compare "
  "<b>expansion</b> side to side (PD2 Thorax slide 40). Listen for a rub in the <b>axilla and lower "
  "bases</b>, press the stethoscope firmly, ask the patient to <b>cough</b>, then to <b>hold their "
  "breath</b>: a pleural rub stops, a pericardial rub continues (PD2 Thorax slide 50).",
  [("Pericarditis", "The rub <b>persists when the breath is held</b>, and the pain is worse lying flat or "
                    "breathing in and better sitting forward (PD2 Thorax slides 14, 50)"),
   ("Myocardial infarction", "<b>Pressure or squeezing</b> retrosternal pain, often on exertion, radiating to "
                             "the arm, neck, jaw or back; not pleuritic or positional (PD2 Thorax slide 14)"),
   ("Pulmonary embolism", "Pleuritic pain with <b>sudden unexplained dyspnea</b>, hemoptysis, syncope or "
                          "one-sided leg symptoms (PD2 Thorax slide 17)")],
  "<b>Auscultation</b> &rarr; a pleural friction rub that disappears when the patient holds their breath "
  "(slide 12) and grows louder with firm stethoscope pressure (PD2 Thorax slide 50). <b>History</b> &rarr; "
  "well-localized sharp or stabbing chest-wall pain made worse by deep breathing, coughing, movement or "
  "sneezing (slide 11). No test confirms pleurisy itself: testing depends on the underlying condition "
  "(slide 14).",
  "A rub that <b>persists with the breath held</b> (slide 12), with PR depression and widespread concave ST "
  "elevation on the electrocardiogram, means pericarditis; reciprocal ST depression or any Q waves mean "
  "myocardial infarction must be considered (PDM 16 slide 5). Sudden dyspnea (PD2 Thorax slide 17) with "
  "tachycardia and right axis deviation (PDM 16 slide 50) points to pulmonary embolism. Hyperresonance points to pneumothorax "
  "(slide 23).",
  "<b>Treat the underlying condition</b> (slide 14), so first exclude the dangerous causes: myocardial "
  "infarction, pericarditis, aortic dissection, pneumonia, pneumothorax and pulmonary embolism (slide 13). "
  "Then look for the listed causes: infection, systemic lupus erythematosus or rheumatoid arthritis, trauma, "
  "cancer, or a drug reaction to methotrexate, amiodarone or hydralazine (slide 10). For the pain, a "
  "<b>nonsteroidal anti-inflammatory drug</b> (slide 14).",
  "ROUTINE &mdash; clinic visit once the history and examination exclude the dangerous causes (slide 13); "
  "follow-up then depends on the underlying condition (slide 14).",
  "The pain comes from <b>inflamed pleural layers rubbing together</b> as you breathe (slide 9). It is a "
  "symptom, not a diagnosis, so we are looking for its cause (slides 9, 14). Take the anti-inflammatory as "
  "directed. Get emergency care for sudden breathlessness, coughing blood, fainting, a swollen leg, or "
  "crushing chest pressure (PD2 Thorax slides 14, 17)."),

"Pneumothorax": R(
  "emergent",
  "CMS L44 Pleural Disorders (Gray) &middot; slides 16, 17, 19&ndash;23, 25&ndash;30, 33, 34, 51, 53, 55, "
  "57, 59&ndash;61, 63, 64, 66&ndash;68 &middot; PD2 Thorax slides 4, 7, 14, 17, 40, 61, 64 &middot; PDM 16 "
  "slides 5, 50",
  "Collapses part or all of a lung; a secondary pneumothorax can be life-threatening through lost pulmonary "
  "reserve, and a tension pneumothorax cuts venous return and cardiac output, causing hypotension "
  "(slides 16, 20, 63, 64).",
  "&ldquo;I was sitting at my desk when a sudden, stabbing pain hit the right side of my chest, and now "
  "I can&rsquo;t catch my breath &mdash; it&rsquo;s worse when I breathe in.&rdquo; After a fall: "
  "&ldquo;I landed on my ribs, and now I can barely breathe.&rdquo;",
  "Inspection: <b>tachypnea</b>, <b>decreased expansion on the affected side</b> (slide 22). Palpation: "
  "<b>decreased or absent tactile fremitus</b> (slide 22); trachea midline in a simple pneumothorax (PD2 "
  "Thorax slide 64). Percussion: <b>hyperresonant</b> (slide 23), or tympanic (PD2 Thorax slide 61). "
  "Auscultation: <b>diminished or absent breath sounds</b> and voice sounds on that side (slide 23); "
  "possible pleural rub (PD2 Thorax slide 61). Vitals: <b>tachycardia</b> (slide 23). <b>Tension</b>: "
  "trachea deviated to the other side, <b>hypotension</b>, distended neck veins (slide 64).",
  "Count the respiratory rate and check the <b>stability criteria</b>: respiratory rate under 24, heart rate "
  "60&ndash;120, normal blood pressure, room-air saturation over 90%, whole sentences (slide 51). Watch both "
  "sides move, and check the <b>trachea</b> and <b>neck veins</b> (slide 64). Palpate <b>expansion and "
  "tactile fremitus</b> side to side (PD2 Thorax slide 40). <b>Percuss</b> both sides, then compare "
  "<b>breath and voice sounds</b> (slide 23). Ask about trauma, a recent procedure and prior "
  "pneumothorax (slides 17, 21, 61).",
  [("Pulmonary embolism", "The same sudden dyspnea and pleuritic pain, but with hemoptysis, syncope or "
                          "one-sided leg symptoms after surgery, immobility, cancer or estrogen (PD2 Thorax "
                          "slide 17)"),
   ("Myocardial infarction", "<b>Pressure or squeezing</b> retrosternal pain, often on exertion, radiating to "
                             "the arm, neck or jaw, rather than one-sided pleuritic pain (PD2 Thorax slide 14)"),
   ("Aortic dissection", "<b>Sudden tearing</b> pain, maximal at onset, radiating to the back (PD2 Thorax "
                         "slide 14)")],
  "<b>Upright chest X-ray</b> &rarr; a thin, sharp <b>visceral pleural line</b>, convex toward the chest "
  "wall, with no lung markings beyond it (slide 26); 3 cm or more from apex to cupola is large (slide 28); "
  "supine, a deep, dark costophrenic angle, the <b>deep sulcus sign</b> (slide 29). <b>Chest computed "
  "tomography</b> &rarr; best for presence, size and location, and shows blebs and bullae, but impractical "
  "when time is critical (slide 33). <b>Tension</b> is a clinical diagnosis: no time for the X-ray "
  "(slide 66).",
  "Hemoptysis, syncope or one-sided leg symptoms (PD2 Thorax slide 17), with tachycardia and right axis "
  "deviation on the electrocardiogram (PDM 16 slide 50), point to pulmonary embolism. Exertional "
  "retrosternal pressure (PD2 Thorax slide 14), with reciprocal ST depression or Q waves (PDM 16 slide 5), "
  "points to myocardial infarction. Tearing pain into the back points to aortic dissection (PD2 Thorax "
  "slide 14).",
  "<b>Tension</b>: immediate chest tube, or <b>needle decompression</b> at the 2nd intercostal space, over "
  "the 3rd rib, midclavicular line, then a chest tube and admission (slides 66, 67). <b>Chest tube</b>: 4th "
  "or 5th intercostal space, midaxillary line (slide 68), in the triangle of safety (PD2 Thorax slide 7), "
  "just above the rib (PD2 Thorax slide 4). "
  "<b>Small primary</b>: observation, analgesia, 100% oxygen by non-rebreather, repeat X-ray in "
  "6&ndash;12 hours (slide 53). <b>Large or secondary</b>: chest tube (slides 55, 57). <b>Recurrent</b>: "
  "video-assisted thoracoscopic surgery with pleurodesis (slide 55).",
  "EMERGENT &mdash; emergency department now; tension needs decompression before any imaging (slide 66), and "
  "bedside ultrasound showing absent lung sliding helps in the unstable patient (slide 30).",
  "Recurrence approaches <b>50% within three years</b> of a first spontaneous pneumothorax (slide 59), so "
  "come back at once for sudden chest pain or breathlessness. <b>Stop smoking</b>: it raises recurrence risk "
  "up to 100-fold (slide 60). Delay air travel 7&ndash;14 days after an X-ray confirms resolution, and avoid "
  "scuba diving (slide 60). Video-assisted surgery with pleurodesis best prevents recurrence (slide 59)."),

"Hemothorax": R(
  "emergent",
  "CMS L44 Pleural Disorders (Gray) &middot; slides 23, 64, 66, 69&ndash;74, 83, 87, 88, 105 &middot; "
  "PD2 Thorax slides 4, 7, 39, 40, 42",
  "Bleeding into the pleural space, most often from trauma to the heart, vessels, lung, or the intercostal, "
  "pulmonary or internal thoracic arteries; "
  "persistent hemorrhage or shock needs surgery, and chest tube blood loss over 200 mL an hour means "
  "thoracotomy (slides 69, 74).",
  "&ldquo;I was stabbed in the side about an hour ago. It hurts when I breathe, and I can&rsquo;t get "
  "enough air.&rdquo; Or, after a crash: &ldquo;My chest hit the steering wheel, and I&rsquo;m getting more "
  "and more short of breath.&rdquo;",
  "The thorax lecture lists hemothorax under <b>dullness to percussion</b> (PD2 Thorax slide 42). The "
  "pleural slides class it as an exudative pleural effusion (slides 74, 83), so also expect effusion signs on "
  "the bleeding side: <b>asymmetric expansion</b> and decreased tactile fremitus (slide 87) and "
  "<b>diminished or absent breath sounds</b> (slide 88). Look for the chest-wall injury (slide 70): "
  "bruising, tenderness or bony step-offs over fractured ribs (PD2 Thorax slide 39). Vitals: the slides "
  "name only <b>persistent hemodynamic shock</b> (slide 74).",
  "Take the <b>blood pressure and heart rate</b>, and repeat them (slide 74). Expose and inspect the chest "
  "wall for the <b>wound or bruising</b>, and palpate the ribs for tenderness, step-offs and crepitus (PD2 "
  "Thorax slide 39). Compare <b>expansion and tactile fremitus</b> (PD2 Thorax slide 40), <b>percuss</b> "
  "for dullness (PD2 Thorax slide 42), and compare breath sounds side to side. Check the <b>trachea and "
  "neck veins</b> for tension (slide 64).",
  [("Tension pneumothorax", "Also after chest trauma, but the note is <b>hyperresonant</b>, with hypotension, "
                            "the trachea deviated away and distended neck veins (slides 23, 64)"),
   ("Hemorrhagic pleural effusion", "Bloody fluid whose hematocrit is <b>under 50%</b> of the peripheral "
                                    "blood hematocrit: an effusion, not a hemothorax (slide 74)"),
   ("Chylothorax", "Also most often after trauma such as thoracic surgery, but the fluid is <b>milky</b>, "
                   "with high triglycerides (slide 105)")],
  "<b>Chest X-ray</b> &rarr; fluid in the pleural space; with air above it, a hemopneumothorax, the top "
  "is a <b>straight air-fluid line with no meniscus</b> (slides 71, 72). <b>Pleural fluid hematocrit</b> "
  "&rarr; more than 50% of the peripheral blood hematocrit (slide 74). <b>Chest tube output</b> &rarr; "
  "evacuates and quantifies the bleeding; more than <b>200 mL an hour</b> means thoracotomy (slide 69).",
  "<b>Hyperresonance</b> with hypotension, tracheal deviation and distended neck veins means tension "
  "pneumothorax: decompress without waiting for the film (slides 64, 66). Pleural fluid hematocrit "
  "<b>under 50%</b> of the blood&rsquo;s means a hemorrhagic effusion, not hemothorax (slide 74). "
  "<b>Milky</b> fluid with high triglycerides on thoracentesis means chylothorax (slide 105).",
  "<b>Chest tube</b> to evacuate and quantify the bleeding (slide 69), the essential first step (slide 74), "
  "at the 4th or 5th intercostal space, midaxillary line (slide 73), in the triangle of safety (PD2 Thorax "
  "slide 7), just above the rib (PD2 Thorax slide 4). Blood loss <b>over 200 mL an hour</b>: "
  "<b>thoracotomy</b> (slide 69). Surgery also for persistent hemorrhage or shock; undrained blood leads to "
  "empyema, fibrothorax and trapped lung (slide 74).",
  "EMERGENT &mdash; emergency department now; bedside ultrasound finds the fluid at once (slide 74); "
  "immediate chest tube, with thoracotomy if the bleeding continues (slide 69).",
  "The tube drains the blood and shows how fast you are bleeding; if it keeps coming quickly, you need an "
  "<b>operation to stop it</b> (slides 69, 74). All of the blood has to come out, because blood left behind "
  "can become infected or scar and <b>trap the lung</b> (slide 74). Tell the team at once if your breathing "
  "gets harder."),
}

AGES = {
    "Pleural effusion": (
        "", "",
        "Mostly older adults, since its leading causes (heart failure, pneumonia, cancer) cluster in later "
        "life."),
    "Pleurisy": (
        "", "",
        "Any age; it follows its cause, with viral pleurisy common in otherwise healthy younger adults."),
    "Pneumothorax": (
        "Primary spontaneous: 20&ndash;40 years, classically tall, thin young men; secondary spontaneous "
        "comes with underlying lung disease, most often chronic obstructive pulmonary disease.",
        "CMS L44 slides 19, 20", ""),
    "Hemothorax": (
        "", "",
        "Any age; most patients are trauma victims, most often young adult men."),
}

TELLTALE = {
    "Pleural effusion": (
        "<b>Dullness</b> with <b>decreased fremitus</b> and <b>absent breath sounds</b> over the same area, "
        "bronchial sounds near its top, and <b>blunted costophrenic angles</b> on the upright film.",
        "CMS L44 slides 87, 88, 90"),
    "Pleurisy": (
        "Sharp, <b>well-localized pain worse with a deep breath or cough</b>, plus a <b>pleural friction rub "
        "that disappears when the patient holds their breath</b>.",
        "CMS L44 slides 11, 12"),
    "Pneumothorax": (
        "Sudden one-sided <b>pleuritic pain and dyspnea</b> with <b>hyperresonance</b> and <b>absent breath "
        "sounds and fremitus</b> on that side; add <b>hypotension, tracheal deviation and distended neck "
        "veins</b> for tension.",
        "CMS L44 slides 21&ndash;23, 64"),
    "Hemothorax": (
        "<b>Chest trauma</b> with fluid that is <b>dull to percussion</b>; on the film a <b>straight "
        "air-fluid line with no meniscus</b> when air is present too, and pleural fluid hematocrit "
        "<b>over 50%</b> of the blood&rsquo;s.",
        "CMS L44 slides 69, 71, 74; PD2 Thorax slide 42"),
}
