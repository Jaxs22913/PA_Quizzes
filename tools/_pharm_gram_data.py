# -*- coding: utf-8 -*-
"""Rows for the gram-coverage sheet -- Pharmacology I Exam 1, Lecture 1.

The three verdicts in every row are READ OUT OF THE DECK, not written by hand:
each class slide carries a small traffic-light table and
extract_pharm_gram_coverage.py pulls the colour under each heading. That is the
lecturer's own judgement of coverage, which is the whole point of the page.

`drugs` and `note` are transcribed from the same slide. `slide` is cited on
every row so any cell can be checked in seconds.

WHY THIS PAGE EXISTS. Dr. Wood, at the exam review the night before the paper:
he will not ask which single drug treats one named organism, he will ask
whether an agent covers gram-positives, gram-negatives, anaerobes or atypicals,
and he described the item outright -- three agents with strictly gram-negative
coverage and one good gram-positive, pick it. This is the axis he said he tests.
"""
# class, drugs, note, slide
ROWS = [
 ("Natural penicillins", "penicillin G, penicillin V",
  "Good against gram-positive <b>cocci</b>, but <b>no staph coverage</b>. Drug of choice for "
  "syphilis, gas gangrene and meningococcus. No activity against aerobic gram-negatives.", 17),
 ("Aminopenicillins", "ampicillin, amoxicillin",
  "As the natural penicillins, plus <b>some gram-negative aerobes</b>. Drug of choice for "
  "Enterococcus, Listeria and endocarditis prophylaxis. Still <b>no staph coverage</b>.", 19),
 ("Aminopenicillin + beta-lactamase inhibitor",
  "amoxicillin/clavulanate, ampicillin/sulbactam",
  "<b>Adding the inhibitor buys anaerobes</b> (including Bacteroides) and <b>MSSA</b>. Drug of "
  "choice for skin and soft tissue, diabetic foot, and animal or human bites.", 25),
 ("Penicillinase-resistant penicillins", "nafcillin, oxacillin, dicloxacillin",
  "<b>Designed solely to cover S. aureus (MSSA)</b>, with decreased activity against everything "
  "else. Not for MRSA &mdash; vancomycin is the choice there.", 26),
 ("Antipseudomonal penicillins", "piperacillin, piperacillin/tazobactam",
  "Broad spectrum. <b>Keeps gram-positive coverage (MSSA only), adds gram-negative and "
  "antipseudomonal activity.</b> Drug of choice for polymicrobial, nosocomial and "
  "intra-abdominal infection.", 27),
 ("Cephalosporins &mdash; 1st generation", "cefazolin, cephalexin",
  "<b>Great gram-positive activity</b> (but no Enterococcus). Some gram-negatives &mdash; "
  "E. coli, Proteus, Klebsiella. Surgical prophylaxis, cellulitis, urinary infection.", 32),
 ("Cephalosporins &mdash; 2nd generation", "cefotetan, cefoxitin, cefuroxime, cefprozil",
  "<b>More gram-negative activity than first generation</b> &mdash; H. influenzae, Enterobacter, "
  "Neisseria, Proteus, E. coli, Klebsiella.", 33),
 ("Cephalosporins &mdash; 3rd generation", "ceftriaxone, ceftazidime, cefotaxime, cefdinir, cefixime",
  "<b>Better gram-negative coverage than second generation, and loses more gram-positive.</b> "
  "Adds Serratia and Moraxella catarrhalis. Ceftriaxone needs no renal adjustment but is "
  "avoided in the first 30 days of life.", 34),
 ("Cephalosporins &mdash; 4th generation", "cefepime",
  "<b>The exception to the trade-off: gram-negative activity WITHOUT sacrificing "
  "gram-positive.</b> Antipseudomonal. No MRSA, no Enterococcus.", 36),
 ("Cephalosporins &mdash; 5th generation", "ceftaroline",
  "<b>The cephalosporin with MRSA coverage.</b> Gram-negative and gram-positive, no "
  "Enterococcus, no anaerobes.", 37),
 ("Cephalosporins &mdash; 5th generation", "ceftolozane/tazobactam",
  "Antipseudomonal, with <b>some anaerobic activity including Bacteroides</b>. No MRSA, no "
  "Enterococcus.", 38),
 ("Monobactam", "aztreonam",
  "<b>Gram-negative ONLY.</b> Spectrum resembles the aminoglycosides, with activity against "
  "P. aeruginosa.", 40),
 ("Carbapenems", "imipenem, meropenem, ertapenem",
  "<b>Very broad</b> &mdash; gram-positive (not MRSA), gram-negative, anaerobes, and "
  "P. aeruginosa <b>except ertapenem</b>.", 43),
 ("Vancomycin", "vancomycin",
  "<b>Gram-positive ONLY.</b> Drug of choice for MRSA and for penicillin-allergic infections.", 47),
 ("Macrolides", "azithromycin, clarithromycin, erythromycin",
  "Gram-positive and gram-negative aerobes, and the <b>atypicals</b>. Does <b>not</b> cover "
  "enterococci.", 55),
 ("Tetracyclines", "tetracycline, doxycycline, minocycline",
  "<b>Moderate across all three</b> rather than strong anywhere &mdash; the only class the deck "
  "marks that way. Watch the calcium and iron binding, and photosensitivity.", 62),
 ("Tigecycline", "tigecycline",
  "Broad across all three. Bacteriostatic, for complicated skin infection.", 65),
 ("Aminoglycosides", "gentamicin, tobramycin, amikacin",
  "<b>Gram-negatives</b>, including Pseudomonas and Enterobacter. <b>No gram-positive "
  "coverage.</b> The trough is checked to confirm it is undetectable.", 68),
 ("Oxazolidinone", "linezolid",
  "For <b>vancomycin-resistant Enterococcus</b>. Gram-positive only.", 72),
 ("Fluoroquinolones &mdash; 2nd generation", "ciprofloxacin",
  "<b>Gram-negative and atypical</b> coverage, with variable Pseudomonas activity. "
  "Gram-positive cover is limited.", 76),
 ("Fluoroquinolones &mdash; 3rd generation", "levofloxacin",
  "Second-generation coverage <b>with improved gram-positive activity</b>, and it "
  "<b>keeps</b> Pseudomonas. Community-acquired pneumonia.", 77),
 ("Fluoroquinolones &mdash; 3rd generation", "moxifloxacin",
  "Second-generation coverage with improved gram-positive activity, but <b>loses</b> "
  "Pseudomonas. Community-acquired pneumonia.", 78),
 ("Clindamycin", "clindamycin",
  "Gram-positive aerobes <b>including MRSA</b>, and gram-positive anaerobes. It binds toxin, "
  "which is why it appears in toxic shock.", 80),
 ("Sulfamethoxazole and trimethoprim", "sulfamethoxazole/trimethoprim",
  "Gram-positive aerobes <b>including MRSA</b>, and gram-negative aerobes. Does <b>not</b> "
  "cover enterococci.", 83),
 ("Metronidazole", "metronidazole",
  "<b>Anaerobes only</b> &mdash; gram-positive and gram-negative anaerobes. The alcohol "
  "interaction is its signature.", 86),
 ("Polymyxins", "polymyxin B, colistin (polymyxin E)",
  "<b>Gram-negative only.</b> A detergent-like mechanism against the lipopolysaccharide of the "
  "gram-negative outer membrane.", 87),
]

# The lecturer's own rule, stated as its own slide, and the single most
# quotable line for the cephalosporin block.
PROGRESSION = dict(slide=31, lines=[
 "As one moves up in cephalosporin generation, <b>more gram-negative activity</b> is seen",
 "Consequently, <b>gram-positive activity is decreased</b> advancing in generation",
 "<b>4th generation has gram-negative activity without sacrificing gram-positive activity</b>",
])
