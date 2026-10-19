# -*- coding: utf-8 -*-
from _pd2_cardiac_osce_data import R
BATCH = {

"Primary hypertension": R(
  "routine",
  "CMS L20 Hypertension (Jaquith) &middot; slides 4, 7, 10, 12, 20, 26, 31, 37&ndash;41, 45, 46, 48, 50, "
  "51, 53, 55&ndash;57, 61, 65, 66, 72 &middot; PD2 Cardiovascular slides 20, 23, 42, 102, 106",
  "The vast majority of adult hypertension is primary (slide 10); 47.7% of adults have hypertension and only "
  "20.7% are controlled (slide 7).",
  "&ldquo;The machine at the pharmacy said 152 over 94, but I feel completely fine.&rdquo; Sometimes: "
  "&ldquo;I&rsquo;ve been getting headaches &mdash; is it my pressure?&rdquo;",
  "Vitals form: <b>&ge;130/80 is hypertension</b> &mdash; stage 1 is 130&ndash;139/80&ndash;89, stage 2 "
  "&ge;140/&ge;90; use the higher category when the two numbers disagree. Usually <b>a normal "
  "examination</b>. With long-standing disease: a <b>sustained, forceful but non-displaced apical "
  "impulse</b> and an <b>S4</b> (left ventricular hypertrophy), and arteriolar narrowing or arteriovenous "
  "nicking on fundoscopy.",
  "Re-measure properly: <b>seated after 5 minutes&rsquo; rest</b>, back supported, feet flat, bare arm at "
  "heart level, correct cuff, at least two readings, and <b>both arms</b> at the first visit; standing "
  "pressure in older adults or anyone on medication. Palpate <b>radial and femoral pulses together</b> for "
  "delay (coarctation) and auscultate for a renal bruit. <b>Fundoscopy</b>; palpate the apical impulse and "
  "listen with the bell at the apex in left lateral decubitus for an S4.",
  [("White coat hypertension", "High in the office but a normal home average; needs surveillance, not drugs"),
   ("Secondary hypertension", "Early or abrupt onset, resistance to three drugs, unexplained low potassium, "
                              "snoring with witnessed apneas, or radial-femoral delay"),
   ("Hypertensive emergency", "The same high numbers PLUS acute organ injury &mdash; confusion, vision change, "
                              "chest or back pain, dyspnea, oliguria")],
  "<b>Home blood pressure monitoring</b> &rarr; two readings a minute apart, morning and evening, for 7 days; "
  "a raised average confirms it. <b>Baseline panel</b> (comprehensive metabolic panel, estimated glomerular "
  "filtration rate, urine albumin-to-creatinine ratio, urinalysis, complete blood count, glucose or glycated "
  "hemoglobin, lipids, thyroid-stimulating hormone) &rarr; organ damage and secondary clues. <b>12-lead "
  "electrocardiogram</b> &rarr; left ventricular hypertrophy voltage (specific, not sensitive).",
  "A <b>normal home average</b> with high office readings is white coat hypertension. A secondary clue "
  "triggers its test: <b>aldosterone-to-renin ratio</b> (resistance, low potassium), <b>renal duplex "
  "ultrasound</b> (abrupt onset, bruit, flash pulmonary edema), <b>sleep study</b> (snoring, apneas), "
  "<b>plasma metanephrines</b> (paroxysms of headache, sweating, palpitations). Any acute organ-injury "
  "symptom moves the patient to the emergency row.",
  "<b>Lifestyle for everyone</b>: a Dietary Approaches to Stop Hypertension eating pattern, sodium under "
  "2,300 mg a day, 150 minutes a week of aerobic exercise plus resistance training, weight loss, limited "
  "alcohol, no smoking. Goal <b>below 130/80</b>. Stage 1: one first-line drug if cardiovascular disease, "
  "diabetes, chronic kidney disease or a 10-year risk &ge;7.5%; stage 2: <b>two complementary first-line "
  "drugs</b>, ideally in one pill &mdash; a thiazide-type diuretic (chlorthalidone preferred), an "
  "angiotensin-converting enzyme inhibitor (lisinopril) or angiotensin receptor blocker (losartan), never both, or a dihydropyridine "
  "calcium channel blocker (amlodipine).",
  "ROUTINE &mdash; primary care clinic; confirm with a week of home readings, recheck about 4 weeks after "
  "starting drugs; hypertension specialist only if truly resistant.",
  "<b>Feeling well does not mean it is controlled</b> &mdash; most people have no symptoms, and headache is "
  "not a gauge. Take the pills every day (missed doses are the commonest reason pressure stays high), keep a "
  "home log and don&rsquo;t react to one high reading. Avoid anti-inflammatory painkillers and decongestants, "
  "which raise pressure. Emergency department for a sudden severe headache, confusion, vision change, "
  "weakness, chest or back pain, or breathlessness."),

"Hypertensive emergency": R(
  "emergent",
  "CMS L20 Hypertension (Jaquith) &middot; slides 5, 20, 27, 29, 37, 39, 40, 42, 44, 49, 59, 69, 75, 76 "
  "&middot; CMS L27 Arterial Occlusive Disease and Aneurysm (Carter) &middot; slides 116, 118 &middot; PD2 "
  "Cardiovascular slides 40, 77, 86, 102 &middot; Pharm ANS Pharmacology slide 122 &middot; Pharm Diuretics slide 12",
  "Lethal through acute organ injury &mdash; encephalopathy, pulmonary edema, acute kidney injury, aortic "
  "dissection, acute coronary syndrome &mdash; and lowering the pressure too fast itself causes stroke, "
  "myocardial injury or renal failure (slides 5, 69).",
  "&ldquo;I have a sudden, pounding headache and my vision is blurry &mdash; my home machine read 230 over "
  "130.&rdquo; Or: &ldquo;I can&rsquo;t breathe lying down, and I ran out of my pressure pills last "
  "week.&rdquo;",
  "Vitals form: <b>severe elevation, often above 180 systolic and/or 120 diastolic</b> &mdash; but the "
  "organ injury, not the number, defines it, and lower values with injury qualify. Look for confusion or a "
  "focal deficit, <b>optic disc edema</b> on fundoscopy, hypoxemia with <b>diffuse bilateral crackles</b> "
  "(pulmonary edema), and a pulse deficit, unequal arm pressures or a new aortic regurgitation murmur "
  "(dissection).",
  "Repeat the pressure in <b>both arms</b> and palpate radial, femoral and distal pulses for a deficit or "
  "delay. <b>Fundoscopy</b> for disc edema and a focused <b>neurologic examination</b> (mental status, "
  "speech, strength, visual fields). Auscultate the lung bases for crackles and the heart for an S3, and for "
  "an early diastolic aortic regurgitation murmur with the patient sitting, leaning forward, breath held "
  "after exhalation.",
  [("Severe hypertension without acute organ injury", "The same numbers in a well patient with a normal "
     "neurologic, fundal and lung examination &mdash; not an emergency (the old term was hypertensive urgency)"),
   ("Aortic dissection", "Tearing chest or back pain maximal at onset, a pulse deficit or unequal arm "
                         "pressures; the systolic target is 100&ndash;120, not the gradual 20&ndash;25% rule"),
   ("Acute stroke", "A sudden focal deficit; imaging decides, and stroke follows its own blood pressure "
                    "protocol rather than the emergency targets")],
  "Organ injury, not the number, makes the diagnosis &mdash; do not wait for repeat visits. "
  "<b>Electrocardiogram and troponin</b> &rarr; ischemia or myocardial injury; <b>B-type natriuretic "
  "peptide</b> &rarr; heart failure. <b>Creatinine and urinalysis</b> &rarr; acute kidney injury (rising "
  "creatinine, casts, hematuria). <b>Chest radiograph</b> &rarr; pulmonary edema or a widened mediastinum; "
  "<b>head computed tomography or magnetic resonance imaging</b> &rarr; encephalopathy, stroke or hemorrhage.",
  "No acute organ injury on history, examination and tests means severe hypertension, not an emergency "
  "&mdash; so no rapid intravenous lowering. A normal chest radiograph and normal pulses do NOT exclude "
  "dissection; <b>computed tomography angiography</b> does. A focal deficit with an infarct or bleed on "
  "imaging is a stroke and follows its own protocol.",
  "<b>Airway, breathing, circulation</b>; intravenous access, continuous cardiac monitoring, an arterial "
  "line, and a <b>titratable intravenous drug matched to the organ syndrome</b> (for example labetalol). Lower mean arterial pressure "
  "<b>no more than 20&ndash;25% in the first hour</b>, toward about 160/100&ndash;110 over 2&ndash;6 hours, "
  "then normal over 24&ndash;48 hours (dissection and some strokes excepted). Pulmonary edema: intravenous "
  "nitroglycerin or nitroprusside, oxygen, continuous or bilevel positive airway pressure, and a loop "
  "diuretic (furosemide) if overloaded.",
  "EMERGENT &mdash; emergency department now; call 911; continuous monitoring with titratable intravenous "
  "therapy.",
  "Once stable: take the pressure pills every day and <b>never stop them suddenly</b> &mdash; clonidine in "
  "particular rebounds. Avoid cocaine, stimulants, decongestants, heavy drinking and sudden alcohol "
  "withdrawal. Keep a home log and come to every follow-up. Call 911 for a sudden severe headache, "
  "confusion, vision change, weakness, chest or back pain, or breathlessness."),

"Vasovagal syncope": R(
  "routine",
  "CMS L21 Hypotension (Carter) &middot; slides 9, 13&ndash;17, 23, 27, 37, 40 &middot; PD2 "
  "Cardiovascular slides 9, 60&ndash;62, 70",
  "The most common type of syncope, &ldquo;the common faint&rdquo;, most often in young women (L21 slide "
  "14; PD2 slide 9).",
  "&ldquo;I was getting my blood drawn and suddenly felt hot, sick to my stomach and sweaty, then everything "
  "went gray. My friend said I was out for a few seconds, and I felt fine right after.&rdquo;",
  "Usually <b>normal vitals and a normal examination afterward</b>, with normal standing readings. If seen "
  "during the episode: pale, clammy and diaphoretic, with <b>bradycardia and a falling pressure</b> (the "
  "reflex). No tongue bite, no focal deficit, no murmur.",
  "<b>Orthostatic vital signs</b> (supine, then standing within 3 minutes) to exclude orthostatic "
  "hypotension. Auscultate for an outflow murmur and repeat with <b>Valsalva and squat-to-stand</b> &mdash; "
  "a hypertrophic cardiomyopathy murmur gets louder, the cardiogenic faint you must not miss in a young "
  "patient. Inspect the tongue and do a focused neurologic examination.",
  [("Orthostatic hypotension", "Faints on standing up, with a positive orthostatic pressure fall rather than "
                               "an emotional or pain trigger"),
   ("Cardiogenic syncope", "Collapse without warning or during exertion, often after a racing heartbeat, in "
                           "someone with heart disease; abnormal electrocardiogram"),
   ("Seizure", "Tonic-clonic activity, tongue biting, incontinence and prolonged postictal confusion instead "
               "of rapid full recovery")],
  "<b>The history</b> &rarr; a trigger, a warm, nauseated, sweaty prodrome and rapid full recovery "
  "(&ldquo;history, history, history&rdquo;; a symptom log shows the pattern). <b>Electrocardiogram</b> "
  "&rarr; normal, lowering suspicion of an arrhythmia. <b>Fingerstick glucose</b> &rarr; normal, excluding "
  "hypoglycemia. <b>Tilt-table test</b>, only if recurrent and unclear &rarr; reproduces the prodrome with a "
  "fall in pressure and heart rate.",
  "Positive orthostatic vital signs redirect to orthostatic hypotension. A faint without warning, during "
  "exertion or with palpitations, an abnormal electrocardiogram or a murmur sends you to cardiogenic syncope "
  "(monitor, echocardiogram, cardiology). Tongue biting, tonic-clonic activity or postictal confusion point "
  "to seizure.",
  "<b>Trigger avoidance</b>, and <b>safety precautions</b> when a trigger cannot be avoided (lie down for "
  "blood draws and injections). Education is the treatment: &ldquo;understanding is the key to "
  "compliance.&rdquo; Fluids and physical counter-pressure maneuvers (crossing the legs, tensing the arms) "
  "at the first warning. Refer to cardiology only if the history leaves the source unclear.",
  "ROUTINE &mdash; clinic; no emergency workup once the history is classic and the electrocardiogram is "
  "normal; cardiology referral if unclear.",
  "<b>&ldquo;If you feel faint, sit or lie down wherever you are&rdquo;</b> &mdash; at the first warmth or "
  "nausea. Keep a log of each episode (setting, trigger, warning) and bring it back. Tell staff before blood "
  "draws so you can lie down. Return at once for a faint with no warning, during exercise, with chest pain "
  "or a racing heart, or with an injury."),

"Orthostatic hypotension": R(
  "routine",
  "CMS L21 Hypotension (Carter) &middot; slides 9, 11&ndash;13, 16, 18, 23, 25, 28&ndash;36 &middot; CMS "
  "L20 Hypertension (Jaquith) slides 39, 59 &middot; PD2 Cardiovascular slides 9, 85",
  "Orthostatic syncope is one of the three most common causes of syncope (L21 slide 9); standing pressure "
  "is checked routinely in older adults and anyone on antihypertensives or diabetes drugs (L20 slide 39).",
  "&ldquo;When I get out of bed or stand up fast, I get lightheaded and my vision goes dim &mdash; this "
  "morning I actually passed out.&rdquo; Often: &ldquo;I&rsquo;ve had diarrhea for days&rdquo; or "
  "&ldquo;they just raised my water pill.&rdquo;",
  "Vitals form: the supine-to-standing set is the finding &mdash; <b>systolic falls more than 20 or "
  "diastolic more than 10 within 3 minutes</b>. The <b>heart rate decides the type</b>: a brisk rise "
  "(68 &rarr; 92) is non-neurogenic, with <b>dry mucous membranes</b>; a minimal rise (72 &rarr; 76) is "
  "neurogenic, with moist membranes and often <b>reduced vibration and light touch in the feet</b>. The "
  "cardiac examination is normal.",
  "<b>Orthostatic vital signs</b>: pressure and heart rate supine, then standing, read within 3 minutes. "
  "Mucous membranes and capillary refill for volume; a cardiac examination for rhythm and murmurs; a "
  "<b>neurologic examination with vibration and light touch in the feet</b> for diabetic or autonomic "
  "neuropathy.",
  [("Vasovagal syncope", "A trigger (fear, pain, heat, long standing) and a warm, nauseated, sweaty prodrome, "
                         "with normal orthostatic vital signs"),
   ("Postural orthostatic tachycardia syndrome", "Heart rate rises more than 30 within 10 minutes of standing "
                                                 "WITHOUT a fall in pressure; young women"),
   ("Cardiogenic syncope", "Collapse without warning, often after a racing heartbeat, in someone with heart "
                           "disease; abnormal electrocardiogram")],
  "<b>Orthostatic vital signs</b> &rarr; systolic fall over 20 or diastolic over 10 within 3 minutes of "
  "standing (systolic over 30 with a high baseline or supine hypertension); one criterion is enough. "
  "<b>Heart rate response</b> &rarr; a significant rise means non-neurogenic (volume, drugs), a minimal rise "
  "means neurogenic (autonomic failure). <b>Complete blood count and metabolic panel</b> &rarr; blood loss, "
  "dehydration or an electrolyte cause; <b>electrocardiogram</b> &rarr; normal sinus rhythm lowers cardiac "
  "suspicion.",
  "Normal orthostatic vital signs exclude it &mdash; go back to the history for a reflex trigger. A heart "
  "rate rise without a pressure fall is postural orthostatic tachycardia syndrome (tilt-table test). An "
  "abrupt faint without prodrome, or an abnormal electrocardiogram, sends you to cardiogenic syncope: "
  "monitor, echocardiogram, cardiology.",
  "<b>Slow position changes</b> and <b>treat the real diagnosis</b>: replace volume after diarrhea or "
  "bleeding; <b>reduce or stop the offending drug</b> (diuretic, alpha-1 blocker such as tamsulosin or "
  "doxazosin, other antihypertensives). Compression stockings help venous pooling. Neurogenic: "
  "<b>midodrine</b> is best, avoided with supine hypertension, severe heart disease or chronic kidney "
  "disease; refer to the right specialty (neurology for autonomic failure) when the source is unclear.",
  "ROUTINE &mdash; clinic; adjust medicines, rehydrate and recheck orthostatic vital signs at follow-up; "
  "emergency department instead if the cause is bleeding.",
  "<b>Change position in stages</b>: sit on the edge of the bed, then stand, and sit straight back down at "
  "the first lightheadedness. Keep up fluids when sick with diarrhea or vomiting, and call before changing "
  "your own medicines &mdash; understanding why the pressure falls is what makes the advice work. Come back "
  "at once for black or bloody stools, fainting while sitting or lying, chest pain or a racing heart."),

"Chronic heart failure": R(
  "routine",
  "CMS L25 Heart Failure (Carter) &middot; slides 5, 6, 8&ndash;10, 18, 24, 26, 29, 30, 32&ndash;34, "
  "38&ndash;40, 52&ndash;54, 56 &middot; CMS L20 Hypertension slides 20, 57 &middot; CMS L26 Venous "
  "Disorders (Shah) slides 14, 26&ndash;29 &middot; PD2 Cardiovascular slides 7, 8, 20, 23, 40, 42, 88, 89 &middot; Pharm Antihypertensives slide 70",
  "6.7 million Americans have heart failure, lifetime risk is 1 in 4, and it causes 45% of cardiovascular "
  "deaths (slide 6); left-sided failure is the most common by far, 70&ndash;80% (slide 8).",
  "&ldquo;I get winded walking to the mailbox, I sleep on three pillows, and my shoes are tight by "
  "evening.&rdquo; Sometimes: &ldquo;I wake up at night gasping and have to sit up.&rdquo;",
  "Vitals: <b>normal or low pressure with a reduced ejection fraction, hypertension with a preserved "
  "one</b>; a narrow pulse pressure and cool extremities warn of low output. <b>Raised jugular venous "
  "pressure</b>, bilateral <b>pitting edema</b> and hepatomegaly. A <b>displaced, diffuse apical impulse "
  "with an S3</b> (dilated ventricle), or a sustained impulse with an <b>S4</b> (stiff, hypertrophied "
  "ventricle). <b>Crackles are rare when compensated</b> &mdash; finding them suggests decompensation.",
  "Head of the bed at 30&ndash;45 degrees to measure the <b>jugular venous pressure</b>, then "
  "<b>hepatojugular reflux</b> (firm pressure over the liver &rarr; a sustained rise in the neck veins). "
  "Turn to <b>left lateral decubitus, bell at the apex</b> for an S3 or S4; locate and size the apical "
  "impulse. Auscultate the posterior lung bases; press a thumb for 2 seconds over the dorsum of the foot, "
  "behind the medial malleolus and on the shin to <b>grade pitting edema</b> and how high it climbs; "
  "palpate the liver edge.",
  [("Chronic obstructive pulmonary disease", "Exertional breathlessness with a smoking history, cough and "
     "wheeze, but no orthopnea, S3 or raised neck veins, and a normal B-type natriuretic peptide"),
   ("Chronic venous insufficiency", "Leg edema with brown hemosiderin staining and varicosities, worse on "
                                    "standing, without breathlessness or raised jugular venous pressure"),
   ("Dihydropyridine calcium channel blocker edema", "Dependent ankle edema that began after amlodipine, "
                                                     "with normal neck veins and no dyspnea")],
  "<b>B-type natriuretic peptide</b> &rarr; elevated; above 400 makes heart failure likely (below 100 rules "
  "out acute failure). <b>Echocardiogram</b> &rarr; the ejection fraction group: &le;40% reduced, "
  "41&ndash;49% mildly reduced, &ge;50% preserved. <b>Chest radiograph</b> &rarr; cephalization, Kerley B "
  "lines, pleural effusion, a raised cardiothoracic ratio. <b>Electrocardiogram</b> &rarr; ischemic changes "
  "or left ventricular hypertrophy (tall R in V5&ndash;V6, deep S in V1&ndash;V2); metabolic panel for "
  "potassium and renal function.",
  "A <b>B-type natriuretic peptide below 100</b> rules out acute failure and makes heart failure an unlikely "
  "cause of the breathlessness &mdash; look to the lungs (spirometry for chronic obstructive pulmonary "
  "disease). Edema with a normal natriuretic peptide and echocardiogram points to the veins (<b>venous "
  "duplex ultrasound</b> &rarr; reflux) or to a drug. A complete blood count looks for anemia, a "
  "high-output cause.",
  "<b>Guideline-directed medical therapy by ejection fraction (2022)</b>. Reduced (&le;40%): an angiotensin "
  "receptor-neprilysin inhibitor (sacubitril-valsartan) or an angiotensin-converting enzyme inhibitor (lisinopril) or "
  "angiotensin receptor blocker (losartan), a <b>beta blocker</b> (carvedilol, metoprolol succinate or bisoprolol), a mineralocorticoid receptor antagonist "
  "(spironolactone), a sodium-glucose cotransporter 2 inhibitor (dapagliflozin) and a loop diuretic "
  "(furosemide) as needed; hydralazine with isosorbide dinitrate for African American patients in New York "
  "Heart Association class III&ndash;IV; <b>avoid calcium channel blockers</b>, above all verapamil and diltiazem. Mildly reduced or "
  "preserved: diuretics as needed and a sodium-glucose cotransporter 2 inhibitor first. Implantable "
  "cardioverter-defibrillator if ejection fraction &le;35%, class II&ndash;III on optimal therapy, life "
  "expectancy &ge;1 year; cardiac rehabilitation; follow potassium and renal function; co-manage with "
  "cardiology.",
  "ROUTINE &mdash; clinic with cardiology co-management to titrate therapy; same-day review if weight or "
  "breathlessness is climbing; emergency department now for breathlessness at rest, chest pain or fainting.",
  "<b>Weigh every morning</b> and know your dry weight &mdash; an overnight gain is fluid, not fat; call for "
  "more than 2&ndash;3 pounds in a day or 5 in a week. Take every medicine even when you feel well: the "
  "goals are longer survival and slower progression, not just comfort. Limit salt, avoid anti-inflammatory "
  "painkillers (they hold salt and water), stop smoking, limit alcohol. <b>Decompensation red flags</b>: "
  "more pillows, waking up gasping, swelling climbing the legs, less urine or new confusion &mdash; call the "
  "same day; breathless at rest, chest pain or fainting &mdash; call 911."),

}
