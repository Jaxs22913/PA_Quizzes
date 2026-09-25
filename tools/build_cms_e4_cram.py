#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 4 cram sheet.

Condensed from the Exam 4 study guide, per the template README: compress what
the guide already says, keep numbers and names verbatim, add nothing new.

Six topics matching the guide's sections. More will be added as the rest of the
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
 ["Hypertensive emergency", "Severe elevation <b>with acute hypertension-mediated organ injury</b>. <b>No numeric cutoff exists</b> &mdash; 230/130 with no acute organ involvement is severe <i>asymptomatic</i> hypertension. Qualifying injury: encephalopathy, acute pulmonary oedema, acute kidney injury, aortic dissection, acute coronary syndrome."],
 ["White coat vs masked", "<b>White coat</b> = high office, normal out-of-office. <b>Masked</b> = normal office, high out-of-office &mdash; and it carries <b>real cardiovascular risk</b>, which is why out-of-office measurement is not only about avoiding overtreatment."],
 ["Epidemiology", "Roughly <b>one in five</b> of those affected are controlled to goal nationally. <b>Prevalence rises sharply with age</b>: 23.4% at 18&ndash;39 years, 52.5% at 40&ndash;59 and 71.6% at 60 and over."],
 ["Risk factors (primary)", "Advancing age &middot; family history &middot; excess adiposity &middot; high dietary sodium &middot; inactivity &middot; excess alcohol &middot; dyslipidaemia &middot; insulin resistance. Low potassium intake and poor sleep are modifiable too."],
]},

{"id": "secondary", "label": "Secondary Causes", "color": "#8a5a2b", "rows": [
 ["When to go looking", "<b>Early onset &middot; abrupt new onset &middot; resistance &middot; sudden loss of previously stable control.</b> The pattern is the clue, not any single reading."],
 ["Chronic kidney disease", "Impaired sodium excretion expands extracellular volume, with renin-angiotensin-aldosterone and sympathetic activation. Needs an abnormality persisting <b>&ge; 3 months</b>. Relationship is <b>bidirectional</b> &mdash; evaluate diabetes rather than assuming which came first."],
 ["Renovascular disease", "Atherosclerotic (older, vascular, often bilateral and progressive) or fibromuscular dysplasia (young). Clues: resistant or abrupt elevation &middot; <b>abdominal bruit</b> &middot; <b>asymmetric kidneys</b> &middot; recurrent <b>flash pulmonary oedema</b> &middot; <b>marked creatinine rise after starting an ACE inhibitor</b>. Refer early for flash oedema, progressive renal decline despite optimal therapy, or truly refractory control."],
 ["Primary aldosteronism", "<b>Autonomous aldosterone production independent of renin.</b> Screen for resistant pressure, <b>unexplained hypokalaemia</b>, adrenal incidentaloma, early or familial hypertension. Test: <b>morning aldosterone to renin ratio</b>, positive above roughly <b>20:1</b> with an adequate aldosterone concentration."],
 ["Obstructive sleep apnoea", "Recurrent airway obstruction &rarr; intermittent hypoxaemia and arousal &rarr; <b>sustained sympathetic activation</b>. Snoring, witnessed apnoeas, daytime sleepiness. Confirm with <b>polysomnography or validated home testing</b>."],
 ["Drugs & substances", "Ask beyond the prescription list: <b>over-the-counter drugs, recreational substances, licorice, herbal supplements</b>. Excess alcohol raises pressure chronically, and <b>withdrawal can raise it acutely</b>."],
 ["Thyroid", "<b>Hyper</b> &rarr; raises cardiac output &rarr; <b>systolic</b> elevation. <b>Hypo</b> &rarr; raises vascular resistance &rarr; <b>diastolic</b> elevation."],
 ["Cushing syndrome", "Glucocorticoid excess. Proximal muscle weakness &middot; easy bruising &middot; thin skin &middot; broad purple striae &middot; central adiposity. Test: low-dose dexamethasone suppression."],
 ["Pheochromocytoma", "Catecholamine excess. The <b>five Ps</b>: pressure, perspiration, palpitations, pallor, tremor &mdash; <b>paroxysmal, with well intervals</b>. Test: plasma free metanephrines or 24-hour urinary fractionated metanephrines. <b>Surgery: ALPHA blockade first, then beta</b> &mdash; isolated beta blockade is dangerous."],
 ["Coarctation", "<b>Radial-femoral delay</b>; leg systolic <i>lower</i> than arm (<b>normally it is higher</b>). <b>Echocardiography</b> establishes it; refer to a vascular surgeon or structural cardiologist."],
]},

{"id": "organ", "label": "Target Organ Damage", "color": "#a3341f", "rows": [
 ["Heart", "Left ventricular hypertrophy with impaired diastolic relaxation &mdash; <b>independently</b> raises risk. Progresses to heart failure with <b>either preserved OR reduced</b> ejection fraction, so <b>a normal ejection fraction does not reassure</b>."],
 ["Brain", "<b>Both</b> ischaemic stroke and intracerebral haemorrhage, plus small-vessel white matter change, lacunar infarcts and cognitive decline. <b>Acute stroke follows a distinct protocol &mdash; never apply chronic targets acutely.</b>"],
 ["Kidney", "Injury to vessels, glomeruli and interstitium. Earliest markers: <b>rising urine albumin-to-creatinine ratio, falling estimated filtration rate</b> &mdash; both read as <i>trends</i>."],
 ["Aorta", "Dissection: abrupt severe chest/back/abdominal pain, <b>maximal at onset</b>, often tearing. Pulse deficits, asymmetric arm pressures, aortic regurgitation murmur, new neurological deficit. <b>Neither normal pulses NOR a normal chest radiograph excludes it.</b> Immediate cross-sectional vascular imaging; urgent surgery."],
 ["Arteries", "Shear stress &rarr; intimal injury &rarr; low-density lipoprotein oxidation &rarr; smooth muscle proliferation. <b>Treat total cardiovascular risk, not pressure alone.</b>"],
 ["Retina", "Predicts long-term stroke risk <b>independently of the pressure level</b>; retinal arterial narrowing predicts future hypertension; <b>control can produce regression</b>. <b>Focal</b> narrowing, haemorrhages and exudates = <b>current</b> pressure. <b>Generalised</b> narrowing and AV nicking = <b>current AND previous</b>. Disc oedema = emergency."],
]},

{"id": "assess", "label": "Assessment", "color": "#2f5d6b", "rows": [
 ["Symptoms", "Most patients with mild to moderate primary hypertension have <b>no reliable blood pressure-related symptoms</b>. Headache is common but nonspecific and cannot guide anything."],
 ["Immediate evaluation", "Confusion or seizures &middot; visual disturbance or focal deficit &middot; <b>abrupt severe</b> headache &middot; chest or severe back pain &middot; oliguria."],
 ["Measurement technique", "Rest <b>&ge; 5 minutes</b>, empty bladder, no smoking/caffeine/vigorous activity for 30 minutes. Back supported, feet flat, <b>legs uncrossed</b>, bare arm at heart level, <b>not speaking</b>. Cuff matched to arm circumference. At least two readings. <b>Both arms initially &mdash; use the higher consistent arm at follow-up.</b>"],
 ["Why technique matters", "Measurement error is one of the first things to exclude before labelling a patient resistant &mdash; <b>bad technique mimics true resistance exactly</b>."],
 ["Baseline panel", "Creatinine with filtration rate, <b>urine albumin-to-creatinine ratio</b>, electrolytes, glucose or glycated haemoglobin, lipids, thyroid-stimulating hormone, full blood count, urinalysis. Three jobs at once: screen secondary causes, measure organ damage, set a baseline before drugs that move potassium and creatinine."],
 ["Electrocardiogram", "Voltage criteria for hypertrophy are <b>specific but NOT sensitive</b> &mdash; a normal tracing does <i>not</i> exclude hypertensive heart disease."],
 ["Not routine", "<b>Chest radiograph</b> &mdash; only for suspected pulmonary oedema, cardiomegaly, or widened mediastinum. <b>Echocardiography</b> &mdash; only for suspected heart failure, significant murmur, hypertrophy on ECG, or unexplained dyspnoea."],
 ["Home monitoring", "Validated upper-arm device. <b>Two readings a minute apart, morning and evening, seven days; report the average.</b> Educate: <b>do not overreact to the highest single reading.</b>"],
]},

{"id": "treat", "label": "Treatment", "color": "#1f5c3a", "rows": [
 ["Lifestyle", "Recommended at <b>every</b> blood pressure category, and continues alongside drugs. DASH-style with reduced sodium &middot; ~<b>150 min/week</b> moderate aerobic plus resistance training &middot; sustained <b>5&ndash;10 kg</b> loss meaningfully lowers systolic &middot; alcohol to low-risk thresholds (<b>never start alcohol for cardiovascular benefit</b>)."],
 ["First-line classes", "<b>Thiazide-type diuretic</b> (chlorthalidone preferred) &middot; <b>ACE inhibitor OR angiotensin receptor blocker</b> &middot; <b>dihydropyridine calcium channel blocker</b>. Beta blockers are deliberately absent."],
 ["Thiazide", "Monitor electrolytes, uric acid, volume status. Hyponatraemia &middot; hypokalaemia &middot; <b>hyperuricaemia may precipitate gout</b> &middot; volume depletion. <b>At 65+, check sodium</b> &mdash; especially women and low-normal sodium. With a beta blocker: higher new-onset diabetes risk."],
 ["ACE inhibitor / ARB", "<b>Dry cough</b> (bradykinin-mediated, up to ~1 in 5 &rarr; switch to an ARB) &middot; hyperkalaemia &middot; creatinine rise &middot; <b>angioedema</b>, <b>2&ndash;4&times; more common in Black patients</b>. <b>Avoid:</b> pregnancy, prior angioedema, bilateral renal artery stenosis."],
 ["Dihydropyridine", "<b>Dependent ankle oedema</b> is commonest &mdash; vasodilatory, so <i>a diuretic does not fix it</i>. Also flushing, headache, gingival enlargement."],
 ["NEVER combine", "<b>ACE inhibitor + ARB</b> &mdash; hyperkalaemia and acute kidney injury risk <i>with no added benefit</i>; one is used INSTEAD of the other. <b>Beta blocker + verapamil/diltiazem</b> &mdash; both slow the sinus and AV nodes &rarr; severe bradycardia and heart block. Non-dihydropyridines are also avoided where the ejection fraction is reduced."],
 ["Beta blockers", "<b>NOT first-line</b> for uncomplicated hypertension. Preferred where the comorbidity selects them: <b>heart failure with reduced ejection fraction, recent myocardial infarction, ischaemic disease</b>."],
 ["Starting", "<b>Stage 1</b> &rarr; one first-line agent. <b>Stage 2</b> &rarr; two complementary agents, ideally a <b>single-pill combination</b> (adherence is itself a main determinant of control). <b>Preferred pairings:</b> a renin-angiotensin blocker with <i>either</i> a dihydropyridine <i>or</i> a thiazide-type diuretic."],
]},

{"id": "resist", "label": "Resistance & Emergency", "color": "#7a2d47", "rows": [
 ["Exclude the impostors first", "<b>Nonadherence is the commonest cause</b> of apparent resistance. Then measurement error &middot; white coat effect &middot; high sodium or alcohol &middot; interfering drugs &middot; undiagnosed sleep apnoea or secondary hypertension."],
 ["Step 1", "<b>Optimise the diuretic</b> &mdash; chlorthalidone preferred, class matched to renal function. An inadequate diuretic is a common reason the other two agents appear to fail."],
 ["Step 2", "Titrate the renin-angiotensin blocker and the dihydropyridine to maximally tolerated doses."],
 ["Step 3", "Add <b>spironolactone</b> &mdash; the most evidence-supported fourth agent &mdash; if filtration rate and potassium allow."],
 ["Step 4", "Escalate by physiology and comorbidity: beta blockade &middot; <b>hydralazine</b> (reflex tachycardia and fluid retention &rarr; needs combination therapy) &middot; <b>clonidine</b> (sedation, dry mouth, <b>rebound hypertension on abrupt withdrawal</b>). Then refer to a hypertension specialist."],
 ["Emergency: how fast", "<b>Reduce mean arterial pressure by no more than ~20&ndash;25% in the first hour</b>, then toward ~160/100&ndash;110 over 2&ndash;6 hours, normalising gradually over a day or two."],
 ["Emergency: why not faster", "<b>Autoregulation has adapted to the higher pressure.</b> The organs reset the range over which they protect their own perfusion, so normalising too fast leaves them underperfused at a value that would be safe in anyone else &mdash; causing ischaemic stroke, myocardial injury or renal failure."],
 ["Exceptions", "<b>Aortic dissection</b> and <b>some stroke syndromes</b> &mdash; acute stroke follows its own protocol."],
]},
]

html = render(
    title="Cram Sheet — CMS I Exam 4",
    kicker="Clinical Medicine and Surgery I · Exam 4 · Class of 2028",
    h1="CMS I Exam 4 Cram Sheet",
    sub="Hypertension condensed: classification, the nine secondary causes with their clues, "
        "target organ damage, assessment, the drug classes with what to avoid, and the "
        "resistance and emergency sequences. More topics as the rest of the block is posted.",
    topics=topics,
    guide_href="cms-exam-4-study-guide.html",
    footer_note="Condensed from the CMS I Exam 4 Study Guide (Class of 2028). "
                "For the full explanation behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 4", "cms-exam-4-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics")
