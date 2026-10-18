# -*- coding: utf-8 -*-
from _pd2_cardiac_osce_data import R
BATCH = {

"Chronic venous insufficiency and varicose veins": R(
  "routine",
  "CMS L26 Venous Disorders (Shah) &middot; slides 5&ndash;15, 27&ndash;44 &middot; PD2 Cardiovascular "
  "slides 85, 88, 90&ndash;95, 110&ndash;113",
  "Chronic venous disease runs from telangiectasias to varicose veins to chronic venous insufficiency "
  "(slide 5); <b>family history</b> is the most common "
  "predisposing factor for varicose veins (slide 39) and <b>prior deep vein thrombosis</b> one of the "
  "most common causes of insufficiency (slide 11).",
  "&ldquo;My legs feel heavy and achy by the end of a day on my feet, and my ankles swell &mdash; "
  "it&rsquo;s better when I put them up.&rdquo; Later: &ldquo;The skin around my ankle has gone brown "
  "and itchy, and now there&rsquo;s a sore that won&rsquo;t heal.&rdquo;",
  "<b>Pitting edema</b> of the lower leg; <b>brown hemosiderin staining</b> and itchy stasis dermatitis "
  "starting at the medial malleolus; shiny, taut skin and, with time, firm bound-down "
  "lipodermatosclerosis. Dilated, tortuous varicosities seen and felt <b>with the patient standing</b>, "
  "sometimes tender. A venous ulcer sits above the ankle (medial or anterior) with a clean, fibrinous "
  "base. <b>Temperature and pulses are normal</b>; so are the vitals.",
  "Inspect BOTH legs <b>standing</b> (dependent) for varicosities and compare sides. Press a thumb for "
  "at least 2 seconds over the dorsum of the foot, behind the medial malleolus and over the shin, then "
  "grade the pitting. Feel temperature with the back of the hand; palpate the dorsalis pedis and "
  "posterior tibial pulses and check capillary refill. <b>Ankle-brachial index</b> &mdash; done to rule "
  "OUT arterial disease before compression, not to make the diagnosis.",
  [("Peripheral artery disease", "Painful ulcer on the toes or lateral ankle, cool hairless skin, weak "
    "pulses and no edema &mdash; and compression must not be started"),
   ("Deep vein thrombosis", "Acute one-sided swelling with calf pain and warmth over days, not years; "
    "the duplex scan settles it"),
   ("Heart failure, kidney or liver disease", "Bilateral, symmetric leg edema without varicosities, "
    "staining or ulcer; look for the raised jugular venous pressure")],
  "<b>Venous duplex ultrasound</b> &rarr; valvular reflux (incompetence) with a patent deep system and "
  "no thrombus; for varicose veins it maps the reflux, usually in the great saphenous vein. "
  "<b>Ankle-brachial index</b> &rarr; normal, which clears the patient for compression. Catheter "
  "venography is the gold standard but is kept for planning an intervention.",
  "Thrombus on the duplex scan redirects to deep vein thrombosis; a low ankle-brachial index or weak "
  "pulses means arterial disease (no compression). Bilateral edema without reflux points to heart, "
  "kidney, liver or drug causes (calcium channel blockers, nonsteroidal anti-inflammatory drugs); a "
  "punch biopsy can help when the cause of an ulcer is uncertain.",
  "Nonoperative first: <b>leg elevation above heart level</b>, daily walking and ankle flexion, "
  "emollient skin care, and <b>graduated compression stockings once arterial disease is excluded</b>. "
  "Stasis dermatitis: barrier cream, then a mid-potency topical corticosteroid (triamcinolone); "
  "cellulitis: cephalexin or clindamycin; an ulcer needs compression plus wound-care referral. Varicose "
  "veins: weeks to months of stockings, then sclerotherapy, laser or radiofrequency ablation, or "
  "stripping. Vascular referral for a nonhealing or recurrent ulcer, arterial insufficiency, persistent "
  "dermatitis or significant saphenous reflux.",
  "ROUTINE &mdash; primary care clinic, vascular referral for a nonhealing or recurrent ulcer; sudden "
  "one-sided swelling is a deep vein thrombosis until proven otherwise.",
  "Wear the stockings <b>every day</b> &mdash; the swelling, and the ulcers, come back when they are not "
  "worn. Put your feet up above the level of your heart, walk daily, avoid long spells of sitting or "
  "standing, moisturize and do not scratch. Come back for a new sore, a hot red painful leg, or sudden "
  "swelling of one calf."),

"Deep vein thrombosis": R(
  "urgent",
  "CMS L26 Venous Disorders (Shah) &middot; slides 46&ndash;72 &middot; PD2 Cardiovascular slides "
  "87&ndash;88, 114",
  "Lower-extremity clots are 10 times more common than upper (slide 47), and <b>pulmonary embolism is "
  "the complication not to miss</b>: untreated, fatal embolism rises from under 1% with a clot alone to "
  "about 9% with a massive embolism (slide 60).",
  "&ldquo;My left calf has been swollen and sore since the long flight home &mdash; like a charley horse "
  "that keeps getting worse.&rdquo; After a hip or knee replacement: &ldquo;my whole leg has swelled "
  "up.&rdquo;",
  "<b>One-sided</b> calf or whole-leg swelling (swelling is 97% sensitive), warmth, erythema and "
  "<b>tenderness along the deep veins</b>; pitting edema confined to that leg; collateral (nonvaricose) "
  "superficial veins. Homans sign may be positive but is neither sensitive nor specific. Vitals are "
  "usually normal &mdash; <b>tachycardia, a fast respiratory rate or a low oxygen saturation raises "
  "pulmonary embolism</b>.",
  "Compare both legs and <b>measure calf circumference 10 centimeters below the tibial tuberosity</b> "
  "&mdash; more than 3 centimeters larger than the other side is a Wells point. Palpate along the deep "
  "venous system; check for pitting confined to the leg. Homans sign (knee bent, quick dorsiflexion; "
  "pain behind the knee) as a technique only &mdash; a negative does not reassure. Listen to the lungs "
  "and score the <b>Wells criteria</b> out loud.",
  [("Cellulitis", "Leg pain with spreading erythema plus fever and chills; the duplex scan shows no clot"),
   ("Ruptured popliteal (Baker) cyst", "Severe, sudden calf pain rather than a cramp that builds over days"),
   ("Superficial thrombophlebitis", "A tender, red, palpable cord along a superficial vein; the clot "
    "on duplex is in a superficial vein only")],
  "<b>Wells score</b> &rarr; 3 or more is high (skip the D-dimer, go straight to ultrasound); 0 or less "
  "is low. <b>D-dimer</b> &rarr; sensitive, not specific: positive sends you to ultrasound. <b>Venous "
  "duplex ultrasound</b> &rarr; thrombus in a noncompressible deep vein; a diagnostic scan ends the "
  "work-up and treatment starts. Contrast venography is the invasive gold standard, now replaced by duplex.",
  "Low Wells plus a <b>negative D-dimer</b> excludes it. High risk with a negative thigh scan: scan the "
  "lower leg, use phlebography, or repeat the thigh scan in 1 week; a nondiagnostic scan goes to "
  "magnetic resonance imaging or phlebography. A clot confined to a superficial vein is "
  "thrombophlebitis; fever with erythema and a clear scan is cellulitis.",
  "<b>Anticoagulation is the mainstay</b>: rivaroxaban or apixaban alone, or low molecular weight heparin "
  "or fondaparinux followed by dabigatran or edoxaban, or overlapped with warfarin. At least 3 months "
  "for a first clot (3 if provoked by a major transient factor, 3 to 6 if minor, indefinite if "
  "unprovoked). Outpatient if stable, low bleeding risk, normal kidneys and reliable; <b>admit</b> an "
  "iliofemoral clot, symptomatic pulmonary embolism, high bleeding risk or creatinine clearance under 30 "
  "milliliters per minute (unfractionated heparin). Inferior vena cava filter only when anticoagulation "
  "is contraindicated; thrombolysis or thrombectomy for selected large proximal clots.",
  "URGENT &mdash; same-day duplex ultrasound and anticoagulation; EMERGENT (emergency department, call "
  "911) if breathlessness, pleuritic chest pain, coughing blood or fainting suggest pulmonary embolism.",
  "Take the blood thinner <b>every day for the whole course</b> &mdash; at least three months; do not "
  "stop early. Watch for bleeding: black stools, blood in the urine, a severe headache. <b>Call 911 for "
  "sudden shortness of breath, chest pain, coughing blood or fainting.</b> On long trips get up and "
  "walk, and talk to us about estrogen pills, which raise clot risk."),

"Peripheral artery disease": R(
  "routine",
  "CMS L27 Arterial Occlusive Disease and Aneurysms (Carter) &middot; slides 9&ndash;53, 59&ndash;66 "
  "&middot; PD2 Cardiovascular slides 85&ndash;86, 90&ndash;91, 96&ndash;106, 110&ndash;113",
  "<b>50% of patients with peripheral artery disease also have coronary artery disease</b> (slide 10); "
  "smokers carry three times the risk (slide 11), and calf claudication is the most common pattern "
  "(slide 15).",
  "&ldquo;My calf cramps up after I walk a couple of blocks, and it goes away if I stand still for a few "
  "minutes &mdash; I can&rsquo;t get as far as I used to.&rdquo; Later: &ldquo;Now my toes ache at "
  "night unless I hang my foot over the side of the bed.&rdquo;",
  "<b>Diminished or absent pulses below the narrowing</b>, a cool limb (the temperature line roughly "
  "marks the level), slow capillary refill, and bruits over the aorta, iliac, femoral or popliteal "
  "arteries. Thin, shiny, hairless skin, brittle nails, muscle atrophy, <b>no edema</b>; <b>pallor on "
  "elevation and dependent rubor</b>. Dry, punched-out, painful ulcers at the toe tips or metatarsal "
  "heads mean critical ischemia. Vitals: blood pressure in both arms; xanthelasma or a sternotomy scar "
  "is a clue.",
  "Patient supine, warm and rested. <b>Palpate every pulse on both sides</b> &mdash; femoral, popliteal, "
  "posterior tibial, dorsalis pedis &mdash; and grade 0 to 4+; use a handheld Doppler if one cannot be "
  "felt. Listen for bruits; feel temperature with the back of the hand. <b>Buerger test</b>: raise the "
  "leg to 45 degrees for 1 minute (pallor), then dangle it (dependent rubor). <b>Ankle-brachial "
  "index</b>: the higher ankle pressure (dorsalis pedis or posterior tibial) over the higher arm "
  "systolic pressure, after 10 minutes supine.",
  [("Lumbar spinal stenosis", "Claudication-like pain with numbness and weakness, relieved by sitting or "
    "leaning forward rather than by standing still; pulses normal"),
   ("Chronic venous insufficiency", "Calf swelling and heaviness on standing, relieved by elevation; an "
    "edematous, brown-stained leg of normal temperature with normal pulses, and no pain at rest"),
   ("Peripheral neuropathy", "Continuous burning in the foot, unaffected by exercise; common with "
    "diabetes or alcohol use")],
  "<b>Ankle-brachial index</b> &rarr; under 0.90 suggests peripheral artery disease (both decks); 0.4 to "
  "0.9 is claudication and 0 to 0.4 rest pain or tissue loss (CMS); under 0.50 is severe (PD2). "
  "<b>Duplex ultrasound</b> &rarr; the site and degree of stenosis, the mainstay first image. Computed "
  "tomography angiography, magnetic resonance angiography or conventional angiography (the gold "
  "standard) when an intervention is planned. Baseline electrocardiogram, lipid profile, hemoglobin A1c "
  "and renal function.",
  "A normal ankle-brachial index with full pulses argues against it &mdash; but a value <b>above 1.3 "
  "(CMS) or 1.40 (PD2) is not normal</b>: calcified, noncompressible arteries, as in diabetes. Pain "
  "eased by sitting and leaning forward points to spinal stenosis; burning unaffected by walking to "
  "neuropathy; swelling with normal pulses to venous disease.",
  "<b>Risk-factor reduction</b>: stop smoking; control blood pressure, diabetes and weight; and a "
  "<b>supervised exercise program</b> (30 to 45 minutes, three times a week). Antiplatelet therapy "
  "(aspirin or clopidogrel) and cilostazol; a statin. Revascularization (angioplasty with or without a "
  "stent, atherectomy, bypass, endarterectomy) when claudication stays disabling despite exercise and "
  "drugs. Rest pain, a nonhealing ulcer or gangrene &rarr; vascular surgery.",
  "ROUTINE &mdash; clinic work-up and vascular referral; URGENT vascular surgery for rest pain, a "
  "nonhealing ulcer or gangrene (critical limb ischemia); EMERGENT for a sudden cold, pale, pulseless "
  "limb (acute limb ischemia) or wet gangrene.",
  "Smoking triples the risk &mdash; <b>stopping is the first treatment</b>. Walk until the pain comes, "
  "rest until it goes, and walk again, every day. Check your feet daily, wear well-fitting shoes and "
  "show us any sore. <b>Go to the emergency department for a suddenly cold, pale, numb or painful "
  "leg</b>; come back soon for pain at rest or at night, or a toe wound that will not heal."),

"Aortic dissection": R(
  "emergent",
  "CMS L27 Arterial Occlusive Disease and Aneurysms (Carter) &middot; slides 114&ndash;118 &middot; CMS "
  "L20 Hypertension (Jaquith) slides 5, 29, 42, 69 &middot; CMS L24 Coronary Artery Disease slides 28, "
  "31, 86 &middot; CMS L23 Valvular slide 28 &middot; CMS L31 Pericardial slides 13, 17, 22 &middot; "
  "PD2 Cardiovascular slide 59",
  "<b>Acute untreated dissection carries a high mortality</b> (L27 slide 118): the tear propagates, and "
  "pulse deficits, a new neurologic deficit and acute aortic regurgitation follow (L20 slide 29; L27 "
  "slide 116).",
  "&ldquo;It hit me all at once &mdash; a tearing, ripping pain in my chest that went straight through "
  "to my back, between my shoulder blades.&rdquo; Sometimes: &ldquo;&hellip;and then I passed "
  "out.&rdquo;",
  "Vitals: <b>hypertension</b> in most (or hypotension) and <b>unequal arm pressures</b>. <b>Pulse "
  "deficits</b>; a new high-pitched, blowing <b>diastolic murmur of aortic regurgitation</b> at the "
  "third left intercostal space; a new neurologic deficit; a patient in severe distress. <b>Normal "
  "pulses do not exclude it.</b>",
  "<b>Blood pressure in BOTH arms</b>, and compare. Palpate radial, femoral and pedal pulses on both "
  "sides for a deficit. Sit the patient forward, breath held after full expiration, and listen at the "
  "left sternal border for the aortic regurgitation murmur. A quick focused neurologic check &mdash; "
  "none of which may delay imaging.",
  [("Acute coronary syndrome", "Clenched-fist chest pressure (Levine sign) referred to the jaw or arm; "
    "ST changes and a rising troponin, whereas the dissection electrocardiogram may be normal"),
   ("Pulmonary embolism", "Sudden breathlessness with pleuritic pain and tachycardia in a patient with "
    "clot risk factors or a swollen leg; arm pressures equal"),
   ("Acute pericarditis", "Sharp pain worse lying flat and on inspiration, relieved by leaning forward; "
    "a friction rub and widespread ST elevation with PR depression")],
  "<b>Computed tomography angiography of the chest and abdomen</b> &rarr; an intimal tear with a false "
  "lumen, and its extent. <b>Transesophageal echocardiography</b> &rarr; the same tear and false lumen, "
  "plus aortic regurgitation. Magnetic resonance imaging is good but slow. Chest radiograph &rarr; "
  "possibly a <b>widened mediastinum</b>.",
  "Only a negative cross-sectional scan excludes it: <b>a normal chest radiograph, normal pulses or a "
  "normal electrocardiogram do not</b>. ST elevation in two or more leads with a rising troponin favors "
  "acute coronary syndrome; widespread concave ST elevation with a rub favors pericarditis; a clot on "
  "computed tomography pulmonary angiography means embolism.",
  "Intravenous access, continuous monitoring and <b>pain control</b>. Lower the systolic pressure to "
  "<b>100 to 120 millimeters of mercury</b> with an intravenous beta blocker (esmolol) or vasodilator "
  "(nitroprusside) &mdash; the slide lists them as alternatives; guidelines give the beta blocker first. "
  "Dissection is excluded from the gradual hypertensive-emergency targets. <b>Emergency cardiothoracic "
  "and vascular surgery</b>: grafting and replacing the diseased aorta.",
  "EMERGENT &mdash; emergency department now; call 911 for immediate computed tomography angiography "
  "and cardiothoracic surgery.",
  "In plain words: the wall of the main artery leaving the heart has torn, and it needs emergency "
  "treatment and probably surgery. Afterwards, <b>take the blood pressure medicine every day</b> and "
  "keep the pressure controlled for life. <b>Call 911 for any new tearing chest or back pain</b>, "
  "fainting, or weakness on one side."),

"Hypertrophic cardiomyopathy": R(
  "urgent",
  "CMS L28 Cardiomyopathy (Carter) &middot; slides 58&ndash;79, 82 &middot; CMS L23 Valvular slides 17, "
  "54 &middot; PD2 Cardiovascular slides 60&ndash;62, 66, 70 and the special maneuvers handout",
  "<b>Leading cause of sudden death in preadolescent and adolescent children</b> (slide 58), in 1 of "
  "every 500 people (slide 59); over 80% of those deaths are ventricular fibrillation, linked to extreme "
  "exertion (slide 66) &mdash; the murmur not to miss on a sports physical (PD2 slide 60).",
  "&ldquo;I blacked out in the middle of basketball practice &mdash; no warning.&rdquo; Or: &ldquo;I get "
  "short of breath and my chest hurts when I push hard, and I go lightheaded when I stand until I lie "
  "down. My brother has a thick heart muscle.&rdquo;",
  "Blood pressure and heart rate <b>usually normal</b>. <b>Pulsus bisferiens</b> (a double systolic "
  "peak); a forceful, sustained apical impulse, perhaps displaced laterally; an <b>S4</b>. A harsh "
  "<b>crescendo-decrescendo midsystolic murmur at the left sternal border, third to fourth intercostal "
  "space</b>, radiating down the sternal border but <b>not to the carotids</b>; often a holosystolic "
  "mitral regurgitation murmur at the apex radiating to the axilla.",
  "<b>Valsalva</b> (supine, bear down or push against your hand on the mid-abdomen) and <b>standing "
  "quickly from a squat</b> &rarr; the murmur gets LOUDER. <b>Squatting from standing, passive leg "
  "raise or sustained handgrip</b> &rarr; SOFTER. Listen over the carotids to confirm it does not "
  "radiate there; palpate the carotid for the bisferiens upstroke and the apex for a sustained impulse.",
  [("Aortic stenosis", "Older patient; murmur at the right upper sternal border radiating to the "
    "carotids, LOUDER with squatting and softer with Valsalva and standing &mdash; the opposite pattern"),
   ("Mitral valve prolapse", "A midsystolic click at the apex; its murmur moves with Valsalva and "
    "squatting just like hypertrophic cardiomyopathy, so the click is what separates them"),
   ("Innocent flow murmur", "Grade 1 to 3 of 6 and SOFTER on standing, sitting up or Valsalva; no "
    "syncope and no family history")],
  "<b>Echocardiogram</b> (test of choice) &rarr; unexplained left ventricular wall thickness of <b>1.5 "
  "centimeters or more</b>, asymmetric septal hypertrophy, a small cavity, and <b>systolic anterior "
  "motion of the mitral valve</b> in the obstructive form. <b>Electrocardiogram</b> &rarr; left "
  "ventricular hypertrophy, prominent Q waves in the inferior and lateral leads, left axis deviation. "
  "Cardiac magnetic resonance imaging if the echocardiogram is questionable; 24 to 48 hours of "
  "ambulatory electrocardiogram to gauge arrhythmia and sudden-death risk.",
  "Normal wall thickness on echocardiography excludes it, and hypertrophy explained by hypertension or "
  "aortic valve disease is secondary, not hypertrophic cardiomyopathy. A narrowed, calcified aortic "
  "valve confirms aortic stenosis; thickened, redundant mitral leaflets (over 5 millimeters) confirm "
  "prolapse; a structurally normal heart makes the murmur innocent.",
  "<b>Cardiology referral</b>. Outflow obstruction: a <b>beta blocker (metoprolol) first</b>, or "
  "verapamil or diltiazem. <b>Avoid nitrates and positive inotropes</b> (digoxin, epinephrine, "
  "norepinephrine); diuretics only with caution. Sudden-death prevention: an implantable "
  "cardioverter-defibrillator, with amiodarone or disopyramide (the slide credits amiodarone; guidelines "
  "credit only the defibrillator). Refractory obstruction: surgical myectomy or alcohol septal ablation.",
  "URGENT &mdash; cardiology and echocardiogram within days, with no competitive sport or strenuous "
  "exertion until cleared; a repeat faint, chest pain or racing heartbeat goes to the emergency "
  "department.",
  "Until the cardiologist clears you, <b>no competitive sports or hard exercise</b> &mdash; mild to "
  "moderate, noncompetitive activity only. <b>Stay well hydrated</b> and avoid excess alcohol. It is "
  "usually inherited, so your parents, brothers, sisters and children should be checked. Call 911 for "
  "fainting, chest pain or a racing heartbeat."),

}
