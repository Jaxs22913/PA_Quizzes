# -*- coding: utf-8 -*-
"""Lecture 20 vignette pool B -- Hypertension: organ damage, treatment and resistance.

Pool A carries diagnosis, classification and the secondary causes. Same style
and sourcing.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e4l20_vig_a import IO, C

QUESTIONS = [

Q("Lifestyle treatment", IO,
  "A 38-year-old man has an average home blood pressure of 126/78. He has no diabetes, no kidney "
  "disease and no cardiovascular history. What should he be advised?",
  [["Lifestyle treatment",
    "Correct. An elevated reading that does not yet warrant medication still warrants an intervention, and lifestyle measures continue alongside drugs later rather than being replaced by them. It is recommended at every blood pressure category."],
   ["No intervention is needed until he reaches stage 1",
    "Lifestyle treatment is recommended for every category, including readings below the threshold "
    "for medication."],
   ["Start a thiazide-type diuretic now",
    "Medication is not indicated at this reading, and lifestyle measures apply first and throughout."],
   ["Recheck in five years with no advice in the interim",
    "That defers an intervention recommended at every blood pressure category, including this one."]], C(53)),

Q("Lifestyle treatment", IO,
  "A 46-year-old woman with stage 1 hypertension asks what dietary and activity changes will help. "
  "What should she be told?",
  [["A DASH-style pattern with reduced sodium and exercise",
    "Correct. The pattern is rich in fruit, vegetables, low-fat dairy and whole grains, the activity "
    "target is about 150 minutes a week of moderate aerobic work with resistance training, and a "
    "sustained weight loss of five to ten kilograms can meaningfully lower systolic pressure."],
   ["Sodium restriction alone, with no activity component",
    "Regular aerobic exercise with resistance training is described alongside the dietary pattern."],
   ["A high-protein diet with unrestricted sodium",
    "The recommended pattern is DASH-style with sodium reduced rather than unrestricted."],
   ["Moderate alcohol intake for cardiovascular benefit",
    "Alcohol is limited to low-risk thresholds, and starting alcohol for cardiovascular benefit is "
    "specifically not recommended."]], C(53)),

Q("Initial agent selection", IO,
  "A 52-year-old man with no comorbidities has an average blood pressure of 148/92 after three "
  "months of lifestyle change. Which is an appropriate initial drug choice?",
  [["A thiazide-type diuretic",
    "Correct. One first-line agent is reasonable in stage 1, and the first-line classes are thiazide-type diuretics, renin-angiotensin blockers and dihydropyridine calcium channel blockers. Chlorthalidone is the preferred one."],
   ["A beta blocker",
    "Beta blockers are specifically NOT first-line for uncomplicated hypertension; they are chosen "
    "when a comorbidity such as reduced ejection fraction or ischaemic disease selects them."],
   ["Spironolactone",
    "Spironolactone is the evidence-supported fourth agent in confirmed resistant hypertension "
    "rather than an initial choice."],
   ["Clonidine",
    "Central alpha-2 agonists are limited by sedation and rebound hypertension on withdrawal and are "
    "not first-line."]], C(55)),

Q("Initial agent selection", IO,
  "A 57-year-old woman presents with an average blood pressure of 168/104 and no comorbidities. "
  "How should treatment begin?",
  [["Two complementary first-line agents",
    "Correct. Pressure substantially above goal is the reason to start with two rather than one, and a single pill is preferred because adherence is itself a major determinant of control. A single-pill combination is preferred."],
   ["One first-line agent, titrated upward as needed",
    "A single agent is reasonable in stage 1; at this level two complementary agents are considered."],
   ["Four agents from the outset",
    "Two complementary first-line agents are considered when pressure is substantially above goal, not four."],
   ["Lifestyle measures alone for six months",
    "Lifestyle applies to every category, but it does not replace medication at this level."]], C(65)),

Q("Preferred combinations", IO,
  "A 55-year-old man needs two agents. Which pairing is appropriate?",
  [["An angiotensin receptor blocker with a dihydropyridine",
    "Correct. The preferred combinations pair a renin-angiotensin blocker with either a "
    "dihydropyridine or a thiazide-type diuretic, because the classes act by complementary "
    "mechanisms."],
   ["An ACE inhibitor with an angiotensin receptor blocker",
    "This combination must NEVER be used: dual blockade raises hyperkalaemia and acute kidney injury "
    "risk without additional benefit."],
   ["A beta blocker with verapamil",
    "Both slow the sinus and atrioventricular nodes, so combining them risks severe bradycardia and "
    "heart block."],
   ["Two thiazide-type diuretics together",
    "Duplicating a class adds adverse effects without the complementary mechanism the preferred "
    "pairings provide."]], C(65)),

Q("Dual RAAS blockade", IO,
  "A 63-year-old man on lisinopril remains above goal. A colleague suggests adding losartan. What "
  "is the problem?",
  [["Dual blockade raises hyperkalaemia and kidney injury risk",
    "Correct, and the instruction is absolute rather than cautionary: one is used INSTEAD of the other. The two look complementary if the mechanism is read loosely, which is why the rule is stated so plainly. It adds no benefit in exchange."],
   ["The combination is acceptable if potassium is monitored",
    "The instruction is never to combine them rather than to combine them with monitoring."],
   ["The two cancel each other out pharmacologically",
    "They act at different points on the same pathway rather than cancelling; the problem is "
    "additive harm."],
   ["Angioedema occurs in most patients on the combination",
    "Angioedema is a recognised risk of ACE inhibition specifically; the reason to avoid the "
    "combination is renal and potassium harm."]], C(65)),

Q("ACE inhibitor cough", IO,
  "A 59-year-old woman develops a persistent dry cough six weeks after starting lisinopril. Her "
  "blood pressure is at goal. What is the appropriate response?",
  [["Switch to an angiotensin receptor blocker",
    "Correct. The cough is bradykinin-mediated and occurs in up to about one in five. Angiotensin "
    "receptor blockers do not raise bradykinin, so the effect is lost while the therapeutic action "
    "is kept."],
   ["Add an antitussive and continue the lisinopril",
    "Switching class removes the mechanism rather than masking the symptom, and an equally effective "
    "alternative exists."],
   ["Add losartan to the lisinopril",
    "Dual renin-angiotensin blockade is specifically prohibited because of hyperkalaemia and kidney "
    "injury risk."],
   ["Stop all antihypertensive therapy",
    "A tolerability problem with one agent is managed by substitution rather than by abandoning "
    "treatment."]], C(63)),

Q("Angioedema", IO,
  "A 48-year-old Black man develops lip and tongue swelling three months after starting an ACE "
  "inhibitor. What should be known about this?",
  [["It is two to four times more common in this group",
    "Correct. It is a bradykinin-mediated class effect of ACE inhibition. Angiotensin receptor blockers can usually be used instead, though angioedema with them remains possible. An angiotensin receptor blocker is usually substituted."],
   ["It is a dose-related effect that resolves on dose reduction",
    "It is a class effect rather than a dose phenomenon, and the agent is stopped rather than "
    "reduced."],
   ["An angiotensin receptor blocker carries no risk whatsoever",
    "Angioedema with an angiotensin receptor blocker remains possible, although substitution is "
    "usually appropriate."],
   ["A beta blocker is the appropriate substitution",
    "The usual substitution is an angiotensin receptor blocker, and beta blockers are not first-line "
    "for uncomplicated hypertension."]], C(63)),

Q("Calcium channel blockers", IO,
  "A 66-year-old woman on amlodipine reports swollen ankles that are worse by evening. Her jugular venous pressure is normal and her lungs are clear. What is the most likely explanation?",
  [["Dependent ankle oedema",
    "Correct. It follows from arterial vasodilation rather than fluid overload, which is why a diuretic does not fix it. Flushing, headache and gingival enlargement belong to the same class. It is the commonest effect of a dihydropyridine."],
   ["Heart failure requiring a loop diuretic",
    "A normal jugular venous pressure and clear lungs argue against fluid overload, and the oedema "
    "here is vasodilatory."],
   ["An adverse effect of renin-angiotensin blockade",
    "Ankle oedema is a dihydropyridine effect; renin-angiotensin blockers cause cough, "
    "hyperkalaemia, a creatinine rise and angioedema."],
   ["Hypoalbuminaemia from thiazide therapy",
    "Thiazide concerns are hyponatraemia, hypokalaemia, hyperuricaemia and volume depletion."]],
  C(57)),

Q("Non-dihydropyridines", IO,
  "A 70-year-old man with hypertension and atrial fibrillation is on metoprolol. A colleague "
  "suggests adding verapamil for rate control and blood pressure. What is the concern?",
  [["Severe bradycardia and heart block",
    "Correct. Both agents slow the sinus and atrioventricular nodes, so combining them stacks the "
    "same effect. Both are also avoided where the ejection fraction is already reduced."],
   ["Hyperkalaemia and acute kidney injury",
    "Hyperkalaemia and kidney injury follow dual renin-angiotensin blockade rather than this combination."],
   ["Dependent ankle oedema",
    "Ankle oedema is the commonest effect of the DIHYDROPYRIDINE calcium channel blockers rather "
    "than a hazard of this pairing."],
   ["Rebound hypertension on withdrawal",
    "Rebound on abrupt withdrawal is a limitation of the central alpha-2 agonists such as clonidine."]],
  C(57)),

Q("Beta blockers", IO,
  "A 64-year-old man with hypertension has heart failure with a reduced ejection fraction and a "
  "myocardial infarction six months ago. Which class is preferred for him?",
  [["A beta blocker",
    "Correct. Beta blockers are not first-line for uncomplicated hypertension, but reduced ejection "
    "fraction heart failure, recent infarction and ischaemic disease are exactly the comorbidities "
    "that select them."],
   ["A non-dihydropyridine calcium channel blocker",
    "Verapamil and diltiazem are avoided where the ejection fraction is already reduced, as it is here."],
   ["Clonidine",
    "Central alpha-2 agonists are limited by sedation and rebound hypertension and have no preferred "
    "indication here."],
   ["Hydralazine as monotherapy",
    "Hydralazine requires combination therapy because of reflex tachycardia and fluid retention."]],
  C(58)),

Q("Thiazide monitoring", IO,
  "A 78-year-old woman is started on chlorthalidone. Which monitoring matters most for her?",
  [["Sodium, given the risk of thiazide hyponatraemia",
    "Correct, particularly where sodium is already low-normal, and volume status matters in older "
    "adults too. Electrolytes and uric acid are the standing monitoring for the class."],
   ["Liver enzymes every three months",
    "Hepatic monitoring is not among the described concerns for thiazide-type diuretics."],
   ["Thyroid function every six months",
    "Thyroid studies belong to the baseline secondary-cause screen rather than to thiazide "
    "monitoring."],
   ["No monitoring, since chlorthalidone is well tolerated",
    "Electrolytes, uric acid and volume status are all monitored, and the sodium concern is "
    "heightened in this group."]], C(63)),

Q("Thiazide adverse effects", IO,
  "A 62-year-old man on chlorthalidone presents with an acutely painful, swollen first "
  "metatarsophalangeal joint. What connects this to his medication?",
  [["Hyperuricaemia may precipitate gout",
    "Correct, which is why uric acid is monitored alongside electrolytes and volume status in "
    "patients on a thiazide-type diuretic."],
   ["Thiazide-induced hyperkalaemia",
    "Thiazides cause hypokalaemia rather than hyperkalaemia, and neither precipitates gout."],
   ["Thiazide-induced angioedema",
    "Angioedema is an ACE inhibitor class effect mediated by bradykinin rather than a thiazide effect."],
   ["Thiazide-induced ankle oedema",
    "Dependent ankle oedema is a dihydropyridine effect and would not present as an acutely "
    "inflamed single joint."]], C(55)),

Q("Treatment goal", IO,
  "A 54-year-old woman on two agents has an average blood pressure of 134/84. What should happen?",
  [["Intensify therapy, since the goal is below 130/80",
    "Correct, and values closer to 120/80 are encouraged where appropriate. The same threshold "
    "defines the condition and measures control."],
   ["Accept this as at goal, since it is below 140/90",
    "The stated goal is below 130/80 rather than below 140/90, so she remains above it on both numbers."],
   ["Stop one agent, since she is close to goal",
    "She is above the goal of 130/80, so reducing therapy would move her further from it rather than closer."],
   ["Accept whatever value she tolerates without symptoms",
    "A defined numeric goal is given, and most patients have no reliable pressure-related symptoms "
    "to guide by."]], C(61)),

Q("Resistant hypertension", IO,
  "A 59-year-old man remains at 158/96 on three agents at maximally tolerated doses. What is the "
  "commonest explanation to exclude first?",
  [["Medication nonadherence",
    "Correct, and it heads a list that also includes measurement error, white coat effect, high "
    "sodium or alcohol intake, interfering drugs, and undiagnosed sleep apnoea or secondary "
    "hypertension."],
   ["Undiagnosed primary aldosteronism",
    "Secondary hypertension is on the list to rule out, but nonadherence is the commonest single "
    "explanation for apparent resistance."],
   ["An incorrectly sized cuff",
    "Measurement error belongs on the list, but nonadherence is specifically named as commonest."],
   ["Progressive renal artery stenosis",
    "Renovascular disease is one secondary cause to consider, but it is not the commonest reason "
    "control appears resistant."]], C(66)),

Q("Resistant hypertension", IO,
  "A 61-year-old woman has confirmed resistant hypertension: adherent, correctly measured, above "
  "goal on three complementary agents. What is the first step in management?",
  [["Optimise the diuretic, with chlorthalidone preferred",
    "Correct, and it comes before adding anything. An inadequate or inappropriate diuretic is a common reason the other two agents appear to be failing. The diuretic class is matched to renal function."],
   ["Add spironolactone immediately",
    "Spironolactone is the fourth agent, added after the diuretic is optimised and the foundational "
    "three are titrated."],
   ["Refer to a hypertension specialist",
    "Referral is for truly difficult cases after the described sequence rather than as the first "
    "step."],
   ["Stop all agents and restart from the beginning",
    "The approach is to optimise and titrate what is in place rather than to begin again."]], C(67)),

Q("Resistant hypertension", IO,
  "A 57-year-old man with confirmed resistant hypertension has had his diuretic optimised and his "
  "other two agents titrated to maximally tolerated doses. His filtration rate and potassium are "
  "normal. Which fourth agent has the most evidence?",
  [["Spironolactone",
    "Correct, provided the filtration rate and potassium allow. It is added after the foundational "
    "three are optimised rather than instead of doing so."],
   ["A beta blocker",
    "Beta blockade appears among the later escalation options chosen by physiology and comorbidity "
    "rather than as the evidence-supported fourth agent."],
   ["Hydralazine",
    "Hydralazine is a later addition and requires combination therapy because of reflex tachycardia "
    "and fluid retention."],
   ["A second dihydropyridine calcium channel blocker",
    "Adding a second agent of the same class is not among the described steps and duplicates a mechanism."]], C(67)),

Q("Left ventricular hypertrophy", IO,
  "A 67-year-old man with long-standing hypertension has echocardiography showing left ventricular hypertrophy with impaired diastolic relaxation and a normal ejection fraction. He is breathless on exertion. What does this mean for his prognosis?",
  [["Preserved ejection fraction failure is a recognised endpoint",
    "Correct. A normal ejection fraction does not reassure, because preserved-fraction failure is "
    "one of the two routes hypertensive heart disease can take."],
   ["A normal ejection fraction excludes heart failure",
    "Both preserved and reduced ejection fraction failure are recognised endpoints, which is why "
    "diastolic parameters matter as much as the ejection fraction."],
   ["The hypertrophy carries no risk of its own",
    "Hypertrophy independently raises cardiovascular risk beyond the pressure that caused it."],
   ["Valvular stenosis is the likely explanation",
    "Valve calcification is an age-related process rather than the described consequence of chronic "
    "pressure overload."]], C(26)),

Q("Hypertensive kidney disease", IO,
  "A 60-year-old hypertensive woman has a urine albumin-to-creatinine ratio that has risen over "
  "three consecutive visits while her estimated filtration rate has fallen. What do these represent?",
  [["The earliest measurable markers of hypertensive kidney damage",
    "Correct, and both are watched as trends rather than single values, because the direction of "
    "travel is what identifies progression early enough to act on."],
   ["An expected consequence of ageing requiring no action",
    "A consistent trend in both markers indicates ongoing damage rather than the expected change of ageing."],
   ["Evidence that her blood pressure is adequately controlled",
    "Rising albuminuria with falling filtration indicates ongoing injury rather than control."],
   ["A finding specific to diabetic rather than hypertensive disease",
    "Both conditions can produce it, which is precisely why alternative renal causes must be "
    "evaluated rather than assumed."]], C(28)),

Q("Cerebrovascular disease", IO,
  "A 69-year-old man with poorly controlled hypertension asks which strokes he is at risk of. What should he be told?",
  [["Both ischaemic and haemorrhagic stroke",
    "Correct. Hypertension raises the risk of both mechanisms, and chronic small-vessel injury "
    "separately contributes to white matter change, lacunar infarcts and cognitive decline."],
   ["Ischaemic stroke only",
    "Intracerebral haemorrhage is also described, which is part of why sustained systolic burden "
    "matters so much."],
   ["Intracerebral haemorrhage only",
    "Ischaemic stroke is described alongside haemorrhage and chronic small-vessel injury."],
   ["Subarachnoid haemorrhage specifically",
    "The described events are ischaemic stroke and intracerebral haemorrhage rather than "
    "subarachnoid bleeding."]], C(27)),

Q("Emergency symptoms", IO,
  "Which of these findings in a hypertensive patient requires immediate evaluation?",
  [["Abrupt severe headache with a new focal neurological deficit",
    "Correct. Confusion or seizures, visual disturbance or focal deficit, abrupt severe headache, "
    "chest or severe back pain, and oliguria each map to an organ under acute injury."],
   ["Mild ankle swelling after starting amlodipine",
    "Dependent ankle oedema is the commonest adverse effect of a dihydropyridine rather than a "
    "feature of emergency."],
   ["A dry cough three weeks after starting lisinopril",
    "Cough is a recognised bradykinin-mediated class effect prompting a switch to an angiotensin "
    "receptor blocker."],
   ["A mild headache in a patient with known hypertension",
    "Headache is common but nonspecific; it is the ABRUPT SEVERE headache that warrants immediate "
    "evaluation."]], C(37)),

Q("Symptoms", IO,
  "A 50-year-old man says he can tell when his blood pressure is high because he gets a headache. "
  "How should this be addressed?",
  [["Most patients have no reliable blood pressure-related symptoms",
    "Correct. Headache is common but nonspecific and cannot be relied on to indicate the pressure, "
    "which is why the diagnosis and its control rest on measurement rather than on how he feels."],
   ["Headache is a reliable indicator and can guide his dosing",
    "Headache is common but nonspecific, and specifically described as an unreliable guide to the pressure."],
   ["Absence of headache confirms his pressure is controlled",
    "Most patients with mild to moderate hypertension have no reliable symptoms at all."],
   ["Any headache requires emergency evaluation",
    "It is the ABRUPT SEVERE headache that warrants immediate evaluation, not any headache."]],
  C(37)),

Q("Atherosclerosis", IO,
  "A 64-year-old hypertensive man also has a raised low-density lipoprotein. What principle should "
  "guide his management?",
  [["Treat total cardiovascular risk, not pressure alone",
    "Correct. Hypertension accelerates atherosclerosis through shear stress, intimal injury, lipid "
    "oxidation and smooth muscle proliferation, so antiplatelet and lipid-lowering therapy are "
    "considered where indicated."],
   ["Treat the blood pressure and address lipids only if it fails",
    "The two are managed together, because the vascular injury they produce is a single process."],
   ["Treat the lipids first and defer blood pressure control",
    "Neither is deferred; total cardiovascular risk is addressed, since both drive the same vascular injury."],
   ["Lipid therapy is unnecessary once blood pressure reaches goal",
    "Reaching the pressure goal does not remove the contribution of lipids to the same process."]],
  C(30)),

Q("Retinopathy", IO,
  "A 55-year-old man with hypertensive retinopathy achieves good blood pressure control. What can "
  "be expected of his retinal findings?",
  [["Control can lead to regression of the retinopathy",
    "Correct, so the finding is both a prognostic marker and something that can improve with "
    "treatment. Retinopathy predicts long-term stroke risk independently of the pressure level."],
   ["The changes are permanent once established",
    "Control of hypertension can produce regression of retinopathy, so the finding is not a fixed one."],
   ["The changes will progress regardless of control",
    "Progression is not inevitable, and regression of the retinopathy with good control is described."],
   ["The changes have no relationship to blood pressure",
    "Retinal changes are a direct consequence of the pressure, and they predict long-term stroke risk."]], C(31)),

Q("Chest radiography", IO,
  "A 59-year-old hypertensive man is breathless with bibasal crackles and raised jugular venous "
  "pressure. Is chest radiography appropriate?",
  [["Yes, because findings suggest pulmonary oedema",
    "Correct. Radiography is appropriate when dyspnoea or findings suggest pulmonary oedema, when "
    "cardiomegaly is suspected, or when a widened mediastinum is a concern."],
   ["No, because chest radiography is never indicated in hypertension",
    "It is not indicated ROUTINELY for uncomplicated hypertension, which is different from never "
    "being indicated."],
   ["Yes, as a routine part of every hypertensive workup",
    "Routine chest radiography is specifically not indicated for uncomplicated hypertension."],
   ["No, because a normal film would exclude dissection",
    "A normal chest radiograph does not exclude dissection, so that is not a reason either way."]],
  C(42)),

Q("Echocardiography", IO,
  "Which hypertensive patient warrants echocardiography?",
  [["One with suspected heart failure and a significant murmur",
    "Correct, alongside hypertrophy on the electrocardiogram or unexplained dyspnoea. It is not "
    "required for every new hypertensive patient."],
   ["Every newly diagnosed hypertensive patient",
    "It is targeted rather than routine, reserved for the specific indications listed."],
   ["Only patients whose medication has already failed",
    "The indications are clinical findings rather than a treatment failure threshold."],
   ["Only patients who cannot tolerate a chest radiograph",
    "The two answer different questions; echocardiography assesses ventricular mass, geometry, "
    "function and valves."]], C(43)),

Q("Prognosis", IO,
  "A 44-year-old newly diagnosed hypertensive patient asks why treatment matters if she feels well. "
  "What is the strongest answer?",
  [["It causes cumulative organ damage with no reliable symptoms",
    "Correct. The heart, brain, kidneys, aorta, arteries and retina are all injured over years, and "
    "most patients have no reliable blood pressure-related symptoms to warn them."],
   ["She will begin to feel symptoms within a few months if untreated",
    "Most patients with mild to moderate hypertension have no reliable symptoms at any point."],
   ["Treatment is optional until organ damage is demonstrated",
    "Waiting for demonstrable damage forfeits the period in which it could have been prevented."],
   ["Feeling well means her risk is already low",
    "How a patient feels is not a guide to the pressure or to the damage it is doing."]], C(37)),

Q("Adherence", IO,
  "A 58-year-old man on three separate antihypertensive tablets admits he often forgets the midday "
  "dose. What change is most likely to help?",
  [["A single-pill combination",
    "Correct. Where two agents are started, a single-pill combination is preferred precisely because "
    "adherence is itself one of the main determinants of whether control is achieved."],
   ["Adding a fourth agent to compensate",
    "Adding agents to a regimen he is not taking compounds the problem rather than solving it."],
   ["Switching to a beta blocker",
    "Beta blockers are not first-line for uncomplicated hypertension, and the barrier here is the "
    "regimen rather than the class."],
   ["Accepting his current control as the best achievable",
    "Nonadherence is the commonest cause of apparent resistance, and a simpler regimen addresses it."]], C(65)),

Q("Hypertensive emergency", IO,
  "A 57-year-old woman with a hypertensive emergency has her pressure reduced from 240/130 to "
  "125/75 within thirty minutes. She then develops a new hemiparesis. What happened?",
  [["Autoregulation had adapted to the higher pressure",
    "Correct. Her organs had reset the range over which they protect their own perfusion, so a value that would be safe in anyone else left her brain underperfused. Reducing it that fast left her brain underperfused."],
   ["The reduction was appropriate and the deficit is unrelated",
    "Reducing to a chronic goal within the first hour is specifically capable of causing ischaemic "
    "stroke, myocardial injury or renal failure."],
   ["She developed rebound hypertension",
    "Rebound on abrupt withdrawal is a limitation of central alpha-2 agonists and does not explain a "
    "deficit after an over-rapid reduction."],
   ["Hyperkalaemia precipitated the event",
    "Potassium disturbance relates to renin-angiotensin blockade rather than to the rate of pressure "
    "reduction."]], C(69)),

Q("Escalation", IO,
  "A 53-year-old man on an angiotensin receptor blocker and a dihydropyridine remains above goal at "
  "maximally tolerated doses. What is the next step?",
  [["Add a thiazide-type diuretic",
    "Correct. The foundational three are a renin-angiotensin blocker, a dihydropyridine and a thiazide-type diuretic, all titrated before resistance can be considered confirmed. It is the third of the foundational agents."],
   ["Add an ACE inhibitor",
    "Dual renin-angiotensin blockade is prohibited because of hyperkalaemia and kidney injury risk."],
   ["Add spironolactone now",
    "Spironolactone is the fourth agent, added only after the foundational three have been optimised."],
   ["Add a second dihydropyridine",
    "Duplicating a class adds adverse effects without the complementary mechanism a third class gives."]], C(65)),

Q("Patient education", IO,
  "A 47-year-old woman starting home monitoring calls alarmed because one reading was 168/102, although her seven-day average is 128/80. What should she be told?",
  [["Reassure her that the average matters, not one reading",
    "Correct. Overreacting to an outlier generates anxiety and unnecessary changes in therapy, which "
    "is why the schedule is built around averaging fourteen readings."],
   ["Increase her medication on the basis of the highest reading",
    "Acting on a single outlier is precisely what the averaging schedule exists to prevent."],
   ["Tell her home readings are unreliable and to stop monitoring",
    "Home monitoring with a validated upper-arm device is a standard part of assessment."],
   ["Send her to the emergency department",
    "An isolated raised reading without symptoms of acute organ injury is not an emergency."]],
  C(45)),

Q("Referral", IO,
  "A 55-year-old man remains above goal despite the described sequence: adherence confirmed, "
  "diuretic optimised, three agents titrated, spironolactone added and tolerated. What now?",
  [["Refer to a hypertension specialist",
    "Correct. Referral is reserved for truly difficult cases after the full sequence has been worked "
    "through rather than being an early substitute for it."],
   ["Add a second mineralocorticoid antagonist",
    "Duplicating the mineralocorticoid antagonist class is not among the described escalation steps."],
   ["Accept the current pressure as his individual goal",
    "A defined numeric goal of below 130/80 applies, and specialist options remain beyond this sequence."],
   ["Stop spironolactone and restart from a single agent",
    "The approach builds on the regimen already in place rather than discarding it and beginning again."]], C(67)),
]
