# -*- coding: utf-8 -*-
from _pd2_cardiac_osce_data import R
BATCH = {

"Stable angina": R(
  "urgent",
  "CMS L24 Coronary Artery Disease &middot; slides 22&ndash;23, 27&ndash;32, 35, 37&ndash;41, 45&ndash;46, 72a, 79 "
  "&middot; CMS L23 Valvular Heart Disease slides 16&ndash;17 &middot; PD2 Cardiovascular slides 5, 42, 67, 96&ndash;97",
  "The <b>most common form of angina pectoris</b> (CMS L24 slide 37), and chest pain is the most common symptom "
  "of coronary artery disease (PD2 slide 5).",
  "&ldquo;When I walk up the stairs or hurry to the car I get a pressure in the middle of my chest, like "
  "something heavy sitting on it. It goes away after a few minutes when I stop and rest.&rdquo;",
  "Often a <b>normal examination between attacks</b> &mdash; say so. Watch how the patient points: a "
  "<b>clenched fist over the sternum (Levine sign)</b> is the real thing (slide 28). Vitals: hypertension and "
  "obesity as risk factors; heart rate and saturation normal at rest. During pain an S4 may be heard (PD2 slide "
  "42); diminished peripheral pulses suggest atherosclerosis elsewhere (PD2 slide 96).",
  "Ask the patient to <b>point to the pain</b>, then <b>press on the chest wall</b> to see whether pressure "
  "reproduces it. Listen at the right second intercostal space and up into the carotids for the "
  "<b>murmur of aortic stenosis</b>, which also causes exertional angina (CMS L23 slides 16&ndash;17). "
  "Auscultate each carotid with the breath held, then palpate one at a time (PD2 slide 97); palpate the "
  "peripheral pulses.",
  [("Unstable angina", "Pain at rest, new angina that limits activity, or pain that is more frequent or worse "
    "&mdash; the same disease turned acute coronary syndrome (slide 45)"),
   ("Gastroesophageal reflux", "Burning that rises behind the sternum after meals or lying flat and eases with "
    "antacids; not tied to exertion"),
   ("Costochondritis", "Sharp pain the patient points to with one fingertip, reproduced by pressing on the "
    "chest wall")],
  "<b>Electrocardiogram</b> (every chest pain, with a chest X-ray, slide 32) &rarr; often normal at rest. "
  "<b>Exercise treadmill or nuclear stress test</b> &rarr; stress-induced electrocardiogram changes, T-wave "
  "inversion or ST depression, or a <b>reversible</b> perfusion defect on the nuclear images (slides 38, 46). "
  "<b>Coronary angiography</b> &rarr; the fixed stenosis; the <b>gold standard</b> (slide 38).",
  "<b>Troponin, repeated</b> &rarr; normal excludes infarction (a rule-out tool, slide 72a). Pain at rest or "
  "escalating means unstable angina, not stable (slide 45). A normal stress test with post-meal burning "
  "relieved by antacids &rarr; reflux; pain reproduced by chest-wall pressure &rarr; costochondritis. A "
  "calcium score stratifies risk only (slide 35).",
  "<b>Sublingual nitroglycerin</b> for attacks &mdash; the cornerstone (slide 40). <b>Beta blocker</b> (a calcium "
  "channel blocker if a beta blocker is contraindicated), <b>statin</b> and <b>aspirin</b> (slides 39, 41). "
  "Risk-factor control: blood pressure, lipids, glucose, weight, alcohol, exercise, smoking cessation, stress "
  "(slide 79). Refer to cardiology for stress testing and, if positive, catheterization (slide 35).",
  "URGENT &mdash; a stable, predictable pattern (same effort brings it on, rest relieves it, no recent "
  "change): stress test and cardiology within days to weeks. New-onset angina that limits activity, pain at "
  "rest or a worsening pattern is unstable angina &rarr; EMERGENT, emergency department now.",
  "The pain is the heart muscle running short of oxygen during effort. At an attack, stop, sit down and take one "
  "nitroglycerin under the tongue; <b>if the pain is not better or is worse 5 minutes later, call 911</b> "
  "(slide 40). Pain at rest, or attacks that come more often or with less effort, means coming in now. No "
  "nitroglycerin within 24 hours of a phosphodiesterase inhibitor such as sildenafil. Quit smoking, exercise, "
  "and take the aspirin, statin and beta blocker every day."),

"Acute coronary syndrome": R(
  "emergent",
  "CMS L24 Coronary Artery Disease &middot; slides 11, 20, 28&ndash;32, 45&ndash;53, 63, 65&ndash;68, 71&ndash;74, "
  "78, 81&ndash;85, supplement slide 72a &middot; CMS L27 Arterial Occlusive and Aneurysm slides 114&ndash;117 "
  "&middot; CMS L31 Pericardial Disease slides 13, 17, 19 &middot; PD2 Cardiovascular slides 5, 42, 59",
  "Lethal: plaque rupture with thrombus (slide 20). <b>Sudden cardiac death, mostly ventricular fibrillation, is "
  "the first sign of coronary disease in over 20%</b> (slide 85); cardiogenic shock, myocardial rupture and "
  "arrhythmias follow (slide 78) &mdash; &ldquo;time is muscle&rdquo; (slide 68).",
  "&ldquo;A crushing pressure in the middle of my chest came on while I was sitting watching television. It goes "
  "into my jaw and down my left arm, I&rsquo;m sweating and sick to my stomach, and it won&rsquo;t go "
  "away.&rdquo; A woman over 65 or a diabetic may say only &ldquo;I&rsquo;m short of breath and "
  "exhausted&rdquo; (PD2 slide 5; silent ischemia, slides 29&ndash;30).",
  "General survey: distress, <b>diaphoresis</b>, pallor, a <b>clenched fist over the sternum</b> (Levine sign, "
  "slide 28). Vitals: tachycardia, or <b>bradycardia and heart block</b> with a right coronary artery infarct "
  "(it supplies the atrioventricular node, slide 11); <b>hypotension = cardiogenic shock</b> (slide 78). The "
  "heart may sound normal; listen for an S4, an S3 with basal crackles (failure), and a <b>new apical "
  "holosystolic murmur</b> (papillary muscle rupture, CMS L23 slide 45).",
  "Say the <b>electrocardiogram within 10 minutes</b> comes before a full examination (slide 68). <b>Blood "
  "pressure in both arms</b> and radial against femoral pulses (dissection). Jugular venous pressure at "
  "30&ndash;45 degrees and lung bases: hypotension with a raised jugular venous pressure and clear lungs in an "
  "inferior infarct suggests <b>right ventricular infarct</b> (slide 63). Sit the patient forward for a "
  "friction rub (PD2 slide 59); press the chest wall; check the calves.",
  [("Aortic dissection", "Sudden, severe, <b>tearing or ripping</b> pain to the back between the shoulder "
    "blades; syncope; a new aortic regurgitation murmur; arm pressures differ (CMS L27 slide 116, L24 slide 31)"),
   ("Acute pericarditis", "Sharp pleuritic pain, worse lying flat and better leaning forward; friction rub; "
    "<b>widespread</b> concave ST elevation with PR depression (CMS L31 slides 13, 17, 19)"),
   ("Pulmonary embolism", "Pleuritic pain with sudden dyspnea, tachycardia and low saturation; a swollen calf "
    "or recent immobility")],
  "<b>Electrocardiogram within 10 minutes</b> &rarr; ST elevation over 1 mm in two or more consecutive leads = "
  "<b>ST-elevation myocardial infarction</b>: reperfuse without waiting for troponin, which rises later; the lecturer corrected the slide that says markers must be present (slide 68). ST "
  "depression over 1 mm and/or T-wave inversion in two or more consecutive leads = non-ST-elevation syndrome "
  "(slide 47). <b>Troponin I, repeated</b> &rarr; <b>ELEVATED</b> (over 0.04 ng/mL; high-sensitivity over "
  "12 ng/L in women, 20 ng/L in men) = <b>non-ST-elevation myocardial infarction</b>; <b>NORMAL = unstable "
  "angina</b> (slides 46&ndash;47, 72a).",
  "<b>Normal electrocardiogram with normal serial troponins</b> &rarr; infarction excluded (one draw means two, "
  "slide 72a); go on to stress testing. <b>Computed tomography of the chest</b> &rarr; an intimal tear with a "
  "false lumen = dissection (the electrocardiogram may be normal, CMS L27 slides 114, 117). ST elevation in "
  "every territory with PR depression and reciprocal change in aVR &rarr; pericarditis (CMS L31 slide 19). "
  "<b>D-dimer</b> (slide 32), then computed tomography pulmonary angiography &rarr; a filling defect = "
  "pulmonary embolism.",
  "Call 911. <b>Chewable aspirin</b> now; oxygen only if saturation is under 91%; nitroglycerin, but "
  "<b>never in a right ventricular infarct</b> or after a phosphodiesterase inhibitor; beta blocker if no "
  "bradycardia; clopidogrel, ticagrelor or prasugrel plus heparin (slides 49, 63, 66&ndash;67). ST elevation: "
  "catheterization team, <b>door-to-balloon under 90 minutes</b>, or thrombolytics (tenecteplase) within 30 "
  "minutes of arrival if intervention is 2 or more hours away (slides 68, 74). Non-ST elevation: stabilize, "
  "then catheterization, early if the Thrombolysis in Myocardial Infarction score is 3 or more (slide 72). "
  "Discharge on a high-intensity statin and aspirin (slides 81, 83).",
  "EMERGENT &mdash; call 911; emergency department now (electrocardiogram within 10 minutes, door-to-balloon "
  "under 90 minutes).",
  "Chest pain like this again, or pain not better 5 minutes after one nitroglycerin: <b>call 911 and do not "
  "drive yourself</b>. Take the aspirin and the second antiplatelet every day &mdash; <b>stopping them early "
  "after a stent can suddenly close it</b> (slide 52). Statin and beta blocker daily; quit smoking, low-salt "
  "low-fat diet, exercise as tolerated; follow-up at 3, 6 and 12 months (slides 53, 79). No erectile "
  "dysfunction drugs (phosphodiesterase inhibitors) if you may need nitroglycerin."),

"Aortic stenosis": R(
  "urgent",
  "CMS L23 Valvular Heart Disease &middot; slides 11&ndash;13, 16&ndash;22, 48 &middot; CMS L28 Cardiomyopathy "
  "slides 64&ndash;72 &middot; PD2 Cardiovascular slides 23, 42, 50, 59&ndash;64, 67, 70; PD2 special maneuvers "
  "handout",
  "The <b>most common valvular disease</b> (slide 11), present in 25% of patients over 65 and 35% over 70 "
  "(slide 13); once symptomatic, <b>3-year mortality is 75%</b> (angina 5 years, syncope 3, heart failure 2; "
  "slides 16, 22).",
  "&ldquo;I get tight in the chest and out of breath when I walk any distance now, and last week I nearly "
  "passed out climbing the stairs.&rdquo;",
  "<b>Harsh, midsystolic, crescendo-decrescendo murmur at the right second intercostal space radiating to both "
  "carotids</b> (slide 17; PD2 slide 67); a thrill means grade 4/6 or more. A <b>forceful, sustained apical "
  "impulse with a delayed, weak carotid pulse</b> felt together = severe stenosis (slide 17; PD2 slide 23). "
  "S4 from the stiff hypertrophied ventricle (PD2 slide 42); crackles once it fails (slide 16).",
  "Sit the patient up and <b>leaning forward</b> &mdash; heard better (PD2 slide 67). Palpate the carotid "
  "while listening to time it (PD2 slide 50), and feel apex and carotid together. <b>Squatting from standing "
  "or passive leg raise &rarr; LOUDER; Valsalva or standing quickly &rarr; SOFTER</b> or unchanged &mdash; "
  "the opposite of hypertrophic cardiomyopathy (PD2 slides 61&ndash;62); handgrip softens it (slide 17). "
  "Trace it into both carotids before calling them bruits.",
  [("Hypertrophic obstructive cardiomyopathy", "Younger, family history of sudden death; loudest at Erb&rsquo;s "
    "point and the left lower sternal border, <b>not into the carotids</b>; <b>louder with Valsalva and "
    "standing</b> (PD2 slides 60&ndash;62, 70; CMS L28 slides 68&ndash;69)"),
   ("Mitral regurgitation", "Holosystolic at the apex, radiating to the axilla rather than the neck; louder "
    "with handgrip (CMS L23 slide 48)"),
   ("Stable angina from coronary artery disease", "The same exertional chest pressure without an ejection "
    "murmur; the two often coexist, so a murmur does not end the angina workup")],
  "<b>Transthoracic echocardiogram</b> &rarr; thickened, calcified leaflets with reduced systolic opening and "
  "left ventricular hypertrophy; <b>severe = valve area under 1.0 cm&sup2;, mean gradient over 40 mmHg, jet "
  "velocity over 4.0 m/s</b> (&ldquo;4, 40 and 1&rdquo;, slides 18&ndash;19). <b>Electrocardiogram</b> &rarr; "
  "left ventricular hypertrophy in severe disease (low sensitivity). <b>Left heart catheterization</b> &rarr; "
  "the definitive finding (slide 18).",
  "Echocardiogram with a normal aortic valve but <b>asymmetric septal hypertrophy and systolic anterior motion "
  "of the mitral leaflet</b> &rarr; hypertrophic cardiomyopathy (CMS L28 slide 72). A regurgitant jet into "
  "the left atrium with a normal aortic valve &rarr; mitral regurgitation. A normal valve with ischemia on "
  "stress testing &rarr; coronary disease alone.",
  "Medicines do not fix it (mild and moderate only); the patient is <b>preload dependent</b>: avoid dehydration, "
  "strenuous activity and competitive sports; with hypertension avoid beta blockers and calcium channel "
  "blockers; with angina <b>avoid nitrates</b> (slide 20). <b>Every patient with aortic stenosis on "
  "echocardiogram goes to cardiology</b> (slide 22). Severe stenosis with symptoms or left ventricular systolic "
  "dysfunction &rarr; transcatheter aortic valve replacement, or a mechanical (lifelong anticoagulation) versus "
  "biological valve; balloon valvuloplasty in children and young adults (slide 21).",
  "URGENT &mdash; once symptomatic (exertional angina, syncope, dyspnea): echocardiogram and cardiology valve "
  "referral within days; an asymptomatic murmur gets a routine echocardiogram and cardiology consult.",
  "The valve out of the heart has narrowed, so the heart works harder to push blood through; it is watched until "
  "symptoms appear, and then it is replaced. <b>Report chest pain, fainting or breathlessness on exertion right "
  "away</b> &mdash; they change the plan. Stay well hydrated, avoid heavy exertion and competitive sports, and "
  "do not take nitroglycerin unless cardiology prescribes it. Keep the echocardiogram and cardiology "
  "appointments."),

"Mitral regurgitation": R(
  "routine",
  "CMS L23 Valvular Heart Disease &middot; slides 9, 17, 44&ndash;52, 54, 71 &middot; PD2 Cardiovascular slides "
  "23, 30, 39&ndash;40, 63, 73&ndash;74",
  "Mild-to-moderate isolated mitral regurgitation is <b>usually asymptomatic</b> (slide 47), so it presents as a "
  "murmur to work up in clinic; the axilla is what separates it from tricuspid regurgitation (PD2 slides "
  "73&ndash;74, professor emphasized).",
  "&ldquo;I get winded more easily than I used to, and sometimes I feel my heart pounding.&rdquo; Often "
  "nothing at all &mdash; the murmur is found at a routine physical.",
  "<b>Holosystolic murmur at the apex radiating to the left axilla</b> (blowing on the CMS slide, harsh on the "
  "PD2 slide), with or without an S3 and an apical thrill (slide 48; PD2 slide 74). Apical impulse "
  "<b>diffuse and displaced to the left and down</b> from volume overload (PD2 slide 23). An irregularly "
  "irregular pulse if atrial fibrillation has developed; decompensated: rales, raised jugular venous pressure, "
  "leg edema (slide 47).",
  "Roll the patient into <b>left lateral decubitus</b> and listen at the apex with the diaphragm (slide 48; PD2 "
  "slide 30), then <b>follow the murmur into the axilla</b>. <b>Handgrip or squatting &rarr; LOUDER</b>; "
  "standing or Valsalva &rarr; softer (slide 48; PD2 slides 63, 74). No inspiratory increase &mdash; that is "
  "the Carvallo sign of tricuspid regurgitation (slides 9, 71). Bell at the apex for an S3 (PD2 slide 40); "
  "jugular venous pressure at 30&ndash;45 degrees, lung bases and ankles.",
  [("Tricuspid regurgitation", "Holosystolic at the lower left sternal border, <b>louder on inspiration</b> "
    "(Carvallo sign), <b>never to the axilla</b>; raised jugular venous pressure (CMS L23 slide 71; PD2 slide 73)"),
   ("Mitral valve prolapse", "A mid-systolic click followed by a LATE systolic murmur, not one that runs from "
    "S1 to S2 (PD2 slide 39)"),
   ("Aortic stenosis", "Midsystolic crescendo-decrescendo at the right second intercostal space into the "
    "carotids; softer, not louder, with handgrip (CMS L23 slide 17)")],
  "<b>Transthoracic echocardiogram</b> &rarr; the regurgitant flow into the left atrium, left atrial "
  "enlargement and left ventricular hypertrophy; <b>severe = regurgitant fraction 50% or more</b> (slides "
  "49&ndash;50). <b>Electrocardiogram</b> &rarr; left atrial enlargement and left ventricular hypertrophy in "
  "severe disease (low sensitivity), or atrial fibrillation. Left heart catheterization is not required.",
  "A jet into the right atrium with a competent mitral valve &rarr; tricuspid regurgitation. Leaflets over "
  "5 mm thick flaring into the left atrium &rarr; prolapse as the cause (slide 54). A calcified aortic valve "
  "with a high gradient &rarr; aortic stenosis.",
  "Medical therapy increases forward output while reducing the regurgitant volume, and treats the "
  "comorbidities &mdash; <b>atrial fibrillation and pulmonary hypertension</b> (slide 51). Echocardiogram "
  "surveillance with cardiology. <b>Severe regurgitation with symptomatic left ventricular dysfunction, "
  "ejection fraction under 60% or end-systolic dimension over 40 mm</b> &rarr; mitral valve clip, "
  "transcatheter mitral valve replacement, or a mechanical (lifelong anticoagulation) versus biological valve "
  "(slide 52).",
  "ROUTINE &mdash; clinic echocardiogram and cardiology referral; sudden regurgitation after an infarction "
  "(papillary muscle rupture) with pulmonary edema is EMERGENT.",
  "The valve between the two left heart chambers leaks, so some blood flows backward with each beat; mild leaks "
  "are simply watched with periodic echocardiograms. Come back for breathlessness on exertion, needing more "
  "pillows, waking up short of breath, leg swelling, or a racing irregular heartbeat. If a blood thinner is "
  "prescribed for atrial fibrillation or a mechanical valve, never skip it."),

"Mitral valve prolapse": R(
  "routine",
  "CMS L23 Valvular Heart Disease &middot; slides 45, 48, 54 &middot; PD2 Cardiovascular slides 6, 38&ndash;39, "
  "60&ndash;64, 70; PD2 special maneuvers handout",
  "<b>Usually benign and asymptomatic, in healthy women 15&ndash;30</b> (slide 54), but it is the classic "
  "systolic click (PD2 slide 39) and a chronic cause of mitral regurgitation (slide 45).",
  "&ldquo;Every now and then I feel my heart skip or flutter, but otherwise I feel fine.&rdquo; Often no "
  "complaint &mdash; the click is found at a school or sports physical.",
  "A young, healthy woman with normal vitals. <b>Mid-systolic click</b>, high pitched, at or just medial to the "
  "apex and the lower left sternal border, often followed by a <b>late systolic murmur crescendoing up to "
  "S2</b> &mdash; the mitral regurgitation it causes (CMS L23 slide 54; PD2 slide 39).",
  "Diaphragm at the apex and lower left sternal border for the click (PD2 slide 39), then <b>make it move</b>: "
  "<b>standing quickly or Valsalva &rarr; click EARLIER, murmur longer and louder</b>; <b>squatting or "
  "passive leg raise &rarr; click LATER, murmur shorter</b> (PD2 slides 62, 64; handout). A click that moves "
  "with filling is prolapse.",
  [("Hypertrophic obstructive cardiomyopathy", "Also louder with Valsalva and standing, but a midsystolic "
    "ejection murmur at Erb&rsquo;s point and the left lower sternal border with <b>no click</b> (PD2 slides "
    "60, 70)"),
   ("Chronic mitral regurgitation", "Holosystolic from S1 to S2, radiating to the axilla, rather than a late "
    "murmur after a click (CMS L23 slide 48)"),
   ("Early aortic ejection sound (bicuspid aortic valve)", "Clicks right AFTER S1, not in mid-systole, and is "
    "heard at the base as well as the apex (PD2 slide 38)")],
  "<b>Echocardiogram</b> &rarr; <b>thickened, redundant mitral leaflets (over 5 mm)</b> flaring into the left "
  "atrium in systole (slide 54); Doppler shows whether there is mitral regurgitation. "
  "<b>Electrocardiogram</b> for the palpitations (PD2 slide 6) &rarr; usually normal.",
  "Normal leaflet thickness and motion on echocardiogram excludes it. Asymmetric septal hypertrophy with "
  "systolic anterior motion &rarr; hypertrophic cardiomyopathy (CMS L28 slide 72); a holosystolic jet through "
  "a non-prolapsing valve &rarr; another cause of mitral regurgitation; a bicuspid aortic valve &rarr; the "
  "ejection sound.",
  "<b>Usually no treatment</b> &mdash; reassurance and observation (slide 54). If it progresses to mitral "
  "regurgitation: mitral valve clip, transcatheter mitral valve replacement, or biological or mechanical "
  "replacement (slide 54), with cardiology referral at that point.",
  "ROUTINE &mdash; outpatient echocardiogram to confirm; cardiology only if mitral regurgitation develops.",
  "This is a usually harmless shape of the valve that most people live with and need nothing for but an "
  "occasional check. Come back if you notice breathlessness on exertion, leg swelling, fainting, or "
  "palpitations that last or come with dizziness."),
}
