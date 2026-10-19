# -*- coding: utf-8 -*-
"""One real 12-lead electrocardiogram for every Cardiac OSCE chart row whose
work-up includes one (18 of the 20; chronic venous insufficiency and deep vein
thrombosis do not).

Jaxon, 2026-10-19: "find 12 lead EKG that match all the disease/disorders that
require you to get a EKG ... They need to be 100% accurate", then "Make sure
they are good EKGs that clearly show the EKG changes. Could we also put like a
highlight yellow box around the leads where the changes occur".

Rules every entry keeps:
- The picture is LABELLED by its source as the thing the caption says: a
  course slide titled with the finding, or a Wikimedia Commons file whose own
  description names it. Nothing is identified by eye alone.
- Where the condition has no electrocardiogram signature of its own (mitral
  valve prolapse, peripheral artery disease, the two kinds of syncope, aortic
  dissection) the row shows a normal tracing and says that normal is the
  expected finding, and what an abnormal one would mean instead.
- Where the source shows the PATTERN rather than a patient with the disease
  (mitral regurgitation, ischemia), the caption says so.
- Every claim in a caption is visible on that tracing or stated by its source
  (an independent reviewer checked each one on 2026-10-19).
- Course-deck pictures cite deck and slide; Commons pictures name author,
  licence and file page, all linked, and say what was changed (memory
  media_asset_licensing.md).

The yellow boxes are drawn INTO the picture (tools/box_pd2_cardiac_ecgs.py), so
they survive the click-to-enlarge view, the PDF and the Word copy. Box
coordinates are pixels on the shipped picture. The clean pictures live outside
the repo, in ~/Desktop/PA Quizzes/Semester 2/Physical Diagnosis 2 Inbox/
Cardiac OSCE ECGs (clean)/.
"""

def deck(name, slide):
    return {"kind": "deck", "deck": name, "slide": slide}


def commons(title, author, lic, licurl, extra=""):
    return {"kind": "commons", "title": title, "author": author, "lic": lic, "licurl": licurl,
            "extra": extra,
            "page": "https://commons.wikimedia.org/wiki/" + title.replace(" ", "_")}


PDM14 = "14. EKG Axis, BBB.pptx"
PDM15 = "15. EKG Ischemia and Infarction.pptx"
PDM16 = "16. EKG Pericarditis Electrolytes and Other Abnormalities.pptx"
BYSA3 = ("CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0")

# file -> (source, boxes as (x0, y0, x1, y1) on the shipped picture)
IMAGES = {
    "ecg-normal.jpg": (
        commons("File:Normal ECG from a 66-year old British male subject 2019.jpg",
                "Rodhullandemu", "Public domain", ""), []),
    "ecg-lvh-voltage.jpg": (deck(PDM14, 37), [
        (603, 40, 899, 485),            # V1-V3: deep S waves
        (904, 40, 1198, 485)]),         # V4-V6: tall R in V5, strain in V5-V6
    "ecg-ischemia-st-depression.jpg": (deck(PDM15, 9), [
        (28, 95, 298, 292),             # II, III
        (302, 190, 565, 292),           # aVF
        (842, 2, 1109, 292)]),          # V4-V6
    "ecg-atrial-fibrillation.jpg": (
        commons("File:ECG Atrial Fibrillation 90 bpm.jpg", "Ewingdo", "CC BY-SA 4.0",
                "https://creativecommons.org/licenses/by-sa/4.0"), [
        (30, 480, 1282, 575)]),         # lead II rhythm strip
    "ecg-pvc-bigeminy.jpg": (
        commons("File:Bigeminy.jpg", "James Heilman, MD", *BYSA3), [
        (5, 598, 1595, 795)]),          # rhythm strip
    "ecg-lvh-aortic-stenosis.jpg": (
        commons("File:Extreme lvh2 (CardioNetworks ECGpedia).jpg", "CardioNetworks", *BYSA3), [
        (812, 225, 1585, 725),          # V2-V4: huge complexes
        (812, 755, 1585, 1045)]),       # V5-V6: strain
    "ecg-pericarditis.jpg": (deck(PDM16, 6), [
        (3, 12, 249, 240),              # I, II
        (253, 45, 499, 115),            # aVR
        (503, 140, 748, 378),           # V2, V3
        (752, 25, 1000, 378)]),         # V4-V6
    "ecg-lvh-left-atrial.jpg": (
        commons("File:E307 (CardioNetworks ECGpedia).jpg", "Michael Rosengarten, MD", *BYSA3), [
        (812, 195, 1168, 305),          # V1: the P wave
        (812, 400, 1168, 795),          # V2, V3: deep S
        (1174, 10, 1535, 495)]),        # V4, V5: tall R
    "ecg-hypertrophic-cardiomyopathy.jpg": (
        commons("File:E242 (CardioNetworks ECGpedia).jpg", "Michael Rosengarten, MD", *BYSA3), [
        (190, 225, 490, 365),           # II: tall R
        (790, 95, 1092, 525),           # V1-V3
        (1098, 95, 1388, 525)]),        # V4-V6
    "ecg-stemi-anteroseptal.jpg": (deck(PDM15, 18), [
        (602, 15, 898, 485),            # V1-V3
        (902, 15, 1198, 135),           # V4
        (3, 395, 298, 490),             # III: reciprocal
        (302, 395, 598, 490)]),         # aVF: reciprocal
    "ecg-tamponade-alternans.jpg": (
        commons("File:PulsusAlternans (CardioNetworks ECHOpedia).png", "CardioNetworks (Vdbilt)",
                *BYSA3, extra="tracing courtesy of J.S.S.G. de Jong, AMC"), [
        (35, 15, 780, 370),             # limb leads: low voltage
        (790, 135, 1160, 370)]),        # V2, V3: alternans
    "ecg-ventricular-tachycardia.jpg": (
        commons("File:Electrocardiogram of Ventricular Tachycardia.png",
                "Karthik Sheka, MD (uploaded by Ksheka)", "CC BY-SA 2.5",
                "https://creativecommons.org/licenses/by-sa/2.5"), [
        (28, 478, 1086, 566)]),         # lead II rhythm strip
}

NORMAL_BOXED = "Nothing is boxed: every lead is normal."
LVH_BOXED = ("Yellow boxes: V1 to V3, the deep S waves (V2 measures 45 mm); V4 to V6, the tall R wave "
             "of V5 (40 mm), with the strain pattern, ST depression into an inverted T wave, in V5 and V6.")
ISCH_BOXED = "Yellow boxes: ST depression in II, III and aVF, and in V4 to V6."

ECGS = {
    "Primary hypertension": dict(
        file="ecg-lvh-voltage.jpg",
        title="Left ventricular hypertrophy by voltage",
        shows="The S wave in V2 (45 mm) plus the R wave in V5 (40 mm) adds up to 85 mm, well over "
              "the course's 35 mm cutoff. Years of high pressure thicken the left ventricle. Most "
              "patients with hypertension have a normal tracing, so a normal one does not rule out "
              "organ damage (specific, not sensitive).",
        boxed=LVH_BOXED),
    "Stable angina": dict(
        file="ecg-ischemia-st-depression.jpg",
        title="The pattern of ischemia: ST depression",
        shows="The course's picture of subendocardial ischemia: the ST segment sits below the "
              "baseline, measured at the J point, across many leads, with the mirror-image "
              "elevation in aVR. It shows the pattern, not a patient labelled with angina. In "
              "stable angina this appears during exertion or a stress test and settles with rest; "
              "the resting tracing is often normal.",
        boxed=ISCH_BOXED),
    "Peripheral artery disease": dict(
        file="ecg-normal.jpg",
        title="Expected: normal (a baseline tracing)",
        shows="Peripheral artery disease has no electrocardiogram pattern of its own; this is a "
              "normal tracing for comparison (sinus rhythm, normal intervals and axis). The "
              "baseline tracing looks for the coronary disease that so often comes with it: "
              "Q waves, ST depression or T-wave inversion.",
        boxed=NORMAL_BOXED),
    "Atrial fibrillation": dict(
        file="ecg-atrial-fibrillation.jpg",
        title="Rate controlled, at about 90 a minute",
        shows="Irregularly irregular narrow QRS complexes with no P waves and no PR interval: the "
              "gaps between beats never repeat. This 54-year-old man's ventricular rate is "
              "controlled, at about 90 a minute.",
        boxed="Yellow box: the lead II rhythm strip, where the uneven spacing and the missing P "
              "waves are easiest to see."),
    "Chronic heart failure": dict(
        file="ecg-lvh-voltage.jpg",
        title="Left ventricular hypertrophy",
        shows="Deep S waves in V1 to V3 and a tall R wave in V5, adding up to 85 mm against a 35 mm "
              "cutoff (the same course tracing as primary hypertension). In heart failure the "
              "tracing looks for the cause: hypertrophy, as here, or ischemic changes.",
        boxed=LVH_BOXED),
    "Premature ventricular contractions": dict(
        file="ecg-pvc-bigeminy.jpg",
        title="Bigeminy: every other beat is premature",
        shows="Every other beat comes early, wide and bizarre, with its T wave pointing the "
              "opposite way, and each one alternates with a narrow normal beat. A premature "
              "ventricular beat has no P wave of its own. Every third beat would be trigeminy.",
        boxed="Yellow box: the rhythm strip along the bottom: narrow beat, wide early beat, narrow "
              "beat, wide early beat."),
    "Vasovagal syncope": dict(
        file="ecg-normal.jpg",
        title="Expected: normal",
        shows="A normal tracing between episodes is what you expect, and it is the point of "
              "getting one. Heart block, a long QT interval, pre-excitation or a hypertrophy "
              "pattern would make the faint cardiogenic instead.",
        boxed=NORMAL_BOXED),
    "Aortic stenosis": dict(
        file="ecg-lvh-aortic-stenosis.jpg",
        title="Extreme left ventricular hypertrophy from severe stenosis",
        shows="Very large QRS voltages, and the strain pattern in the lateral leads: ST depression "
              "and inverted T waves in V5 and V6. The ventricle thickened against the narrowed "
              "valve. A tracing this extreme usually means severe, long-standing disease; many "
              "patients with severe stenosis have a less striking tracing, so it is insensitive.",
        boxed="Yellow boxes: V2 to V4, the huge QRS complexes; V5 and V6, the strain pattern."),
    "Acute pericarditis": dict(
        file="ecg-pericarditis.jpg",
        title="Diffuse ST elevation with PR depression",
        shows="Concave (smiling) ST elevation across many leads with the PR segment pushed below "
              "the baseline, and the mirror image in aVR: PR elevation with ST depression. No "
              "regional pattern, which is what separates it from an infarction.",
        boxed="Yellow boxes: ST elevation with PR depression in I and II; PR elevation with ST "
              "depression in aVR; concave ST elevation across V2 to V6."),
    "Mitral regurgitation": dict(
        file="ecg-lvh-left-atrial.jpg",
        title="The pattern: left ventricular hypertrophy with left atrial enlargement",
        shows="Large QRS voltages (left ventricular hypertrophy), and a P wave in V1 with a "
              "prominent negative second half (left atrial enlargement). Severe mitral "
              "regurgitation can produce this pattern; the source illustrates the pattern and does "
              "not name this patient's disease. Atrial fibrillation is the other finding to look for.",
        boxed="Yellow boxes: V1, the P wave's negative second half; V2 and V3, the deep S waves; "
              "V4 and V5, the tall R waves."),
    "Mitral valve prolapse": dict(
        file="ecg-normal.jpg",
        title="Expected: usually normal",
        shows="Most patients with mitral valve prolapse have a normal tracing like this one. The "
              "tracing is ordered for the palpitations, to catch an arrhythmia such as premature "
              "beats.",
        boxed=NORMAL_BOXED),
    "Orthostatic hypotension": dict(
        file="ecg-normal.jpg",
        title="Expected: normal",
        shows="Orthostatic hypotension is diagnosed by the lying and standing pressures, not the "
              "tracing; a normal one like this is the expected finding. An arrhythmia, heart "
              "block or a long QT interval would send you to cardiogenic syncope instead.",
        boxed=NORMAL_BOXED),
    "Hypertrophic cardiomyopathy": dict(
        file="ecg-hypertrophic-cardiomyopathy.jpg",
        title="A woman with the obstructive form",
        shows="Left ventricular hypertrophy by voltage (R wave in V5 and S wave in V2 each over "
              "30 mm, R wave in II over 20 mm) with diffuse ST and T-wave changes, and a P wave "
              "ending negative in V1 (left atrial abnormality). Deep, narrow Q waves in the "
              "inferior and lateral leads are a classic further clue; this tracing does not show "
              "them, and not every patient has them.",
        boxed="Yellow boxes: II, the tall R wave; V1 to V3, the negative end of the V1 P wave and "
              "the deep S wave of V2; V4 to V6, the tall R wave of V5 and the ST and T-wave changes."),
    "Acute coronary syndrome": dict(
        file="ecg-stemi-anteroseptal.jpg",
        title="Anteroseptal ST-elevation myocardial infarction",
        shows="ST elevation in V1, V2 and V3, contiguous leads facing the septal and anterior walls "
              "(the course slide's label); on this tracing it carries on into V4, with reciprocal "
              "ST depression in III and aVF. Elevation in two or more contiguous leads means "
              "reperfusion now, without waiting for troponin. The course threshold is over 1 mm; "
              "current guidelines set V2 and V3 higher (2 mm in men 40 and over, 2.5 mm in younger "
              "men, 1.5 mm in women).",
        boxed="Yellow boxes: ST elevation in V1 to V3 and V4; reciprocal ST depression in III and aVF."),
    "Aortic dissection": dict(
        file="ecg-normal.jpg",
        title="Often normal, and normal does not rule it out",
        shows="The tracing in a dissection is often normal or shows only nonspecific changes. "
              "Its job is to look for an infarction; a normal one must never reassure you about "
              "tearing pain that radiates to the back.",
        boxed=NORMAL_BOXED),
    "Cardiac tamponade": dict(
        file="ecg-tamponade-alternans.jpg",
        title="Low voltage and electrical alternans",
        shows="A 40-year-old man with multiple myeloma and tamponade: tiny QRS complexes in the "
              "limb leads, and in the chest leads the QRS height alternates beat to beat as the "
              "heart swings in the fluid (electrical alternans).",
        boxed="Yellow boxes: the limb leads, low voltage; V2 and V3, tall and short QRS complexes "
              "taking turns."),
    "Ventricular tachycardia": dict(
        file="ecg-ventricular-tachycardia.jpg",
        title="Monomorphic: every beat the same shape",
        shows="A fast, regular, wide-complex rhythm (QRS over 0.12 seconds), every beat the same "
              "shape. Treat a wide, regular tachycardia as ventricular until proven otherwise.",
        boxed="Yellow box: the lead II rhythm strip, every beat wide and identical."),
    "Hypertensive emergency": dict(
        file="ecg-ischemia-st-depression.jpg",
        title="What myocardial ischemia looks like",
        shows="The course's picture of subendocardial ischemia, widespread ST depression; it shows "
              "the pattern, not a patient with a hypertensive emergency. Here the tracing, with "
              "troponin, asks whether the heart is a damaged organ: ischemia or infarction. Left "
              "ventricular hypertrophy from long-standing pressure is common too.",
        boxed=ISCH_BOXED),
}
