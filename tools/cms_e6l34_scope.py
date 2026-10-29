# -*- coding: utf-8 -*-
"""Lecture 34 scope -- Acid-Base Part I (Finck), CMS I Exam 6 (Respiratory Block Exam I).

Read by cms_e6_partition.py (guards) and imported by every Lecture 34 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Megan B. Finck, MMS, PA-C -- title slide 1, and the 2026-10-27 recording (Notability, two clips:
13:08 for 51.4 min and 14:19 for 45.6 min). She opens by tying it to "what I talked about this morning" (her
PDM Lecture 19, Acid-Base Balance and Blood Gas Interpretation). Agrees with calendar-data.js ("CMS I -
LECTURE #34 -Acid Base Part I - Professor Finck"). The deck file carries no lecture number.

RECORDING GAP: clip 1 ends at her ten-minute break ("before I get into metabolic acidosis"), clip 2 starts at
slide 54 (the two mnemonics). Slides 45-53 (metabolic acidosis, the anion gap, its errors, compensation, lab
findings) were taught in the unrecorded minutes after the break; their emphasis is unknown, so they are weighted
as plain slide content.

THE CASES: from about 16 minutes into clip 2 to its end she worked four cases on the board that are NOT in the
deck (slide 64 is only the title "Case Studies"; slide 67 credits "Case studies 1-4 ... Dr. John Long" and "5
... Step-Up to Medicine"). She said she will post them on Canvas. Per Jaxon (2026-10-29) nothing is written from
the case portion until she uploads them; it is used for emphasis only. No item reuses a case's patient or values.

EMPHASIS (minutes spoken, Notability + our Whisper transcript): normal values ("burn this into your eyeballs,
the 7.35 to 7.45"; carbon dioxide 40 and bicarbonate 24 as the working midpoints); "the answer to how do we
treat an acid-base problem is always going to be correct the underlying disorder"; respiratory acidosis = COPD
first ("first thing that comes to mind"), the sleepy, confused patient, acute vs chronic read from how far the
kidneys have compensated; obesity hypoventilation syndrome "a frequent ... question because it has a triad";
paper bag "doesn't actually do anything" (placebo); metabolic alkalosis: saline responsive is the common one,
"rarely ... above 55" carbon dioxide from compensation, urine chloride to split the types, blood pressure next
for the unresponsive ones, licorice as "a unicorn"; metabolic acidosis "by far the most complex": the two
mnemonics, and "Winter's formula ... I want you to commit to memory ... along with the anion gap calculation".
On the compensation table (s59): "not that you memorize this exact table, but have a sense for how things change
acutely versus chronically ... be able to use Winter's formula" -- so the table's ratios are GIVEN in any stem
that needs them; Winter's formula and the anion gap formula are not given.

NORMAL RANGES IN STEMS: every blood value carries its range (s5-s6 for the blood gas, s47 for the anion gap;
sodium, chloride and potassium ranges are standard laboratory ranges and are scaffolding, never a tested fact).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 17, "Acid - Base: Part I", letters dropped; d's
four sub-items joined in the syllabus's own order).

EXCLUDED_SLIDES (never cited): 1 title, 2 objectives, 64 "Case Studies" title, 65 external link, 66 "Part II
Coming Later", 67 references.

CONTESTED on the slides, so NEVER KEYED the contested way (the guide notes each):
  s8 "pH < 6.7 or > 7.6 is unsustainable" -- commonly quoted as below about 6.8 or above about 7.8. The slide's
      values are keyed; no option offers 6.8 or 7.8.
  s59 chronic respiratory acidosis "3.5 mEq/L per 10 mm Hg"; on the recording she rounded to 4 for the math.
      The slide's 3.5 is given in stems; no item turns on 3.5 versus 4.
  s43 files "exogenous alkali" under HYPERTENSIVE saline-unresponsive alkalosis; usually it is listed with the
      normotensive causes. Never keyed by blood pressure group.
  s41 urine chloride cutoffs (<25 and >40 mEq/L) are the deck's; keyed as written.
  Recording-only (never keyed): which mudpiles cause is most common (DKA, lactic acidosis, uremia), diarrhea as
      the most common normal-gap cause, box breathing, the "oblicap" placebo, ceviche, Godzilla.
"""

DECK = "PAJ5500 CMSI Acid Base MBF 2026sc.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = "Describe the major buffer systems of the body."
IO_B = "Explain how acid-base disorders affect electrolytes and oxygenation."
IO_C = "Identify mechanisms for maintaining acid-base homeostasis."
IO_D = ("Identify the etiologies, clinical manifestations, and management of simple acid-base disorders, "
        "including: a. Respiratory acidosis b. Respiratory alkalosis c. Metabolic acidosis d. Metabolic alkalosis")
IO_E = "Identify compensatory mechanisms for simple acid-base disorders."
IO_F = ("Identify simple acid-base disorders by interpreting diagnostic test results and patient "
        "presentations")
IOS = [IO_A, IO_B, IO_C, IO_D, IO_E, IO_F]

EXCLUDED_SLIDES = {1, 2, 64, 65, 66, 67}

# Normal ranges carried by every stem that shows the value.
PH = "(normal 7.35 to 7.45)"
PCO2 = "(normal 36 to 44 mm Hg)"
HCO3 = "(normal 22 to 26 mEq/L)"
PO2 = "(normal 80 to 100 mm Hg)"
AG = "(normal 9 to 15)"
NA = "(normal 135 to 145 mEq/L)"
CL = "(normal 98 to 106 mEq/L)"
K = "(normal 3.5 to 5.0 mEq/L)"


def gas(ph, pco2, hco3):
    """The standard blood gas phrase with every range."""
    return ("pH %s %s, partial pressure of carbon dioxide %s mm Hg %s, bicarbonate %s mEq/L %s"
            % (ph, PH, pco2, PCO2, hco3, HCO3))


SCOPE_BANNED = [
    r"delta[- ]delta|osmolar gap|albumin[- ]corrected|corrected anion gap",
    r"\b6\.8\b|\b7\.8\b",
    r"box breathing|ceviche|oblicap",
    r"most common (?:cause|reason)[^?.;]{0,60}(?:anion gap|ketoacidosis|lactic|uremia|diarrhea)",
]

REQUIRED = [
    # (label, stem regex, key regex, minimum per form) -- the two formulas she said to commit to memory
    ("Winter formula", r"Winter", r".", 2),
    ("anion gap calculation", r"calculated anion gap|anion gap (?:is|for this|from these)|what is (?:her|his|the) anion gap", r".", 1),
]

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "kussmaul": "deep",
    "asterixis": "flapping",
    "myoclonus": "jerk",
    "papilledema": "optic",
    "tetany": "spasm",
    "flail chest": "segment",
    "paresthesia": "tingling",
}
