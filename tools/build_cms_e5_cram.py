#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 5 cram sheet (Cardiology Block Exam II).

Condensed from the Exam 5 study guide, per the template README: compress what
the guide already says, keep numbers and names verbatim, add nothing new.

Topics match the guide's sections: four for Lecture 27 (Arterial Occlusive
Disease and Aortic Aneurysm) and four for Lecture 28 (Cardiomyopathy), built
2026-09-25 from the slides only -- the lectures are on 2026-10-01, so the sub
line says audio emphasis follows. Lectures 26 and 29-32 are added as their
decks are posted. Same palette rotation as the guide (Exam 5 rose).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

topics = [
# ---- Lecture 27, condensed from guide section 1 ----
{"id": "l27-pad", "label": "Peripheral Artery Disease", "color": "#7a2d5a", "rows": [
 ["Who", "Older than <b>60</b> with no other risk factors, or <b>50 with risk factors</b>; males &gt; females; <b>half also have coronary artery disease</b>. Smoking = <b>three times</b> the risk; elevated homocysteine = earlier atherosclerosis."],
 ["Claudication", "Activity pain relieved by rest in <b>about 10 minutes</b>, analogous to angina. <b>Site = level:</b> buttock/hip = aortoiliac; thigh = common femoral; <b>upper two-thirds of calf = superficial femoral (most common)</b>; lower third of calf = popliteal; foot = tibial/peroneal."],
 ["Leriche triad", "Claudication + <b>absent or diminished femoral pulses</b> + <b>erectile dysfunction</b> (aortoiliac)."],
 ["Exam", "Dry, thin, shiny skin; hair and nail loss; atrophy; cool limb (temperature line &asymp; level); pulses gone <b>below</b> the stenosis; capillary refill &gt; 2 s; bruits. <b>Buerger:</b> leg up 45&deg; for 1 minute &rarr; <b>pallor</b>; dangle &rarr; <b>dependent rubor</b>. Darker skin: use temperature, texture, capillary refill."],
 ["Ankle-brachial index", "Initial bedside test. Higher ankle &divide; higher arm; the <b>lower leg</b> is the overall index. <b>0.9&ndash;1.3</b> normal &middot; <b>0.4&ndash;0.9</b> claudication &middot; <b>0&ndash;0.4</b> rest pain / tissue loss &middot; <b>&gt; 1.3 abnormal</b> (calcified, non-compressible &mdash; diabetes)."],
 ["Imaging", "<b>Duplex ultrasound</b> = mainstay initial imaging (no contrast, no radiation). Computed tomography angiography: no with contrast allergy or poor renal function. Magnetic resonance angiography: the contrast-allergy alternative; no with pacemaker or intracranial aneurysm clips. <b>Conventional angiography = gold standard</b>, used to guide intervention."],
 ["Treatment", "Stop smoking; blood pressure &lt; 140/90 (&lt; 130/80 diabetes or renal failure); diabetes and weight control; <b>supervised exercise</b> (beats home-based) 30&ndash;45 min &times;3/week. Aspirin, clopidogrel, <b>cilostazol</b>; simvastatin or pravastatin (low-density lipoprotein &lt; 100, &lt; 70 high risk); pentoxifylline; folic acid + B12 + B6 for high homocysteine."],
 ["Revascularize when", "Disabling claudication despite exercise and drugs: angioplasty &plusmn; stent, atherectomy; <b>bypass (saphenous vein or synthetic) mainly for critical limb ischemia</b>; endarterectomy; amputation."],
]},
{"id": "l27-cli", "label": "Critical Limb Ischemia &amp; Acute Occlusion", "color": "#a3341f", "rows": [
 ["Rest pain", "Constant, burning, forefoot and toes, <b>worse elevated or reclining</b>, wakes at night, narcotics fail. <b>Relieved by dangling the leg or walking</b> (the paradox)."],
 ["Ulcers &amp; gangrene", "Ulcers at toe tips, between digits, metatarsal heads: <b>dry, punched out, painful, little bleeding</b>; osteomyelitis risk. <b>Dry gangrene</b>: hard, clear demarcation. <b>Wet gangrene = surgical emergency</b> (moist, edema, blisters, clostridial gas, sepsis)."],
 ["Acute limb ischemia", "<b>Sudden occlusion of a previously patent artery &mdash; vascular emergency.</b> Emboli: heart is the source in <b>80&ndash;90%</b> (atrial fibrillation, post-infarct ventricular thrombus). Six P&rsquo;s: pain, pallor, pulselessness, paresthesia, paralysis, poikilothermia. <b>Earliest neurologic sign: sensory loss over the dorsum of the foot.</b>"],
 ["Rutherford", "<b>I</b> viable &middot; <b>IIA</b> salvageable if prompt (no sensory loss, no weakness) &middot; <b>IIB</b> salvageable only with immediate revascularization &rarr; surgical suite &middot; <b>III</b> irreversible &rarr; major amputation, no imaging needed. (IIA arterial Doppler: slides disagree.)"],
 ["Treat", "<b>Immediate vascular surgery consult</b> + <b>intravenous heparin</b>; catheter-directed thrombolysis (alteplase) if <b>&lt; 14 days</b>; thromboembolectomy; bypass; amputation."],
 ["Blue toe", "Atheroembolism (cholesterol, fibrin, platelets from proximal plaque): painful blue toe, livedo reticularis &mdash; <b>distal pulses still palpable</b>."],
]},
{"id": "l27-carotid", "label": "Carotid Artery Disease", "color": "#2f5d6b", "rows": [
 ["Why it matters", "<b>80% of new noncardioembolic strokes</b>; strokes mostly from <b>plaque rupture</b>. Asymptomatic outnumber symptomatic <b>4:1</b>."],
 ["Symptoms", "Transient ischemic attack (&lt; 24 h), stroke, <b>amaurosis fugax</b> (monocular blindness like a curtain descending). Auscultate each carotid separately, breath held."],
 ["Tests", "<b>Duplex ultrasonography</b> = initial screening and follow-up. Computed tomography / magnetic resonance angiography. <b>Digital subtraction angiography = gold standard</b>, not for screening. <b>Do not screen asymptomatic adults.</b>"],
 ["Treat", "&lt; 50%: medical (antiplatelets, blood pressure, glucose, statins, <b>stop smoking &mdash; nearly doubles stroke risk</b>). Surgery: <b>symptomatic &gt; 70%</b> or <b>asymptomatic &gt; 80% with life expectancy &gt; 5 years</b>. <b>Endarterectomy = gold standard</b> (stroke or nerve damage); stenting for poor surgical candidates."],
]},
{"id": "l27-aorta", "label": "Aneurysms &amp; Dissection", "color": "#8a5a2b", "rows": [
 ["Definition", "Dilation &gt; <b>50%</b> of normal. Infrarenal aorta 2 cm; <b>&gt; 3 cm = aneurysm</b>; <b>90% infrarenal</b>. True = all three layers (saccular or fusiform)."],
 ["Abdominal: risk", "<b>Smoking ever = strongest</b>; male (2:1 under 80, 1:1 over 80); age; Caucasian; atherosclerosis; hypertension; family history; other aneurysms. <b>Protective: female, non-Caucasian, diabetes</b> (but women rupture more). 15,000 deaths/year."],
 ["Abdominal: signs", "Mostly incidental. Expansion pain (hypogastrium, back, flank, groin), early satiety, blue toe. <b>Rupture triad (50%): pain + pulsatile mass (virtually diagnostic) + hypotension</b>; Grey Turner sign (flank ecchymosis). Bruit nonspecific."],
 ["Abdominal: tests", "<b>Ultrasound = initial screening</b> and serial size. X-ray calcified outline 75%. <b>Computed tomography angiography = best diagnostic and planning study.</b> Magnetic resonance imaging for stable dye-allergic patients. Type and crossmatch."],
 ["Abdominal: sizes", "3.0&ndash;3.9 cm ultrasound <b>every 3 years</b>; 4.0&ndash;5.4 cm <b>every 6&ndash;12 months</b>. Specialist at <b>4.5 cm</b>; urgent for pain at any size. <b>Repair: &ge; 5.0 cm women, &gt; 5.5 cm men, or 0.5 cm growth in 6 months.</b> Rupture rare &lt; 5 cm."],
 ["Abdominal: treat", "Stop smoking, aggressive blood pressure control, moderate exercise. Endovascular or open repair. Symptomatic unruptured: large-bore lines, pain and blood pressure control (beta blocker), repair. <b>Ruptured: surgical emergency</b> &mdash; large-bore lines, type and crossmatch."],
 ["Thoracic", "Hypertension common; mostly incidental on chest X-ray (<b>widened mediastinum</b>). Ascending &rarr; aortic regurgitation, heart failure; <b>arch &rarr; hoarseness</b>; descending &rarr; dysphagia, stridor, cough. <b>Computed tomography angiography most used.</b> Beta blockers, blood pressure control; urgent imaging for pain. <b>Repair all symptomatic</b>; ascending &gt; 5.5, descending &gt; 6.0 cm, growth &gt; 0.5 cm/<b>year</b>."],
 ["Pseudoaneurysm", "Blood outside the wall after arterial rupture &mdash; <b>femoral artery after catheterization</b>. Thin wall, irregular, hematoma. <b>&lt; 2 cm watch</b>; ultrasound-guided <b>thrombin injection</b>."],
 ["Dissection", "Intimal tear &rarr; false lumen in the media. 60s&ndash;70s (younger in <b>Marfan</b>), male, <b>hypertension</b>. <b>Sudden tearing chest pain</b> that moves; syncope; aortic regurgitation. Electrocardiogram may be normal; <b>computed tomography chest and abdomen</b>. <b>Systolic 100&ndash;120 mmHg with esmolol or nitroprusside</b>; surgery; high untreated mortality."],
]},

# ---- Lecture 28, condensed from guide section 2 ----
{"id": "l28-dcm", "label": "Dilated Cardiomyopathy", "color": "#5a3d8a", "rows": [
 ["What", "<b>Most common</b> cardiomyopathy: dilated, poorly contracting ventricle(s) <b>without</b> severe coronary disease or pressure/volume overload &rarr; systolic failure, globular heart; mitral (early) and tricuspid regurgitation."],
 ["Who / why", "Ages 20&ndash;60, male, high in African Americans. Idiopathic; <b>familial up to 35%</b> (autosomal dominant); viral or Chagas myocarditis; chemotherapy; <b>alcohol (can recover if stopped)</b>; thiamine deficiency; lupus, rheumatoid arthritis; <b>peripartum</b> (last trimester to 6 months after delivery). Idiopathic = main indication for transplant."],
 ["Signs", "Progressive exertional dyspnea, orthopnea, paroxysmal nocturnal dyspnea, edema; <b>laterally displaced impulse, third heart sound</b>, regurgitant murmurs, narrow pulse pressure, jugular distension, hepatojugular reflux."],
 ["Tests", "<b>Normal electrocardiogram almost rules it out.</b> Echo: <b>dilated thin walls</b>, ejection fraction &lt; 40%. X-ray: cardiomegaly, Kerley B lines. B-type natriuretic peptide &lt; 100 pg/mL excludes heart failure. Magnetic resonance imaging for inflammatory or infiltrative causes; biopsy rarely."],
 ["Treat", "As chronic heart failure: <b>every patient gets a beta blocker + angiotensin-converting enzyme inhibitor</b>; loop diuretics; spironolactone; sacubitril/valsartan. Anticoagulate only for atrial fibrillation, artificial valve or mural thrombus. <b>Defibrillator if ejection fraction &lt; 35% after maximal therapy</b>; biventricular pacemaker; assist device (bridge or destination); transplant."],
 ["Teach / outlook", "Remove the cause; <b>sodium &lt; 2 g/day</b>; genetic counseling if familial. <b>50% dead at 5 years once symptomatic.</b>"],
]},
{"id": "l28-myo", "label": "Myocarditis &amp; Takotsubo", "color": "#1f5c3a", "rows": [
 ["Myocarditis: who", "Otherwise healthy, <b>young males</b>; <b>flulike illness 1&ndash;2 weeks before</b>; viral most frequent (Coxsackie B, parvovirus B19, human herpesvirus 6, COVID-19 (coronavirus disease 2019)...). Viral myocarditis = 20% of dilated cardiomyopathy."],
 ["Myocarditis: picture", "New heart failure or cardiogenic shock with no prior heart disease; palpitations, syncope, sudden death (ventricular arrhythmia, heart block)."],
 ["Myocarditis: tests", "Troponin, leukocytosis, sedimentation rate, echo; angiography to exclude ischemia; gadolinium magnetic resonance imaging. <b>Endomyocardial biopsy = gold standard</b>, for unexplained deterioration not responding to treatment."],
 ["Myocarditis: treat", "<b>Supportive care is the mainstay</b>; stabilize. Most mild cases recover; <b>one third later develop dilated cardiomyopathy</b>."],
 ["Takotsubo", "<b>90% postmenopausal women</b> after a big emotional or physical stressor; low cardiac risk. Mimics acute coronary syndrome: chest pain, dyspnea; troponin up; <b>ST elevation, T inversion</b>; echo <b>mid and apical hypokinesis</b>. <b>Confirmed by catheterization: normal coronaries.</b> Treat by the acute coronary syndrome protocol, admit to cardiology; beta blockers. <b>Most recover completely.</b>"],
]},
{"id": "l28-hcm", "label": "Hypertrophic Cardiomyopathy", "color": "#7a2d47", "rows": [
 ["What / who", "Unexplained left ventricular hypertrophy, <b>asymmetric septal</b>. <b>Autosomal dominant</b> (sarcomere genes); <b>1 in 500</b>; male. <b>Leading cause of sudden death in preadolescents and adolescents</b> (extreme exertion; &gt; 80% ventricular fibrillation)."],
 ["Obstruction", "Septum narrows the outflow tract + <b>systolic anterior motion</b> of the anterior mitral leaflet &rarr; mid-systolic obstruction."],
 ["Symptoms", "Dyspnea (commonest), palpitations, <b>exertional syncope / presyncope on standing = high sudden-death risk, urgent work-up</b>, angina without coronary disease."],
 ["Signs", "Normal blood pressure and rate; <b>pulsus bisferiens</b> (double peak); forceful sustained apex; <b>fourth heart sound</b>. Crescendo-decrescendo murmur, left sternal border 3rd&ndash;4th space, to the suprasternal notch, <b>not the carotids</b>."],
 ["Maneuvers", "<b>More blood in the heart = softer; less = louder.</b> Squat, leg raise, handgrip &rarr; softer. <b>Valsalva, standing</b>, amyl nitrite &rarr; louder. Breathing: no effect."],
 ["Tests", "<b>Echocardiography = test of choice</b>: wall <b>&ge; 1.5 cm</b>, septal pattern, small cavity, ejection fraction normal (&gt; 75% late). Electrocardiogram: inferior and lateral Q waves, left axis deviation. Magnetic resonance imaging if echo questionable; 24&ndash;48 h ambulatory monitor; catheterization only before invasive therapy; genetic testing does not change treatment."],
 ["Treat", "<b>Beta blocker first</b>, then verapamil or diltiazem. <b>AVOID nitrates, dehydrating diuretics, digoxin, epinephrine, norepinephrine.</b> Amiodarone (cuts sudden death), disopyramide, defibrillator; atrial fibrillation &rarr; anticoagulate. <b>Myectomy</b> or <b>alcohol septal ablation</b> (months to thin)."],
 ["Teach", "Mild to moderate <b>noncompetitive</b> activity; <b>stay hydrated</b>; avoid excess alcohol. Sudden death = leading cause of death."],
]},
{"id": "l28-rcm", "label": "Restrictive Cardiomyopathy &amp; Populations", "color": "#2f5d6b", "rows": [
 ["What", "<b>Least common.</b> Stiff, normal-size ventricles; <b>big atria</b>, atrial fibrillation; ejection fraction preserved until late; <b>right-sided failure dominates</b>; heart block from nodal fibrosis. <b>Poorest prognosis</b> of all."],
 ["Causes", "<b>Amyloidosis (most common in the United States)</b>, hemochromatosis, sarcoidosis, <b>mediastinal radiation, chemotherapy</b>; idiopathic; genetic."],
 ["Signs", "Late presentation; hepatomegaly, ascites, pedal edema; prefers sitting; raised jugular venous pressure; <b>Kussmaul sign</b> (jugular pressure <b>rises with inspiration</b>); fourth heart sound if no regurgitation."],
 ["Tests", "Electrocardiogram: <b>low QRS voltage in amyloid</b>. Echo: big atria, preserved function &mdash; <b>not definitive</b>. <b>Cardiac magnetic resonance imaging separates it from constrictive pericarditis (pericardial thickening = pericarditis).</b> Biopsy when all else is negative."],
 ["Treat", "Treat the cause; <b>diuretics with caution (preload-dependent)</b>; beta blockers, verapamil or diltiazem; anticoagulate atrial thrombi; pacemaker for heart block; transplant."],
 ["Populations", "<b>Adolescent:</b> genetic screening for hypertrophic cardiomyopathy, activity restriction if high risk. <b>Adult:</b> guideline-directed therapy, devices, sodium restriction, alcohol cessation, assist device or transplant. <b>Elderly:</b> tailored to frailty, <b>cautious diuretics and vasodilators</b>, symptom control, palliative discussions. Rehab and hospice referral in end-stage disease."],
]},
]

html = render(
    title="Cram Sheet — CMS I Exam 5",
    kicker="Clinical Medicine and Surgery I · Exam 5 · Class of 2028",
    h1="CMS I Exam 5 Cram Sheet",
    sub="Arterial occlusive disease and aortic aneurysm, and cardiomyopathy, condensed from the Exam 5 "
        "study guide: claudication and the ankle-brachial index, acute limb ischemia, carotid and aneurysm "
        "thresholds, dissection, and the five cardiomyopathies. Built from the slides only; lecture audio "
        "emphasis to be added after 10/01. The rest of the block follows when posted.",
    topics=topics,
    guide_href="cms-exam-5-study-guide.html",
    footer_note="Condensed from the CMS I Exam 5 Study Guide (Class of 2028). "
                "For the full explanation behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 5", "cms-exam-5-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics")
