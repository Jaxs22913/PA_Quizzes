#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Lecture 5 (Chemistry Panels) Arcade deck to arcade.js.

One deck per topic, joining the existing PDM Exam 1 group in syllabus order.
Cards are single atomic facts for Sprint's eight-second clock; matchCards are
recognition pairs with compressed identity tags.

NO CARD IS BUILT ON ONE OF THE THREE DISPUTED RANGES. Bicarbonate, glucose and
blood urea nitrogen each appear twice in this deck with different figures --
once on a teaching slide, once on the fishbone picture -- so there is no single
right answer to grade. Asserted below. This is the same rule the Lecture 4 deck
carries, and it matters more here because Reynolds said outright she supplies
reference ranges rather than asking anyone to recall them.

THE ANION GAP IS THE EXCEPTION AND IS CARDED. It appears once, she said 8 to 12
aloud, and it is a calculated threshold rather than a laboratory range.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a test tube with a level line
ICON5 = ('<path d="M9 3h6"/><path d="M10 3v13a2 2 0 0 0 4 0V3"/><path d="M10 12h4"/>'
         '<circle cx="12" cy="15" r="1"/>')

DECK = dict(
    id="pdm-chemistry-panels",
    name="Chemistry Panels &amp; Electrolytes",
    color="accent2",
    icon=ICON5,
    cards=[
  ["What does a chemistry panel measure?", "Metabolites, electrolytes and kidney markers, plus liver and protein markers on the expanded version."],
  ["How many tests are on a basic metabolic panel?", "Eight."],
  ["How many tests are on a comprehensive metabolic panel?", "Fourteen."],
  ["What is the difference between a chem-7 and a chem-8?", "The chem-8 includes calcium."],
  ["What does the comprehensive panel add to the basic one?", "Six markers of liver function and protein: albumin, total protein, alkaline phosphatase, alanine transaminase, aspartate aminotransferase and bilirubin."],
  ["When is a basic metabolic panel enough?", "For electrolytes, glucose and renal screening."],
  ["When should you order a comprehensive panel instead?", "When you need a fuller picture of liver and nutritional protein status."],
  ["On a panel, what does Cr mean?", "Creatinine — not chromium."],
  ["Which is the major extracellular cation?", "Sodium."],
  ["Which is the major intracellular cation?", "Potassium."],
  ["Which is the major extracellular anion?", "Chloride."],
  ["What is the primary extracellular buffer?", "Bicarbonate."],
  ["An abnormal sodium is a problem with what, first?", "Water — ask about free water before asking about salt."],
  ["What does serum sodium actually reflect?", "Water balance, not total-body sodium."],
  ["What controls water handling, and therefore serum sodium?", "Thirst and antidiuretic hormone."],
  ["What governs extracellular volume?", "Total-body sodium, through the renin–angiotensin–aldosterone system."],
  ["How do the kidneys compensate when free body water rises?", "By conserving sodium and excreting water."],
  ["Why does potassium have to be replaced by diet or supplement?", "It is excreted by the kidneys with no reabsorption, so the level can drop rapidly."],
  ["Which hormone drives renal potassium excretion, and where?", "Aldosterone, at the distal tubule and collecting duct."],
  ["What three things shift potassium across the cell membrane?", "Insulin, acid-base status and catecholamines."],
  ["What complication threatens at BOTH ends of the potassium range?", "Life-threatening cardiac arrhythmias."],
  ["Why does chloride follow sodium?", "To maintain electrical neutrality."],
  ["What does a low chloride with a high bicarbonate suggest?", "Metabolic alkalosis — classically from vomiting."],
  ["Why is bicarbonate reported as CO2 on a panel?", "The panel reports total carbon dioxide, which is mostly serum bicarbonate."],
  ["A low bicarbonate means what, and triggers what?", "Metabolic acidosis — and it is the trigger to calculate the anion gap."],
  ["A high bicarbonate means what?", "Metabolic alkalosis."],
  ["What is the anion gap formula?", "Sodium minus the sum of chloride and bicarbonate."],
  ["What is the normal anion gap?", "8 to 12 milliequivalents per litre."],
  ["What is the normal range for the extended anion gap?", "10 to 14 — the extended formula adds potassium to sodium."],
  ["A raised anion gap means what?", "An increase in unmeasured acids."],
  ["What causes a NORMAL anion gap acidosis?", "Bicarbonate loss from the gut or the kidney — hyperchloraemic acidosis."],
  ["How do you correct the anion gap for a low albumin?", "Add about 2.5 for every 1 g/dL the albumin has fallen."],
  ["What does acidosis do to serum potassium?", "Drives it out of cells, so the serum level rises."],
  ["What does alkalosis do to serum potassium?", "Drives it into cells, so the serum level falls."],
  ["Where is blood urea nitrogen produced and cleared?", "Produced by the liver, cleared by the kidneys."],
  ["Name four non-renal things that raise blood urea nitrogen.", "Dehydration, gastrointestinal bleeding, high protein intake and catabolic states."],
  ["What does a urea nitrogen to creatinine ratio above 20 to 1 suggest?", "A prerenal cause."],
  ["Where does creatinine come from?", "Muscle creatine metabolism."],
  ["What three things influence creatinine and can mislead?", "Muscle mass, age and sex."],
  ["In whom can a normal creatinine hide a reduced filtration rate?", "Elderly or cachectic patients — low muscle mass."],
  ["Which is more liver-specific, aspartate aminotransferase or alanine transaminase?", "Alanine transaminase — the other is also in cardiac and skeletal muscle, kidney and brain."],
  ["What does a raised alkaline phosphatase mark?", "Cholestasis or bile duct obstruction."],
  ["Which three non-hepatic tissues contain alkaline phosphatase?", "Bone, placenta and intestine."],
  ["How do you confirm a raised alkaline phosphatase is hepatic?", "Gamma-glutamyl transferase."],
  ["Are the transaminases, alkaline phosphatase and bilirubin markers of function?", "No — they mark liver INJURY. Function is albumin, prothrombin time and bilirubin."],
  ["Which liver test is the most sensitive marker of function?", "The prothrombin time with its ratio — it can prolong within 24 hours."],
  ["Which clotting factors does the prothrombin time reflect?", "Factors two, seven, nine and ten."],
  ["Why does a low albumin mean chronic liver disease?", "Its half-life is about three weeks, so the level takes that long to fall."],
  ["What defines a hepatocellular pattern?", "Transaminases raised out of proportion to alkaline phosphatase."],
  ["What defines a cholestatic pattern?", "Alkaline phosphatase raised out of proportion to the transaminases."],
  ["What does an aspartate to alanine ratio above 2 to 1 suggest?", "Alcoholic liver disease."],
  ["Transaminases in the thousands narrow to which three causes?", "Viral hepatitis, ischaemia and toxins."],
  ["A raised aspartate aminotransferase with a normal alanine transaminase points where?", "Cardiac or skeletal muscle, not liver."],
  ["What causes isolated hyperbilirubinaemia?", "Gilbert syndrome and haemolysis."],
  ["Which syndrome shows liver and kidney failure together?", "Hepatorenal syndrome."],
  ["What does serum osmolality let you distinguish?", "True hypotonic hyponatraemia from the pseudo- and hypertonic forms."],
  ["What does a urine sodium below 20 suggest?", "Hypovolaemia."],
  ["What does a urine sodium above 40 with concentrated urine suggest?", "The syndrome of inappropriate antidiuretic hormone secretion."],
  ["What does hyperglycaemia do to the measured sodium?", "Lowers it by dilution — use a corrected sodium."],
  ["What causes pseudohyponatraemia, and what gives it away?", "Severe hyperlipidaemia or hyperproteinaemia — the osmolality is normal."],
  ["Why does a normal result not exclude disease?", "A normal range is the mean plus or minus two standard deviations, so about 2.5 per cent of healthy people fall outside it."],
  ["How long must a reduced filtration rate persist to be called chronic?", "At least three months."],
  ["Which test confirms an estimated filtration rate when accuracy matters?", "Cystatin C."],
  ["Which imaging comes first for abnormal liver tests?", "Ultrasound."],
  ["In the vomiting case, what does the panel show?", "Low sodium, low potassium, low chloride, a raised bicarbonate and alkalaemia."],
  ["What keeps that alkalosis going?", "Volume, potassium and chloride depletion force the kidney to reabsorb sodium and bicarbonate."],
  ["What corrects it?", "Replacing sodium, chloride and potassium — saline with potassium chloride."],
    ],
    matchCards=[
  ["Sodium", "Major extracellular cation; reflects WATER balance"],
  ["Potassium", "Major intracellular cation; no renal reabsorption"],
  ["Chloride", "Major extracellular anion; follows sodium"],
  ["Bicarbonate", "Primary extracellular buffer; reported as CO2"],
  ["Blood urea nitrogen", "Liver-made protein waste; non-specific"],
  ["Creatinine", "Muscle creatine waste; more specific for the kidney"],
  ["Alanine transaminase", "The MORE liver-specific transaminase"],
  ["Aspartate aminotransferase", "Also in heart, muscle, kidney, brain"],
  ["Alkaline phosphatase", "Cholestasis; confirm hepatic with GGT"],
  ["Albumin", "Synthetic function; 3-week half-life = chronic"],
  ["Prothrombin time", "Most sensitive FUNCTIONAL marker; 24 hours"],
  ["Hepatocellular pattern", "Transaminases out of proportion to ALP"],
  ["Cholestatic pattern", "ALP out of proportion to the transaminases"],
  ["Anion gap 8 to 12", "Normal, standard formula"],
  ["Urine sodium under 20", "Hypovolaemia"],
  ["Urine sodium over 40", "Inappropriate antidiuretic hormone secretion"],
  ["Urea : creatinine over 20", "Prerenal"],
  ["Pseudohyponatraemia", "Low sodium with a NORMAL osmolality"],
    ])

# ---- guard: no card may turn on one of the three disputed ranges -----------
_DISPUTED = [
    ("bicarbonate range", r"\b22\s*(?:to|-|–)\s*(?:26|28|29)\b"),
    ("glucose range",     r"\b70\s*(?:to|-|–)\s*(?:99|120)\b"),
    ("urea nitrogen range", r"\b7\s*(?:to|-|–)\s*(?:18|20)\b"),
]
_bad = []
for _pair in DECK["cards"] + DECK["matchCards"]:
    for _label, _rx in _DISPUTED:
        if any(re.search(_rx, _t, re.I) for _t in _pair):
            _bad.append((_label, _pair[0][:50]))
assert not _bad, ("a card turns on a range the deck states two different ways: %r" % _bad[:3])

# ---- guard: no duplicate prompts (the arcade duplicate-answer bug class) ---
_p = [c[0] for c in DECK["cards"]]
assert len(_p) == len(set(_p)), "duplicate card prompt: %r" % [x for x in _p if _p.count(x) > 1][:3]
_a = [c[1] for c in DECK["matchCards"]]
assert len(_a) == len(set(_a)), "duplicate match answer -- Match mode becomes unwinnable"


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render():
    lines = ['      { id: "%s", name: "%s", color: "%s",' % (DECK["id"], DECK["name"], DECK["color"]),
             '        icon: \'%s\',' % DECK["icon"],
             '        cards: [']
    for q, a in DECK["cards"]:
        lines.append('          ["%s", "%s"],' % (esc(q), esc(a)))
    lines.append('        ],')
    lines.append('        matchCards: [')
    for q, a in DECK["matchCards"]:
        lines.append('          ["%s", "%s"],' % (esc(q), esc(a)))
    lines.append('        ] },')
    return "\n".join(lines)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    fence_o, fence_c = "/*PDML5*/", "/*/PDML5*/"
    if fence_o in src:
        src = re.sub(re.escape(fence_o) + r".*?" + re.escape(fence_c), "", src, flags=re.S)

    # insert after the Lecture 4 deck inside the PDM Exam 1 group
    anchor = 'id: "pdm-cbc-hematology"'
    assert anchor in src, "PDM Lecture 4 deck not found -- has arcade.js been restructured?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fence_o + "\n" + render() + "\n" + fence_c + src[j:]

    open(ARCADE, "w", encoding="utf-8").write(src)
    print("added deck %s: %d cards, %d match pairs"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))


if __name__ == "__main__":
    main()
