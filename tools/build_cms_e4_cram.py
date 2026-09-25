#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 4 cram sheet.

Condensed from the Exam 4 study guide, per the template README: compress what
the guide already says, keep numbers and names verbatim, add nothing new.

Topics matching the guide's sections: six for Hypertension, then three each for
Hypotension, Lipids and Valvular Heart Disease and two for Heart Failure (added
2026-09-25). More will be added as the rest of the
cardiovascular block is posted -- the sub line says so rather than implying the
block is complete.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

topics = [
{"id": "def", "label": "Definitions & Classification", "color": "#702d7a", "rows": [
 ["Treatment goal", "<b>Below 130/80</b>, with values closer to 120/80 encouraged where appropriate. The same number defines the condition and measures control."],
 ["Primary (essential)", "No single identifiable underlying cause. <b>The vast majority of adult cases.</b>"],
 ["Secondary", "An identifiable underlying condition drives the pressure. Go looking when the <i>pattern</i> is wrong (see next topic)."],
 ["Resistant", "Above goal despite <b>three complementary drugs at maximally tolerated doses</b>."],
 ["Hypertensive emergency", "Severe elevation <b>with acute hypertension-mediated organ injury</b>. <b>No numeric cutoff exists</b> &mdash; 230/130 with no acute organ involvement is severe <i>asymptomatic</i> hypertension. Qualifying injury: encephalopathy, acute pulmonary edema, acute kidney injury, aortic dissection, acute coronary syndrome."],
 ["White coat vs masked", "<b>White coat</b> = high office, normal out-of-office. <b>Masked</b> = normal office, high out-of-office &mdash; and it carries <b>real cardiovascular risk</b>, which is why out-of-office measurement is not only about avoiding overtreatment."],
 ["Epidemiology", "Roughly <b>one in five</b> of those affected are controlled to goal nationally. <b>Prevalence rises sharply with age</b>: 23.4% at 18&ndash;39 years, 52.5% at 40&ndash;59 and 71.6% at 60 and over."],
 ["Risk factors (primary)", "Advancing age &middot; family history &middot; excess adiposity &middot; high dietary sodium &middot; inactivity &middot; excess alcohol &middot; dyslipidemia &middot; insulin resistance. Low potassium intake and poor sleep are modifiable too."],
]},

{"id": "secondary", "label": "Secondary Causes", "color": "#8a5a2b", "rows": [
 ["When to go looking", "<b>Early onset &middot; abrupt new onset &middot; resistance &middot; sudden loss of previously stable control.</b> The pattern is the clue, not any single reading."],
 ["Chronic kidney disease", "Impaired sodium excretion expands extracellular volume, with renin-angiotensin-aldosterone and sympathetic activation. Needs an abnormality persisting <b>&ge; 3 months</b>. Relationship is <b>bidirectional</b> &mdash; evaluate diabetes rather than assuming which came first."],
 ["Renovascular disease", "Atherosclerotic (older, vascular, often bilateral and progressive) or fibromuscular dysplasia (young). Clues: resistant or abrupt elevation &middot; <b>abdominal bruit</b> &middot; <b>asymmetric kidneys</b> &middot; recurrent <b>flash pulmonary edema</b> &middot; <b>marked creatinine rise after starting an ACE inhibitor</b>. Refer early for flash edema, progressive renal decline despite optimal therapy, or truly refractory control."],
 ["Primary aldosteronism", "<b>Autonomous aldosterone production independent of renin.</b> Screen for resistant pressure, <b>unexplained hypokalemia</b>, adrenal incidentaloma, early or familial hypertension. Test: <b>morning aldosterone to renin ratio</b>, positive above roughly <b>20:1</b> with an adequate aldosterone concentration."],
 ["Obstructive sleep apnea", "Recurrent airway obstruction &rarr; intermittent hypoxemia and arousal &rarr; <b>sustained sympathetic activation</b>. Snoring, witnessed apneas, daytime sleepiness. Confirm with <b>polysomnography or validated home testing</b>."],
 ["Drugs & substances", "Ask beyond the prescription list: <b>over-the-counter drugs, recreational substances, licorice, herbal supplements</b>. Excess alcohol raises pressure chronically, and <b>withdrawal can raise it acutely</b>."],
 ["Thyroid", "<b>Hyper</b> &rarr; raises cardiac output &rarr; <b>systolic</b> elevation. <b>Hypo</b> &rarr; raises vascular resistance &rarr; <b>diastolic</b> elevation."],
 ["Cushing syndrome", "Glucocorticoid excess. Proximal muscle weakness &middot; easy bruising &middot; thin skin &middot; broad purple striae &middot; central adiposity. Test: low-dose dexamethasone suppression."],
 ["Pheochromocytoma", "Catecholamine excess. The <b>five Ps</b>: pressure, perspiration, palpitations, pallor, tremor &mdash; <b>paroxysmal, with well intervals</b>. Test: plasma free metanephrines or 24-hour urinary fractionated metanephrines. <b>Surgery: ALPHA blockade first, then beta</b> &mdash; isolated beta blockade is dangerous."],
 ["Coarctation", "<b>Radial-femoral delay</b>; leg systolic <i>lower</i> than arm (<b>normally it is higher</b>). <b>Echocardiography</b> establishes it; refer to a vascular surgeon or structural cardiologist."],
]},

{"id": "organ", "label": "Target Organ Damage", "color": "#a3341f", "rows": [
 ["Heart", "Left ventricular hypertrophy with impaired diastolic relaxation &mdash; <b>independently</b> raises risk. Progresses to heart failure with <b>either preserved OR reduced</b> ejection fraction, so <b>a normal ejection fraction does not reassure</b>."],
 ["Brain", "<b>Both</b> ischemic stroke and intracerebral hemorrhage, plus small-vessel white matter change, lacunar infarcts and cognitive decline. <b>Acute stroke follows a distinct protocol &mdash; never apply chronic targets acutely.</b>"],
 ["Kidney", "Injury to vessels, glomeruli and interstitium. Earliest markers: <b>rising urine albumin-to-creatinine ratio, falling estimated filtration rate</b> &mdash; both read as <i>trends</i>."],
 ["Aorta", "Dissection: abrupt severe chest/back/abdominal pain, <b>maximal at onset</b>, often tearing. Pulse deficits, asymmetric arm pressures, aortic regurgitation murmur, new neurological deficit. <b>Neither normal pulses NOR a normal chest radiograph excludes it.</b> Immediate cross-sectional vascular imaging; urgent surgery."],
 ["Arteries", "Shear stress &rarr; intimal injury &rarr; low-density lipoprotein oxidation &rarr; smooth muscle proliferation. <b>Treat total cardiovascular risk, not pressure alone.</b>"],
 ["Retina", "Predicts long-term stroke risk <b>independently of the pressure level</b>; retinal arterial narrowing predicts future hypertension; <b>control can produce regression</b>. <b>Focal</b> narrowing, hemorrhages and exudates = <b>current</b> pressure. <b>Generalized</b> narrowing and AV nicking = <b>current AND previous</b>. Disc edema = emergency."],
]},

{"id": "assess", "label": "Assessment", "color": "#2f5d6b", "rows": [
 ["Symptoms", "Most patients with mild to moderate primary hypertension have <b>no reliable blood pressure-related symptoms</b>. Headache is common but nonspecific and cannot guide anything."],
 ["Immediate evaluation", "Confusion or seizures &middot; visual disturbance or focal deficit &middot; <b>abrupt severe</b> headache &middot; chest or severe back pain &middot; oliguria."],
 ["Measurement technique", "Rest <b>&ge; 5 minutes</b>, empty bladder, no smoking/caffeine/vigorous activity for 30 minutes. Back supported, feet flat, <b>legs uncrossed</b>, bare arm at heart level, <b>not speaking</b>. Cuff matched to arm circumference. At least two readings. <b>Both arms initially &mdash; use the higher consistent arm at follow-up.</b>"],
 ["Why technique matters", "Measurement error is one of the first things to exclude before labeling a patient resistant &mdash; <b>bad technique mimics true resistance exactly</b>."],
 ["Baseline panel", "Creatinine with filtration rate, <b>urine albumin-to-creatinine ratio</b>, electrolytes, glucose or glycated hemoglobin, lipids, thyroid-stimulating hormone, full blood count, urinalysis. Three jobs at once: screen secondary causes, measure organ damage, set a baseline before drugs that move potassium and creatinine."],
 ["Electrocardiogram", "Voltage criteria for hypertrophy are <b>specific but NOT sensitive</b> &mdash; a normal tracing does <i>not</i> exclude hypertensive heart disease."],
 ["Not routine", "<b>Chest radiograph</b> &mdash; only for suspected pulmonary edema, cardiomegaly, or widened mediastinum. <b>Echocardiography</b> &mdash; only for suspected heart failure, significant murmur, hypertrophy on ECG, or unexplained dyspnea."],
 ["Home monitoring", "Validated upper-arm device. <b>Two readings a minute apart, morning and evening, seven days; report the average.</b> Educate: <b>do not overreact to the highest single reading.</b>"],
]},

{"id": "treat", "label": "Treatment", "color": "#1f5c3a", "rows": [
 ["Lifestyle", "Recommended at <b>every</b> blood pressure category, and continues alongside drugs. DASH-style with reduced sodium &middot; ~<b>150 min/week</b> moderate aerobic plus resistance training &middot; sustained <b>5&ndash;10 kg</b> loss meaningfully lowers systolic &middot; alcohol to low-risk thresholds (<b>never start alcohol for cardiovascular benefit</b>)."],
 ["First-line classes", "<b>Thiazide-type diuretic</b> (chlorthalidone preferred) &middot; <b>ACE inhibitor OR angiotensin receptor blocker</b> &middot; <b>dihydropyridine calcium channel blocker</b>. Beta blockers are deliberately absent."],
 ["Thiazide", "Monitor electrolytes, uric acid, volume status. Hyponatremia &middot; hypokalemia &middot; <b>hyperuricemia may precipitate gout</b> &middot; volume depletion. <b>At 65+, check sodium</b> &mdash; especially women and low-normal sodium. With a beta blocker: higher new-onset diabetes risk."],
 ["ACE inhibitor / ARB", "<b>Dry cough</b> (bradykinin-mediated, up to ~1 in 5 &rarr; switch to an ARB) &middot; hyperkalemia &middot; creatinine rise &middot; <b>angioedema</b>, <b>2&ndash;4&times; more common in Black patients</b>. <b>Avoid:</b> pregnancy, prior angioedema, bilateral renal artery stenosis."],
 ["Dihydropyridine", "<b>Dependent ankle edema</b> is commonest &mdash; vasodilatory, so <i>a diuretic does not fix it</i>. Also flushing, headache, gingival enlargement."],
 ["NEVER combine", "<b>ACE inhibitor + ARB</b> &mdash; hyperkalemia and acute kidney injury risk <i>with no added benefit</i>; one is used INSTEAD of the other. <b>Beta blocker + verapamil/diltiazem</b> &mdash; both slow the sinus and AV nodes &rarr; severe bradycardia and heart block. Non-dihydropyridines are also avoided where the ejection fraction is reduced."],
 ["Beta blockers", "<b>NOT first-line</b> for uncomplicated hypertension. Preferred where the comorbidity selects them: <b>heart failure with reduced ejection fraction, recent myocardial infarction, ischemic disease</b>."],
 ["Starting", "<b>Stage 1</b> &rarr; one first-line agent. <b>Stage 2</b> &rarr; two complementary agents, ideally a <b>single-pill combination</b> (adherence is itself a main determinant of control). <b>Preferred pairings:</b> a renin-angiotensin blocker with <i>either</i> a dihydropyridine <i>or</i> a thiazide-type diuretic."],
]},

{"id": "resist", "label": "Resistance & Emergency", "color": "#7a2d47", "rows": [
 ["Exclude the impostors first", "<b>Nonadherence is the commonest cause</b> of apparent resistance. Then measurement error &middot; white coat effect &middot; high sodium or alcohol &middot; interfering drugs &middot; undiagnosed sleep apnea or secondary hypertension."],
 ["Step 1", "<b>Optimize the diuretic</b> &mdash; chlorthalidone preferred, class matched to renal function. An inadequate diuretic is a common reason the other two agents appear to fail."],
 ["Step 2", "Titrate the renin-angiotensin blocker and the dihydropyridine to maximally tolerated doses."],
 ["Step 3", "Add <b>spironolactone</b> &mdash; the most evidence-supported fourth agent &mdash; if filtration rate and potassium allow."],
 ["Step 4", "Escalate by physiology and comorbidity: beta blockade &middot; <b>hydralazine</b> (reflex tachycardia and fluid retention &rarr; needs combination therapy) &middot; <b>clonidine</b> (sedation, dry mouth, <b>rebound hypertension on abrupt withdrawal</b>). Then refer to a hypertension specialist."],
 ["Emergency: how fast", "<b>Reduce mean arterial pressure by no more than ~20&ndash;25% in the first hour</b>, then toward ~160/100&ndash;110 over 2&ndash;6 hours, normalizing gradually over a day or two."],
 ["Emergency: why not faster", "<b>Autoregulation has adapted to the higher pressure.</b> The organs reset the range over which they protect their own perfusion, so normalizing too fast leaves them underperfused at a value that would be safe in anyone else &mdash; causing ischemic stroke, myocardial injury or renal failure."],
 ["Exceptions", "<b>Aortic dissection</b> and <b>some stroke syndromes</b> &mdash; acute stroke follows its own protocol."],
]},

# ---- Lecture 21 (Carter), condensed from guide section 2 ----
{"id": "l21-hypo", "label": "Hypotension: Definitions & Types", "color": "#5a3d8a", "rows": [
 ["Hypotension", "A decrease in systemic pressure below normal. <b>Not a diagnosis</b> &mdash; syncope is the <i>result</i> of symptomatic hypotension; treat the <b>real diagnosis</b>. Norms change with age; consider comorbidities and <b>relative</b> hypotension; each reading is a snapshot."],
 ["Syncope vs near-syncope", "Syncope = transient, self-limited loss of consciousness and postural tone, spontaneous recovery. Near-syncope = dizziness, lightheadedness, tunnel vision <i>without</i> losing consciousness."],
 ["Acute vs chronic", "<b>Acute</b>: sudden, usually symptomatic, specific trigger (toxic or overdose; infection = <i>long-lasting</i> acute). <b>Chronic</b>: waxes and wanes, intermittently symptomatic, cause may be unavoidable (reduced ejection fraction heart failure, cardiomyopathy)."],
 ["Three syncope groups", "<b>Orthostatic</b> (neurogenic, non-neurogenic) &middot; <b>reflex</b> (situational, vasovagal) &middot; <b>cardiogenic</b> (arrhythmia, structural, vascular)."],
 ["Non-hypotensive syncope", "Hypoglycemia, seizure, toxic overdose, electrolyte imbalance, hypoxia, anxiety, anemia, postural tachycardia syndrome. Against seizure: no tongue biting, incontinence or prolonged confusion."],
]},
{"id": "l21-orth", "label": "Orthostatic & Reflex Syncope", "color": "#7a2d5c", "rows": [
 ["&#9733; Orthostatic criteria", "Supine then standing. Systolic fall <b>&gt;20</b> or diastolic <b>&gt;10 mmHg within 3 minutes</b>; systolic <b>&gt;30</b> with elevated baseline or supine hypertension. One criterion is enough (spoken). <b>History is THE most important part.</b>"],
 ["&#9733; The big tell: heart rate", "Pressure falls in both. <b>Significant heart rate rise = non-neurogenic</b> (intact reflex; e.g. 68 &rarr; 92). <b>Minimal rise = neurogenic</b> (autonomic failure; e.g. 72 &rarr; 76)."],
 ["Neurogenic", "Autonomic failure: <b>diabetes, Parkinson disease, multiple system atrophy</b>. Volume depletion usually absent; autonomic symptoms often present. Clue: numb feet in long-standing diabetes."],
 ["Non-neurogenic", "Hypovolemia, medication, <b>advanced age</b>: <b>diarrhea, hemorrhage, diuretics</b>. Volume depletion often present (dry mucous membranes); autonomic symptoms usually absent."],
 ["Orthostatic treatment", "Slow positional changes; treat the underlying cause; iatrogenic &rarr; reduce or remove the drug."],
 ["Vasovagal", "&ldquo;The common faint&rdquo;, most common type, <b>young women</b>. Triggers: emotional stress, fear, pain, heat, prolonged standing. Warm, nauseated, sweaty prodrome."],
 ["Situational", "A bodily function or action: cough, sneeze, <b>micturition</b> (voiding standing at night; alcohol, dehydration, alpha-1 blocker with lisinopril)."],
 ["&#9733; Reflex diagnosis & care", "<b>History, history, history</b> + a <b>log</b> of pattern and frequency. <b>Trigger avoidance</b>; safety precautions during unavoidable triggers."],
]},
{"id": "l21-pots", "label": "Postural Tachycardia, Cardiogenic & Drugs", "color": "#2f5d6b", "rows": [
 ["Postural orthostatic tachycardia syndrome", "Heart rate rise <b>&gt;30 or above 120 within 10 minutes</b> (adolescents: <b>40</b>); improves lying down. Ages 15&ndash;50, women &gt; men, Ehlers-Danlos. <b>Tilt-table</b>: sensitivity 40% (negative tells little), specificity &gt;80%. Water + salt; fludrocortisone. (Deck: &ldquo;positional&rdquo;.)"],
 ["Cardiogenic", "Abrupt collapse <b>without warning</b>, palpitations, heart disease. Arrhythmia &rarr; electrocardiogram, monitor, stress test. Structural &rarr; echocardiogram, stress echo. Vascular &rarr; <b>emergent testing in the emergency department</b>. All: cardiology consultation."],
 ["&#9733; Drug &harr; condition", "<b>Midodrine</b>: best with <b>neurogenic</b>; avoid with supine hypertension, severe heart disease, chronic kidney disease. <b>Fludrocortisone</b>: best with postural tachycardia syndrome; avoid in heart failure (salt and water retention). <b>Droxidopa</b>: mild, better with supine hypertension, adjunct."],
 ["Pressors", "Epinephrine, norepinephrine, dopamine, phenylephrine, vasopressin: <b>emergency department and intensive care only</b>."],
 ["&#9733; Education", "&ldquo;<b>Understanding is the key to compliance.</b>&rdquo; No dosing or mechanism questions."],
]},

# ---- Lecture 22 (Carter), condensed from guide section 3 ----
{"id": "l22-lipo", "label": "Lipids: Garbage System & Lipoproteins", "color": "#8a5a2b", "rows": [
 ["Memory aid: the garbage system", "<i>A story, not a fact.</i> <b>HDL (high-density lipoprotein) = garbage trucks</b> (apo A-I, never apo B): excess cholesterol back to the liver and bile. <b>LDL (low-density lipoprotein) = building-material trucks</b> (B-100), the highest risk &mdash; <b>clear them first</b>, then fuel if triglyceride is still &gt;200. <b>Chylomicrons = gut fuel barges</b> (B-48); <b>VLDL (very-low-density) = liver fuel tankers</b> (B-100) &rarr; IDL (intermediate-density) after drop-off. <b>Lp(a) = delivery truck with an armored trailer</b>. <b>LDL receptor = the liver&rsquo;s gate</b> (broken in familial hypercholesterolemia); <b>PCSK9 = the demolition crew</b>. <b>Apo E = tow ticket</b> for empty tankers."],
 ["Lipoproteins", "Chylomicrons: least dense, after fatty food, triglyceride. VLDL: mainly triglyceride. LDL: mostly cholesterol, &ldquo;bad&rdquo;, <b>highest risk</b>, primary target. HDL: densest, reverse cholesterol transport, &ldquo;good&rdquo;, raised by exercise. Lp(a): LDL-like + apo(a), causal independent risk &rarr; aggressive LDL lowering."],
 ["Apolipoproteins", "B-48 intestine (chylomicrons) &middot; B-100 liver (VLDL, IDL, LDL, Lp(a)) &middot; B absent from HDL &middot; A-I on all HDL &middot; E critical in triglyceride clearance (E2 homozygosity &rarr; dysbetalipoproteinemia)."],
 ["Lab bands (mg/dL)", "Total &lt;200 desirable, &gt;240 high &middot; LDL &lt;100 optimal, 160&ndash;189 high, &gt;190 very high &middot; HDL &lt;40 low, &gt;60 high &middot; Triglyceride &lt;150 normal, 200&ndash;499 high, &gt;500 very high."],
 ["Exam findings", "Eruptive xanthomas (small yellow-white papules, back, buttocks, extensors) &rarr; very high triglyceride. Tendon xanthomas (Achilles, hands) &rarr; high LDL / familial hypercholesterolemia. Xanthelasma; corneal arcus before 40 &rarr; genetic."],
]},
{"id": "l22-disorders", "label": "Lipids: Disorders & Screening", "color": "#a3341f", "rows": [
 ["&#9733; Familial chylomicronemia", "Fasting triglyceride &gt;500, usually <b>&gt;1000</b>; <b>acute pancreatitis</b> (severe abdominal pain), eruptive xanthomas, <b>lipemia retinalis</b> (opalescent retinal vessels). &ldquo;One that can save somebody&rsquo;s life.&rdquo;"],
 ["Severe hypertriglyceridemia", "Triglyceride &gt;500, high total, low HDL, usually no LDL rise; risk = pancreatitis. Very low-fat diet (&lt;15%), weight, activity, <b>fibrate and/or niacin</b>. Take an alcohol history."],
 ["&#9733; Homozygous familial hypercholesterolemia", "Two mutant LDL-receptor alleles; 1 in 1 million; <b>child</b> with xanthomas, total ~400 to &gt;1000, atherosclerosis before puberty. <b>Skin biopsy</b> (receptor activity) confirms. <b>LDL apheresis</b> = treatment of choice; add drugs; refractory &rarr; PCSK9 inhibitor."],
 ["&#9733; Heterozygous familial hypercholesterolemia", "One allele; 1 in 250; <b>adult</b> with LDL 200&ndash;400, normal triglyceride, Achilles xanthomas (~75%), arcus, premature coronary disease in the family. <b>No definitive test.</b> High-intensity statin &rarr; ezetimibe &rarr; PCSK9 inhibitor if refractory (&ldquo;don&rsquo;t jump straight to the PCSK9&rdquo;)."],
 ["Other genetic types", "Familial defective apo B-100: familial-hypercholesterolemia picture, 1 in 1,500. Mixed: triglyceride &gt;150 + LDL &gt;130 (most common in practice). Dysbetalipoproteinemia: triglyceride and total <b>both 250&ndash;500</b>, palmar and tuberoeruptive xanthomas, apo E2."],
 ["Low HDL", "&lt;40 (women &lt;50 for metabolic syndrome). Lifestyle first: stop smoking (+10%), weight loss, aerobic exercise (+5%), healthier fats. Rule out diabetes, smoking, obesity; anabolic steroids lower it."],
 ["Metabolic syndrome", "Any 3: waist &gt;40 in men / &gt;35 in women; triglyceride &gt;150; HDL &lt;40 men / &lt;50 women; blood pressure &gt;130/&gt;85; fasting glucose &gt;110. Lifestyle first."],
 ["Secondary causes", "Before a statin rule out: <b>LDL</b> &rarr; hypothyroidism, nephrotic syndrome, primary biliary cirrhosis, anorexia. <b>Triglyceride &ge;500</b> &rarr; diabetes, chronic kidney disease, alcoholism, pregnancy, hypothyroidism. <b>Low HDL</b> &rarr; diabetes, smoking, obesity."],
 ["Screening", "All adults <b>&ge;20</b>. Children once at <b>9&ndash;11</b> (non-fasting), again in late adolescence; from 2 with a family history. Total cholesterol and HDL need no fast; triglyceride and calculated LDL need 9&ndash;12 hours."],
]},
{"id": "l22-tx", "label": "Lipids: Drugs & 2018 Statin Decisions", "color": "#1f5c3a", "rows": [
 ["&#9733; LDL first, then triglyceride", "&ldquo;Address the LDLs, then address the triglycerides.&rdquo; If triglyceride stays &gt;200 after the LDL target, add triglyceride treatment. 200&ndash;499: intensify LDL drugs and/or add fibrate or niacin. Non-HDL = total &minus; HDL."],
 ["&#9733; Drug &harr; lipid", "<b>Statin &rarr; LDL</b> (&darr;25&ndash;63%; monitor lipids, liver function, creatine kinase). <b>Fibrate &rarr; triglyceride</b>. <b>Niacin &rarr; raises HDL best</b>. <b>Ezetimibe, bile acid sequestrant &rarr; add-on LDL</b>. <b>PCSK9 inhibitor</b> (evolocumab, alirocumab) &rarr; refractory familial hypercholesterolemia / very high risk after statin + ezetimibe. Generic names only."],
 ["Statin intensity", "By LDL fall, never milligrams: high &ge;50%, moderate 30&ndash;49%, low &lt;30%."],
 ["&#9733; 2018 risk categories", "10-year risk &lt;5% low (lifestyle) &middot; 5&ndash;7.5% borderline (moderate statin if enhancers) &middot; 7.5&ndash;20% intermediate (moderate, &darr;30&ndash;49%) &middot; &ge;20% high (&darr;&ge;50%). Age 40&ndash;75, LDL 70&ndash;189, no diabetes."],
 ["&#9733; 2018 statin groups", "Clinical ASCVD (atherosclerotic cardiovascular disease) &le;75 &rarr; high intensity. LDL &ge;190 &rarr; high intensity, no risk calculation. Diabetes 40&ndash;75 &rarr; moderate. Very high risk, LDL &ge;70 on max statin &rarr; add ezetimibe, then PCSK9 inhibitor. Uncertain &rarr; coronary artery calcium (0 may defer; &ge;100 statin)."],
 ["Lifestyle", "Saturated fat <b>&lt;7%</b> (slide wins over the spoken 10%), soluble fiber 20&ndash;30 g, plant stanols, lose 5&ndash;10%, 30 minutes activity, stop smoking. <b>2026 / PREVENT: rotations only, not tested.</b>"],
]},

# ---- Lecture 23 (Carter), condensed from guide section 4 (added 2026-09-25) ----
{"id": "l23-murmurs", "label": "Valves: Murmur Words & Test Tips", "color": "#5a3d8a", "rows": [
 ["&#9733; The words", "<b>Harsh / rumble = stenosis</b> &rarr; abnormal forward flow &rarr; pressure overload. <b>Blowing = regurgitation</b> &rarr; abnormal backflow &rarr; volume overload. No audio on the test &mdash; murmurs come as words."],
 ["&#9733; Timing", "<b>Systolic</b>: aortic stenosis, mitral regurgitation, pulmonic stenosis, tricuspid regurgitation. <b>Diastolic</b>: aortic regurgitation, mitral stenosis, pulmonic regurgitation, tricuspid stenosis &mdash; &ldquo;ARMS rest because they are PRetty TiredS&rdquo;."],
 ["&#9733; Where (A-P-E-T-M)", "<b>Aortic</b> 2nd right intercostal space, sternal border &middot; <b>Pulmonic</b> 2nd left &middot; <b>Erb&rsquo;s point</b> 3rd left &middot; <b>Tricuspid</b> 5th, lower left sternal border &middot; <b>Mitral</b> apex, 5th space, midclavicular line. Stems give the location, not the valve name."],
 ["Respiration (RILE)", "<b>Right-sided louder on inspiration</b> (more venous return) &middot; <b>left-sided louder on expiration</b>. Carvallo sign = the inspiratory increase; it tells tricuspid from mitral regurgitation."],
 ["Heart sounds", "S1 = mitral + tricuspid closing &middot; S2 = aortic + pulmonic closing &middot; S3 = dilated, volume-loaded ventricle (systolic failure) &middot; S4 = hypertrophied, pressure-loaded ventricle (diastolic failure, e.g. aortic stenosis)."],
 ["Equal weight", "&ldquo;Just as likely a tricuspid valve question as an aortic valve question.&rdquo; Grading is tested only for aortic and mitral stenosis, plus <b>severe regurgitation = regurgitant fraction &ge;50%</b>."],
]},
{"id": "l23-left", "label": "Valves: Aortic & Mitral", "color": "#7a2d5c", "rows": [
 ["&#9733; Aortic stenosis", "Most common valve disease. &gt;70 degenerative, &lt;70 <b>bicuspid</b>. <b>Harsh systolic crescendo-decrescendo, 2nd right space, to the carotids</b>; softer with Valsalva, standing, handgrip; louder squatting, sitting forward. Forceful apex + <b>delayed, weak carotid = severe</b>."],
 ["&#9733; Aortic stenosis numbers", "Severe = <b>area &lt;1.0 cm&sup2;, mean gradient &gt;40 mmHg, jet &gt;4.0 m/s</b> (&ldquo;4, 40 and 1&rdquo;). Survival: angina 5 y &middot; syncope 3 y &middot; <b>heart failure 2 y (most common, worst)</b>. Symptomatic: <b>75% dead at 3 years</b>."],
 ["&#9733; Aortic stenosis care", "<b>Preload dependent</b>: avoid strenuous activity / competitive sports, dehydration; hypertension &rarr; avoid beta blockers and calcium channel blockers; angina &rarr; <b>avoid nitrates</b>. Surgery: severe + symptomatic systolic dysfunction, or bicuspid &rarr; transcatheter replacement; children / young adults &rarr; balloon valvuloplasty. <b>All on echo &rarr; cardiology.</b>"],
 ["&#9733; Aortic regurgitation", "<b>High-pitched blowing DIASTOLIC</b>, 3rd space / left upper sternal border, to the apex (the slide&rsquo;s &ldquo;holosystolic&rdquo; is struck). <b>Corrigan pulse</b> (water hammer: rapid upstroke, rapid collapse), de Musset (head bobbing), wide pulse pressure. Root causes: Marfan, dissection, aortitis, hypertension."],
 ["Aortic regurgitation care", "Echo finds the <b>cause</b> (root dilation, dissection). Chronic, preserved fraction &rarr; <b>afterload reduction</b>. <b>Acute severe &rarr; emergency replacement (&lt;24 h)</b>; if delayed, IV diuretics + nitroprusside. Falling fraction &rarr; surgery; untreated survival 2&ndash;3 y. Audible murmur &rarr; cardiology."],
 ["&#9733; Mitral stenosis", "<b>Rheumatic</b> (most common; 80% women; ~20 y after the fever). <b>Left atrium enlarges &rarr; atrial fibrillation &rarr; thromboembolism.</b> Hemoptysis, hoarseness (Ortner), dysphagia. <b>Low diastolic rumble at the apex after an opening snap</b>, bell, left side. Severe = <b>&lt;1.0 cm&sup2;, gradient &gt;10, velocity &gt;3.0</b>. Loop diuretic &rarr; balloon valvotomy."],
 ["Mitral regurgitation", "Backflow into the left atrium in systole. Acute: papillary muscle / chordae rupture, endocarditis. <b>Holosystolic blowing at the apex &rarr; axilla</b>; louder squatting, handgrip; softer standing, Valsalva. Severe = <b>regurgitant fraction &ge;50%</b>. Surgery: ejection fraction &lt;60% or end-systolic dimension &gt;40 mm &rarr; clip, transcatheter or surgical replacement."],
 ["Mitral valve prolapse", "Myxomatous; <b>healthy women 15&ndash;30</b>; <b>mid-systolic click at the apex</b>; echo: redundant leaflets &gt;5 mm. Usually benign, no treatment; may progress to mitral regurgitation."],
]},
{"id": "l23-right", "label": "Valves: Right Side & Prosthetic Valves", "color": "#2f5d6b", "rows": [
 ["Pulmonic stenosis", "Almost always congenital (tetralogy of Fallot; carcinoid). <b>Harsh mid-systolic ejection, left upper sternal border, louder on inspiration</b>, split S2. Electrocardiogram: right axis deviation, right ventricular hypertrophy. Mild&ndash;moderate: none, 94% 20-y survival. Severe: diuretics + <b>balloon valvuloplasty</b>. On echo &rarr; cardiology."],
 ["&#9733; Pulmonic regurgitation", "<b>Iatrogenic = most common</b> (after valvotomy / valvuloplasty for outflow obstruction); pulmonary hypertension = the high-pressure cause. <b>Graham Steell</b>: brief early diastolic decrescendo, 2nd left space. Usually incidental. Treat the cause; refer on echo or right heart failure."],
 ["Tricuspid stenosis", "Rheumatic worldwide, congenital in the US; women. Right atrium &rarr; right ventricle blocked. <b>Mid-diastolic rumble near the xiphoid, louder on inspiration</b>; right upper quadrant pain, cold skin. Electrocardiogram: right atrial enlargement out of proportion. Low salt, diuretics, aldosterone antagonist; <b>bioprosthetic</b> replacement. (Suffusion sign not tested.)"],
 ["&#9733; Tricuspid regurgitation", "Most common = <b>annular dilation from pulmonary hypertension</b>; primary = <b>endocarditis in intravenous drug users</b>. <b>Holosystolic, lower left sternal border, louder on inspiration (Carvallo)</b> &mdash; that separates it from mitral regurgitation. Raised jugular pressure, venous thrill; severe: edema, ascites. Annuloplasty."],
 ["&#9733; Mechanical valve", "Titanium and carbon &rarr; <b>lifelong vitamin K antagonist (warfarin)</b> &mdash; over no therapy and over antiplatelets. International normalized ratio: <b>aortic 2.5</b> (2.0&ndash;3.0) &middot; <b>mitral 3.0</b> (2.5&ndash;3.5) &middot; <b>both 3.0</b>. Surgery &rarr; <b>bridge with heparin</b>."],
 ["Biological valve", "Pig or cow tissue &rarr; no anticoagulation beyond the immediate postoperative period; preferred when anticoagulation is contraindicated. (Valve type by age on slide 74 is unsettled &mdash; not learned.)"],
]},

# ---- Lecture 25 (Carter), condensed from guide section 5 ----
{"id": "l25-core", "label": "Heart Failure: Groups, Stages & Classes", "color": "#7a2d47", "rows": [
 ["2022, not the deck", "Tested on the <b>2022</b> guideline; slide 57 (2026 changes) = rotations only. Learn <b>&ldquo;mildly&rdquo;</b> reduced (not &ldquo;moderately&rdquo;), <b>&le;40 / 41&ndash;49 / &ge;50</b> (not &lt;40 / &gt;50), stage D = <b>advanced</b> (not &ldquo;decompensated&rdquo;), calcium channel blockers = <b>avoid</b> (no subclass ranking), beta blockers by <b>class</b>. Digitalis not keyed."],
 ["&#9733; Systolic vs diastolic", "<b>Systolic</b> = squeeze fails: ischemic or dilated cardiomyopathy &rarr; reduced ejection fraction &rarr; normal or low pressure &rarr; <b>third heart sound</b> &rarr; pulmonary edema. <b>Diastolic</b> = relaxation fails: hypertrophic (hypertension) &rarr; preserved fraction &rarr; hypertension &rarr; <b>fourth heart sound</b> &rarr; peripheral then pulmonary edema. Add an elevated B-type natriuretic peptide = slam dunk."],
 ["&#9733; Normal values", "Cardiac output <b>5&ndash;6 L/min</b>. Normal ejection fraction <b>&ge;50%</b> &mdash; the treatment line is 50 and above vs 49 and below."],
 ["Reduced", "Ejection fraction <b>&le;40%</b>."],
 ["Mildly reduced", "<b>41&ndash;49%</b>, never previously &le;40%."],
 ["Preserved", "<b>&ge;50%</b>."],
 ["Improved", "Was &le;40%, now &gt;40% &mdash; history decides the label (30% &rarr; 46% is improved, not mildly reduced)."],
 ["New York Heart Association class", "I no symptoms &middot; II symptoms with exertion &middot; III with slight exertion &middot; IV at rest. A grade of symptoms."],
 ["Stages A&ndash;D (natural history)", "<b>A</b> at risk, normal heart &middot; <b>B</b> pre-heart failure: structural disease, no symptoms (asymptomatic left ventricular hypertrophy = <b>B</b>, not A) &middot; <b>C</b> symptomatic, past or current &middot; <b>D</b> advanced. Never moves backward."],
 ["&#9733; Stage A / B therapy", "<b>Stage A with diabetes &rarr; sodium-glucose cotransporter 2 inhibitor, NOT a beta blocker</b> (&ldquo;it&rsquo;ll be on your test&rdquo;). Stage B adds ACE (angiotensin-converting enzyme) inhibitor (receptor blocker if intolerant) and beta blocker."],
]},
{"id": "l25-dx", "label": "Heart Failure: Diagnosis & Therapy", "color": "#2f5d6b", "rows": [
 ["&#9733; Clinical diagnosis", "Signs and symptoms + an <b>elevated B-type natriuretic peptide</b> or <b>objective congestion</b>. &ldquo;Clinical diagnosis requires congestion; congestion = edema.&rdquo;"],
 ["&#9733; Natriuretic peptide cut-offs", "<b>BNP (B-type natriuretic peptide)</b>: &lt;100 rules out acute failure; 100&ndash;400 gray zone; &gt;400 likely; <b>&gt;900 likely acute</b>. <b>NT-proBNP (N-terminal pro-B-type)</b>: &lt;300 rules out; &gt;125 likely if &lt;75 years, <b>&gt;450 if &gt;75</b>. BNP is degraded by neprilysin, so sacubitril-valsartan alters it."],
 ["Which test answers what", "Echocardiogram: structures, ejection fraction group, definitive for right-sided. Multigated acquisition scan: most accurate ejection fraction. Chest radiograph: effusion, cephalization, Kerley B lines, big heart. Metabolic panel: potassium, renal function. Troponin only if ischemia is suspected."],
 ["Left vs right", "<b>Left</b> = 70&ndash;80%, pulmonary congestion, orthopnea, paroxysmal nocturnal dyspnea. <b>Right</b> = edema, jugular venous distension, hepatomegaly; most often from <b>chronic left failure</b> (also mitral stenosis, pulmonary arterial hypertension); worse prognosis."],
 ["&#9733; Reduced fraction therapy (all strong)", "Angiotensin receptor-neprilysin inhibitor (class II&ndash;III) or ACE inhibitor / receptor blocker (II&ndash;IV) + <b>beta blocker</b> + <b>mineralocorticoid receptor antagonist</b> + <b>sodium-glucose cotransporter 2 inhibitor</b> + diuretics as needed. Hydralazine + isosorbide dinitrate for African American patients, class III&ndash;IV."],
 ["Mildly reduced &amp; preserved", "Diuretics as needed (strong); sodium-glucose cotransporter 2 inhibitor (moderate); the rest weak. &ldquo;Very similar&rdquo; to each other; different from reduced."],
 ["Avoid", "<b>Calcium channel blockers.</b> Inotropes (dobutamine, milrinone) = <b>intensive care only</b>."],
 ["Defibrillator", "Ejection fraction <b>&le;35%</b>, class II&ndash;III, on optimal therapy, life expectancy <b>&ge;1 year</b> (the slide wins over the spoken &ldquo;under a year&rdquo;). After an acute event with fraction &lt;35%: wearable vest &rarr; optimize + rehab &rarr; recheck echo."],
 ["High-output", "Raised output from demand: anemia, hyperthyroidism, arteriovenous fistula (also obesity, chronic lung disease, cirrhosis, Paget disease). Treat the cause; diuretic."],
]},
]

html = render(
    title="Cram Sheet — CMS I Exam 4",
    kicker="Clinical Medicine and Surgery I · Exam 4 · Class of 2028",
    h1="CMS I Exam 4 Cram Sheet",
    sub="Hypertension, hypotension, atherosclerosis and lipid disorders, valvular heart disease "
        "and heart failure condensed: classification and causes, the orthostatic heart-rate tell, "
        "the lipid memory aid and 2018 statin decisions, the murmur words and valve-by-valve "
        "essentials, and the 2022 heart failure groups, stages and therapy. Coronary artery "
        "disease follows when posted.",
    topics=topics,
    guide_href="cms-exam-4-study-guide.html",
    footer_note="Condensed from the CMS I Exam 4 Study Guide (Class of 2028). "
                "For the full explanation behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 4", "cms-exam-4-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics")
