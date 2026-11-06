# -*- coding: utf-8 -*-
"""Data for the Pulmonary OSCE Disease Chart (Physical Diagnosis 2).

Jaxon, 2026-11-06: a pulmonary version of the Cardiac OSCE Disease Chart for the
Pulmonary OSCE (Tuesday 10 November): the top 10 most common diagnoses, the top 5
non-emergent and the top 5 emergent, everything the cardiac chart has.

Twenty conditions, drawn only from the two Clinical Medicine and Surgery I
pulmonary blocks (Exam 6, Lectures 33-38; Exam 7, Lectures 39-44), with the
examination findings from the Physical Diagnosis 2 thorax lecture. The three
lists do not overlap. Each list runs roughly from the most common condition to
the least common, on the figures the slides give (or a standard figure where a
deck gives none). Rows are written in five batch modules
(_pulm_osce_batch_*.py), merged here; the builder asserts that every name in
the three lists has exactly one row.
"""


def R(tier, source, why, says, findings, exam, ddx, rule_in, rule_out, tx, urgency, edu):
    """One condition (the cardiac chart's schema).

    tier      "routine" | "urgent" | "emergent"  (decides which block it sits in)
    source    "CMS L37 Respiratory Infections (Bobilin) &middot; slides 15, 16 &middot; PD2 Thorax slides 40, 41"
    why       one line: why it is on its list (how common, or how dangerous)
    says      how the patient describes it, in their own words
    findings  what you see, feel and hear: inspection, palpation (fremitus, expansion),
              percussion, auscultation, transmitted voice sounds, the vitals clue
    exam      the maneuvers that rule it in or out (not the findings)
    ddx       exactly three (name, what separates it from this row) tuples
    rule_in   tests that confirm it, each written  test &rarr; what a positive looks like
    rule_out  tests or findings that send you to one of the three differentials instead
    tx        treatment and referral; drug names from the slides, no doses
    urgency   one short line beginning ROUTINE, URGENT or EMERGENT
    edu       what you tell the patient
    """
    assert tier in ("routine", "urgent", "emergent"), tier
    assert len(ddx) == 3, "exactly three differentials"
    assert urgency.split()[0].rstrip(":&mdash;,").upper() in ("ROUTINE", "URGENT", "EMERGENT"), urgency
    assert "&rarr;" in rule_in, "every test names its finding (test &rarr; positive)"
    return dict(tier=tier, source=source, why=why, says=says, findings=findings, exam=exam,
                ddx=ddx, rule_in=rule_in, rule_out=rule_out, tx=tx, urgency=urgency, edu=edu)


# The three lists, each roughly from the most common to the least common.
TOP10 = [
    "Obstructive sleep apnea",
    "Influenza",
    "Asthma",
    "Chronic obstructive pulmonary disease",
    "Acute bronchitis",
    "Pulmonary hypertension and cor pulmonale",
    "Pleural effusion",
    "Community-acquired pneumonia",
    "Lung cancer",
    "Idiopathic pulmonary fibrosis",
]
NONEMERGENT5 = [
    "Pleurisy",
    "Obesity hypoventilation syndrome",
    "Pulmonary tuberculosis",
    "Sarcoidosis",
    "Hypersensitivity pneumonitis",
]
EMERGENT5 = [
    "Acute cardiogenic pulmonary edema",
    "Pulmonary embolism",
    "Acute respiratory distress syndrome",
    "Pneumothorax",
    "Hemothorax",
]

BATCHES = ("1", "2", "3", "4", "5")


def _load(attr):
    import importlib
    out = {}
    for mod in BATCHES:
        try:
            m = importlib.import_module("_pulm_osce_batch_" + mod)
        except ModuleNotFoundError:
            continue
        # A batch imported first is still half-built when it imports this
        # module back; it has no BATCH yet, so skip it rather than crash.
        part = getattr(m, attr, None)
        if part is None:
            continue
        clash = set(part) & set(out)
        assert not clash, "condition written twice: %r" % clash
        out.update(part)
    return out


ROWS = _load("BATCH")
