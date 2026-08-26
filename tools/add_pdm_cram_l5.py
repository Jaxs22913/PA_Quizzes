#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 5 topics to the PDM I Exam 1 cram sheet.

Same colour-coded topic/table structure as the earlier lectures: the guide
carries the explanation, this carries only what has to be recallable cold.

WHAT IS DELIBERATELY NOT HERE: the three reference ranges this deck states two
different ways. Reynolds said on 26 August that she always supplies reference
ranges, so a cram row demanding one back would be teaching the wrong reflex.
The DISAGREEMENT gets its own row instead, because that is the thing worth
knowing. The anion gap's 8 to 12 IS here -- she said it aloud and it is a
calculated threshold, not a laboratory range.

Appended after the Lecture 4 sections, in syllabus order. Idempotent.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1",
                    "pdm-exam-1-cram-sheet.html")

TOPICS = [
 ("l5-panels", "Chem Panels — What Is On Which", "#8a5f2f", "#f3ebe0", "#f9f4ec", "#6b4722", [
   ("BASIC metabolic panel — 8 tests", "GLUCOSE · CALCIUM · SODIUM · POTASSIUM · CHLORIDE · CO2 (bicarbonate) · BUN · CREATININE. Also called chem-7 or chem-8."),
   ("CHEM-7 vs CHEM-8", "CALCIUM. The chem-8 has it, the chem-7 does not. That is the whole difference."),
   ("COMPREHENSIVE panel — 14 tests", "All 8 above PLUS ALBUMIN · TOTAL PROTEIN · ALKALINE PHOSPHATASE · ALANINE TRANSAMINASE · ASPARTATE AMINOTRANSFERASE · BILIRUBIN. Also called chem-14."),
   ("Which panel when", "BASIC is enough for ELECTROLYTES, GLUCOSE and RENAL SCREENING. Step up to COMPREHENSIVE when you need LIVER and NUTRITIONAL PROTEIN status."),
   ("The functional groups", "FUEL: glucose. ELECTROLYTES/ACID-BASE: sodium, potassium, chloride, bicarbonate. KIDNEY: BUN, creatinine. MINERAL: calcium. LIVER/PROTEIN (comprehensive only): the six."),
   ("Two abbreviation traps she called out", "Cr = CREATININE, not chromium. BUN = BLOOD UREA NITROGEN, not boron-uranium-nitrogen. And DO NOT ABBREVIATE IN THE ELECTRONIC NOTE — write sodium out."),
   ("THE RANGES YOU DO NOT HAVE TO MEMORISE", "Her words: “we ALWAYS give you reference ranges.” Learn DIRECTION of abnormality and the rough figure. Sodium “around 140” is the level of detail she asked for."),
   ("Where this deck contradicts itself", "BICARBONATE text 22–29 vs fishbone 22–28 (22–26 in the gas column). GLUCOSE text 70–99 fasting vs fishbone 70–120. BUN text 7–20 vs fishbone 7–18. CREATININE 0.6–1.2 agrees. Nothing is graded on which is right."),
   ("Why a normal result does not exclude disease", "A normal range is the MEAN ± 2 STANDARD DEVIATIONS, so ~2.5% OF HEALTHY PEOPLE fall outside it by chance."),
 ]),
 ("l5-lytes", "The Electrolytes & Acid-Base", "#2f5f8a", "#e2ecf5", "#f0f5fa", "#22465f", [
   ("The four cations and anions", "SODIUM = major EXTRAcellular cation. POTASSIUM = major INTRAcellular cation. CHLORIDE = major EXTRAcellular anion. BICARBONATE = primary extracellular BUFFER."),
   ("THE SODIUM RULE", "An abnormal sodium is a WATER PROBLEM FIRST. Ask “too much or too little free water?” BEFORE “too much or too little salt?” Serum sodium reflects WATER BALANCE, not total-body sodium."),
   ("Who controls what", "WATER handling → THIRST and ANTIDIURETIC HORMONE. EXTRACELLULAR VOLUME → total-body sodium via RENIN–ANGIOTENSIN–ALDOSTERONE."),
   ("Potassium handling", "EXCRETED BY THE KIDNEY WITH NO REABSORPTION → must be replaced by DIET or SUPPLEMENT or it drops fast. Driven by ALDOSTERONE at the DISTAL TUBULE and COLLECTING DUCT."),
   ("What shifts potassium across the membrane", "INSULIN · ACID-BASE STATUS · CATECHOLAMINES. This is why the potassium in DKA misleads — serum can be HIGH while TOTAL BODY IS DEPLETED."),
   ("Potassium ↔ pH — both directions", "ACIDOSIS drives K OUT of cells (serum rises). ALKALOSIS drives K IN (serum falls). And K DEPLETION INCREASES RENAL ACID SECRETION."),
   ("Potassium danger", "BOTH hyper- and hypokalaemia cause LIFE-THREATENING ARRHYTHMIAS. Small serum changes = large physiological effect."),
   ("Chloride", "Follows SODIUM to preserve ELECTRICAL NEUTRALITY. Useless alone. RECIPROCAL WITH BICARBONATE. LOW Cl + HIGH HCO3 = METABOLIC ALKALOSIS (vomiting). Losing Cl raises the strong ion difference."),
   ("Bicarbonate", "Reported as “CO2” = TOTAL carbon dioxide, mostly bicarbonate. LOW = METABOLIC ACIDOSIS → CALCULATE THE ANION GAP. HIGH = METABOLIC ALKALOSIS."),
 ]),
 ("l5-gap", "The Anion Gap — She Wants This Calculated", "#7a2f5f", "#f3e2ee", "#f9f0f6", "#5c2247", [
   ("THE FORMULA", "ANION GAP = SODIUM − (CHLORIDE + BICARBONATE). NORMAL 8–12 mEq/L. She said this aloud: “quick and dirty, calculate your anion gap, and our normal range is 8 to 12.”"),
   ("Extended formula", "(SODIUM + POTASSIUM) − (CHLORIDE + BICARBONATE). NORMAL 10–14. Potassium is added to the CATIONS."),
   ("RAISED gap", "Unmeasured ACIDS. MUDPILES: Methanol · Uraemia · Diabetic ketoacidosis · Paraldehyde/propylene glycol · Isoniazid/iron · Lactic acidosis · Ethylene glycol · Salicylates."),
   ("NORMAL gap", "BICARBONATE LOSS from GUT or KIDNEY = HYPERCHLORAEMIC metabolic acidosis."),
   ("Albumin correction", "ADD ~2.5 to the gap for every 1 g/dL the ALBUMIN HAS FALLEN — albumin is itself an unmeasured anion."),
   ("WHAT SHE DOES NOT WANT CALCULATED", "GLOMERULAR FILTRATION RATE — “I don’t need you to calculate that or know that just yet, but know OF it.” CORRECTED SODIUM — she uses UpToDate/MedCalc. Know WHAT it is for and WHICH WAY it moves."),
 ]),
 ("l5-kidney-liver", "Kidney & Liver Markers", "#2f6b4a", "#e0efe7", "#f0f7f3", "#235238", [
   ("BUN", "Nitrogenous waste of PROTEIN metabolism. Made by the LIVER, cleared by the KIDNEY. NON-SPECIFIC — also raised by DEHYDRATION, GI BLEEDING, HIGH PROTEIN INTAKE, CATABOLIC STATES."),
   ("Creatinine", "Waste of MUSCLE CREATINE metabolism. Filtered by the kidney. MORE SPECIFIC than BUN. Influenced by MUSCLE MASS, AGE, SEX."),
   ("THE RATIO", "BUN : CREATININE > 20 : 1 = PRERENAL. Below that = INTRINSIC RENAL."),
   ("The creatinine trap", "A NORMAL creatinine can HIDE a reduced filtration rate in the ELDERLY or CACHECTIC — low muscle mass makes less creatinine."),
   ("INJURY vs FUNCTION — the asterisk on her slide", "AST · ALT · ALK PHOS · BILIRUBIN mark liver INJURY. ALBUMIN · PROTHROMBIN TIME · BILIRUBIN measure FUNCTION."),
   ("AST vs ALT", "ALT is MORE liver-specific. AST is ALSO in CARDIAC and SKELETAL MUSCLE, KIDNEY and BRAIN — so a raised AST with a NORMAL ALT points to MUSCLE, not liver."),
   ("Alkaline phosphatase", "CHOLESTASIS / BILE DUCT OBSTRUCTION. Also in BONE, PLACENTA, INTESTINE. CONFIRM HEPATIC ORIGIN WITH GGT."),
   ("Albumin", "Made ONLY by the liver, HALF-LIFE ~3 WEEKS → a LOW albumin means CHRONIC disease (>3 weeks). May also drop in severe illness."),
   ("Prothrombin time / INR", "MOST SENSITIVE FUNCTIONAL MARKER. Can prolong WITHIN 24 HOURS. Factors II, VII, IX, X."),
   ("The four hepatic patterns", "HEPATOCELLULAR: AST/ALT out of proportion to ALP. CHOLESTATIC: ALP out of proportion to AST/ALT. MIXED: both. ISOLATED HYPERBILIRUBINAEMIA: bilirubin up, enzymes normal (Gilbert, haemolysis)."),
   ("Three liver shortcuts", "AST:ALT > 2:1 = ALCOHOL. AST/ALT IN THE THOUSANDS = only 3 causes — VIRAL, ISCHAEMIA, TOXINS. Magnitude: mild <5×, moderate 5–15×, severe >15×."),
 ]),
 ("l5-fluid", "Patterns, Fluid Balance & The Vomiting Case", "#5a3a5e", "#ece3ee", "#f6f1f6", "#432c46", [
   ("RENAL pattern", "↑ BUN · ↑ CREATININE · ↓ FILTRATION RATE · ± ↑ POTASSIUM, ↑ PHOSPHATE, ↓ CALCIUM · METABOLIC ACIDOSIS · ALBUMINURIA."),
   ("HEPATIC pattern", "↑ AST/ALT (hepatocellular) OR ↑ ALP/BILIRUBIN (cholestatic); ↓ ALBUMIN and ↑ PROTHROMBIN TIME in advanced disease."),
   ("METABOLIC pattern (DKA)", "↑ GLUCOSE · ↓ BICARBONATE · ↑ ANION GAP · LOW pH · ± ↑ POTASSIUM DESPITE TOTAL-BODY DEPLETION."),
   ("Two overlaps by name", "HEPATORENAL SYNDROME = liver AND kidney failure together. CARDIORENAL SYNDROME = the cardiac equivalent. DKA hits electrolytes and kidney at once."),
   ("Reading order for an abnormal panel", "ELECTROLYTES/ACID-BASE (then the gap) → RENAL (BUN, creatinine, ratio) → GLUCOSE → LIVER → MINERALS."),
   ("Fluid balance core tests", "SERUM SODIUM = water balance. SERUM OSMOLALITY (~275–285) separates TRUE hypotonic from PSEUDO/HYPERTONIC. URINE SODIUM <20 = HYPOVOLAEMIA; >40 with concentrated urine = SIADH. BUN:Cr >20 = PRERENAL."),
   ("THREE PITFALLS", "HYPERGLYCAEMIA lowers measured sodium ~1.6–2 per 100 mg/dL glucose → CORRECTED SODIUM. PSEUDOHYPONATRAEMIA from HYPERLIPIDAEMIA/HYPERPROTEINAEMIA — low sodium with a NORMAL OSMOLALITY. And THE NUMBER ALONE NEVER GIVES THE DIAGNOSIS."),
   ("Correlating with other tests", "ABNORMAL LFTs → ULTRASOUND first. LOW eGFR/ALBUMINURIA → urine studies + renal ultrasound; CHRONIC needs ≥3 MONTHS; CYSTATIN C confirms. DKA → ketones/beta-hydroxybutyrate, venous gas, urinalysis, ECG (for potassium), CBC. HYPONATRAEMIA → serum osm + urine sodium/osm."),
   ("THE VOMITING CASE", "↓ Na · ↓ K · ↓ Cl · ↑ HCO3 · ALKALAEMIA. WHY IT PERSISTS: volume + K + Cl depletion force the kidney to reabsorb sodium AND bicarbonate. WHAT FIXES IT: SALINE + POTASSIUM CHLORIDE — replacing all three. NOT bicarbonate."),
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
    assert order.index("l4-cbc-wbc") < order.index("l5-panels"), "Lecture 5 must follow Lecture 4"

    # the three disputed ranges must not appear as a value to recall
    for rx, label in ((r"\b22\s*[–-]\s*29\b", "bicarbonate"),
                      (r"\b70\s*[–-]\s*99\b", "glucose"),
                      (r"\b7\s*[–-]\s*20\b", "urea nitrogen")):
        rows = "".join(r[1] for t in TOPICS for r in t[6] if "contradicts" not in r[0])
        assert not re.search(rx, rows), ("%s range is being drilled as a recallable value, "
                                         "but the deck states it two ways" % label)

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 5 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, syllabus order and disputed-range guard verified")


if __name__ == "__main__":
    main()
