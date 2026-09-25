#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 4 Arcade decks -- Lecture 20, Hypertension.

Three decks rather than one, split the way the lecture divides: definitions and
secondary causes, target organ damage and assessment, and treatment. A single
77-slide lecture makes an unwieldy deck.

ATOMIC FACTS ONLY, per [[arcade_content_policy]].

Idempotent: fenced between markers, re-runnable.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCADE = os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--CMSE4-DECKS-->", "  // <!--/CMSE4-DECKS-->"

GAUGE_ICON = ('<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-5"/><circle cx="12" cy="18" r="1.5"/>'
              '<path d="M4 18h16"/>')
ORGAN_ICON = ('<path d="M12 20s-7-4.5-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.5-7 9-7 9z"/>'
              '<path d="M3 12h4l2-3 2 6 2-4 1.5 2H21"/>')
PILL_ICON = ('<rect x="2" y="9" width="20" height="7" rx="3.5" transform="rotate(-35 12 12)"/>'
             '<path d="M8.5 15.5l7-7"/>')

DECKS = [
 ("cms-htn-definitions", "Hypertension &mdash; Definitions &amp; Causes", "accent1", GAUGE_ICON, [
  ("What defines a hypertensive emergency?", "Severe elevation with acute hypertension-mediated organ injury &mdash; no numeric cutoff."),
  ("Examples of that acute injury?", "Encephalopathy, acute pulmonary edema, acute kidney injury, aortic dissection, acute coronary syndrome."),
  ("Define resistant hypertension.", "Above goal despite three complementary drugs at maximally tolerated doses."),
  ("What is the treatment goal?", "Below 130/80, with values closer to 120/80 encouraged where appropriate."),
  ("What characterizes primary hypertension?", "No single identifiable underlying cause; the vast majority of adult cases."),
  ("Risk factors for primary hypertension?", "Advancing age, family history, excess adiposity, high dietary sodium, inactivity, excess alcohol, dyslipidemia, insulin resistance."),
  ("Which onset pattern suggests a secondary cause?", "Early onset, abrupt onset, resistance, or sudden loss of previously stable control."),
  ("Common contributors to secondary hypertension?", "Chronic kidney disease, primary aldosteronism, obstructive sleep apnea, renovascular disease, drugs."),
  ("How does chronic kidney disease raise pressure?", "Impaired sodium excretion expands extracellular volume, with renin-angiotensin-aldosterone and sympathetic activation."),
  ("What is needed to diagnose chronic kidney disease?", "A kidney abnormality persisting at least three months."),
  ("Which renal artery stenosis predominates in older vascular patients?", "Atherosclerotic, often bilateral and progressive."),
  ("Creatinine rises sharply after starting an ACE inhibitor &mdash; suspect?", "Bilateral or hemodynamically significant renal artery stenosis."),
  ("Warning features for renovascular disease?", "Resistant or abrupt elevation, abdominal bruit, asymmetric kidneys, recurrent flash pulmonary edema."),
  ("When is renovascular disease referred early?", "Recurrent flash pulmonary edema, progressive renal decline despite optimal therapy, truly refractory control."),
  ("Underlying abnormality in primary aldosteronism?", "Autonomous aldosterone production independent of renin."),
  ("When to screen for primary aldosteronism?", "Resistant pressure, unexplained hypokalemia, adrenal incidentaloma, early or familial hypertension."),
  ("Screening test for aldosteronism, and positive result?", "Morning aldosterone to renin ratio; positive above roughly 20:1 with adequate aldosterone."),
  ("How does obstructive sleep apnea raise pressure?", "Intermittent hypoxemia and arousal drive sustained sympathetic activation."),
  ("How is sleep apnea confirmed?", "Polysomnography or validated home sleep apnea testing."),
  ("What should a medication review cover beyond prescriptions?", "Over-the-counter drugs, recreational substances, licorice, herbal supplements."),
  ("How does alcohol relate to blood pressure?", "Excess raises it; withdrawal can produce acute severe hypertension."),
  ("Thyroid effect on blood pressure?", "Hyperthyroidism raises cardiac output &rarr; systolic; hypothyroidism raises vascular resistance &rarr; diastolic."),
  ("Clues to Cushing syndrome?", "Proximal muscle weakness, easy bruising, thin skin, broad purple striae, central adiposity."),
  ("The five Ps of pheochromocytoma?", "Pressure, perspiration, palpitations, pallor, tremor."),
  ("Initial biochemical test for pheochromocytoma?", "Plasma free metanephrines, or 24-hour urinary fractionated metanephrines."),
  ("Blockade order before pheochromocytoma surgery?", "Alpha blockade FIRST, then beta &mdash; isolated beta blockade is dangerous."),
  ("Bedside clue to coarctation?", "Radial-femoral delay, and leg systolic lower than arm (normally it is higher)."),
  ("Which study establishes coarctation, and referral?", "Echocardiography; refer to a vascular surgeon or structural cardiologist."),
  ("White coat hypertension?", "High office readings with normal out-of-office readings."),
  ("Masked hypertension?", "Normal office readings with raised out-of-office readings &mdash; and real cardiovascular risk."),
 ]),

 ("cms-htn-organ-damage", "Hypertension &mdash; Organ Damage &amp; Assessment", "accent3", ORGAN_ICON, [
  ("What does chronic pressure overload do to the heart?", "Left ventricular hypertrophy with impaired diastolic relaxation &mdash; independently raises risk."),
  ("How may hypertensive heart disease progress?", "To heart failure with either preserved OR reduced ejection fraction."),
  ("Which strokes does hypertension predispose to?", "Both ischemic and intracerebral hemorrhagic."),
  ("Blood pressure caution in acute stroke?", "Acute stroke follows a distinct protocol; do not apply chronic targets acutely."),
  ("Earliest markers of hypertensive kidney damage?", "Rising urine albumin-to-creatinine ratio and falling estimated filtration rate."),
  ("Why not blame all kidney disease on hypertension?", "Alternative renal causes such as diabetes must be evaluated; the relationship is bidirectional."),
  ("How does aortic dissection present?", "Abrupt severe chest, back or abdominal pain, maximal at onset, often tearing."),
  ("Examination findings in dissection?", "Pulse deficits, asymmetric arm pressures, aortic regurgitation murmur, new neurological deficit."),
  ("Do normal pulses exclude dissection?", "No."),
  ("Does a normal chest radiograph exclude dissection?", "No &mdash; immediate cross-sectional vascular imaging is required."),
  ("How does hypertension accelerate atherosclerosis?", "Endothelial shear stress, intimal injury, lipid oxidation, smooth muscle proliferation."),
  ("Why perform fundoscopy in every new hypertensive?", "It allows direct visualization of the microvasculature."),
  ("Which retinal findings relate to CURRENT pressure only?", "Focal narrowing, hemorrhages, exudates."),
  ("Which relate to current AND previous pressure?", "Generalized narrowing and arteriovenous nicking."),
  ("Prognostic value of hypertensive retinopathy?", "Predicts long-term stroke risk independently of the pressure level; can regress with control."),
  ("What do most patients with mild to moderate hypertension report?", "No reliable blood pressure-related symptoms."),
  ("Symptoms requiring immediate evaluation?", "Confusion or seizures, visual disturbance or focal deficit, abrupt severe headache, chest or severe back pain, oliguria."),
  ("How should a patient be prepared for measurement?", "Rest five minutes, empty bladder, no smoking, caffeine or vigorous activity for thirty minutes."),
  ("How should they be positioned?", "Back supported, feet flat, legs uncrossed, bare arm at heart level, not speaking."),
  ("Why measure both arms initially?", "To find a difference and use the higher consistent arm at follow-up."),
  ("Normal leg-to-arm systolic relationship?", "Leg is normally HIGHER than arm."),
  ("What does radial-femoral delay suggest?", "Coarctation of the aorta."),
  ("Baseline laboratory panel?", "Creatinine with filtration rate, urine albumin-to-creatinine ratio, electrolytes, glucose, lipids, thyroid-stimulating hormone, blood count, urinalysis."),
  ("How sensitive are ECG voltage criteria for hypertrophy?", "Specific but NOT sensitive &mdash; a normal tracing does not exclude it."),
  ("When is chest radiography appropriate?", "Suspected pulmonary edema, cardiomegaly, or widened mediastinum &mdash; not routinely."),
  ("When is echocardiography appropriate?", "Suspected heart failure, significant murmur, hypertrophy on ECG, unexplained dyspnea."),
  ("Home monitoring schedule?", "Two readings a minute apart, morning and evening, seven days; report the average."),
  ("Home monitoring education point?", "Do not overreact to the highest single reading."),
 ]),

 ("cms-htn-treatment", "Hypertension &mdash; Treatment", "accent2", PILL_ICON, [
  ("Which blood pressure categories get lifestyle treatment?", "Every category."),
  ("Dietary and activity targets?", "DASH-style with reduced sodium; ~150 minutes a week moderate aerobic plus resistance training."),
  ("Effect of weight loss?", "A sustained 5&ndash;10 kg loss can meaningfully lower systolic pressure."),
  ("First-line drug classes?", "Thiazide-type diuretics, ACE inhibitors or angiotensin receptor blockers, dihydropyridine calcium channel blockers."),
  ("Preferred thiazide-type diuretic?", "Chlorthalidone."),
  ("What is monitored on a thiazide?", "Electrolytes, uric acid, volume status."),
  ("Thiazide adverse effects?", "Hyponatremia, hypokalemia, hyperuricemia (may precipitate gout), volume depletion."),
  ("Thiazide caution at 65 and over?", "Check sodium, especially in women and those with low-normal sodium."),
  ("ACE inhibitor adverse effects?", "Dry cough, hyperkalemia, creatinine rise, angioedema."),
  ("ACE inhibitor contraindications?", "Pregnancy, prior angioedema, bilateral renal artery stenosis."),
  ("Why does the ACE inhibitor cough happen, and the fix?", "Bradykinin-mediated, up to ~1 in 5; switch to an angiotensin receptor blocker."),
  ("In whom is angioedema more common?", "Black patients &mdash; two to four times more common."),
  ("Why never combine an ACE inhibitor with an ARB?", "Dual blockade raises hyperkalemia and kidney injury risk with no added benefit."),
  ("Commonest dihydropyridine adverse effect?", "Dependent ankle edema (also flushing, headache, gingival enlargement)."),
  ("Which combination must be avoided with verapamil or diltiazem?", "A beta blocker &mdash; severe bradycardia and heart block."),
  ("When are non-dihydropyridines avoided?", "Where the ejection fraction is already reduced."),
  ("Standing of beta blockers in uncomplicated hypertension?", "NOT first-line &mdash; preferred for reduced ejection fraction heart failure, recent infarction, ischemic disease."),
  ("Stage 1 versus stage 2 initial therapy?", "One first-line agent in stage 1; two complementary agents considered in stage 2."),
  ("Preferred initial combinations?", "A renin-angiotensin blocker with either a dihydropyridine or a thiazide-type diuretic."),
  ("Why a single-pill combination?", "Adherence is itself a main determinant of whether control is achieved."),
  ("Commonest cause of apparent resistance?", "Medication nonadherence."),
  ("Other causes of apparent resistance?", "Measurement error, white coat effect, high sodium or alcohol, interfering drugs, sleep apnea, secondary hypertension."),
  ("First step in confirmed resistant hypertension?", "Optimize the diuretic &mdash; chlorthalidone preferred, class matched to renal function."),
  ("Best-evidenced fourth agent?", "Spironolactone, if filtration rate and potassium allow."),
  ("Hydralazine limitation?", "Reflex tachycardia and fluid retention &mdash; requires combination therapy."),
  ("Clonidine limitations?", "Sedation, dry mouth, rebound hypertension on abrupt withdrawal."),
  ("First-hour target in a hypertensive emergency?", "Reduce mean arterial pressure by no more than about 20&ndash;25 percent."),
  ("Then what?", "Around 160/100&ndash;110 over two to six hours, gradual normalization over a day or two."),
  ("Why is rapid reduction harmful?", "Autoregulation has adapted; rapid reduction can cause ischemic stroke, myocardial injury or renal failure."),
  ("Which situations are excepted from that approach?", "Aortic dissection and some stroke syndromes."),
 ]),
]


def json_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def js(decks):
    out = []
    for did, name, colour, icon, cards in decks:
        rows = "\n".join('      [%s, %s],' % (json_str(q), json_str(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ]},\n" % (did, name, colour, icon, rows))
    return "\n".join(out)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(DECKS) + CLOSE

    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)
    else:
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]

    # Register under CMS I, Exam 4. SCOPED TO THE CMS GROUP ONLY -- a global
    # substitution on an exam id once rewrote three other classes' deck lists.
    exam4 = ('    { id: "exam4", name: "Exam 4", deckIds: [\n      %s\n    ] }'
             % ", ".join('"%s"' % d[0] for d in DECKS))
    g_start = src.index('  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 3"') == 1, "CMS group not isolated cleanly"
    if 'name: "Exam 4"' in group:
        group = re.sub(r'    \{ id: "exam4", name: "Exam 4", deckIds: \[.*?\] \}',
                       lambda _m: exam4, group, flags=re.S)
    else:
        e3 = group.rindex("] }")
        group = group[:e3 + len("] }")] + ",\n" + exam4 + group[e3 + len("] }"):]
    src = src[:g_start] + group + src[g_end:]

    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did, *_ in DECKS:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did

    open(ARCADE, "w", encoding="utf-8").write(src)
    n = sum(len(d[4]) for d in DECKS)
    print("wrote %d decks, %d cards into arcade.js" % (len(DECKS), n))
    for did, name, _c, _i, cards in DECKS:
        print("   %-24s %-46s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))


if __name__ == "__main__":
    main()
