# -*- coding: utf-8 -*-
# PDM I Lecture 19 (Acid-Base Balance and Blood Gas Interpretation, Professor Finck) -- pool A.
# Objectives a (compare the laboratory studies: what the arterial blood gas order holds and what each
# value means: the carbon dioxide and oxygen pressures, pH, saturation, oxygen content, the
# dissociation curve, base excess, carboxyhemoglobin), b (arterial against venous: why arterial,
# the sample, its handling, the venous values) and c (indications for arterial blood gas testing).
# Pool B carries d (interpreting results), e (the four disorders' expected findings, potassium),
# f (calculating the anion gap) and g (an abnormal anion gap).
#
# LECTURER: Megan B. Finck, MMS, PA-C (title slide 1 and the 27 October recording, two segments,
# 90 minutes). The calendar and the syllabus both number it Lecture / Topic Outline 19. Exam 4's
# course director is Professor Reynolds; her rules hold.
#
# REYNOLDS' RULES, asserted in the partition: vignette and next-best-test style leaning to the tests;
# EVERY value in a stem carries its normal range "(normal ...)" (slide 54's table; venous values
# from slides 11, 14 and 18; the anion gap's 9 to 15 from slide 46; base excess plus or minus 2 from
# slide 41). Nothing calculated EXCEPT the anion gap: objective f is "Calculate the anion gap", and
# the lecturer said so aloud (1:18:52-1:19:23: "I do want you to memorize and understand this
# equation ... if I were to give you a list of lab values and ask you to calculate the anion gap");
# so an anion-gap item gives the sodium, chloride and bicarbonate with their ranges and asks for the
# gap (numeric options, ascending). The albumin correction is NOT calculated ("just know that it
# needs to be corrected if it's abnormal", 1:22:14). Winter's formula, the delta-delta and the
# osmolar gap are not in the deck and are never asked. Compensation is asked by DIRECTION only
# (slides 28, 50-53), never by an expected value.
#
# SLIDES ONLY. Every fact is on a visible slide (text or picture); speaker notes do not count (slide 9's
# asterisks are explained only in the notes, so "which electrolytes come from the metabolic panel" is
# not asked). The recording re-weights which items are selected and never adds a fact.
#
# NOT ASKED, by the lecturer's word or by the deck's own conflict:
#   - The saturation thresholds (slide 36: below 90% worrisome, below 75% critical): "I'm not going to
#     ask you ... my patient has an O2 saturation of 92%. Is this worrisome, or is this critical?"
#     (1:01:57-1:02:06).
#   - Memorized normal values: she named the first five rows of slide 54 to know by heart (1:28:28),
#     but "you're gonna have reference ranges when you're presented with clinical cases" and the course
#     rule supplies every range, so no item asks for a reference value.
#   - The arterial oxygen pressure's normal: slide 14 says greater than 88 mm Hg, slides 23 and 54 say
#     greater than 80 (both said aloud, 24:54 and 40:26). Stems give "(normal greater than 80 mm Hg)",
#     slide 54's table, and use values clear of 80 to 88.
#   - Anemia and polycythemia as causes of a low or high oxygen PRESSURE (slides 15 and 24): physiology
#     puts them on the oxygen CONTENT, so no item keys or refutes with them; the guide notes it.
#
# ABBREVIATIONS. None in options. In a stem or explanation an abbreviation appears only as
# ABBREV (full term), every time (the partition asserts it); values are written in words ("partial
# pressure of carbon dioxide"), never PaCO2.
#
# Correct answer is ALWAYS written first (c=0); the partition rotates (numeric option sets are sorted
# ascending instead and keep the key where its value falls).
SRC = "Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx"
IMG = "pdm-exam-4-quiz-images/"
def c(n): return f"{SRC}, Slide {n}" if isinstance(n, int) else f"{SRC}, {n}"   # "Slides 20 and 21": first = primary

IOA = "Compare and contrast laboratory studies used to diagnose acid-base disorders."
IOB = "Explain differences between arterial and venous blood gas measurements."
IOC = "Discuss indications for arterial blood gas testing."
IOD = "Interpret arterial blood gas results."
IOE = "Describe expected findings in: Metabolic acidosis, Metabolic alkalosis, Respiratory acidosis, Respiratory alkalosis."
IOF = "Calculate the anion gap."
IOG = "Discuss the clinical significance of an abnormal anion gap."

# The normal ranges every stem carries (slide 54 unless named).
PH = "(normal 7.35 to 7.45)"
PCO2 = "(normal 35 to 45 mm Hg)"
PO2 = "(normal greater than 80 mm Hg)"
HCO3 = "(normal 22 to 26 mEq/L)"
SAT = "(normal greater than 94%)"
NA = "(normal 135 to 148 mEq/L)"
CL = "(normal 98 to 106 mEq/L)"
K = "(normal 3.6 to 5.2 mEq/L)"
AG = "(normal 9 to 15)"                                   # slide 46
COHB = "(normal less than 2%)"
BE = "(normal plus or minus 2 mEq/L)"                     # slide 41


def Q(topic, io, slot, q, key, dists, cite, img=None, alt=None, slide=None, mis=None):
    """key/dists are (text, explanation)."""
    r = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": [list(key)] + [list(d) for d in dists], "c": 0,
         "cite": c(cite)}
    if img:
        r["img"] = IMG + img
        r["alt"] = alt
        r["slide"] = "Slide %d" % (slide or cite)
    if mis:
        r["mis"] = mis
    return r


POOL_A = [
]
