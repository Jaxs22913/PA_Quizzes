#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Pharmacology I Exam 3 topic quizzes and vignette pairs: Lecture 9 (Diuretics and Heart Failure Drugs),
Lecture 10 (Antiarrhythmic Drugs) and Lecture 11 (Pulmonary Infections, Asthma and Chronic Obstructive Pulmonary Disease; vignettes in
tools/pharm_e3_l11_vignette_sets.json, key v11). Topic sets come from tools/pharm_e3_sets/<key>.json (pharm_e3_partition.py),
the vignettes from tools/pharm_e3_vignette_sets.json (Lecture 9) and tools/pharm_e3_l10_vignette_sets.json (Lecture 10).
Rendering skips whatever is not built yet.

    python3 tools/render_pharm_e3.py                         # everything
    python3 tools/render_pharm_e3.py aa1a aa1bc v10          # only these topic keys / vignette pairs (v9, v10)

Options may carry a third element (`mis`, the WRITER.md misconception tag) and questions a `lead`; both are
bookkeeping for the blind review and are stripped before render.

Topic quizzes use the slate-blue Exam 2 topic palette and the vignettes the brown palette, as in Exam 2 (the Pharmacology
palettes are shared across exams; no new accent hex).
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 3")
PALETTE = dict(navy="#2f4f6b", indigo="#4a7fa5", gold="#b8862f", ice="#eef3f7")
PAL_V = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
SUB = "Pharmacology I &middot; Exam 3 &middot; Diuretics and Heart Failure Drugs"

NOTE = ("<b>What these do and do not ask.</b> <b>Indications, adverse effects, contraindications and patient "
        "education are in</b>, weighted above mechanism. <b>Doses are out</b>, and so is the digoxin target level, "
        "which is why the sets run shorter than the usual 30. Every option carries its own reason, correct and "
        "incorrect alike.")

# key, heading, file stem, chips, blurb
TOPICS = [
 ("loops", "The Nephron &amp; Loop Diuretics", "diuretics-loop-quiz",
  ["Nephron sites", "Loop diuretics", "Adverse effects", "Interactions"],
  "Every diuretic works at a different stretch of the nephron, and <b>where it works</b> predicts what it does to "
  "potassium, calcium, uric acid and acid-base balance. <b>Loop diuretics</b> are the most potent, still work when "
  "kidney function is poor, and cost the patient potassium, calcium and magnesium."),
 ("thiazides", "Thiazide Diuretics", "diuretics-thiazide-quiz",
  ["Distal tubule", "Hypertension", "Calcium", "Adverse effects", "Metolazone"],
  "Thiazides block sodium and chloride in the <b>distal convoluted tubule</b>. Know what they do to "
  "<b>calcium</b> (the opposite of loops), who responds best in hypertension, their adverse effects and why they "
  "fail at a low creatinine clearance (metolazone is the exception)."),
 ("ksparing", "Potassium-Sparing Diuretics, Aldosterone Antagonists &amp; Carbonic Anhydrase Inhibitors",
  "diuretics-k-sparing-cai-quiz",
  ["Potassium-sparing", "Aldosterone antagonists", "Carbonic anhydrase inhibitors"],
  "These are the weak diuretics, used for what they do to <b>potassium</b> and acid-base balance rather than for "
  "volume. <b>Hyperkalemia</b> is the danger of the first two groups, <b>androgen-receptor effects</b> distinguish "
  "spironolactone from eplerenone, and carbonic anhydrase inhibitors cause a <b>metabolic acidosis</b>."),
 ("hfcore", "Heart Failure: Diuretics, ACE Inhibitors &amp; Beta Blockers", "hf-diuretics-acei-beta-blockers-quiz",
  ["Heart failure types", "Decompensation", "Diuretics", "ACE inhibitors", "Beta blockers"],
  "Heart failure therapy splits into drugs that relieve <b>symptoms</b> (diuretics) and drugs that "
  "prolong <b>survival</b> (ACE inhibitors, and three named beta blockers). Know which is which, why beta "
  "blockers must be started low and slow, and how to monitor fluid status."),
 ("digoxin", "Digoxin", "hf-digoxin-quiz",
  ["Mechanism", "Clinical benefit", "Toxicity", "Contraindications", "Antidote"],
  "Digoxin helps symptoms but <b>does not improve survival</b>, has a <b>narrow therapeutic index</b>, and its "
  "toxicity (<b>yellow-green halos</b>, nausea, bradycardia, arrhythmia) is made worse by electrolyte "
  "disturbances. Digoxin immune Fab reverses it."),
 ("inotropes", "Other Heart Failure Drugs: Inotropes, Newer Agents &amp; Aldosterone Antagonists", "hf-inotropes-newer-agents-quiz",
  ["Aldosterone antagonists", "Inotropes", "Ivabradine", "Sacubitril-valsartan", "SGLT2 inhibitors"],
  "The add-on drugs: <b>spironolactone and eplerenone</b> for survival in advanced failure, <b>milrinone</b> for short-term "
  "intravenous support, <b>ivabradine</b> when the heart rate stays high, <b>sacubitril-valsartan</b> (never with an ACE "
  "inhibitor) and the <b>SGLT2 inhibitors</b>."),
]

SUB10 = "Pharmacology I &middot; Exam 3 &middot; Antiarrhythmic Drugs"
NOTE10 = ("<b>What these do and do not ask.</b> <b>Classes, indications, adverse effects, contraindications and patient "
          "education are in</b>, weighted above mechanism. <b>Doses are out</b>, and so are channel-binding affinity and "
          "dissociation rates and the few slide points that current guidelines no longer follow, which is why the sets run "
          "shorter than the usual 30. Every option carries its own reason, correct and incorrect alike.")

# Lecture 10 topics: key, heading, file stem, chips, blurb
TOPICS10 = [
 ("aa1a", "Antiarrhythmic Classes &amp; Class IA Drugs", "antiarrhythmic-classes-1a-quiz",
  ["Classification", "Indication trends", "Quinidine", "Procainamide", "Disopyramide"],
  "Antiarrhythmics fall into <b>four classes plus a few others</b>, and the class predicts where a drug works: "
  "classes II and IV act above the ventricles, classes I and III on both. The <b>class IA</b> drugs (quinidine, "
  "procainamide, disopyramide) slow phase 0 and lengthen the action potential, and each has a signature toxicity: "
  "<b>cinchonism</b>, a <b>lupus-like syndrome</b>, <b>anticholinergic</b> effects."),
 ("aa1bc", "Class IB &amp; IC Antiarrhythmics", "antiarrhythmic-1b-1c-quiz",
  ["Lidocaine", "Ischemic tissue", "Flecainide", "Propafenone", "Toxicity"],
  "<b>Lidocaine</b> (class IB) is given intravenously, works best in <b>ischemic</b> tissue and shows toxicity in the "
  "brain first (nystagmus, then seizures). <b>Flecainide</b> and <b>propafenone</b> (class IC) slow conduction even in "
  "the normal heart, prolong the PR, QRS and QT intervals and can provoke arrhythmias; flecainide raises mortality after "
  "a myocardial infarction."),
 ("aa24", "Class II &amp; IV: Beta Blockers &amp; Calcium Channel Blockers", "antiarrhythmic-beta-calcium-blockers-quiz",
  ["Phase 4", "Propranolol", "Beta-1 selective", "Esmolol", "Verapamil and diltiazem"],
  "Both classes act on the <b>nodes</b>: they flatten phase 4 and slow atrioventricular conduction, so they control "
  "<b>supraventricular</b> rhythms. Know why <b>propranolol</b> is a problem in asthma and what replaces it, which "
  "beta blocker is the short-acting intravenous one, and when <b>verapamil and diltiazem</b> must be avoided."),
 ("aa3", "Class III: Potassium Channel Blockers", "antiarrhythmic-class-3-quiz",
  ["Phase 3", "Amiodarone", "Dofetilide", "Sotalol", "Interactions"],
  "Class III drugs <b>reduce potassium efflux</b> and prolong repolarization. <b>Amiodarone</b> blocks almost "
  "everything, has a very long half-life and a long list of organ toxicities and interactions; <b>dofetilide</b> is "
  "the pure potassium blocker with a torsades risk; <b>sotalol</b> adds beta blockade."),
 ("aamisc", "Adenosine, Digoxin &amp; Magnesium Sulfate", "antiarrhythmic-misc-agents-quiz",
  ["Adenosine", "Digoxin", "Magnesium sulfate", "Toxicity"],
  "The agents outside the four classes: <b>adenosine</b> hyperpolarizes and briefly stops the heart to end "
  "paroxysmal supraventricular tachycardia, <b>digoxin</b> slows the ventricular rate in atrial fibrillation and "
  "flutter, and <b>magnesium sulfate</b> treats torsades de pointes."),
]

SUB11 = "Pharmacology I &middot; Exam 3 &middot; Pulmonary Infections, Asthma and Chronic Obstructive Pulmonary Disease"
NOTE11 = ("<b>What these do and do not ask.</b> <b>Drug choice, indications, adverse effects, contraindications and patient "
          "education are in</b>, weighted above mechanism. <b>Doses are out</b> (milligram amounts, fluid volumes, inhaler "
          "and nebulizer doses), and so are bare drug levels and the slide points that current guidelines no longer follow, "
          "which is why the sets run shorter than the usual 30. Every option carries its own reason, correct and incorrect alike.")

# Lecture 11 topics: key, heading, file stem, chips, blurb
TOPICS11 = [
 ("pucap", "Acute Bronchitis &amp; Community-Acquired Pneumonia", "pulm-bronchitis-cap-quiz",
  ["Acute bronchitis", "Pathogens by setting", "Resistant pneumococcus", "Outpatient regimens", "Inpatient regimens"],
  "Acute bronchitis is usually <b>viral</b> and needs supportive care, not routine antibiotics. Community-acquired pneumonia "
  "is treated <b>by setting</b>: outpatient, inpatient ward or intensive care unit, and by whether the patient carries a "
  "<b>risk factor for drug-resistant <i>Streptococcus pneumoniae</i></b>."),
 ("puhap", "Nosocomial Pneumonia &amp; Its Antibiotics", "pulm-nosocomial-pneumonia-quiz",
  ["Hospital-acquired pneumonia", "Limited or broad spectrum", "Antipseudomonal agents", "Aminoglycosides", "Vancomycin and linezolid"],
  "Pneumonia that starts <b>more than 48 hours after admission</b> is treated at once, broadly, and must cover "
  "<b>methicillin-resistant <i>Staphylococcus aureus</i></b> and <b><i>Pseudomonas</i></b> when multidrug-resistant risk factors are present. "
  "Know the antipseudomonal agents, which ones need renal adjustment, and what sets linezolid apart."),
 ("putb", "Tuberculosis Drugs", "pulm-tuberculosis-drugs-quiz",
  ["Combination therapy", "Isoniazid", "Rifampin", "Ethambutol", "Pyrazinamide", "Second-line agents"],
  "Active tuberculosis is never treated with one drug. Four drugs for two months, then <b>isoniazid and rifampin</b> for four, "
  "and each first-line drug has a signature: <b>peripheral neuritis</b> (give pyridoxine), <b>orange secretions</b> and enzyme "
  "induction, <b>red-green color vision</b> loss, and <b>hyperuricemia with hepatitis</b>."),
 ("puana", "Anaphylaxis Treatment", "pulm-anaphylaxis-quiz",
  ["Epinephrine", "Volume expansion", "Histamine blockers", "Albuterol", "Corticosteroids"],
  "Anaphylaxis is a severe, systemic allergic reaction. <b>Epinephrine</b> (intramuscular unless the patient is coding) is the "
  "drug that acts on both alpha and beta receptors; fluids, histamine H1 and H2 blockers, albuterol and corticosteroids each treat one "
  "part of the reaction, and corticosteroids take hours to work."),
 ("pubd", "Asthma &amp; the Bronchodilators", "asthma-bronchodilators-quiz",
  ["Asthma basics", "Quick relief or controller", "Beta-2 agonists", "Theophylline", "Anticholinergics"],
  "Asthma is <b>reversible</b> airway narrowing driven by inflammation. The bronchodilators reverse bronchospasm: "
  "<b>beta-2 agonists</b> raise cyclic adenosine monophosphate (short-acting for relief; long-acting never alone in asthma), "
  "<b>theophylline</b> has a narrow therapeutic index, and the <b>anticholinergics</b> block muscarinic receptors."),
 ("puctl", "Asthma Controllers: Steroids, Leukotriene Modifiers, Mast Cell Stabilizers &amp; Biologics", "asthma-controllers-quiz",
  ["Inhaled corticosteroids", "Combination inhalers", "Montelukast", "Cromolyn and nedocromil", "Omalizumab and biologics", "Systemic steroids"],
  "The drugs that <b>control inflammation</b> long term: inhaled corticosteroids (thrush, growth), the combination inhalers, "
  "<b>montelukast</b>, the mast cell stabilizers that must be taken <b>before</b> exposure, <b>omalizumab</b> and the other "
  "biologics, and the systemic steroids kept for exacerbations because of their side effects."),
 ("puinh", "Asthma Steps, Inhaler Devices &amp; Status Asthmaticus", "asthma-inhalers-status-quiz",
  ["Stepwise therapy", "Nebulizers", "Dry powder inhalers", "Metered dose inhalers and spacers", "Technique", "Status asthmaticus"],
  "How the drug reaches the lung matters as much as which drug it is. Match the <b>device to the patient</b> (coordination, "
  "inspiratory force), teach the <b>technique</b>, read albuterol overuse as poor control, and know the escalation for "
  "<b>status asthmaticus</b>."),
 ("pucopd", "Chronic Obstructive Pulmonary Disease, Smoking Cessation &amp; Immunizations", "copd-smoking-cessation-quiz",
  ["Chronic obstructive pulmonary disease", "Treatment groups", "Bupropion", "Nicotine replacement", "Varenicline", "Vaccines"],
  "Chronic obstructive pulmonary disease is <b>not fully reversible</b>, and stopping smoking is the intervention that changes "
  "its course. Know the treatment by group, what each smoking cessation drug does and <b>who must avoid it</b>, and the two "
  "vaccines every patient should get."),
]

VCHIPS11 = ["Pneumonia", "Tuberculosis", "Anaphylaxis", "Asthma", "Inhalers", "Smoking cessation"]
VINTRO11 = ("Clinical vignettes that open with a patient rather than a fact. The topic quizzes test the drugs one at a time; "
            "these ask what you would <b>choose</b> for the setting, what you would <b>avoid</b>, which drug explains a new "
            "symptom and what you would <b>teach</b>. The last sentence decides the answer, so read it twice. Expect the "
            "classic contrasts: outpatient against inpatient pneumonia, limited against broad hospital coverage, the "
            "signature toxicity of each tuberculosis drug, quick-relief against controller inhalers, and which smoking "
            "cessation drug a seizure history rules out. <b>No doses</b> are asked. Every option carries its own reason, "
            "correct and incorrect alike, and every question cites its slide.")

VCHIPS10 = ["Class IA", "Class IB and IC", "Beta blockers", "Calcium channel blockers", "Class III", "Adenosine and digoxin"]
VINTRO10 = ("Clinical vignettes that open with a patient rather than a fact. The topic quizzes test the drugs one at a time; "
            "these ask what you would <b>choose</b>, what you would <b>avoid</b>, which toxicity explains a new symptom "
            "and what to <b>watch for</b>. The last sentence decides the answer, so read it twice. Expect the classic "
            "contrasts: a nonselective against a beta-1 selective blocker, which drug belongs in ischemic tissue, the "
            "signature toxicities of quinidine, procainamide, lidocaine and amiodarone, and what treats torsades de "
            "pointes. <b>No doses</b> are asked. Every option carries its own reason, correct and incorrect alike, and "
            "every question cites its slide.")

VCHIPS = ["Loop diuretics", "Thiazides", "Potassium-sparing", "Heart failure", "Digoxin", "Newer agents"]
VINTRO = ("Clinical vignettes that open with a patient rather than a fact. The topic quizzes test the drugs one at a time; "
          "these ask what you would <b>choose</b>, what you would <b>avoid</b>, what you would <b>warn the patient about</b> "
          "and what would go wrong if two drugs were combined. The last sentence decides the answer, so read it twice. "
          "Expect the classic contrasts: loop against thiazide against potassium-sparing, what each does to potassium and "
          "calcium, which heart failure drugs prolong survival and which only relieve symptoms, and the clues of digoxin "
          "toxicity. <b>No doses</b> are asked. Every option carries its own reason, correct and incorrect alike, and every "
          "question cites its slide.")


def clean(qs):
    """Drop review bookkeeping (option `mis`, question `lead`) so the page carries only text and explanation."""
    out = []
    for q in qs:
        q = {k: v for k, v in q.items() if k != "lead"}
        q["opts"] = [list(o[:2]) for o in q["opts"]]
        out.append(q)
    return out


def topics(table, sub, note, want):
    for key, label, stem, chips, blurb in table:
        if want and key not in want:
            continue
        p = os.path.join(HERE, "pharm_e3_sets", key + ".json")
        if not os.path.exists(p):
            print("skip (no sets yet): " + key); continue
        S = json.load(open(p, encoding="utf-8"))
        for n in (1, 2):
            qs = clean(S["%s%d" % (key, n)])
            fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
            html = render(title="%s Quiz %d &mdash; Pharmacology I Exam 3" % (label, n), h1=label, sub=sub,
                          pill="%d questions" % len(qs), chips=chips, intro=blurb + " " + note,
                          questions=qs, already_converted=True, **PALETTE)
            open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
            print("wrote %-52s %d questions" % (fn, len(qs)))


def vignettes(setfile, stem, topic_title, topic_h1, chips, intro):
    p = os.path.join(HERE, setfile)
    if not os.path.exists(p):
        print("skip (no sets yet): " + setfile); return
    V = json.load(open(p, encoding="utf-8"))
    for n, key in ((1, "set1"), (2, "set2")):
        fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
        qs = clean(V[key])
        html = render(title="%s &mdash; Clinical Vignettes %d | Pharmacology I Exam 3" % (topic_title, n),
                      h1="%s &mdash; Clinical Vignettes %d" % (topic_h1, n),
                      sub="Pharmacology I &middot; Exam 3 &middot; apply it to a patient",
                      pill="%d questions" % len(qs), chips=chips, intro=intro,
                      questions=qs, already_converted=True, **PAL_V)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote %-52s %d questions" % (fn, len(qs)))


def main():
    want = set(a for a in sys.argv[1:] if not a.startswith("-"))
    known = {t[0] for t in TOPICS + TOPICS10 + TOPICS11} | {"v9", "v10", "v11"}
    bad = want - known
    if bad:
        sys.exit("unknown key(s): %s (known: %s)" % (", ".join(sorted(bad)), ", ".join(sorted(known))))
    topics(TOPICS, SUB, NOTE, want)
    topics(TOPICS10, SUB10, NOTE10, want)
    topics(TOPICS11, SUB11, NOTE11, want)
    if not want or "v9" in want:
        vignettes("pharm_e3_vignette_sets.json", "pharm-e3-vignettes", "Diuretics and Heart Failure Drugs",
                  "Diuretics &amp; Heart Failure Drugs", VCHIPS, VINTRO)
    if not want or "v10" in want:
        vignettes("pharm_e3_l10_vignette_sets.json", "pharm-e3-antiarrhythmic-vignettes", "Antiarrhythmic Drugs",
                  "Antiarrhythmic Drugs", VCHIPS10, VINTRO10)
    if not want or "v11" in want:
        vignettes("pharm_e3_l11_vignette_sets.json", "pharm-e3-pulmonary-vignettes",
                  "Pulmonary Infections, Asthma and Chronic Obstructive Pulmonary Disease", "Pulmonary Infections, Asthma &amp; Chronic Obstructive Pulmonary Disease", VCHIPS11, VINTRO11)


if __name__ == "__main__":
    main()
