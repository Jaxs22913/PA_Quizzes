#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Lecture 6 (Urinalysis) Arcade deck to arcade.js.

One deck per topic, joining the existing PDM Exam 1 group in syllabus order.
Cards are single atomic facts for Sprint's eight-second clock; matchCards are
recognition pairs with compressed identity tags.

NO CARD DRILLS A REFERENCE RANGE. Gopal said on 1 September that she is not
asking anyone to memorise ranges and that any range needed will be supplied, so
a card demanding one back would teach the wrong reflex. Asserted below. WHICH
PADS READ NEGATIVE is carded heavily, because that is what she did say to know.

The two definitional thresholds that ARE carded -- three red cells for
microscopic hematuria, four hours for the nitrite conversion -- are
definitions and procedural intervals, not laboratory ranges.
"""
import os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a specimen cup with a fill line
ICON6 = ('<path d="M6 6h12l-1.2 13a2 2 0 0 1-2 1.8H9.2a2 2 0 0 1-2-1.8Z"/>'
         '<path d="M5 6h14"/><path d="M7.4 13h9.2"/>')

DECK = dict(
    id="pdm-urinalysis",
    name="Urinalysis",
    color="accent3",
    icon=ICON6,
    cards=[
  ["What does a urinalysis examine?", "The physical, chemical and microscopic contents of urine."],
  ["Which two serum tests does a urinalysis complement in a renal workup?", "Creatinine and blood urea nitrogen."],
  ["Which three presentations always warrant a urinalysis?", "Abdominal, pelvic or back pain."],
  ["Pale yellow, almost colourless urine suggests what?", "Dilute urine."],
  ["Dark yellow or amber urine suggests what?", "Concentrated urine."],
  ["Yellow-brown or green urine points to what?", "Bilirubin."],
  ["Which foods turn urine red?", "Beets, blueberries and rhubarb."],
  ["What should you tell a patient starting a medication that discolours urine?", "Warn them in advance so the colour does not alarm them."],
  ["What is the transparency scale?", "Clear, then hazy, then cloudy, then turbid."],
  ["Foamy urine points to what?", "Protein."],
  ["What is the normal odour of urine called?", "Aromatic."],
  ["An ammonia odour means what?", "The sample stood long enough for bacteria to decompose its urea."],
  ["How should a specimen be held if it cannot be read within one to two hours?", "Refrigerated, with no preservative added."],
  ["A faecal odour in urine suggests what?", "An enterovesical fistula."],
  ["A fruity or sweet odour points to what?", "Ketones."],
  ["Which six dipstick pads should read negative?", "Leukocyte esterase, nitrites, ketones, glucose, blood and bilirubin."],
  ["Which two dipstick parameters always carry a value rather than positive or negative?", "Specific gravity and pH."],
  ["What kind of result is trace, one plus, two plus?", "Semi-quantitative — a graded estimate."],
  ["Why can a reagent strip not be read all at once?", "The reading time differs by analyte."],
  ["Why must a strip be read against its own manufacturer's chart?", "Different brands order the pads differently."],
  ["What does urine pH report on?", "The renal tubules' ability to hold the hydrogen ion concentration steady."],
  ["How do the kidneys maintain pH?", "By excreting hydrogen ions as ammonium and reabsorbing and producing bicarbonate."],
  ["Which four things alter urine pH?", "Diet, medications, systemic acid-base disorders and tubular function."],
  ["Which organisms make urine alkaline?", "Urea-splitting bacteria — Proteus, Staphylococcus, Klebsiella, Pseudomonas."],
  ["Which stones form in acidic urine?", "Calcium oxalate and uric acid."],
  ["Which stones form in alkaline urine?", "Triple phosphate and struvite."],
  ["How are uric acid stones managed?", "Alkalinise the urine."],
  ["How are struvite stones managed?", "Treat the urinary tract infection driving them."],
  ["Renal tubular acidosis gives which urine pH?", "Alkaline — the defect is a failure to excrete acid."],
  ["What does leukocyte esterase detect?", "The esterase that white cells release into the urine."],
  ["A positive leukocyte esterase indicates what?", "Pyuria — white cells in the urine."],
  ["Which two non-infective conditions raise leukocyte esterase?", "Interstitial cystitis and glomerulonephritis."],
  ["How do nitrites appear in urine?", "Urease-producing bacteria reduce urinary nitrates to nitrites."],
  ["How long must urine sit in the bladder for nitrites to form?", "More than four hours."],
  ["Why does a negative nitrite fail to exclude infection?", "Escherichia coli causes most infections and is rarely urease-positive."],
  ["Which is more sensitive for urinary tract infection, nitrites or leukocyte esterase?", "Leukocyte esterase."],
  ["A symptomatic patient has a negative dipstick. What do you still do?", "Send urine culture and sensitivity."],
  ["Why is the nitrite pad less reliable in young children?", "They void too often for the conversion to happen."],
  ["What does ketonuria indicate?", "Cells are metabolising fatty acids instead of glucose."],
  ["Where are ketones formed?", "In the liver."],
  ["Name causes of ketonuria.", "Uncontrolled diabetes, starvation, fasting, alcoholic ketoacidosis, high-fat diets, liver disease, febrile illness in children."],
  ["Ketones on a dipstick should prompt which other check?", "The glucose."],
  ["Why is there normally no glucose in urine?", "It is filtered freely then wholly reabsorbed in the proximal tubules."],
  ["What is the tubular threshold?", "The blood glucose above which the tubules can no longer reabsorb it all."],
  ["Why is glucosuria not diagnostic?", "The tubular threshold varies between individuals."],
  ["Why can pregnancy give trace glucosuria?", "The tubular threshold falls."],
  ["What does the blood pad actually detect?", "Heme."],
  ["Why can a positive blood pad not identify its source?", "Heme sits in red cells, free hemoglobin and myoglobin alike."],
  ["What is hematuria?", "Intact red cells in the urine."],
  ["How many red cells define microscopic hematuria?", "Three or more."],
  ["Name causes of hematuria.", "Infection, inflammation, trauma, tumour, calculus, over-aggressive anticoagulation."],
  ["What is hemoglobinuria?", "Free hemoglobin in urine from intravascular hemolysis, with no intact cells."],
  ["Which serum finding confirms hemoglobinuria?", "A raised unconjugated bilirubin."],
  ["What is myoglobinuria?", "Myoglobin in urine from skeletal muscle injury, with no intact cells."],
  ["Which serum finding confirms myoglobinuria?", "A raised creatine phosphokinase."],
  ["Name causes of rhabdomyolysis.", "Compression injury, hyperthermia and statins."],
  ["Which form of bilirubin appears in urine, and why?", "Conjugated, because it is water soluble."],
  ["Why is bilirubinuria useful as a screen?", "It can appear days before the patient looks jaundiced."],
  ["Which protein does the dipstick mainly detect?", "Albumin."],
  ["In which three situations can trace protein be normal?", "Pregnancy, fever and strenuous exercise."],
  ["What causes a false positive protein result?", "Contamination with prostatic or vaginal secretions."],
  ["Which test follows a positive protein dipstick?", "A twenty-four hour urine collection."],
  ["Name the four mechanisms of proteinuria.", "Diminished tubular reabsorption, transient or mild, glomerular damage, and increased serum protein."],
  ["Why can a dipstick not find multiple myeloma?", "Reagent strips are insensitive to Bence Jones proteins."],
  ["Which test finds Bence Jones proteins?", "Urine protein electrophoresis."],
  ["What does specific gravity measure?", "The weight of solutes in urine against an equal volume of water."],
  ["Why does radiographic contrast raise specific gravity so sharply?", "Its particles are large, and particle size affects the measurement."],
  ["Name causes of a low specific gravity.", "Overhydration, diuresis, chronic kidney disease and diabetes insipidus."],
  ["Name causes of a high specific gravity.", "Dehydration, reduced renal blood flow and the syndrome of inappropriate antidiuretic hormone."],
  ["What does a microscopic urinalysis add?", "White cells, red cells, squamous epithelial cells, casts and crystals."],
  ["When are bacteria in urine likely significant?", "From straight catheterisation, or with raised white cells and a positive leukocyte esterase."],
  ["More than twenty squamous epithelial cells per high power field means what?", "The specimen is likely contaminated."],
  ["Bacteria from a longstanding indwelling catheter usually mean what?", "Colonisation rather than acute infection."],
  ["What makes a urinary infection diagnosis definitive?", "Gram stain and culture."],
    ],
    matchCards=[
  ["Leukocyte esterase", "Positive means PYURIA"],
  ["Nitrites", "Urease-producing bacteria; E. coli misses it"],
  ["Ketones", "Burning fatty acids instead of glucose"],
  ["Glucose", "Blood level past the TUBULAR THRESHOLD"],
  ["Blood", "Detects HEME; cannot say which source"],
  ["Bilirubin", "CONJUGATED only; precedes jaundice"],
  ["Protein", "Albumin; glomerular and tubular function"],
  ["Specific gravity", "Solute weight; particle SIZE matters"],
  ["pH", "Tubular handling of hydrogen ions"],
  ["Hematuria", "INTACT red cells"],
  ["Hemoglobinuria", "No cells; raised UNCONJUGATED BILIRUBIN"],
  ["Myoglobinuria", "No cells; raised CREATINE PHOSPHOKINASE"],
  ["Foamy urine", "Protein"],
  ["Ammonia odour", "Sample stood; urea decomposed"],
  ["Faecal odour", "Enterovesical fistula"],
  ["Fruity odour", "Ketones"],
  ["Acidic urine stones", "Calcium oxalate and uric acid"],
  ["Alkaline urine stones", "Triple phosphate and struvite"],
  ["Diabetes insipidus", "LOW specific gravity, dilute urine"],
  ["Bence Jones proteins", "Missed by the strip; needs ELECTROPHORESIS"],
    ])


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
    # No card may drill a reference range she said she supplies.
    blob = " ".join(q + " " + a for q, a in DECK["cards"] + DECK["matchCards"])
    for rx, label in ((r"4\.6", "urine pH range"),
                      (r"1\.00[25]\s*[-–]", "specific gravity range"),
                      (r"\b0\s*[-–]\s*8\s*mg", "protein range")):
        assert not re.search(rx, blob), "%s is being drilled, but she supplies ranges" % label

    src = open(ARCADE, encoding="utf-8").read()
    fence_o, fence_c = "/*PDML6*/", "/*/PDML6*/"
    if fence_o in src:
        src = re.sub(re.escape(fence_o) + r".*?" + re.escape(fence_c), "", src, flags=re.S)

    anchor = 'id: "pdm-chemistry-panels"'
    assert anchor in src, "PDM Lecture 5 deck not found -- has arcade.js been restructured?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fence_o + "\n" + render() + "\n" + fence_c + src[j:]

    open(ARCADE, "w", encoding="utf-8").write(src)
    print("added deck %s: %d cards, %d match pairs"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))


if __name__ == "__main__":
    main()
