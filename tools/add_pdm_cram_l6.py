#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 6 (Urinalysis) topics to the PDM I Exam 1 cram sheet.

Same colour-coded topic/table structure as the earlier lectures: the guide
carries the explanation, this carries only what has to be recallable cold.

WHAT IS DELIBERATELY NOT HERE: the reference ranges printed on slide 14 --
the pH range, the specific gravity range, the protein figures. Gopal said on
1 September that she is not asking anyone to memorise ranges and that any range
needed will be supplied. A cram row demanding one back would drill the wrong
reflex. WHICH PADS READ NEGATIVE is here, because that is exactly what she DID
say to know cold.

Two definitional thresholds are kept, and are not laboratory ranges: three red
cells for microscopic hematuria, and four hours between voids for the nitrite
conversion.

Appended after the Lecture 5 sections, in syllabus order. Idempotent.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1",
                    "pdm-exam-1-cram-sheet.html")

TOPICS = [
 ("l6-basics", "Urinalysis — The Test and the Eye", "#2f5d50", "#e6f0ec", "#eff6f3", "#22463c", [
   ("WHAT IT COVERS", "PHYSICAL, CHEMICAL and MICROSCOPIC contents of urine. Complements — does not replace — SERUM CREATININE and BLOOD UREA NITROGEN in a renal workup."),
   ("ALWAYS ORDER IT FOR", "ABDOMINAL, PELVIC or BACK PAIN. Also routine on admission."),
   ("COLOUR — pale/colourless", "DILUTE urine, possibly overhydrated."),
   ("COLOUR — dark yellow/amber", "CONCENTRATED urine, possibly dehydrated."),
   ("COLOUR — yellow-brown/green", "BILIRUBIN → hepatitis, cirrhosis, biliary obstruction."),
   ("COLOUR — bright/dark red", "BLOOD. Or food: BEETS, blueberries, rhubarb."),
   ("COLOUR — blue/orange/green", "MEDICATIONS. Tell the patient BEFORE they start so it does not alarm them."),
   ("TRANSPARENCY scale", "CLEAR → HAZY → CLOUDY → TURBID. Cloudiness = cells, bacteria, yeast, crystals, mucus, contrast or fat."),
   ("FOAM", "PROTEIN. The one inspection finding that points at a specific pad."),
   ("ODOUR — normal", "AROMATIC."),
   ("ODOUR — ammonia", "Sample STOOD too long; bacteria decomposed the urea. Refrigerate if not read in 1–2 hours, and add NO preservative."),
   ("ODOUR — foul", "Bacterial infection. FAECAL odour → enterovesical FISTULA."),
   ("ODOUR — fruity/sweet", "KETONES → check the blood sugar."),
 ]),
 ("l6-strip", "The Reagent Strip", "#3d6f8a", "#e6eef3", "#f0f5f8", "#2b5164", [
   ("SPECIMEN", "FRESH, in a STERILE container. Strips stored DESICCATED."),
   ("TIMING", "READING TIME DIFFERS BY ANALYTE — glucose 30 seconds, leukocytes 2 minutes. Cannot be read all at once."),
   ("MANUFACTURER TRAP", "Pads are in DIFFERENT ORDERS on different brands. Read a strip against ITS OWN chart."),
   ("QUALITATIVE result", "Positive or negative."),
   ("SEMI-QUANTITATIVE result", "TRACE / 1+ / 2+ / 3+ — a GRADED ESTIMATE, not a measurement."),
   ("SHOULD READ NEGATIVE", "LEUKOCYTE ESTERASE · NITRITES · KETONES · GLUCOSE · BLOOD · BILIRUBIN. Protein is negative or trace."),
   ("ALWAYS CARRY A VALUE", "SPECIFIC GRAVITY and pH. Neither is ever simply 'negative'."),
   ("What you are NOT asked", "To memorise reference RANGES. If a range is needed it will be given. Know DIRECTION and MEANING."),
 ]),
 ("l6-ph", "pH and Stones", "#7a5aa0", "#ede8f4", "#f4f1f8", "#54397a", [
   ("WHAT pH REPORTS", "The RENAL TUBULES' ability to hold the hydrogen ion concentration steady."),
   ("HOW the kidney does it", "EXCRETES hydrogen ions as AMMONIUM; REABSORBS and PRODUCES bicarbonate."),
   ("WHAT MOVES IT", "DIET · MEDICATIONS · SYSTEMIC ACID-BASE DISORDERS · TUBULAR FUNCTION."),
   ("ACIDIC urine", "Ketoacidosis · E. COLI infection · metabolic and respiratory ACIDOSIS · diet high in MEAT or cranberries."),
   ("ALKALINE urine", "UREA-SPLITTING bacteria (PROTEUS, STAPH, KLEBSIELLA, PSEUDOMONAS) · contamination · acute and chronic renal failure · RENAL TUBULAR ACIDOSIS · metabolic and respiratory ALKALOSIS · diet high in FRUIT and VEG."),
   ("THE NAME TRAP", "RENAL TUBULAR ACIDOSIS gives ALKALINE urine — the defect is a failure to EXCRETE acid."),
   ("ACIDIC urine stones", "CALCIUM OXALATE and URIC ACID. Treat by ALKALINISING the urine (chiefly for uric acid)."),
   ("ALKALINE urine stones", "TRIPLE PHOSPHATE and STRUVITE. Treat the INFECTION — urease-producing bacteria drive them."),
 ]),
 ("l6-infection", "The Two Infection Pads", "#a0522d", "#f4eae4", "#f9f3ef", "#73391f", [
   ("LEUKOCYTE ESTERASE — what", "Detects the ESTERASE white cells release. POSITIVE = PYURIA. That is the take-home point."),
   ("LEUKOCYTE ESTERASE — also raised by", "INTERSTITIAL CYSTITIS and GLOMERULONEPHRITIS — inflammatory, not infective."),
   ("NITRITES — mechanism", "UREASE-producing bacteria carry a REDUCTASE that turns urinary NITRATES into NITRITES."),
   ("NITRITES — the naming point", "It is NITRITES, not nitrates. She asked for this twice."),
   ("NITRITES — time needed", "MORE THAN FOUR HOURS in the bladder between voids for the conversion."),
   ("THE BIG ONE", "E. COLI causes MOST urinary tract infections and is RARELY UREASE-POSITIVE. So a POSITIVE nitrite is helpful; a NEGATIVE one DOES NOT rule out infection."),
   ("NITRITE sensitivity", "About 50% — LESS sensitive than leukocyte esterase."),
   ("EITHER PAD NEGATIVE + symptoms", "STILL SEND URINE CULTURE AND SENSITIVITY."),
   ("PAEDIATRIC caveat", "Less reliable in young children — they void too often for the conversion."),
 ]),
 ("l6-ketones", "Ketones and Glucose", "#b8862f", "#f6efe1", "#faf6ee", "#8a6420", [
   ("KETONES — meaning", "Cells are burning FATTY ACIDS instead of GLUCOSE. Made in the LIVER, normally fully metabolised."),
   ("KETONES — causes", "Uncontrolled DIABETES / DKA · STARVATION · FASTING · ALCOHOLIC KETOACIDOSIS · HIGH-FAT LOW-CARB diet · LIVER DISEASE · FEBRILE ILLNESS IN INFANTS AND CHILDREN."),
   ("KETONES — next move", "CHECK THE GLUCOSE."),
   ("GLUCOSE — why normally none", "Filtered freely, then WHOLLY REABSORBED in the PROXIMAL tubules."),
   ("TUBULAR THRESHOLD", "The blood glucose above which the tubules can no longer reabsorb it all — around 180 mg/dL. VARIES BETWEEN PEOPLE, which is why glucosuria is NOT diagnostic."),
   ("GLUCOSE without high blood sugar", "IMPAIRED TUBULAR REABSORPTION · DEXTROSE-containing IV fluids · PREGNANCY (trace is normal, threshold falls)."),
 ]),
 ("l6-blood", "Blood — The Three Meanings", "#9c2b2b", "#f6e6e6", "#faf0f0", "#6f1c1c", [
   ("WHAT THE PAD DETECTS", "HEME — present in RED CELLS, FREE HAEMOGLOBIN and MYOGLOBIN alike. A positive result DOES NOT SAY WHICH."),
   ("HAEMATURIA", "INTACT RED CELLS. From bleeding ANYWHERE along the urinary tract."),
   ("HAEMATURIA — causes", "INFECTION · INFLAMMATION · TRAUMA · TUMOUR · CALCULUS · OVER-AGGRESSIVE ANTICOAGULATION."),
   ("GROSS vs MICROSCOPIC", "GROSS is visible to the naked eye. MICROSCOPIC needs analysis — defined as THREE OR MORE red cells."),
   ("HAEMOGLOBINURIA", "FREE HAEMOGLOBIN, NO intact cells. From INTRAVASCULAR HAEMOLYSIS — sickle cell, transfusion reaction, severe BURNS."),
   ("HAEMOGLOBINURIA — the confirming test", "RAISED SERUM UNCONJUGATED BILIRUBIN (a direct product of hemoglobin metabolism)."),
   ("MYOGLOBINURIA", "MYOGLOBIN, NO intact cells. From SKELETAL MUSCLE injury — trauma, ELECTRIC SHOCK, RHABDOMYOLYSIS (compression, hyperthermia, STATINS)."),
   ("MYOGLOBINURIA — the confirming test", "RAISED SERUM CREATINE PHOSPHOKINASE."),
   ("TRACE blood, well patient", "Can follow STRENUOUS EXERCISE."),
 ]),
 ("l6-protein", "Bilirubin, Protein, Specific Gravity", "#2f6b8a", "#e4eef3", "#eff5f8", "#204c63", [
   ("BILIRUBIN — which form", "CONJUGATED only — it is the WATER-SOLUBLE one."),
   ("BILIRUBIN — what it means", "Disease AFTER conjugation, or BILIARY OBSTRUCTION. Can appear DAYS BEFORE JAUNDICE is visible."),
   ("PROTEIN — what and what for", "ALBUMIN mostly. Reports GLOMERULAR and TUBULAR function. Semi-quantitative."),
   ("PROTEIN — normal trace", "PREGNANCY · FEVER · STRENUOUS EXERCISE ('functional proteinuria')."),
   ("PROTEIN — false positive", "CONTAMINATION with PROSTATIC or VAGINAL secretions."),
   ("PROTEIN — the four mechanisms", "DIMINISHED TUBULAR REABSORPTION (tubular disease, pyelonephritis, interstitial nephritis) · TRANSIENT/MILD (exercise, acute illness, urinary tract bleeding or infection) · GLOMERULAR DAMAGE (nephrotic syndrome, glomerulonephritis, diabetes, polycystic kidney disease, lupus, preeclampsia) · INCREASED SERUM PROTEIN (myeloma)."),
   ("PROTEIN — next test", "TWENTY-FOUR HOUR URINE COLLECTION. The strip only estimates."),
   ("THE MYELOMA TRAP", "REAGENT STRIPS ARE INSENSITIVE TO BENCE JONES PROTEINS. Use URINE PROTEIN ELECTROPHORESIS, not a dipstick."),
   ("PROTEIN is NOT pathognomonic", "It narrows the field; it does not name the disease."),
   ("SPECIFIC GRAVITY — what", "WEIGHT of SOLUTES against an equal volume of WATER. Estimates CONCENTRATING and EXCRETORY ability."),
   ("SPECIFIC GRAVITY — particle SIZE matters", "Marbles vs glitter. RADIOGRAPHIC CONTRAST has large particles and drives it ABOVE 1.040."),
   ("LOW specific gravity (dilute)", "OVERHYDRATION · DIURESIS · CHRONIC KIDNEY DISEASE · DIABETES INSIPIDUS (less ADH → more water out)."),
   ("HIGH specific gravity (concentrated)", "DEHYDRATION · REDUCED RENAL BLOOD FLOW (heart failure, hypotension, renal artery stenosis) · SIADH (more ADH → less water out)."),
 ]),
 ("l6-after", "After the Strip", "#5a6b2f", "#eef1e4", "#f5f7ef", "#414d21", [
   ("MICROSCOPIC urinalysis adds", "WHITE CELLS · RED CELLS · SQUAMOUS EPITHELIAL CELLS · CASTS · CRYSTALS."),
   ("BACTERIA — significant when", "Collected by STRAIGHT CATHETERISATION, or alongside RAISED WHITE CELLS and a POSITIVE LEUKOCYTE ESTERASE."),
   ("BACTERIA — probably NOT significant when", "More than TWENTY SQUAMOUS EPITHELIAL CELLS per high power field (contamination), or from a LONGSTANDING INDWELLING CATHETER (colonisation, not acute infection)."),
   ("DEFINITIVE diagnosis", "GRAM STAIN and CULTURE."),
   ("THE WORKED CASE", "Dysuria/frequency/urgency + LEUKOCYTE ESTERASE, NITRITES and BLOOD positive; glucose, bilirubin, ketones, protein NEGATIVE → URINARY TRACT INFECTION → send CULTURE AND SENSITIVITY."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    for tid in [t[0] for t in TOPICS]:
        s = re.sub(r'\n  <section class="topic" id="%s".*?\n  </section>\n' % re.escape(tid),
                   "", s, flags=re.S)
        s = re.sub(r'      <a href="#%s"[^\n]*\n' % re.escape(tid), "", s)

    last = s.rindex('<section class="topic"')
    end = s.index("\n  </section>", last) + len("\n  </section>\n")
    links_anchor = s.rindex("</a>\n", 0, s.index("</nav>") if "</nav>" in s else len(s)) + len("</a>\n")

    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:end] + "".join(section(t) for t in TOPICS) + s[end:]
    s = s[:links_anchor] + links + s[links_anchor:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row"
    order = re.findall(r'<section class="topic" id="([^"]+)"', s)
    assert order.index("l5-panels") < order.index("l6-basics"), "Lecture 6 must follow Lecture 5"

    # Ranges she said she supplies must not be drilled as recallable values.
    rows = "".join(r[1] for t in TOPICS for r in t[6])
    for rx, label in ((r"4\.6\s*[–-]\s*8", "urine pH"),
                      (r"1\.00[25]\s*[–-]\s*1\.0", "specific gravity"),
                      (r"\b0\s*[–-]\s*8\s*mg", "protein")):
        assert not re.search(rx, rows), ("%s range is being drilled, but she supplies ranges" % label)

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 6 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))


if __name__ == "__main__":
    main()
