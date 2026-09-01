# -*- coding: utf-8 -*-
"""Length-bias fixes for the PDM I Lecture 6 pool.

Jaxon's rule, 2026-08-30: SHORTEN THE ANSWER, do not pad the distractors -- and
never shorten at the cost of learning. So KEYS holds shortened correct answers,
and it is asserted that every one really is shorter.

SPECIFIC holds the exception. Where the correct answer is a LIST and the list
IS the content -- the six analytes that read negative, the sediment elements --
cutting it would cost the fact. There the fix is to make one distractor
genuinely more specific rather than longer for its own sake, so it competes on
content instead of on being obviously too short.

Indices are positions in POOL (pool A, then B, C, D, E).
"""

# --- shortened CORRECT answers ------------------------------------------
KEYS = {
  5:   "Warn the patient to expect it",
  8:   "Cells, organisms, crystals, mucus, or fat",
  10:  "Bacteria broke down the urea as it stood",
  20:  "Leukocyte esterase, nitrites, ketones, glucose, blood, bilirubin",
  23:  "Acts as a selective filter into the tubules",
  25:  "Tubular handling of hydrogen ions",
  26:  "Excreting hydrogen ions and keeping bicarbonate",
  27:  "Diet, drugs, acid-base status, and tubular function",
  28:  "Proteus, Klebsiella, or Pseudomonas",
  33:  "The infection driving them",
  37:  "Send a urine culture and sensitivity anyway",
  39:  "Bacteria reduce urinary nitrates to nitrites",
  41:  "Escherichia coli is rarely urease-positive",
  43:  "Proteus, Klebsiella, and Staphylococcus",
  47:  "Fever in infants and children",
  50:  "The blood glucose the tubules can no longer fully reabsorb",
  52:  "Normal in pregnancy, from a lower tubular threshold",
  57:  "It can precede visible jaundice by days",
  58:  "Hepatitis, cirrhosis, cancer, or gallstones",
  59:  "Albumin, reflecting glomerular and tubular function",
  62:  "Contamination by genital secretions",
  69:  "Solute weight against an equal volume of water",
  71:  "Its particles are large",
  75:  "Red cells, white cells, epithelial cells, casts, and crystals",
  80:  "Which source is responsible",
  84:  "Infection, trauma, tumour, or a stone",
  85:  "Over-aggressive anticoagulation",
  92:  "Compression, hyperthermia, or a statin",
  101: "As unhelpful for excluding infection",
  102: "Children void too often for the conversion",
  109: "Send urine protein electrophoresis",
  111: "Radiographic contrast material",
  113: "Treat it as likely contaminated",
  114: "Catheter colonisation",
}

# --- distractors made more SPECIFIC, where the key is an irreducible list ---
# (question index, option index) -> replacement. Each has to stay wrong.
SPECIFIC = {
  (20, 1): "Leukocyte esterase, nitrites, ketones, and specific gravity",
  (35, 1): "Bacteriuria, confirmed by the pad",
  (38, 1): "Diabetes insipidus and severe dehydration",
  (52, 1): "It establishes gestational diabetes mellitus",
  (99, 1): "Specific gravity, pH, and appearance",
}
