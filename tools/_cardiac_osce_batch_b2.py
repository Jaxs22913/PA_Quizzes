# -*- coding: utf-8 -*-
from _pd2_cardiac_osce_data import R
BATCH = {

"Atrial fibrillation": R(
  "urgent",
  "CMS L29 Arrhythmias I: Supraventricular (Elwaya) &middot; slides 24, 28, 32, 42, 46&ndash;50, 56, 58 "
  "&middot; PD2 Cardiovascular slides 6, 30, 99 &middot; Pharm Antiarrhythmics slides 29, 39",
  "Commonly seen in older patients with hypertension, diabetes, heart disease, obesity, sleep apnea or "
  "heavy alcohol use (slide 48), and the most common sustained arrhythmia; its danger is <b>stroke from "
  "atrial clot</b>, which anticoagulation prevents (slide 50).",
  "&ldquo;Since last night my heart has been racing and fluttering &mdash; all irregular, not a steady "
  "beat &mdash; and I get winded and a bit dizzy.&rdquo;",
  "An <b>irregularly irregular pulse</b>, usually fast (a ventricular rate of 110 to 160 is typical), so "
  "the vitals form shows tachycardia. The apical rate often exceeds the radial rate (a pulse deficit) and "
  "S1 varies in loudness. <b>Hypotension, crackles or a raised jugular venous pressure</b> mean it has "
  "tipped into heart failure &mdash; an emergency.",
  "Count the <b>apical rate by stethoscope and the radial pulse together for a full 60 seconds</b>; a short "
  "count misleads in an irregular rhythm. Jugular venous pressure at 30&ndash;45 degrees, lung bases and "
  "ankles for heart failure. Palpate the thyroid, and screen for a stroke (face, arm drift, speech).",
  [("Atrial flutter", "Regular sawtooth flutter waves, 2:1 block most common; irregular only with variable block"),
   ("Multifocal atrial tachycardia", "Also irregular, but every QRS has a P wave, of at least three shapes; acutely ill lung or heart failure patients"),
   ("Frequent premature atrial contractions", "A regular rhythm broken by early beats, each with its own abnormally shaped P wave")],
  "<b>12-lead electrocardiogram</b> &rarr; irregularly irregular, <b>no P waves and no PR interval</b>, "
  "narrow QRS. <b>CHA2DS2-VASc score</b> &rarr; stroke risk (0 in a man or 1 in a woman is low risk and "
  "may not need anticoagulation). <b>HAS-BLED score</b> &rarr; bleeding risk on anticoagulation. "
  "Thyroid-stimulating hormone, electrolytes and an echocardiogram look for the cause.",
  "Organized atrial activity before every QRS excludes it: sawtooth waves send you to flutter, three or "
  "more P-wave shapes to multifocal atrial tachycardia, isolated early P waves on a regular rhythm to "
  "premature atrial contractions. A low thyroid-stimulating hormone makes hyperthyroidism the driver to treat.",
  "<b>Unstable &rarr; synchronized cardioversion.</b> Stable with rapid ventricular response &rarr; "
  "intravenous rate control (diltiazem or metoprolol); stable without it &rarr; <b>oral rate control</b> (a beta blocker such as metoprolol, or a "
  "nondihydropyridine calcium channel blocker, diltiazem or verapamil) &mdash; rate, not rhythm, is goal one. Anticoagulate by "
  "stroke risk: direct oral anticoagulants preferred if nonvalvular (dabigatran, apixaban, edoxaban, "
  "rivaroxaban), or warfarin to an international normalized ratio of 2 to 3; the slide says a HAS-BLED of "
  "3 or more means no anticoagulation (guidelines treat it as bleeding risk to fix, not a bar). Outpatient "
  "cardioversion only after <b>21 days of anticoagulation</b>; ablation; cardiology referral.",
  "URGENT &mdash; same day: rate control and the anticoagulation decision if stable without rapid "
  "ventricular response; rapid ventricular response needs intravenous rate control in the emergency "
  "department; EMERGENT (call 911, synchronized cardioversion) if unstable &mdash; hypotension, pulmonary "
  "edema or an acute myocardial infarction",
  "Take the anticoagulant <b>every day without gaps</b> &mdash; it prevents the stroke; report black stools, "
  "blood in the urine or easy bruising. Call 911 for <b>face drooping, arm weakness or slurred speech</b>, "
  "chest pain, fainting or severe breathlessness. Cut alcohol, lose weight, treat sleep apnea, and keep "
  "blood pressure and diabetes controlled."),

"Premature ventricular contractions": R(
  "routine",
  "CMS L30 Arrhythmias II: Blocks and Ventriculars (Elwaya) &middot; slides 33, 35, 36, 40 &middot; "
  "CMS L29 slides 46, 54, 56 &middot; PD2 Cardiovascular slides 6, 30, 99 &middot; Pharm Antiarrhythmics slides 27, 29",
  "Elwaya&rsquo;s top point of the lecture: the main causes are <b>hypoxemia and electrolyte imbalance</b>, "
  "so check oxygen saturation and electrolytes (slide 36). They occur with or without structural heart "
  "disease and most patients are asymptomatic; they are the commonest ventricular ectopic beat.",
  "&ldquo;My heart skips a beat and then gives a big thump &mdash; I feel it in my neck. It&rsquo;s worse "
  "when I&rsquo;ve had a lot of coffee.&rdquo;",
  "Usually <b>normal vitals</b>, with a regular pulse broken by an <b>early beat and a pause</b>; the "
  "early beat may not reach the wrist. Look for a cause or for structural disease: a low oxygen "
  "saturation, a displaced impulse, a murmur, an S3, crackles, edema.",
  "Palpate the radial pulse while auscultating the apex for a full minute to catch early beats and any "
  "that fail to reach the wrist. Read the pulse oximetry, since hypoxemia is a main cause. Jugular venous "
  "pressure at 30&ndash;45 degrees, palpate for a displaced impulse, and listen for murmurs or an S3 "
  "&mdash; <b>structural heart disease makes the patient high-risk</b>.",
  [("Premature atrial contractions", "The early beat has its own early, abnormally shaped P wave and a NARROW QRS"),
   ("Non-sustained ventricular tachycardia", "Three or more wide beats in a row &mdash; runs, not single early beats"),
   ("Atrial fibrillation", "Irregularly irregular throughout with no P waves, not a regular rhythm with occasional early beats")],
  "<b>Electrocardiogram or monitor</b> &rarr; an <b>early, wide (over 0.12 seconds), bizarre QRS with no P "
  "wave</b>; every other beat is bigeminy, every third trigeminy. <b>Ambulatory monitor</b> &rarr; the "
  "burden: over 15% of beats (15,000 a day) is high, under 1% (1,000 a day) is low. <b>Potassium, "
  "magnesium, calcium and oxygen saturation</b> &rarr; the reversible causes.",
  "A narrow early beat with its own P wave means premature atrial contractions; three or more consecutive "
  "wide beats mean ventricular tachycardia; no P waves anywhere means atrial fibrillation. An "
  "echocardiogram showing a structurally normal heart keeps the patient low-risk.",
  "Correct hypoxemia and electrolytes; cut alcohol, caffeine and stimulants. <b>Low-risk, low burden, no "
  "symptoms &rarr; reassurance.</b> Low-risk with symptoms &rarr; a <b>beta blocker first</b> (metoprolol), catheter "
  "ablation if refractory or not tolerated. High-risk (burden over 15%, induced cardiomyopathy, structural "
  "or conduction disease, past syncope) &rarr; beta blocker and optimized treatment of the heart disease, "
  "or ablation for an isolated induced cardiomyopathy with heart failure; refer to cardiology.",
  "ROUTINE &mdash; clinic electrocardiogram, labs and ambulatory monitor; cardiology referral if high-risk "
  "(fainting, a sustained racing heartbeat or chest pain is not routine)",
  "Usually <b>benign</b>; trim caffeine, alcohol and stimulants. If a beta blocker is started, take it "
  "daily and do not stop it suddenly. Come back, or call 911, for <b>fainting</b>, a racing heartbeat that "
  "does not stop, chest pain or breathlessness."),

"Ventricular tachycardia": R(
  "emergent",
  "CMS L30 Arrhythmias II: Blocks and Ventriculars (Elwaya) &middot; slides 37&ndash;47 &middot; "
  "CMS L29 slides 23, 26, 33, 35, 52 &middot; PD2 Cardiovascular slides 6, 9, 97",
  "Sustained ventricular tachycardia can collapse the circulation in under 30 seconds, and pulseless "
  "ventricular tachycardia is one of the four arrest rhythms of sudden cardiac death (slides 37, 40); "
  "<b>polymorphic is never truly stable</b> (slide 46).",
  "&ldquo;All of a sudden my heart started pounding really fast and I felt like I was going to pass out. "
  "My chest feels tight.&rdquo; Often someone with a past heart attack, heart failure or cardiomyopathy.",
  "A <b>regular tachycardia of 100 to 250</b> on the vitals form. Instability is any one of <b>chest pain, "
  "altered mental status, shortness of breath or hypotension</b>; a lost pulse is cardiac arrest. "
  "Atrioventricular dissociation gives irregular cannon a waves in the neck and an S1 that varies in "
  "loudness.",
  "<b>Check for a pulse first</b> (carotid, one side at a time), then blood pressure and mental status "
  "&mdash; stability decides the treatment. Inspect the jugular veins for cannon a waves; listen for an S3 "
  "and crackles. Do not delay for a full examination: monitor, intravenous access, oxygen and a 12-lead "
  "electrocardiogram come first.",
  [("Supraventricular tachycardia", "QRS NARROW (under 0.12) unless antidromic reentry; often breaks with a vagal maneuver or adenosine"),
   ("Atrial fibrillation with Wolff-Parkinson-White", "Wide but IRREGULAR, rates approaching 300; the sinus tracing shows a short PR and a delta wave"),
   ("Torsades de pointes", "Polymorphic QRS twisting around the baseline on a prolonged QT &mdash; magnesium, never amiodarone or procainamide")],
  "<b>12-lead electrocardiogram or monitor</b> &rarr; <b>regular, 100 to 250, wide QRS (over 0.12 "
  "seconds), no PR interval</b>: three or more consecutive premature ventricular contractions, sustained if "
  "30 seconds or more or if it collapses the patient sooner. One QRS shape is monomorphic; changing shapes "
  "are polymorphic. Potassium, magnesium, calcium and troponin look for the trigger.",
  "A narrow QRS means supraventricular tachycardia; an irregular wide rhythm near 300 means pre-excited "
  "atrial fibrillation; twisting complexes on a long QT mean torsades. Until proven otherwise, a regular "
  "wide-complex tachycardia is ventricular.",
  "<b>No pulse &rarr; defibrillation</b> and cardiopulmonary resuscitation. <b>Unstable with a pulse &rarr; "
  "synchronized cardioversion.</b> Stable sustained monomorphic &rarr; intravenous lidocaine, amiodarone or "
  "procainamide (no procainamide with a long QT or heart failure); polymorphic &rarr; defibrillate, then "
  "urgent coronary angiography; torsades &rarr; intravenous magnesium. Once stable, most need an "
  "<b>implantable cardioverter-defibrillator</b>; symptomatic non-sustained runs start a beta blocker "
  "(metoprolol, carvedilol).",
  "EMERGENT &mdash; sustained or symptomatic: call 911 from the office; emergency department now, on a "
  "monitor with defibrillator pads on (only brief, asymptomatic non-sustained runs go to outpatient cardiology)",
  "Call 911 for <b>fainting, chest pain or a racing heartbeat that will not stop</b>. After an implanted "
  "defibrillator fires, call the cardiologist; call 911 if it fires repeatedly or you feel unwell. Take "
  "the medicines exactly as prescribed and ask before any new drug that can prolong the QT. Family members "
  "should learn cardiopulmonary resuscitation."),

"Acute pericarditis": R(
  "urgent",
  "CMS L31 Pericardial Disease (Reynolds) &middot; slides 4, 5, 7, 8, 13&ndash;17, 19, 24, 26&ndash;28, "
  "32, 33 &middot; PD2 Cardiovascular slides 30, 59, 81",
  "The <b>most common disorder of the pericardium</b> (slide 4), about 5% of emergency department visits "
  "for nonischemic chest pain; it recurs in 15 to 30% (slide 7).",
  "&ldquo;Sharp pain in the middle of my chest &mdash; it&rsquo;s worse when I lie flat or take a deep "
  "breath, and better when I sit up and lean forward. I had a cold last week.&rdquo;",
  "Often sitting forward; may have <b>fever and sinus tachycardia</b>. The <b>pericardial friction "
  "rub</b>, highly specific: a high-pitched, scratchy or squeaking, often triphasic sound that waxes and "
  "wanes, loudest at the left sternal border (Erb&rsquo;s point) with the diaphragm. Hypotension, "
  "distended neck veins or muffled heart sounds would mean tamponade.",
  "Auscultate with the patient <b>seated, leaning forward, breath fully exhaled and held</b>, diaphragm "
  "pressed firmly at the left sternal border. The held breath separates the rubs: <b>a pericardial rub "
  "persists, a pleural rub stops</b>. Check jugular venous pressure at 30&ndash;45 degrees and measure "
  "pulsus paradoxus to exclude tamponade; press on the chest wall for reproducible tenderness.",
  [("Acute coronary syndrome", "Pressure-like, exertional, not positional or pleuritic; REGIONAL ST elevation with reciprocal depression, not widespread"),
   ("Pulmonary embolism", "Pleuritic pain with sudden dyspnea, hypoxemia and often a swollen leg; no rub, not eased by leaning forward"),
   ("Pleuritis or pneumonia", "The pleural rub stops when the breath is held; cough, crackles and an infiltrate on the chest radiograph")],
  "Clinical: <b>two of four</b> &mdash; sharp substernal pleuritic chest pain, friction rub, widespread ST "
  "elevation, new or worsening effusion. <b>Electrocardiogram</b> &rarr; <b>widespread concave ST elevation "
  "with PR depression</b>, reciprocal ST depression and PR elevation in aVR. <b>C-reactive protein and "
  "erythrocyte sedimentation rate</b> &rarr; raised; <b>echocardiogram</b> &rarr; often normal unless "
  "there is an effusion. <b>Troponin</b> raised &rarr; myopericarditis.",
  "Regional ST elevation with reciprocal depression and a rising troponin send you to acute coronary "
  "syndrome; hypoxemia with a computed tomography pulmonary angiogram showing clot to pulmonary embolism; "
  "an infiltrate on the chest radiograph (normal in pericarditis) to pneumonia. Right ventricular diastolic "
  "collapse on echocardiogram means tamponade.",
  "<b>A nonsteroidal anti-inflammatory drug (aspirin, ibuprofen or indomethacin) plus colchicine</b>, with "
  "gastrointestinal protection; prednisone only if those cannot be taken; after a myocardial infarction, "
  "<b>aspirin plus colchicine</b> and no other anti-inflammatory. Taper once symptom-free and the "
  "C-reactive protein (checked weekly) normalizes. <b>Admit for any high-risk feature</b>: fever above 38 "
  "degrees Celsius, subacute onset, signs of tamponade, moderate-to-large effusion, immunosuppression, oral "
  "anticoagulants, trauma, raised troponin, or no improvement after 7 days. Cardiology for no response, "
  "recurrence or constriction.",
  "URGENT &mdash; same-day diagnosis and outpatient anti-inflammatory treatment when there is no high-risk "
  "feature; any high-risk feature means admission, and signs of tamponade mean the emergency department now",
  "<b>Finish the full course</b> even after the pain is gone &mdash; stopping early invites recurrence, "
  "which happens in about 15 to 30% of patients. <b>No strenuous exercise for at least a month</b>, keeping the heart "
  "rate under 100, until symptoms and the C-reactive protein settle; sleep with the head of the bed raised. "
  "Take the anti-inflammatory with food and the stomach protection. <b>Breathlessness, lightheadedness or "
  "fainting means the emergency department.</b>"),

"Cardiac tamponade": R(
  "emergent",
  "CMS L31 Pericardial Disease (Reynolds) &middot; slides 53&ndash;60, 63, 65, 67&ndash;71 &middot; "
  "PD2 Cardiovascular slides 20, 28",
  "Fluid under pressure compresses the heart until it cannot fill; an acute effusion does it with "
  "<b>under 200 mL</b> (slide 53). The short-term outcome is often good with prompt recognition and treatment (slide 69).",
  "&ldquo;I can&rsquo;t catch my breath and I feel like I&rsquo;m going to pass out; my chest feels "
  "heavy.&rdquo; Often after recent pericarditis, cancer, a heart procedure or chest trauma.",
  "<b>Beck triad: hypotension, distended jugular veins, muffled heart sounds.</b> <b>Pulsus "
  "paradoxus</b> &mdash; systolic pressure falls more than 10 mmHg on inspiration. Tachycardia and "
  "tachypnea on the vitals form (sinus tachycardia signals serious compromise); the apical impulse is "
  "faint and the lungs are usually clear.",
  "<b>Measure pulsus paradoxus</b> with a manual cuff: deflate slowly, note the pressure where Korotkoff "
  "sounds appear only in expiration, then where they are heard throughout breathing; a gap over 10 mmHg is "
  "positive. Jugular venous pressure at 30&ndash;45 degrees. Palpate for the apical impulse and auscultate "
  "for distant heart sounds.",
  [("Right ventricular myocardial infarction", "Hypotension with distended neck veins too, but ST elevation, a troponin rise and no effusion on echocardiogram"),
   ("Massive pulmonary embolism", "Hypoxemia with a dilated, overloaded right ventricle and no effusion; often a swollen leg"),
   ("Aortic dissection", "Tearing pain to the back with unequal arm pressures or pulses &mdash; and it can itself bleed into the pericardium")],
  "A clinical diagnosis, confirmed by the response to drainage. <b>Echocardiogram</b> &rarr; effusion "
  "with <b>right ventricular diastolic collapse</b>, the heart swinging in fluid. <b>Electrocardiogram</b> "
  "&rarr; low-voltage QRS, tachycardia, <b>electrical alternans</b>. <b>Chest radiograph</b> &rarr; a "
  "globular, water-bottle heart with clear lung fields.",
  "No effusion on echocardiogram excludes it and turns you to the differentials: electrocardiogram and "
  "troponin for right ventricular infarction, computed tomography pulmonary angiogram for embolism, "
  "computed tomography angiogram of the chest for dissection.",
  "<b>Expedient pericardiocentesis</b> is definitive; <b>intravenous fluids</b> raise preload to hold off "
  "right ventricular collapse until then; no diuretics. Traumatic hemorrhagic tamponade &rarr; emergent "
  "surgery. Send the fluid (cell count, Gram stain, cultures, acid-fast stain, cytology); recurrent or "
  "loculated effusions get a pericardial window or pericardiectomy; treat the cause.",
  "EMERGENT &mdash; suspected in the office: call 911; emergency department now for pericardiocentesis",
  "Explain that fluid around the heart is squeezing it and must be drained today. After drainage: "
  "follow-up with the specialty that matches the cause, and repeat echocardiograms for a large effusion; "
  "<b>returning breathlessness, lightheadedness or fainting means 911</b>. In a malignant effusion, offer "
  "a palliative care conversation."),

}
