# -*- coding: utf-8 -*-
"""Data for the Cardiac OSCE Disease Chart (Physical Diagnosis 2).

Jaxon, 2026-10-17: "For PD cardiac Osce can you make a list (from the CMS
Cardio block 1 and 2) top 10 most common diagnoses, top 5 most non emergent,
top 5 most emergent and give everything like the ENT OSCE disease chart."

Twenty conditions, drawn only from the two Clinical Medicine and Surgery I
cardiology blocks (Exam 4, Lectures 20-25; Exam 5, Lectures 26-32). Each row
carries the ENT chart's columns in the station's own order. Rows are written in
four batch modules (_cardiac_osce_batch_*.py), merged here; the builder asserts
that every name in the three lists has exactly one row.
"""


def R(tier, source, why, says, findings, exam, ddx, rule_in, rule_out, tx, urgency, edu):
    """One condition.

    tier      "routine" | "urgent" | "emergent"  (decides which block it sits in)
    source    "CMS L24 Coronary Artery Disease &middot; slides 12, 30" plus any PD2 deck cite
    why       one line: why it is on its list (how common, or how dangerous)
    says      how the patient describes it, in their own words
    findings  what you see, feel and hear: inspection, palpation, auscultation, the vitals clue
    exam      the maneuvers that rule it in or out (not the findings)
    ddx       exactly three (name, what separates it from this row) tuples
    rule_in   tests that confirm it, each written  test &rarr; what a positive looks like
    rule_out  tests or findings that send you to one of the three differentials instead
    tx        treatment and referral; generic names, no doses
    urgency   one short line beginning ROUTINE, URGENT or EMERGENT
    edu       what you tell the patient
    """
    assert tier in ("routine", "urgent", "emergent"), tier
    assert len(ddx) == 3, "exactly three differentials"
    assert urgency.split()[0].rstrip(":&mdash;,").upper() in ("ROUTINE", "URGENT", "EMERGENT"), urgency
    return dict(tier=tier, source=source, why=why, says=says, findings=findings, exam=exam,
                ddx=ddx, rule_in=rule_in, rule_out=rule_out, tx=tx, urgency=urgency, edu=edu)


# The three lists, in Jaxon's order. A name may sit on more than one list only
# if it truly belongs there; it still gets one row.
TOP10 = [
    "Primary hypertension",
    "Chronic venous insufficiency and varicose veins",
    "Stable angina",
    "Peripheral artery disease",
    "Atrial fibrillation",
    "Chronic heart failure",
    "Premature ventricular contractions",
    "Vasovagal syncope",
    "Deep vein thrombosis",
    "Aortic stenosis",
]
NONEMERGENT5 = [
    "Acute pericarditis",
    "Mitral regurgitation",
    "Mitral valve prolapse",
    "Orthostatic hypotension",
    "Hypertrophic cardiomyopathy",
]
EMERGENT5 = [
    "Acute coronary syndrome",
    "Aortic dissection",
    "Cardiac tamponade",
    "Ventricular tachycardia",
    "Hypertensive emergency",
]


def _load():
    import importlib
    rows = {}
    for mod in ("a1", "a2", "b1", "b2"):
        try:
            m = importlib.import_module("_cardiac_osce_batch_" + mod)
        except ModuleNotFoundError:
            continue
        # A batch imported first is still half-built when it imports this
        # module back; it has no BATCH yet, so skip it rather than crash.
        batch = getattr(m, "BATCH", None)
        if batch is None:
            continue
        clash = set(batch) & set(rows)
        assert not clash, "condition written twice: %r" % clash
        rows.update(batch)
    return rows


ROWS = _load()
