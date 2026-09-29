#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 5 cram sheet (Cardiology Block Exam II).

Condensed from the Exam 5 study guide, per the template README: compress what
the guide already says, keep numbers and names verbatim, add nothing new.

Topics match the guide's sections: six for Lecture 26 (Venous Disorders, Prof.
Shah; built with the lecture's emphasis: the Virchow triad and the Wells criteria
are the top card, marked with a star and the gold palette used for emphasis
cards on the CMS I Exam 2 sheet; the guide's other highlighted "most common"
facts carry a star in the row label), four for Lecture 27 (Arterial Occlusive
Disease and Aortic Aneurysm) and four for Lecture 28 (Cardiomyopathy). Lectures
27 and 28 were built 2026-09-25 from the slides only -- the lectures are on
2026-10-01, so their emphasis follows. Lectures 29-32 are added as their decks
are posted. Same palette rotation as the guide (Exam 5 rose).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

topics = [
# ---- Lecture 26, condensed from guide section 1 (built with the lecture's emphasis) ----
{"id": "l26-emph", "label": "★ Professor Emphasized — Virchow Triad &amp; Wells Criteria", "color": "#b8860b", "rows": [
 ["★ Virchow triad", "Why a clot forms in a vein: <b>venous stasis</b> + <b>hypercoagulable state</b> + <b>endothelial trauma</b> (vascular endothelial injury). Three big overarching categories; she named all three three times in a row. Several arms often act together (a hip fracture is trauma, then immobilization)."],
 ["Stasis (alterations in blood flow)", "Immobilization: long flights, prolonged sitting, postoperative inactivity (the deck gives about a <b>20-fold</b> risk). Venous insufficiency. Heart failure."],
 ["Hypercoagulable state", "Inherited: <b>factor V Leiden = the most common inherited cause</b>; prothrombin gene mutation; protein C or protein S deficiency; antithrombin deficiency. Acquired: cancer; oral contraceptive pill (more if she also smokes or is obese) or postmenopausal estrogen replacement therapy; pregnancy."],
 ["Endothelial trauma", "Surgery, especially <b>knee or hip replacement</b> or hip fracture repair; trauma and burns; intravenous drug use (lower extremity injection). The slide also files smoking and hypertension here."],
 ["Triad on a case", "Long car ride or a cast &rarr; stasis. Cancer, pregnancy, estrogen or a known clotting disorder &rarr; hypercoagulable state. Recent surgery, fracture, burns or injection drug use &rarr; endothelial trauma."],
 ["★ Wells criteria: use", "Stratifies the pretest likelihood of deep vein thrombosis. <b>Outpatient and emergency department only &mdash; not inpatients.</b> She said the criteria come straight from the risk factors, so know the risk factors best."],
 ["Wells: +1 each", "Active cancer (treatment or palliation within 6 months) &middot; bedridden more than 3 days or major surgery within 12 weeks &middot; calf swelling more than 3 cm versus the other leg (measured 10 cm below the tibial tuberosity) &middot; collateral (nonvaricose) superficial veins &middot; entire leg swollen &middot; localized tenderness along the deep venous system &middot; pitting edema confined to the symptomatic leg &middot; paralysis, paresis or recent plaster immobilization of the lower extremity &middot; previously documented deep vein thrombosis."],
 ["Wells: &minus;2", "<b>Alternative diagnosis at least as likely as deep vein thrombosis = &minus;2.</b>"],
 ["Wells: score &rarr; order", "<b>Zero or less = low</b> &rarr; D-dimer first (negative: stop; positive: ultrasound). <b>1 to 2 = moderate</b> (pretest probability about 17%) &rarr; D-dimer, then ultrasound if positive. <b>3 or more = high</b> &rarr; <b>skip the D-dimer, order the ultrasound.</b>"],
 ["Wells: pathway", "Low or moderate: D-dimer negative = stop; positive = ultrasound of the thigh; negative = stop. High: ultrasound of the thigh; if negative, either ultrasound of the lower leg, phlebography (venography), or a repeat thigh ultrasound in <b>1 week</b>."],
 ["Travel is NOT a criterion", "&ldquo;Bedridden&rdquo; means after surgery or immobilized in a cast or plaster, so a long flight scores nothing (travel is still a risk factor and a minor transient trigger for treatment duration)."],
 ["★ D-dimer", "<b>Sensitive but not specific.</b> A raised D-dimer means increased fibrinolysis somewhere, not necessarily a leg clot; a rule-out test for deep vein thrombosis and pulmonary embolism, only when the Wells score is low or moderate. Know what you will do next with either result. Contrast venography (gold standard, invasive) was replaced by venous duplex ultrasound."],
]},
{"id": "l26-dvt", "label": "Deep Vein Thrombosis", "color": "#a3341f", "rows": [
 ["Epidemiology", "Clot in the deep veins, usually the legs; lower extremity about <b>10 times</b> more common than upper. Starts in the calf and moves proximally (popliteal, femoral, iliac). Proximal: femoral and popliteal; distal: <b>peroneal</b>; pregnancy: pelvic veins. Upper extremity 5&ndash;10% of all, from <b>pacemakers, implantable cardiac defibrillators, central venous catheters</b>. Pulmonary embolism: up to 6% upper vs <b>15&ndash;30%</b> lower."],
 ["Other risk factors", "<b>★ Personal or family history of clot &mdash; prior episode about 30 times the recurrence risk.</b> Age older than 60; obesity; slightly more males; smoking, heart failure, hypertension, chronic kidney disease, chronic obstructive pulmonary disease, inflammatory bowel disease; cancer and chemotherapy; air travel and sedentary life; estrogen contraceptives, postmenopausal hormone replacement, first <b>6&ndash;12 weeks postpartum</b>."],
 ["Presentation", "Swelling (<b>97%</b> sensitive), pain (86%), warmth (72%), &plusmn; erythema; a calf cramp that persists and worsens over days. Distal clot: calf only; proximal: calf or whole leg. <b>Homan sign</b> is neither sensitive nor specific. Upper extremity: arm swelling and discomfort."],
 ["Differential", "Ruptured popliteal (Baker) cyst: severe sudden calf discomfort. Cellulitis: erythema, possibly fever and chills. Post-thrombotic syndrome: chronic venous insufficiency 6&ndash;24 months after a clot. Superficial thrombophlebitis: tender cord. Lymphedema: chronic edema, pelvic surgery, malignancy or radiation. Calf muscle tear: inciting injury, ankle bruising. Drug-induced edema (amlodipine): often bilateral, no inflammation."],
 ["Diagnosis", "Wells score (top card), then D-dimer and/or <b>venous duplex ultrasound of the involved extremity</b>; say why you are ordering it."],
 ["★ Treatment: mainstay", "<b>Anticoagulation is the mainstay &mdash; &ldquo;the biggest thing that we need to know.&rdquo;</b> Thrombolysis and thrombectomy are add-ons for selected large clots, never routine. Strategies: (1) heparin, then bridge to warfarin; (2) parenteral for <b>5 days</b>, then dabigatran or edoxaban; (3) oral monotherapy, loading then maintenance: rivaroxaban or apixaban."],
 ["Anticoagulant classes", "Low molecular weight heparin: enoxaparin. Unfractionated heparin: intravenous bolus then infusion, adjusted by the activated partial thromboplastin time. Fondaparinux: indirect factor Xa inhibitor. Rivaroxaban, apixaban: direct factor Xa inhibitors. Dabigatran: direct thrombin inhibitor. Warfarin: vitamin K antagonist, monitored by the international normalized ratio."],
 ["Contraindications", "<b>Active bleeding, acute intracranial hemorrhage, major trauma, severe bleeding disorders.</b>"],
 ["★ Duration", "Minimum <b>3 months</b> for every first episode. <b>Major transient (reversible) factor</b> (general anesthesia over 30 minutes, hospitalization or bed rest 3 days or more, major trauma or fracture): <b>3 months</b>. <b>Minor transient factor</b> (estrogen, pregnancy, minor surgery, prolonged travel, minor leg injury): <b>3&ndash;6 months</b>. <b>Unprovoked first clot: indefinite</b> (an undiscovered clotting condition cannot be excluded)."],
 ["★ Outpatient", "<b>Yes:</b> hemodynamically stable, low bleeding risk, no renal insufficiency, good support and reliable adherence. <b>No:</b> iliofemoral (proximal) clot, concurrent symptomatic pulmonary embolism, high bleeding risk, other comorbidities needing inpatient care. Options: rivaroxaban; apixaban; low molecular weight heparin or fondaparinux 5 days then dabigatran or edoxaban; or either heparin 5 days overlapping warfarin until the international normalized ratio is above 2. <b>Creatinine clearance below 30 mL/min: hospitalize</b>; unfractionated heparin + warfarin overlapped at least 5 days and until the ratio is above 2 for 24 hours."],
 ["Reversal agents", "Unfractionated or low molecular weight heparin: <b>protamine sulfate</b>. Dabigatran: <b>idarucizumab</b>. Apixaban, rivaroxaban: <b>andexanet alfa</b>. Warfarin: four-factor prothrombin complex concentrate, fresh frozen plasma or intravenous vitamin K; oral vitamin K is the usual outpatient choice. Bleeding is the most serious adverse effect."],
 ["Vena cava filter", "Inferior vena cava filter <b>only</b> with an acute proximal lower extremity clot and active bleeding, or when anticoagulation is otherwise contraindicated; keeps the clot from traveling to the lungs."],
 ["Prevention", "<b>Intermittent pneumatic compression</b> (sequential compression devices), especially when immobilized after surgery or in a long hospital stay. It does the calf muscles&rsquo; job so blood does not stagnate: it treats the stasis arm of the triad."],
 ["Complications", "<b>Pulmonary embolism = the biggest</b>: ask every patient about breathing difficulty right away. Post-thrombotic syndrome (chronic venous insufficiency, 6&ndash;24 months later). Recurrence. Bleeding from treatment. Fatal pulmonary embolism without adequate treatment: under 1% (clot alone), about 3% (non-massive), about 9% (massive)."],
]},
{"id": "l26-cvi", "label": "Chronic Venous Insufficiency", "color": "#2f5d6b", "rows": [
 ["What", "Severe manifestation of venous hypertension (also <b>post-thrombotic syndrome</b>): edema, skin changes (hyperpigmentation, dermatitis, lipodermatosclerosis) and ulceration from reflux and/or obstruction. <b>Primary</b> = wall or valve abnormality; <b>secondary</b> = prior deep vein thrombosis."],
 ["Causes", "<b>★ Prior deep vein thrombosis = the most common cause</b> (about 25% have no known clot; ask about leg trauma or surgery). Also progressive superficial venous reflux, pelvic vein obstruction, arteriovenous fistula. Risk factors: advancing age, female, family history, ligamentous laxity (flat feet), higher body mass index, smoking, leg trauma, higher parity, high estrogen states."],
 ["Presentation", "<b>Progressive pitting edema of the lower leg</b> is the primary symptom. Dull discomfort, heaviness, throbbing, burning, pruritus from the <b>medial malleolus</b>; worse standing or sitting with feet dependent, <b>relieved by elevation and walking</b>. Grade and document the pitting."],
 ["Skin findings", "<b>Stasis dermatitis</b>: pruritic, eczematous; earliest sign is erythema, scaling and slight hyperpigmentation above the medial malleolus. <b>Hemosiderin</b> staining: brown or blue-gray, separates venous from arterial. <b>Lipodermatosclerosis</b>: firm, indurated, skin tacked down, medial ankle, may form a constrictive band. Cellulitis: blanching erythema, hard to diagnose &mdash; outline and date it."],
 ["Venous ulcer", "Above the ankle, <b>medial or anterior</b>; painful; clean base, fibrinous exudate, serous drainage. Heals with a thin scar that breaks down easily. Arterial ulcers: dry, punched out, painful at the toes and lateral ankle."],
 ["Differential", "Heart failure, chronic kidney disease, decompensated liver disease: <b>bilateral</b> edema. Drug edema: calcium channel blockers, nonsteroidal anti-inflammatory drugs, thiazolidinediones. Lymphedema: unilateral, no varicosities. Lipedema: bilateral symmetric, just above the ankles, women. Other ulcers: diabetic neuropathic, arterial, autoimmune, sickle cell anemia, erythema induratum. Punch biopsy if unsure."],
 ["Work-up", "<b>Venous duplex ultrasound first</b>: patency (clot?) and valvular competence (reflux?). <b>★ Arterial pulse examination and ankle-brachial index</b> for any leg wound and older patients: not to diagnose the venous disease but to <b>rule out peripheral artery disease before compression</b>. Cross-sectional venography if ultrasound falls short; catheter venography (gold standard) only before an intervention."],
 ["Management", "<b>Always nonoperative first.</b> Feet elevated <b>ABOVE heart level</b>; daily walking and ankle flexion; skin care with emollients (mid-potency topical corticosteroid for stasis dermatitis); <b>★ compression = standard treatment, graduated (tightest at the ankle)</b>; cellulitis: oral antibiotics (cephalexin or clindamycin). Ulcers need edema control and compression, wound care referral, <b>4&ndash;6 months</b> to heal. No oral drug proven; surgery occludes or removes vessels."],
 ["Refer to vascular", "<b>Arterial insufficiency (same-day)</b>; nonhealing ulcers; recurrent ulcers; persistent stasis dermatitis; suspected contact dermatitis; diagnostic doubt; significant saphenous reflux; long-term edema control."],
]},
{"id": "l26-varicose", "label": "Varicose Veins", "color": "#5a3d8a", "rows": [
 ["What", "Dilated, tortuous superficial veins from <b>venous reflux and venous hypertension</b>; most commonly the <b>great saphenous vein</b>, also the short saphenous vein."],
 ["Risk factors", "<b>★ Family history = the most common predisposing factor.</b> Prolonged standing or heavy lifting; women after pregnancy."],
 ["Symptoms", "<b>★ Dull, achy heaviness or fatigue brought on by standing = the most common symptom.</b> Itching above the ankle or over the veins; may be asymptomatic. Long-standing varicose veins can progress to chronic venous insufficiency."],
 ["Exam", "Dilated, tortuous, palpable veins of the thigh and calf, seen standing; may be tender."],
 ["Diagnosis", "<b>Clinical</b>: examine the leg in a dependent position. Venous duplex (Doppler) ultrasound confirms and maps the extent of reflux."],
 ["Management", "Isolated varicose veins: elevation, exercise, compression, <b>rule out arterial disease before compression</b>; stockings for weeks to months before ablation. Goal = symptoms and appearance; they often recur. Procedures: <b>sclerotherapy</b>, vein stripping, laser or radiofrequency catheter."],
]},
{"id": "l26-phlebitis", "label": "Superficial Phlebitis, Thrombophlebitis &amp; Septic Thrombophlebitis", "color": "#1f5c3a", "rows": [
 ["Definitions", "<b>Phlebitis</b> = inflammation of the vein wall <b>without</b> thrombus. <b>Thrombophlebitis</b> = phlebitis <b>with</b> thrombus. Told apart because treatment differs."],
 ["Risk factors", "<b>Varicose veins = the most common cause in the lower extremity.</b> <b>Recent intravenous catheter use (peripherally inserted central catheter most common) = the most common cause in the upper extremity.</b> Inactivity; local trauma or procedure on superficial veins; pregnancy or estrogen; malignancy or hypercoagulable state; prior superficial vein thrombosis without varicose veins."],
 ["Presentation", "Tenderness, pain, induration and erythema along a superficial vein; an <b>indurated palpable cord</b> with warmth and erythema; you can trace the vein."],
 ["Septic (suppurative)", "Infection within the vein: <b>high fever, fluctuance, purulent drainage</b>, or erythema extending well beyond the vein margin. Uncommon without prior venous cannulation, so ask about a recent intravenous line. The deck gives no treatment; a missed infection can leave the patient septic."],
 ["Diagnosis", "History and examination, confirmed by <b>venous duplex ultrasound (gold standard)</b>: noncompressible superficial vein with wall thickening. Wall thickening alone = phlebitis; with a clot inside = thrombophlebitis."],
 ["★ Treatment", "<b>Nonsteroidal anti-inflammatory drugs first</b> (ibuprofen, diclofenac), warm compresses, compression, elevation. <b>Anticoagulation only for extensive clot burden</b> or intermediate or higher thrombosis risk (unfractionated heparin, enoxaparin, fondaparinux). Repeat examination in <b>7&ndash;10 days</b>; repeat duplex ultrasound if signs persist or worsen."],
 ["Prognosis", "Rarely causes serious complications; <b>rarely embolizes</b>. Counsel: patients worry it is a clot."],
]},
{"id": "l26-avf", "label": "Arteriovenous Fistula", "color": "#8a5a2b", "rows": [
 ["What", "Abnormal artery-to-vein connection that <b>bypasses the capillary bed</b>; created (hemodialysis), acquired (iatrogenic, trauma) or congenital."],
 ["Created (dialysis)", "<b>★ Upper extremity fistulas are the ones most commonly created for hemodialysis access</b> (upper arm or forearm, preferred over the leg). Healthy: <b>diffuse thrill and soft bruit</b>, both systolic and diastolic; <b>collapses completely on arm elevation</b>. <b>Cannot hear a bruit: refer.</b>"],
 ["Acquired (iatrogenic)", "Most common in the <b>lower extremity</b>, the <b>femoral vessels</b>, after groin access for percutaneous procedures such as cardiac catheterization. Examine the puncture site with a complete lower extremity vascular examination; compare pulses with the pre-procedure pulses."],
 ["Diagnosis", "Physical examination; <b>duplex ultrasound</b> confirms a suspected iatrogenic fistula; computed tomography angiography or angiography gives location and size."],
 ["Nicoladoni-Branham sign", "Compressing a large fistula <b>slows the heart rate</b> (reflex). Do not hold the fistula closed to demonstrate it on a patient."],
 ["Complications", "Watch for infection, chronic venous insufficiency, heart failure and ischemia."],
 ["Management", "<b>Acquired:</b> surgical, remove the fistula or decrease its size. <b>Congenital:</b> hard to treat (many communications); elastic support hose, sometimes embolization. Primary care: keep it free of infection, decide congenital versus acquired, find out how, refer."],
]},

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
    sub="Venous disorders, arterial occlusive disease and aortic aneurysm, and cardiomyopathy, condensed "
        "from the Exam 5 study guide: the Virchow triad and Wells criteria first, then deep vein thrombosis, "
        "chronic venous insufficiency, claudication and the ankle-brachial index, acute limb ischemia, carotid "
        "and aneurysm thresholds, dissection, and the five cardiomyopathies. Lecture 26 carries the "
        "lecture&rsquo;s emphasis (starred); Lectures 27&ndash;28 are built from the slides only, with lecture "
        "audio emphasis to be added after 10/01. The rest of the block follows when posted.",
    topics=topics,
    guide_href="cms-exam-5-study-guide.html",
    footer_note="Condensed from the CMS I Exam 5 Study Guide (Class of 2028). "
                "For the full explanation behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 5", "cms-exam-5-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics")
