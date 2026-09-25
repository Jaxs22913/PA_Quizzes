#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Principles of Diagnostic Medicine I, Exam 2 cram sheet.

Condensed from the Exam 2 study guide (build_pdm_e2_guide.py) and nothing else,
per cram_sheets_feature: no row states a fact the guide does not. Lectures 7, 8
and 9; Lecture 10 is added when its deck is posted. No lab content.

Reynolds' rule is asserted: reference values appear only as the scale that reads
a result, and the scope row says so.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 2/pdm-exam-2-cram-sheet.html")

topics = [
 {"id": "scope", "label": "How This Exam Is Written", "color": "#a1363a", "rows": [
   ["Reference ranges are GIVEN", "“I'm not going to just throw a random number at you” — a troponin, triglyceride or C-reactive protein in a stem comes with the limit that reads it. Learn what a value MEANS."],
   ["Name the rhythm", "Electrocardiography is the one place where naming the finding is fair game. Lecture 7 is the toolkit: paper, leads, rate, intervals."],
   ["Next-best-test", "“What would be the next test that you would order?” Know what each imaging study can and cannot show, and what to do when one is equivocal."],
   ["Not examined (said out loud)", "Ion-channel subtypes (but which ion moves in each phase IS). Bazett's formula (“I will never ask you about the formula”). The bifascicular-block aside. The order of the exercise-endpoint chart and the treadmill protocol tables."],
 ]},
 # ---------------- Lecture 7 ----------------
 {"id": "action-potential", "label": "Action Potential & Refractory Periods", "color": "#7a2a2e", "rows": [
   ["Four cell properties", "AUTOMATICITY (makes its own impulse) · EXCITABILITY (responds to one) · CONTRACTILITY · CONDUCTIVITY (passes it on)."],
   ["Phase order", "4 → 0 → 1 → 2 → 3. “You need to know what happens in each phase.”"],
   ["Phase 4 / 0", "4 = rest (diastole), −90 mV, potassium inside. 0 = upstroke: FAST SODIUM CHANNELS open, sodium rushes in."],
   ["Phase 1 / 2 / 3", "1 = early repolarization (sodium closes). 2 = PLATEAU: CALCIUM IN causes contraction, balanced by potassium OUT. 3 = rapid repolarization: calcium closes, potassium out, back to −90 mV. (Slide text says potassium “in”; its own figure shows efflux.)"],
   ["Depolarization vs repolarization", "Depolarization = membrane LESS negative, ACTIVATION, PRECEDES contraction. Repolarization = return toward rest, RECOVERY."],
   ["Absolute refractory", "Will NOT respond. Phase 0 to MID phase 3, about 180 ms."],
   ["Relative refractory", "WILL respond but fragile. Mid phase 3 to END of phase 3. The T-WAVE PEAK divides the two. Basis of R on T, P on T and the danger of a long QTc."],
 ]},
 {"id": "conduction", "label": "Conduction System", "color": "#8f4a3a", "rows": [
   ["Sinoatrial node", "Main pacemaker, upper right atrium below the vena cava. 60–100 per minute. Three internodal tracts; most people use the superior anterior (FAST) tract."],
   ["Atrioventricular node", "Near the coronary sinus. PAUSES and AMPLIFIES the signal; back-up pacemaker. 40–60 per minute."],
   ["Bundle of His", "The ONLY electrical path from atria to ventricles in a normal heart, through the nonconductive atrioventricular septum."],
   ["Bundle branches", "Left splits into THREE fascicles (posterior, septal, anterior). Right is MUCH LONGER than the left. Bifascicular block is NOT a left bundle branch block."],
   ["Purkinje network", "Third pacemaker, 20–40 per minute; fastest conduction of all."],
   ["Cardiac vector", "Direction and strength of current; true pathway is LEFT AND DOWN toward the anterior chest."],
 ]},
 {"id": "paper-leads", "label": "Paper, Leads & Rate", "color": "#2b6f86", "rows": [
   ["Time", "Small box 0.04 s · large box 0.2 s · 5 large boxes = 1 s. Strips are 3 or 6 seconds."],
   ["Voltage", "Small box 1 mm = 0.1 mV; 10 mm (two large boxes) = 1 mV."],
   ["Bipolar vs unipolar", "BIPOLAR = two electrodes: I, II, III (Einthoven's triangle). UNIPOLAR = one electrode: aVR, aVL, aVF (augmented) and V1–V6."],
   ["10 wires, 12 leads", "Four limb electrodes make SIX hexaxial leads (I, II, III, aVR, aVL, aVF, used for axis); plus six chest leads. Placement must be MEMORIZED."],
   ["Lead II", "Best view of the heart's vector, so it is the RHYTHM lead."],
   ["Which leads look where", "Inferior II, III, aVF · septum V1–V2 · anterior V3–V4 · lateral I, aVL, V5–V6. Anteroseptal infarction shows in V1–V4 (both supplied by the left anterior descending artery)."],
   ["Cannot tell you", "Hemodynamic status, cardiac output, or WHETHER THERE IS A PULSE."],
   ["Rate methods", "REGULAR rhythms only. 6-second: QRS count × 10 (P count × 10 for atrial). 300 method: heavy lines count 300, 150, 100, 75, 60, 50."],
 ]},
 {"id": "intervals", "label": "Waves & Intervals", "color": "#1f5566", "rows": [
   ["P wave", "Atrial depolarization; under 0.12 s; upright in lead II."],
   ["PR interval", "0.12–0.20 s (3–5 small boxes): atria, atrioventricular node delay, His-Purkinje."],
   ["QRS", "Ventricular depolarization; under 0.12 s, narrow and sharp. Q = septum, R = anterior left ventricle, S = lateral left ventricle."],
   ["J point & ST", "J point = end of QRS, start of ST; at baseline (1 mm variance). “Very important that you know how to identify the J point.” ST = ventricles holding contraction; at baseline."],
   ["T wave", "Ventricular repolarization, 0.16–0.25 s."],
   ["QT / QTc", "Start of QRS to end of T. 350–450 ms males, 360–460 ms females. QTc = rate-corrected; above 450 (460) to 500 = borderline; ABOVE 500 ms = HIGH-RISK."],
   ["U wave & TP", "U: after T, same direction, best V2–V3; prominent in hypokalemia, hypercalcemia, long QT, post-infarction. TP segment = best place to judge the isoelectric line."],
   ["The system", "Rhythm → rate → P waves → P for every QRS → QRS width → PR → ST → T → QTc → extra waves or beats → voltage."],
 ]},
 # ---------------- Lecture 8 ----------------
 {"id": "cxr", "label": "Chest Radiograph & Cardiothoracic Ratio", "color": "#7a4d1f", "rows": [
   ["Its standing", "NOT the primary modality for function or detailed anatomy, but gives clues when obtained: silhouette, great vessels, pulmonary vasculature, lungs and pleura."],
   ["Right border", "Superior vena cava → right atrium."],
   ["Left border", "Aortic knuckle → main pulmonary artery → left atrial appendage → left ventricle (forms the apex)."],
   ["Cardiac findings", "Pulmonary edema · pleural effusion · cardiomegaly · CEPHALIZATION · great vessel, valve or pericardial calcification · tension physiology."],
   ["Cephalization", "Upper-lobe vessels bigger than lower. Heart failure or pulmonary hypertension."],
   ["Cardiothoracic ratio", "Widest heart ÷ widest INTERNAL thorax. Normal 0.42–0.5; ABOVE 0.5 on a PROPER POSTEROANTERIOR film suggests cardiomegaly."],
 ]},
 {"id": "echo-stress", "label": "Echocardiography & Stress Testing", "color": "#8a5a24", "rows": [
   ["Echo shows", "STRUCTURE AND FUNCTION: chambers, walls, ejection fraction, Doppler flow, valves, shunts, pressures."],
   ["TTE (transthoracic echocardiogram)", "Most common, bedside, noninvasive. Poor for the POSTERIOR heart."],
   ["TEE (transesophageal echocardiogram)", "Probe in the esophagus. Aorta and great vessels, myxoma, prosthetic valves, VEGETATIONS, cerebral ischemia, LEFT ATRIAL APPENDAGE THROMBUS."],
   ["TEE contraindications", "Anything the probe can injure or an airway you cannot protect: esophageal stricture, malignancy, bleeding varices; dysphagia; ZENKER'S DIVERTICULUM; cervical arthritis; sleep apnea; uncooperative patient."],
   ["Valid exercise test", "At least 85% of predicted maximum; predicted maximum = 220 − AGE. Under 85% cannot exclude ischemia."],
   ["Exercise test reads", "Ischemia indirectly: ST DEPRESSION or new premature ventricular contractions. Bruce protocol; bicycle preferred."],
   ["Echo stress", "Can exercise but baseline ST-T changes. Look for NEW WALL-MOTION abnormality right after exercise."],
   ["Pharmacologic stress", "Cannot exercise. ADENOSINE or DIPYRIDAMOLE vasodilate; DOBUTAMINE raises workload."],
 ]},
 {"id": "ct-mri-nuclear", "label": "Nuclear, CT (Computed Tomography) & MRI (Magnetic Resonance Imaging)", "color": "#2b6f86", "rows": [
   ["Nuclear perfusion", "Tracer at rest and after stress. Less uptake after stress = ischemia; NO uptake = dead tissue (VIABILITY). More accurate than standard or echo stress."],
   ["Coronary CT angiography", "Presence and distribution of coronary disease; detect or exclude stenosis or plaque; EQUIVOCAL OR NON-DIAGNOSTIC STRESS TEST → next best step."],
   ["Cardiac CT", "Non-contrast = CALCIUM SCORING. Metoprolol slows the heart, nitroglycerin dilates, electrocardiogram gating."],
   ["CT limits", "ANATOMY ONLY, NOT FUNCTION. Radiation, contrast, rate dependent, BLOOMING artifact overstates calcium."],
   ["Cardiac magnetic resonance", "Anatomy, function, viability, perfusion, INFLAMMATION — no ionizing radiation or iodinated contrast. ECHO FIRST. Aorta, congenital disease, cardiomyopathies, myocarditis, sarcoid."],
   ["Magnetic resonance limits", "Implants (aneurysm clips, some pacemakers), long acquisition, claustrophobia. Titanium is acceptable."],
 ]},
 {"id": "invasive", "label": "Angiography, Catheterization & Vascular Ultrasound", "color": "#1f5566", "rows": [
   ["GOLD STANDARD", "Coronary angiography for coronary disease — “a high-miss last year.” Can treat in the same sitting (balloon, stent)."],
   ["Why go to the catheter", "Noninvasive tests say IF disease is there; angiography says HOW MUCH, and intervention is by percentage. Positive CT angiogram with left anterior descending disease → catheter."],
   ["Left vs right heart cath", "LEFT (artery) = CORONARY ARTERIES. RIGHT (vein) = PULMONARY HYPERTENSION."],
   ["Complications", "Access-site HEMATOMA and PSEUDOANEURYSM (pulsatile, communicates with the artery). Always check the site."],
   ["Electrophysiology testing", "Catheters via a vein into the right heart provoke and locate an arrhythmia; ablation can treat it."],
   ["Vascular ultrasound", "Veins COLLAPSE, arteries PULSATE on compression. Deep vein thrombosis, carotid, peripheral arterial disease, aneurysm, venous insufficiency. No radiation; HIGHLY OPERATOR DEPENDENT."],
 ]},
 # ---------------- Lecture 9 ----------------
 {"id": "biomarkers", "label": "The Four Cardiac Biomarkers", "color": "#a1363a", "rows": [
   ["The frame", "Biomarkers: “is there ACUTE cardiac injury or stress?” Lipids: “what is the LONG-TERM atherosclerotic risk?”"],
   ["Troponin", "Myocyte INJURY. Marker of choice. Infarction = above the 99th PERCENTILE upper reference limit + ischemic symptoms. Sex-specific limits."],
   ["Troponin subunits", "I = CARDIAC SPECIFIC. T = mostly cardiac, trace skeletal. C = NOT useful."],
   ["High-sensitivity troponin", "The ASSAY, not a subunit. Draw at 0 and 1–2 HOURS; up to 90 minutes earlier. Pitfall: measurable in healthy people."],
   ["Injury vs infarction", "Injury = any elevation. Infarction = injury + ISCHEMIA + RISING/FALLING pattern. Chronically raised in kidney disease, heart failure, structural disease — never read one value alone."],
   ["Creatine kinase", "Skeletal muscle: RHABDOMYOLYSIS, STATIN MYOPATHY. Low cardiac specificity. Creatine kinase-MB, myoglobin, lactate dehydrogenase are RETIRED for infarction."],
   ["BNP (B-type natriuretic peptide)", "STRETCH, not injury. Rule-out of new heart failure; monitor, guide, prognosis. Rises with age, female sex, kidney disease; FALSELY LOW IN OBESITY. Not stand-alone."],
   ["hs-CRP (high-sensitivity C-reactive protein)", "Inflammation; a RISK ENHANCER, never an acute test. Non-specific. Highest in bacterial infection. Lowered by statins, NSAIDs (nonsteroidal anti-inflammatory drugs), GLP-1 (glucagon-like peptide-1) agonists, lifestyle. In the Reynolds Risk Score."],
 ]},
 {"id": "order-biomarkers", "label": "When to Order Which", "color": "#7a2a2e", "rows": [
   ["Chest pain", "SERIAL HIGH-SENSITIVITY TROPONIN, first-line; first value is also prognostic."],
   ["Dyspnea / heart failure", "BNP (B-type natriuretic peptide) or NT-proBNP (N-terminal pro B-type natriuretic peptide); also prognostic after acute coronary syndrome."],
   ["Muscle pain on a statin", "CREATINE KINASE, not troponin."],
   ["Risk refinement", "hs-CRP (high-sensitivity C-reactive protein) in select primary prevention."],
   ["Do NOT order", "Routine natriuretic peptides in healthy people; creatine kinase-MB or myoglobin for infarction."],
   ["Troponin, other uses", "Unstable angina (normal = no injury) · reinfarction · infarct size (late 4-week value INVERSELY related to ejection fraction) · procedural: type 4a more than 5×, type 5 (bypass) more than 10× the 99th percentile limit."],
 ]},
 {"id": "lipoproteins", "label": "Lipoproteins & Apolipoproteins", "color": "#7a4d1f", "rows": [
   ["Why particles", "Cholesterol and triglycerides are INSOLUBLE. Lipoprotein = lipid core + phospholipid shell + apolipoproteins."],
   ["One apoB particle", "Liver VLDL (very low-density lipoprotein) → lipoprotein lipase strips triglyceride → remnant → LDL (low-density lipoprotein). Under ~70 nm can be TRAPPED in the artery wall."],
   ["ApoB-48 / ApoB-100", "B-48 = intestine, CHYLOMICRONS. B-100 = liver: very low-, intermediate-, low-density lipoprotein and lipoprotein(a). NOT in HDL (high-density lipoprotein)."],
   ["ApoA-I / ApoE", "A-I = ALL HDL (high-density lipoprotein). E = triglyceride CLEARANCE. C-III and A-V regulate triglyceride metabolism."],
   ["LDL vs HDL", "LDL (low-density lipoprotein) = PRINCIPAL DRIVER, log-linear with risk. HDL = REVERSE CHOLESTEROL TRANSPORT. Remnants carry RESIDUAL risk."],
   ["Lipoprotein(a)", "LDL-like + apo(a) on apoB-100. Over 90% GENETIC, stable, NO FASTING, measure ONCE in all adults; repeat after menopause if borderline; CASCADE test families. STATINS DO NOT LOWER IT. About 20% of people elevated."],
 ]},
 {"id": "lipid-panel", "label": "Ordering & Reading a Lipid Panel", "color": "#8a5a24", "rows": [
   ["Measured", "Total cholesterol, HDL-C (high-density lipoprotein cholesterol), triglycerides."],
   ["Calculated", "LDL-C (low-density lipoprotein cholesterol) — an ESTIMATE — and non-HDL-C = total cholesterol − HDL-C."],
   ["Friedewald", "LDL-C = total − HDL-C − triglycerides ÷ 5. INVALID when triglycerides are 400 mg/dL or above; Martin/Hopkins or Sampson/NIH (National Institutes of Health) preferred."],
   ["Non-HDL-C", "Every atherogenic apoB lipoprotein, NO added cost, BETTER predictor than LDL-C."],
   ["No single normal", "LDL-C and non-HDL-C goals depend on RISK TIER; triglyceride, apoB and lipoprotein(a) thresholds are fixed. HDL-C is a MARKER, not a target."],
   ["Triglycerides", "150+ = risk enhancer · 500+ = SEVERE, PANCREATITIS risk · 1000+ = extreme."],
   ["ApoB", "Modifiable, repeated to monitor therapy; use with triglycerides 150+, diabetes or low LDL-C to find residual risk."],
   ["Fasting?", "NONFASTING for most. Fasting with triglycerides 400+, a triglyceride disorder, or FAMILY HISTORY OF PREMATURE DISEASE or genetic dyslipidemia."],
   ["Screening", "Children 9–11 (from age 2 with family history or familial hypercholesterolemia) · again at 19 · adults about EVERY 5 YEARS · on therapy recheck 4–12 WEEKS, then every 6–12 months."],
 ]},
 {"id": "risk", "label": "Risk Assessment", "color": "#2b6f86", "rows": [
   ["PREVENT (Predicting Risk of cardiovascular disease EVENTs)", "Lipids feed a 10-YEAR risk estimate, which sets treatment intensity."],
   ["Calculate → Personalize → Reclassify", "Low under 3% · borderline 3 to under 5% (add RISK ENHANCERS) · intermediate 5 to under 10% · high 10% or above."],
   ["Uncertain?", "At borderline or intermediate risk, a CORONARY ARTERY CALCIUM SCORE reclassifies."],
   ["LDL-C goals", "Under 100 if risk under 10% · under 70 if 10%+, familial hypercholesterolemia, diabetes with risk factors, or calcium 100+ · under 55 for very-high-risk clinical disease. 190+ = statin regardless of risk."],
   ["Elevated lipoprotein(a)", "Earlier, more intensive control of EVERY OTHER risk factor."],
 ]},
]

html = render(
    title="Cram Sheet — Principles of Diagnostic Medicine I Exam 2",
    kicker="Principles of Diagnostic Medicine I Exam 2 · Class of 2028",
    h1="Principles of Diagnostic Medicine I Exam 2 Cram Sheet",
    sub="Lectures 7, 8 and 9. Electrocardiography — the action potential, the conduction system, paper, leads, rate and the normal intervals. Cardiac imaging — the chest radiograph, echocardiography, stress testing, nuclear, computed tomography, magnetic resonance, angiography and vascular ultrasound. Cardiac biomarkers and lipid testing. Opens with how the exam is written.",
    topics=topics,
    guide_href="pdm-exam-2-study-guide.html",
    footer_note="Condensed from the Principles of Diagnostic Medicine I Exam 2 Study Guide (Class of 2028). Covers Lectures 7–9; Lecture 10 (Coagulation and Hemostasis Testing) is added when its deck is posted. Emphasis rows quote the 15 and 17 September 2026 recordings; the Lecture 9 rows are from the slides alone.",
)
assert not re.search(r"(?i)haem|oedem|tumour|colour|centre|anaem|oesoph", html)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.basename(OUT), len(html) // 1024,
      len(topics), sum(len(t["rows"]) for t in topics)))
