#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Pharmacology I Exam 3 topic quizzes (Lecture 9, Diuretics and Heart Failure Drugs) and the
vignette pair. Topic sets come from tools/pharm_e3_sets/<key>.json (pharm_e3_partition.py), the vignettes from
tools/pharm_e3_vignette_sets.json (pharm_e3_vignette_partition.py). Rendering skips whatever is not built yet.

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

VCHIPS = ["Loop diuretics", "Thiazides", "Potassium-sparing", "Heart failure", "Digoxin", "Newer agents"]
VINTRO = ("Clinical vignettes that open with a patient rather than a fact. The topic quizzes test the drugs one at a time; "
          "these ask what you would <b>choose</b>, what you would <b>avoid</b>, what you would <b>warn the patient about</b> "
          "and what would go wrong if two drugs were combined. The last sentence decides the answer, so read it twice. "
          "Expect the classic contrasts: loop against thiazide against potassium-sparing, what each does to potassium and "
          "calcium, which heart failure drugs prolong survival and which only relieve symptoms, and the clues of digoxin "
          "toxicity. <b>No doses</b> are asked. Every option carries its own reason, correct and incorrect alike, and every "
          "question cites its slide.")


def main():
    for key, label, stem, chips, blurb in TOPICS:
        p = os.path.join(HERE, "pharm_e3_sets", key + ".json")
        if not os.path.exists(p):
            print("skip (no sets yet): " + key); continue
        S = json.load(open(p, encoding="utf-8"))
        for n in (1, 2):
            qs = S["%s%d" % (key, n)]
            fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
            html = render(title="%s Quiz %d &mdash; Pharmacology I Exam 3" % (label, n), h1=label, sub=SUB,
                          pill="%d questions" % len(qs), chips=chips, intro=blurb + " " + NOTE,
                          questions=qs, already_converted=True, **PALETTE)
            open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
            print("wrote %-52s %d questions" % (fn, len(qs)))
    p = os.path.join(HERE, "pharm_e3_vignette_sets.json")
    if os.path.exists(p):
        V = json.load(open(p, encoding="utf-8"))
        for n, key in ((1, "set1"), (2, "set2")):
            fn = "pharm-e3-vignettes.html" if n == 1 else "pharm-e3-vignettes-version-2.html"
            html = render(title="Diuretics and Heart Failure Drugs &mdash; Clinical Vignettes %d | Pharmacology I Exam 3" % n,
                          h1="Diuretics &amp; Heart Failure Drugs &mdash; Clinical Vignettes %d" % n,
                          sub="Pharmacology I &middot; Exam 3 &middot; apply it to a patient",
                          pill="%d questions" % len(V[key]), chips=VCHIPS, intro=VINTRO,
                          questions=V[key], already_converted=True, **PAL_V)
            open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
            print("wrote %-52s %d questions" % (fn, len(V[key])))


if __name__ == "__main__":
    main()
