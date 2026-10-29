# -*- coding: utf-8 -*-
"""Lecture 33 scope -- Oxygen Delivery (Reynolds), CMS I Exam 6 (Respiratory Block Exam I).

Read by cms_e6_partition.py (guards) and imported by every Lecture 33 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Lauren Reynolds, MSPA, PA-C -- title slide 1, and the 2026-10-27 recording (Notability, one clip,
46.1 min, 11:04): she says "tomorrow I'm gonna lecture on COPD", which is Lecture 36 by Professor Reynolds on
the calendar. Agrees with calendar-data.js ("CMS I - LECTURE #33- Oxygen Delivery - Professor Reynolds").

NUMBERING: the deck file is "35. Oxygen Delivery 2026.pptx", the calendar calls it Lecture #33. The syllabus
topic outline is unnumbered (PULMONOLOGY: Oxygen Delivery, Acid-Base: Part I, Asthma, COPD ...), so the
calendar's 33 is used everywhere; the deck's "35." is the file name only.

Built from the DECK; the recording only sets emphasis (slides-only grounding). Speaker notes never count:
s2's notes, s6's color key, s11's note, s19's "similar settings to a venturi mask" are not used.
Picture slides read from the images: s6 is a TABLE PICTURE (the Medicare home oxygen criteria: Group I and
Group II, sleep, exertion, recertification 12 vs 3 months, hematocrit over 56%); s7's picture lists the home
oxygen safety rules (no smoking in the home; at least 10 feet from heat sources -- pilot lights, electric
appliances, candles; avoid petroleum-based products -- lip balms, lotions, oils, grease; working smoke and
carbon monoxide alarms, tested monthly); s21's picture shows oral airway sizes; s10, s12, s14-16, s18-19,
s22-25 are device photographs.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 17, "Oxygen Delivery", letters dropped). The
deck's own objective slide (s2, SmartArt) words f as "Demonstrate the selection, application, and patient
education for oxygen delivery"; the syllabus wording is used.

EMPHASIS (Notability transcript; our Whisper transcription cross-checks it): indications and who qualifies
("one of the big things"), the hazards with FIRE "probably one of the biggest risks", patient education
(flammable, no smoking, signs that also warn firefighters, tanks are returned to the supplier, never thrown
away), the home oxygen qualification walk-through (rest, then exertion, document the room-air value, then
the lowest flow that corrects it), the MI caution, then the devices in order of acuity. Air hunger at end of
life and cluster headache were given as the two non-hypoxic indications.

EXCLUDED_SLIDES (never cited): 1 title, 2 objectives, 26 "Questions?", 27 references.

CONTESTED on the slides, so NEVER KEYED the contested way (the guide notes each):
  s9 prints the nasal cannula range as ".24% to .44%" -- the fractions .24 to .44 are 24% to 44% (its own
      per-liter list says 24% ... 44%). Keyed as 24% to 44%.
  Partial rebreather: s14 says 60-80%, the s20 table says .40-.70 (at least 10 L/min). Its fraction range
      is NEVER keyed; only that it lets some exhaled gas into the bag and is not commonly used.
  Air-entrainment nebulizer: s17 says .28-1.0 (not recommended above .50), s20 says .21-1.0. Only the
      "not recommended above 0.50" ceiling and "can deliver higher" are keyed, never the lower bound.
  Non-rebreather: s15 calls it a "low flow device, but with high FiO2"; s8 says its delivery varies with
      demand. Keyed as written (low flow device with a high fraction, 10-15 L/min = 60-100%).
  s3 "not given in MI unless O2 <91%": current guidance withholds routine oxygen above 90% (the recording:
      "unless they're bordering on hypoxia"). The slide's 91% is keyed; no option offers 90%.
  Recertification: on the recording she linked 3 months to "an acute problem" and 12 months to a chronic
      comorbidity; s5 and s6 say the CONDITIONAL group (Group II, with pulmonary hypertension, cor pulmonale
      or hematocrit over 56%) recertifies at 3 months and Group I at 12. The slides are keyed.
  Recording-only (not keyed): heart failure as a Group II comorbidity, high-flow nasal cannula to 10 L/min,
      CPAP/BiPAP when carbon dioxide rises, the 88-92% target in COPD, nasal prongs "down and back",
      continuous albuterol nebulizers, saline nebulizers in cystic fibrosis.
"""

DECK = "35. Oxygen Delivery 2026.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
Cs = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = "Identify the indications, benefits, and hazards of oxygen therapy."
IO_B = "Select the appropriate equipment and supplies necessary for initiating oxygen therapy."
IO_C = "Explain the rationale for a nebulizer treatment."
IO_D = "Compare and contrast the different oxygen delivery systems."
IO_E = "Evaluate the patient’s response to oxygen therapy."
IO_F = "Discuss the selection and application of oxygen delivery"
IO_G = "Discuss patient education for oxygen delivery"
IOS = [IO_A, IO_B, IO_C, IO_D, IO_E, IO_F, IO_G]

EXCLUDED_SLIDES = {1, 2, 26, 27}

SCOPE_BANNED = [
    r"\.2[48]\s?%|\.44\s?%",                  # s9's ".24% to .44%" notation
    r"\b(?:60|40)\s?(?:to|-|–)\s?(?:80|70)\s?%[^?.;]{0,40}partial|partial[^?.;]{0,60}\b(?:60|40)\s?(?:to|-|–)\s?(?:80|70)",
    r"\b0?\.2[18]\s?(?:to|-|–)\s?1\.0",  # air-entrainment lower bound
    r"high[- ]flow nasal cannula|\bBiPAP\b|\bCPAP\b|88 ?(?:to|-|–) ?92",
    r"\b90\s?%",                               # never offer 90% beside the slide's 91%
    r"heart failure[^?.;]{0,40}Group II|Group II[^?.;]{0,60}heart failure",
]

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "air hunger": "breath",
    "cor pulmonale": "right",
    "polycythemia": "hematocrit",
}
