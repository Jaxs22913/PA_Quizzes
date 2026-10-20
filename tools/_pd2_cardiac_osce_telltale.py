"""The tell-tale sign for each Cardiac OSCE chart row (Jaxon, 2026-10-20: "put the tell tale sign that
tells you it is most likely this disease/disorder").

TELLTALE[name] = (sign, cite)
  sign  the one clue (or tight cluster) that makes this the most likely diagnosis, in plain words
  cite  the slide(s) it comes from, in the batches' shorthand (cite() in the builder spells out CMS / PD2)

Every sign is taken from a slide; slide numbers checked against the decks on 2026-10-20. The atrial
fibrillation ECG clue comes from the Principles of Diagnostic Medicine lecture 12 tracing (slide 34).
"""

PDM12 = "Principles of Diagnostic Medicine 12"
PDM13 = "Principles of Diagnostic Medicine 13"

TELLTALE = {
    "Primary hypertension": (
        "Readings of <b>130/80 or higher</b> on repeated measurement, confirmed outside the office, with "
        "<b>no acute organ injury</b>.",
        "CMS L20 slides 5, 7, 44"),
    "Hypertensive emergency": (
        "Severe pressure, often above 180/120, <b>PLUS new organ injury</b>: encephalopathy, pulmonary edema, acute "
        "kidney injury, dissection or acute coronary syndrome. The injury, not the number, makes it an emergency.",
        "CMS L20 slide 5"),
    "Vasovagal syncope": (
        "<b>A trigger</b> (fear, pain, heat, or standing for a long time) and then a faint, most often in a young woman.",
        "CMS L21 slide 14"),
    "Orthostatic hypotension": (
        "Lightheaded or faints <b>on standing up</b>, and the systolic pressure falls <b>more than 20</b> or the diastolic "
        "<b>more than 10</b> within 3 minutes of standing.",
        "CMS L21 slide 13"),
    "Chronic heart failure": (
        "<b>Orthopnea</b> (sleeps propped up) and breathlessness on exertion, with <b>leg edema</b> and an <b>S3</b>.",
        "CMS L25 slides 5, 26"),
    "Stable angina": (
        "Chest pressure <b>brought on by exertion and relieved by rest and nitroglycerin</b>, not changed by position; "
        "the patient shows a clenched fist over the sternum (Levine sign).",
        "CMS L24 slides 27, 28, 37"),
    "Acute coronary syndrome": (
        "Ischemic chest pain <b>at rest</b>, new, or getting worse, where stable angina is relieved by rest; the "
        "electrocardiogram and troponin then sort out which syndrome it is.",
        "CMS L24 slides 37, 45, 86"),
    "Aortic stenosis": (
        "A <b>harsh crescendo-decrescendo systolic murmur at the right second intercostal space, radiating to the "
        "carotids</b>, in an older patient with exertional angina, syncope or breathlessness.",
        "CMS L23 slides 16, 17"),
    "Mitral regurgitation": (
        "A <b>holosystolic, blowing murmur at the apex that radiates to the axilla</b>, best heard with the patient on "
        "the left side and louder with handgrip.",
        "CMS L23 slide 48"),
    "Mitral valve prolapse": (
        "A <b>mid-systolic click at the apex</b> in a healthy young woman (15 to 30).",
        "CMS L23 slide 54; PD2 slide 39"),
    "Chronic venous insufficiency and varicose veins": (
        "<b>Brown (hemosiderin) staining</b> and pitting edema around the ankle, in legs that ache on standing and feel "
        "better raised; the pulses are normal.",
        "CMS L26 slides 6, 7, 14; PD2 slide 93"),
    "Deep vein thrombosis": (
        "<b>One</b> swollen, painful, warm leg, often a calf cramp that keeps getting worse over a few days.",
        "CMS L26 slide 51"),
    "Peripheral artery disease": (
        "<b>Calf pain on walking that goes away with rest</b> (claudication), with weak pulses below the narrowing and an "
        "ankle-brachial index under 0.90.",
        "CMS L27 slides 15, 19; PD2 slides 91, 113"),
    "Aortic dissection": (
        "<b>Tearing or ripping</b> chest or back pain, worst at onset, with <b>unequal arm pressures</b> or a pulse deficit.",
        "CMS L20 slide 29; CMS L27 slide 116"),
    "Hypertrophic cardiomyopathy": (
        "A young person who <b>faints or nearly faints with exertion</b>, with a systolic murmur that gets "
        "<b>LOUDER with Valsalva or standing</b>.",
        "CMS L28 slides 65, 66; PD2 slides 61, 62"),
    "Atrial fibrillation": (
        "An <b>irregular pulse with no steady beat</b>; on the electrocardiogram, an irregular rhythm with no clear "
        "P waves.",
        PDM12 + " slides 32, 34"),
    "Premature ventricular contractions": (
        "Palpitations <b>felt in the neck</b>; on the electrocardiogram, an <b>early, wide</b> beat before the next "
        "expected one, its T wave pointing the opposite way.",
        "CMS L30 slide 36; " + PDM12 + " slide 70"),
    "Ventricular tachycardia": (
        "A <b>wide-complex tachycardia</b>, three or more ventricular beats in a row, usually in someone with heart "
        "disease. Check for a pulse first.",
        "CMS L30 slides 40, 42, 45; " + PDM13 + " slide 5"),
    "Acute pericarditis": (
        "<b>Sharp, pleuritic chest pain, better leaning forward</b> and worse lying flat, with a <b>friction rub</b>.",
        "CMS L31 slides 13, 17"),
    "Cardiac tamponade": (
        "<b>Beck triad</b> (low blood pressure, distended neck veins, muffled heart sounds) with <b>pulsus paradoxus</b>.",
        "CMS L31 slides 54, 59"),
}
