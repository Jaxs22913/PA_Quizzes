# -*- coding: utf-8 -*-
"""The test pictures under each Pulmonary OSCE chart row, the pulmonary twin of
the Cardiac OSCE chart's 12-lead row (_pd2_cardiac_osce_ecgs).

Jaxon, 2026-11-06: "If it calls for anthing like Xray, ekg or whatever include
it like you did for the cardiac one and explain it".

Rules every entry keeps (the cardiac chart's rules):
- The picture is LABELED by its source as the finding the caption names: the
  slide's title, the picture's own label, or (one Wikimedia Commons file) the
  file's own description. Nothing is identified by eye alone; where a slide
  describes a picture without pointing into it, nothing is boxed and the
  caption says so.
- Course-deck pictures cite the deck and slide; Commons pictures name author,
  licence and file page, and say what was changed (memory media_asset_licensing).
- A condition whose test has no picture of its own shows a normal film labeled
  "Normal" by its slide, captioned "Expected: normal".
- Every row shows at most two pictures, the tests its Tests column names; a
  test with no picture anywhere in the decks is listed under NOPIC in plain words.
- Where a slide gives a criteria table rather than a picture (Light's criteria,
  a severity scale), the table is set out as the slide gives it (kind "table").

The yellow boxes are drawn INTO the pictures by tools/box_pd2_pulm_osce_images.py
from clean copies outside the repo (~/Desktop/PA Quizzes/Semester 2/Physical
Diagnosis 2 Inbox/Pulm OSCE images (clean)/, written by
tools/extract_pd2_pulm_osce_images.py). Box coordinates are pixels on that copy.
Captions are HTML-escaped by the builder: write real characters, never entities.
"""

def deck(name, slide, changed=""):
    return {"kind": "deck", "deck": name, "slide": slide, "changed": changed}


def commons(title, author, lic, licurl, changed=""):
    return {"kind": "commons", "title": title, "author": author, "lic": lic, "licurl": licurl,
            "changed": changed,
            "page": "https://commons.wikimedia.org/wiki/" + title.replace(" ", "_")}


L35 = "PAJ5500 CMSI Asthma MBF 2026sc.pptx"
L36 = "37. svCOPD 2026.pptx"
L37 = "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx"
L38 = "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx"
L40 = "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome - Shah Fallsv.pptx"
L41 = "Inflammatory Lung Disease 2026.pptx"
L43 = "Pulmonary Nodules and Neoplasms 2026.pptx"
L44 = "Pleural Disorders 2026.pptx"
PDM14 = "14. EKG Axis, BBB.pptx"
PDM16 = "16. EKG Pericarditis Electrolytes and Other Abnormalities.pptx"
PDM17 = "17. Pulmonary Imaging - Prof. Fowler (GUEST).pptx"
BYSA3 = ("CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0")

# file -> (source, boxes as (x0, y0, x1, y1) on the clean picture)
IMAGES = {
    "spirometry-normal-vs-asthma.png": (deck(L35, 56), [
        (240, 280, 760, 510),           # the asthma curve at 1 second, FEV1 2.2 L, ratio 61%
        (950, 330, 1370, 770)]),        # the asthma flow-volume loop
    "peak-flow-meter-and-normal-values.png": (deck(L35, 61, "enlarged"), []),
    "spirometry-obstructive-copd.png": (deck(L36, 28, "enlarged"), [
        (500, 215, 965, 355)]),         # FEV1 2.0 L, FVC 3.9 L, ratio 0.51
    "cxr-copd-hyperinflation.jpg": (deck(L36, 31, "enlarged"), [
        (320, 50, 460, 420),            # saber-sheath trachea
        (60, 750, 720, 885)]),          # diaphragmatic tenting, flat low diaphragm
    "stop-bang-questionnaire.png": (deck(L40, 17, "enlarged"), [
        (55, 500, 640, 675)]),          # the scoring rule
    "cxr-influenza-pneumonia.jpg": (deck(L37, 106, "enlarged"), []),   # the slide does not point into the film
    "cxr-normal.jpg": (deck(PDM17, 80, "cropped to the film labeled Normal, enlarged"), []),
    "cxr-right-upper-lobe-consolidation.jpg": (deck(L37, 35), [
        (15, 40, 300, 300),             # the white right upper lobe
        (640, 250, 800, 340)]),         # the bulging fissure, red line on the second film
    "ct-consolidation.jpg": (deck(PDM17, 79), [
        (8, 55, 170, 245),              # panel a
        (8, 320, 175, 530)]),           # panel c
    "tuberculin-skin-test-reading.jpg": (deck(L38, 20, "enlarged"), [
        (165, 350, 500, 440)]),         # the millimeter scale across the forearm
    "cxr-tuberculosis-bilateral.jpg": (deck(L38, 31), [
        (130, 110, 520, 430),           # right upper lung, under the arrow
        (620, 180, 950, 500)]),         # left upper lung, under the arrow
    "hrct-honeycombing.jpg": (deck(L41, 36, "enlarged"), []),         # the slide does not point into the scan
    "pft-restrictive-pattern.png": (deck(L41, 29, "the slide's two graphs set side by side"), [
        (183, 278, 290, 327),           # the restrictive curve's FEV1 at 1 second
        (345, 165, 645, 232),           # its plateau, label and low FVC
        (1010, 148, 1135, 336)]),       # the narrow restrictive loop (overlapping the normal one)
    "cxr-hilar-adenopathy.jpg": (deck(L41, 28), [
        (360, 140, 480, 340),           # right paratracheal, yellow arrow
        (260, 370, 450, 580),           # right hilum
        (590, 380, 770, 580)]),         # left hilum
    "ct-hypersensitivity-pneumonitis.jpg": (deck(L41, 70), []),       # the slide does not point into the scan
    "histology-granulomas.jpg": (deck(L41, 70), []),
    "cxr-ards.jpg": (commons("File:AARDS X-ray cropped.jpg", "Samir; modified by Delldot", *BYSA3), []),
    "ct-lung-tumor.jpg": (deck(L43, 34, "enlarged"), [
        (540, 190, 720, 380)]),         # the cavitating peripheral mass
    "pet-ct-nodule.jpg": (deck(L43, 17, "enlarged"), [
        (580, 95, 650, 155),            # the nodule on CT
        (85, 440, 160, 515),            # its uptake on the fused image
        (585, 445, 655, 525)]),         # and on PET
    "ecg-right-ventricular-hypertrophy.jpg": (deck(PDM14, 34), [
        (10, 15, 300, 115),             # lead I: mainly negative
        (300, 280, 590, 390),           # aVF: positive
        (590, 5, 870, 260)]),           # V1, V2: R > S, strain, P wave
    "cxr-pulmonary-edema.jpg": (deck(PDM17, 82, "enlarged"), [
        (750, 440, 850, 620),           # Kerley B lines
        (250, 220, 650, 330),           # cephalization of the upper-lobe vessels
        (80, 430, 270, 560)]),          # pleural effusion
    "ecg-pulmonary-embolism.jpg": (deck(PDM16, 50, "enlarged"), []),  # the slide lists findings beside it, points to none
    "vq-scan-and-ct-angiogram.jpg": (deck(PDM17, 61), [
        (85, 355, 490, 745),            # B: perfusion
        (140, 820, 260, 935)]),         # C: the clot at the arrow
    "cxr-pleural-effusion.jpg": (deck(L44, 90, "enlarged"), [
        (60, 600, 260, 790),
        (690, 640, 890, 845)]),
    "cxr-pneumothorax.jpg": (deck(L44, 27), [
        (560, 90, 920, 320)]),          # the three arrows at the left apex
    "ct-pneumothorax.jpg": (deck(L44, 33, "reduced"), []),            # titled, but nothing in it is pointed to
    "cxr-hemopneumothorax.jpg": (deck(L44, 72), [
        (130, 870, 470, 990)]),        # the straight air-fluid line
}

NONE = "Nothing is boxed: "


def pic(file, test, title, shows, boxed):
    return dict(file=file, test=test, title=title, shows=shows, boxed=boxed)


def table(test, title, head, rows, hl, shows, boxed, cite):
    """A criteria table set out as its slide gives it; rows in hl are highlighted like a box."""
    return dict(table=dict(head=head, rows=rows, hl=hl), test=test, title=title, shows=shows,
                boxed=boxed, cite=cite)


# row -> its pictures (at most two), in the order its Tests column names them
PICS = {
    "Asthma": [
        pic("spirometry-normal-vs-asthma.png", "Spirometry",
            "Airflow limitation: a low forced expiratory volume in 1 second and a low ratio",
            "Normal (blue, dashed) against asthma (red). In the first second the asthma patient blows out "
            "2.2 L against the normal 3.5 L, so FEV1 (forced expiratory volume in 1 second) over FVC (forced "
            "vital capacity) is 61%; on the flow-volume loop the asthma peak flow is lower and the flow falls "
            "away much faster. A reduced FEV1 "
            "and FEV1/FVC ratio is airflow limitation; an FEV1 that improves 12% or more after a short-acting "
            "bronchodilator is what points to asthma (slide 53).",
            "Yellow boxes: the asthma curve at 1 second with its FEV1 and ratio; the flow-volume loops, normal "
            "against asthma."),
        pic("peak-flow-meter-and-normal-values.png", "Peak expiratory flow",
            "Peak flow: the patient's own number against the normal",
            "A: the hand-held peak flow meter. B: normal peak expiratory flow readings by age for men and "
            "women of three heights. Measured at home in the morning before the bronchodilator and in the "
            "afternoon after it; a 20% change between morning and afternoon, or from day to day, means poor "
            "control (slide 60).",
            NONE + "B is the chart of normal readings a patient's own number is compared with."),
    ],
    "Chronic obstructive pulmonary disease": [
        pic("spirometry-obstructive-copd.png", "Spirometry",
            "FEV1/FVC below 0.70",
            "Right: volume breathed out against time. The curve labeled FEV1 = 2.0 L and FVC = 3.9 L (light "
            "blue) reaches 2.0 L at 1 second and 3.9 L in all, so FEV1 (forced expiratory volume in 1 second) over FVC (forced "
            "vital capacity) is 0.51. Left: the flow-volume loop the same test draws. A post-bronchodilator "
            "FEV1/FVC below 0.70 confirms COPD (chronic obstructive pulmonary disease); an FEV1 improvement "
            "under 12% after the bronchodilator marks the obstruction as irreversible (slide 26).",
            "Yellow box: the 1-second volume, the total and the ratio of 0.51."),
        pic("cxr-copd-hyperinflation.jpg", "Chest X-ray",
            "Overinflated lungs and a flat diaphragm",
            "The film's own labels: a saber-sheath trachea, reticular markings, decreased lung markings and "
            "lucencies, a barrel-shaped chest (spelled barrow on the film) and diaphragmatic tenting. The "
            "chest X-ray does not diagnose COPD (chronic obstructive pulmonary disease), but it can show overinflated lungs with hyperlucent fields "
            "and a flattened diaphragm, and it rules out heart failure or pneumothorax (slide 31).",
            "Yellow boxes: the saber-sheath trachea; the low, tented diaphragm."),
    ],
    "Obstructive sleep apnea": [
        pic("stop-bang-questionnaire.png", "STOP-Bang screening questionnaire",
            "Five or more yes answers: high risk",
            "Eight yes-or-no questions: Snoring, Tired, Observed stopping breathing, high blood Pressure, "
            "BMI (body mass index) over 35, Age over 50, Neck size 16 inches (40 cm) or more, male Gender. "
            "Yes to 0 to 2 is low risk, 3 to 4 intermediate, 5 to 8 high; so is yes to 2 or more STOP "
            "questions plus male sex, a BMI over 35 or a large neck. It screens only: a polysomnogram "
            "confirms the diagnosis (slides 8-9).",
            "Yellow box: the scoring rule."),
    ],
    "Obesity hypoventilation syndrome": [
        table("Arterial blood gas and labs", "Awake carbon dioxide above 45 mmHg",
              ["What is measured", "What points to obesity hypoventilation syndrome"],
              [["PaCO2 (arterial carbon dioxide), awake", "Above 45 mmHg: awake alveolar hypoventilation"],
               ["Serum bicarbonate", "Above 27: a higher chance of the syndrome; obtain an arterial blood gas"],
               ["Body mass index", "Above 30"],
               ["Oxygen saturation", "94% or less awake without a reason, or a lowest overnight saturation under 80%"]],
              [0],
              "A diagnosis of exclusion: obesity, awake hypoventilation on the blood gas, and no other cause of "
              "the high carbon dioxide (slide 32). The saturation line is from the screening slide (slide 31).",
              "Highlighted: the blood gas finding that defines the syndrome.", "CMS L40 slides 31-32"),
    ],
    "Influenza": [
        pic("cxr-influenza-pneumonia.jpg", "Chest X-ray",
            "Influenza pneumonia: patchy infiltrates in several lobes",
            "A chest X-ray is usually obtained to rule out pneumonia, especially in elderly or high-risk "
            "patients with lung symptoms. The film sits beside the slide's description of influenza "
            "pneumonia: peribronchial and patchy interstitial infiltrates in multiple lobes with atelectasis "
            "(slide 106).",
            NONE + "the slide describes the pattern but does not point to it on the film."),
    ],
    "Acute bronchitis": [
        pic("cxr-normal.jpg", "Chest X-ray",
            "Expected: normal",
            "Routine chest radiography is unnecessary in uncomplicated acute bronchitis; a film is taken "
            "only when the vital signs, focal lung findings or risk raise concern for pneumonia (CMS L37 "
            "slide 15). In bronchitis it should look like this film, labeled Normal on its slide: clear "
            "lungs and sharp costophrenic angles. Consolidation means pneumonia instead (CMS L37 slide 16).",
            NONE + "a normal film."),
    ],
    "Community-acquired pneumonia": [
        pic("cxr-right-upper-lobe-consolidation.jpg", "Chest X-ray",
            "Lobar consolidation: a lobe turned white",
            "Chest radiography confirms suspected pneumonia (slide 29). This film's own label: right upper "
            "lobe consolidation in Klebsiella pneumonia, a homogeneous opacity of the right upper lobe with "
            "a bulging fissure (the red line on the second film) and no deviation of the trachea.",
            "Yellow boxes: the white right upper lobe; the bulging fissure on the second film."),
        pic("ct-consolidation.jpg", "CT (computed tomography)",
            "Consolidation on CT",
            "A chest CT follows the X-ray when the diagnosis is in doubt, the opacity is not homogeneous, "
            "atelectasis hides the lower lobes, the inflammation is severe or there is a cavity (CMS L37 "
            "slide 37). The slide labels the dense white areas of one lung consolidation, with arrows to "
            "panels a and c (PDM Imaging slide 79).",
            "Yellow boxes: the consolidation in panels a and c, where the slide's arrows point."),
    ],
    "Pulmonary tuberculosis": [
        pic("tuberculin-skin-test-reading.jpg", "Tuberculin skin test",
            "Read the induration, not the redness",
            "0.1 mL of PPD (purified protein derivative) is injected into the skin of the forearm and read at "
            "48 to 72 hours: measure the transverse induration in millimeters, never the erythema (slide 20). "
            "Positive at 5 mm or more (HIV (human immunodeficiency virus), recent close contact, immunosuppression), 10 mm or more (increased "
            "exposure or medical risk), 15 mm or more with no risk factor (slide 22). A positive test shows "
            "infection, not disease: chest imaging comes next (slide 19).",
            "Yellow box: the millimeter scale laid across the forearm."),
        pic("cxr-tuberculosis-bilateral.jpg", "Chest X-ray",
            "Bilateral abnormalities, possible cavitation",
            "The slide's example: arrows on abnormalities in both lungs, with possible cavitation "
            "(slide 31). Post-primary disease often involves the upper lobes and may cavitate (slide 28), "
            "but imaging cannot confirm tuberculosis: three sputum specimens for acid-fast smear, culture and "
            "a rapid molecular test do (slide 26).",
            "Yellow boxes: the abnormalities under the slide's two arrows."),
    ],
    "Idiopathic pulmonary fibrosis": [
        pic("hrct-honeycombing.jpg", "High-resolution CT (computed tomography)",
            "Patchy fibrosis with pleural-based honeycombing",
            "The scan on the slide titled idiopathic (fibrosing) interstitial pneumonia (slide 36). The "
            "finding slide 34 names for the high-resolution CT: diffuse patchy fibrosis with pleural-based "
            "honeycombing. Over 65, with no cause by history, inspiratory crackles and "
            "restriction, this CT makes the diagnosis without a lung biopsy (slide 35).",
            NONE + "the slide names the pattern but does not point into the scan."),
        pic("pft-restrictive-pattern.png", "Pulmonary function tests",
            "Restriction: small volumes, normal ratio",
            "Left: the restrictive curve (orange) levels off at a much lower FVC (forced vital capacity) than "
            "normal while its FEV1 (forced expiratory volume in 1 second) falls with it, so the ratio holds. "
            "Right: flow-volume loops, normal (green dotted), obstructive (red) and restrictive (blue, "
            "narrow). The restrictive pattern: a normal or increased FEV1/FVC ratio with a decreased TLC "
            "(total lung capacity) and FVC (slide 29).",
            "Yellow boxes: the restrictive curve's FEV1 at 1 second and its low FVC; the narrow restrictive "
            "(blue) loop, where it overlaps the normal loop."),
    ],
    "Sarcoidosis": [
        pic("cxr-hilar-adenopathy.jpg", "Chest X-ray",
            "Sarcoidosis: the slide's film and its arrows",
            "The slide's film, titled Chest X-ray: Sarcoidosis, with three arrows it does not label (slide "
            "28). Slide 44 lists the typical chest X-ray findings: symmetric bilateral hilar and right "
            "paratracheal adenopathy, with or without bilateral reticular infiltrates. A biopsy showing "
            "non-caseating granulomas confirms the diagnosis (slide 44).",
            "Yellow boxes: where the slide's three arrows point."),
        table("Chest X-ray staging", "The four chest X-ray stages",
              ["Stage", "Chest X-ray"],
              [["I", "Bilateral hilar adenopathy alone"],
               ["II", "Hilar adenopathy and parenchymal involvement"],
               ["III", "Parenchymal involvement alone (diffuse reticular infiltrates)"],
               ["IV", "Advanced fibrosis: honeycombing, hilar retraction, bullae, cysts, emphysema"]],
              [],
              "Biopsy is essential whenever the clinical and radiographic findings suggest another diagnosis "
              "such as lymphoma (slide 45).",
              "Nothing is highlighted: the slide gives the stages, not the stage of the film above.",
              "CMS L41 slide 45"),
    ],
    "Hypersensitivity pneumonitis": [
        pic("ct-hypersensitivity-pneumonitis.jpg", "CT (computed tomography)",
            "Chronic fibrotic changes",
            "The slide's CT: chronic fibrotic changes, small nodular densities or opacities (slide 70). "
            "Acute disease shows little change; subacute and chronic disease show fibrosis, with small "
            "nodular opacities that spare the apices and the bases (slide 69).",
            NONE + "the slide describes the scan but does not point into it."),
        pic("histology-granulomas.jpg", "Lung biopsy",
            "Non-caseating granulomas",
            "A lung biopsy may be indicated in subacute or chronic disease (slide 69). The slide's "
            "histology: interstitial infiltrates of lymphocytes and plasma cells, with non-caseating "
            "granulomas in the interstitium and air spaces (slide 70).",
            NONE + "the slide describes this section but does not point to the granulomas in it."),
    ],
    "Acute respiratory distress syndrome": [
        pic("cxr-ards.jpg", "Chest X-ray",
            "New bilateral opacities",
            "A chest X-ray of a patient with acute respiratory distress syndrome (the file's own description). "
            "The criteria the film is read against: new bilateral opacities not explained by effusion, "
            "atelectasis or nodules, within 7 days of a known insult, with failure not fully explained by "
            "heart failure or fluid overload (CMS L41 slide 73).",
            NONE + "the file names the diagnosis, not a place on the film."),
        table("Arterial blood gas: PaO2/FiO2", "Oxygenation sets the severity",
              ["Severity", "PaO2/FiO2 (arterial oxygen over the fraction of inspired oxygen)"],
              [["Mild", "200 to 300 mmHg"], ["Moderate", "100 to 200 mmHg"], ["Severe", "Under 100 mmHg"]],
              [],
              "The threshold is a PaO2/FiO2 under 300 mmHg, or an SaO2/FiO2 (oxygen saturation over the "
              "fraction of inspired oxygen) under 315, with marked hypoxemia that does not correct with "
              "supplemental oxygen (CMS L41 slide 73).",
              "Nothing is highlighted: the scale grades every patient.", "CMS L41 slide 73"),
    ],
    "Lung cancer": [
        pic("ct-lung-tumor.jpg", "CT (computed tomography)",
            "A peripheral mass with cavitation",
            "CT with contrast of the chest and upper abdomen, then biopsy, is the standard work-up of a "
            "suspicious nodule or symptoms (slide 14). The slide's CT of a large cell carcinoma: a tumor in "
            "the periphery with cavitation (slide 34). Nodules are concerning when over 6 mm, in the upper "
            "lobes, spiculated, enlarging, enhancing or cavitated (slide 16); histology confirms the type.",
            "Yellow box: the cavitating peripheral tumor."),
        pic("pet-ct-nodule.jpg", "PET-CT (positron emission tomography with computed tomography)",
            "High uptake suggests malignancy",
            "PET uses a radioactive sugar (fludeoxyglucose): highly metabolic cells take it up, suggesting "
            "the nodule may be malignant, while low or normal uptake is a good sign. Inflammation can take "
            "it up too, so a bright nodule is not proof (slide 17). The slide's four panels are not labeled: "
            "a round opacity in one sits where a bright focus shows in the others.",
            "Yellow boxes: the same spot in three panels, the round opacity and the bright focus."),
    ],
    "Pulmonary hypertension and cor pulmonale": [
        pic("ecg-right-ventricular-hypertrophy.jpg", "12-lead electrocardiogram",
            "Right ventricular hypertrophy",
            "The course's 12-lead titled RVH (right ventricular hypertrophy), with its slide's labels: right "
            "axis deviation (lead I mainly negative, aVF positive), an R wave bigger than the S wave in V1 "
            "and V2, the strain pattern in V1 and right atrial enlargement. The criteria: an R:S ratio of 1 "
            "or more in V1 and V2, supported by right atrial enlargement, right axis deviation and strain "
            "(PDM 14 slides 25, 33-34). In cor pulmonale: peaked P waves, a tall R in V1, right axis deviation "
            "(CMS L42 slide 14).",
            "Yellow boxes: lead I and aVF for the right axis; V1 and V2 for the tall R wave, the strain "
            "pattern and the P wave."),
    ],
    "Acute cardiogenic pulmonary edema": [
        pic("cxr-pulmonary-edema.jpg", "Chest X-ray",
            "Kerley B lines, cephalization, effusion, a big heart",
            "The slide's labeled film: Kerley B lines (short, thin horizontal lines from thickened "
            "interlobular septa), cephalization of the vessels, a pleural effusion and an increased "
            "cardiothoracic ratio (PDM Imaging slide 82). CMS L42 slide 37 adds batwing perihilar opacities "
            "and peribronchial cuffing.",
            "Yellow boxes: the Kerley B lines, the cephalized vessels and the effusion."),
    ],
    "Pulmonary embolism": [
        pic("ecg-pulmonary-embolism.jpg", "12-lead electrocardiogram",
            "Tachycardia and the S1Q3T3 pattern",
            "The tracing on the slide titled Pulmonary Embolism, which lists tachycardia from hypoxia, a "
            "rightward axis from a dilated right ventricle, ST and T wave changes, and the S1Q3T3 pattern "
            "(PDM 16 slide 50); the slide does not point to any lead. S1Q3T3 is a deep S in lead I with a Q wave and an inverted T wave in lead "
            "III; it is highly specific but insensitive, and suggests right ventricular strain rather than "
            "proving an embolism (CMS L42 slide 51).",
            NONE + "the slide lists the findings beside the tracing without pointing into it."),
        pic("vq-scan-and-ct-angiogram.jpg", "CT (computed tomography) pulmonary angiogram or V/Q (ventilation/perfusion) scan",
            "A clot on CT; a perfusion defect on V/Q",
            "The slide's three panels: A, a normal ventilation scan; B, decreased perfusion of the right "
            "lung; C, a contrast CT with the clot in the right main pulmonary artery at the arrow (PDM "
            "Imaging slide 61). CT pulmonary angiography is first-line; the V/Q (ventilation/perfusion) scan "
            "is for renal failure or contrast allergy, and a completely normal one excludes an embolism "
            "(CMS L42 slide 55).",
            "Yellow boxes: panel B, the missing perfusion; panel C, the clot at the arrow."),
    ],
    "Pleural effusion": [
        pic("cxr-pleural-effusion.jpg", "Chest X-ray",
            "Blunted costophrenic angles",
            "The slide's frontal film, with arrows at both costophrenic angles. On an upright film 75 mL of "
            "fluid blunts the posterior angle (seen on the lateral view) and 175 mL the lateral angle "
            "(slide 90).",
            "Yellow boxes: the two blunted angles, at the arrows."),
        table("Thoracentesis: Light's criteria", "Exudate if at least one is met",
              ["Light's criterion", "Exudate when"],
              [["Pleural fluid protein / serum protein", "More than 0.5"],
               ["Pleural fluid LDH / serum LDH (lactate dehydrogenase)", "More than 0.6"],
               ["Pleural fluid LDH", "More than two-thirds of the upper limit of normal serum LDH"]],
              [],
              "An exudate meets at least one criterion; a transudate meets none (slides 101, 110). The fluid "
              "is also sent for cell count, Gram stain, cytology and culture (slide 99).",
              "Nothing is highlighted: any one of the three makes it an exudate.", "CMS L44 slides 99, 101, 110"),
    ],
    "Pneumothorax": [
        pic("cxr-pneumothorax.jpg", "Chest X-ray",
            "Pneumothorax at the left apex",
            "The first test is an upright chest X-ray: the diagnosis is made by seeing the visceral pleural "
            "line, a thin, sharp line convex toward the chest wall, with no lung markings beyond it (slide "
            "26). This film is on the slide titled Pneumothorax: Chest X-Ray (slide 27); the slide's enlarged "
            "view of this apex labels its arrows apical subpleural blebs.",
            "Yellow box: the three arrows at the left apex."),
        pic("ct-pneumothorax.jpg", "CT (computed tomography)",
            "Air around a collapsed lung",
            "CT is the best test for the presence, size and location of the air and shows the blebs and "
            "bullae behind it, but it is impractical when time is critical (slide 33, titled Pneumothorax: "
            "CT). Tension pneumothorax is a clinical diagnosis: there is no time for imaging (slide 66).",
            NONE + "the slide titles the scan but points to nothing in it."),
    ],
    "Hemothorax": [
        pic("cxr-hemopneumothorax.jpg", "Chest X-ray",
            "A straight air-fluid line",
            "The slide's film of a hemopneumothorax (slide 72): a straight, horizontal line across the lower "
            "chest where air sits on top of blood, the straight line with no meniscus that slide 71's "
            "drawing labels.",
            "Yellow box: the straight air-fluid line."),
    ],
    "Pleurisy": [],
}

# Tests a row names that have no picture anywhere in the decks, said in plain words under its pictures.
NOPIC = {
    "Obstructive sleep apnea": "Polysomnography: the slides show no tracing.",
    "Obesity hypoventilation syndrome": "Polysomnography with continuous carbon dioxide monitoring: the slides show no tracing.",
    "Influenza": "Rapid molecular test: no picture on the slides.",
    "Hypersensitivity pneumonitis": "Pulmonary function: the restrictive pattern is pictured under idiopathic "
        "pulmonary fibrosis.",
    "Acute respiratory distress syndrome": "Echocardiogram: no picture on the slides.",
    "Pulmonary hypertension and cor pulmonale": "Echocardiogram and right heart catheterization: no picture on the "
        "slides (the echocardiogram on CMS L42 slide 14 is a drawing). The V/Q (ventilation/perfusion) scan is pictured under pulmonary embolism.",
    "Acute cardiogenic pulmonary edema": "B-type natriuretic peptide, echocardiogram and wedge pressure: no real "
        "tracing or scan on the slides (CMS L42 slide 38 has only an illustrated graph).",
    "Pleurisy": "The slides give pleurisy no test of its own: testing depends on the underlying condition "
        "(CMS L44 slide 14), so there is no picture.",
    "Hemothorax": "Chest tube output: no picture on the slides.",
}
