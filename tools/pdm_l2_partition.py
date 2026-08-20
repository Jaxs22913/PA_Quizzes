#!/usr/bin/env python3
"""Partition the Principles of Diagnostic Medicine I Lecture 2 pool into two 30s.

POOL D COVERS IMAGE-ONLY CONTENT. Slides 13 and 21 carry tables that exist only
as pictures -- the Hounsfield numbers and the typical organ radiation doses --
and the text extraction reported slide 21 as entirely EMPTY. They were found by
looking at all 56 of the deck's images while choosing the guide's figures, after
pools A to C had already been written from text alone.

House format for this class is 2x30 per topic plus 5x60 masters per exam.
Masters wait until the whole Exam 1 block is in -- Exam 1 covers Lectures 1-6
and Lab 1, and only Lectures 1 and 2 exist so far.

PROFESSOR REYNOLDS' RULES, asserted rather than trusted. Both carry over from
the 2026-08-18 Lecture 1 recording; there was no audio for Lecture 2 when this
was built, so nothing here is weighted by spoken emphasis, only by what the deck
spends slides on.

  1. "I'm not going to just throw a random number at you and not give you
     context of whether that's high or low." -> A Hounsfield number, a Tesla
     rating or a millisievert figure may not appear without the scale that makes
     it readable.
  2. "We're not gonna do math, I'm not gonna make you do math." -> No question
     asks the student to calculate anything.

THE SLIDE 34 RULE is specific to this deck. "Anatomical Structures Best
Visualized by..." extracts as seventeen modality entries against six anatomical
categories in two columns, and the pairing cannot be reconstructed from the text
with confidence. Objective c is covered from slides that state a structure-to-
modality claim in a sentence instead. Asserted: nothing cites slide 34.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l2_pool_a import POOL_A
from pdm_l2_pool_b import POOL_B
from pdm_l2_pool_c import POOL_C
from pdm_l2_pool_d import POOL_D
from pdm_l2_pool_e import POOL_E
from pdm_l2_lengthfix import FIXES

# D is APPENDED, never prepended: the length-fix keys are indices into A + B + C
# and prepending would silently retarget every one of them.
POOL = POOL_A + POOL_B + POOL_C + POOL_D + POOL_E

for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Rule 1: a number never appears without the scale that reads it ---------
# Hounsfield numbers, field strength and dose are the three that occur here.
_VALUE = re.compile(r"(?<![\w-])[-+]?\d+(?:\.\d+)?\s*"
                    r"(hounsfield|hu\b|tesla\b|mSv\b|mGy\b|millisievert|milligray)", re.I)
_SCALE = re.compile(r"minus one thousand|-1000|\+1000|from .{0,24}to |range|scale|"
                    r"assigned .{0,20}zero|water is", re.I)
_offenders = [q["q"] for q in POOL
              if _VALUE.search(q["q"]) and not _SCALE.search(q["q"])]
assert not _offenders, ("a number without the scale that makes it readable -- Reynolds "
                        "supplies context on every exam: %r" % _offenders[:2])

# ---- Rule 2: no arithmetic --------------------------------------------------
# \b on "compute" matters: without it, every "computed tomography" question
# in the deck reads as a calculation and the guard fires on 20 of them.
_MATH = re.compile(r"\bcalculate\b|\bcompute\b|\bworking out\b|"
                   r"how many .* would|what is the (sum|product|difference)", re.I)
_math_q = [q["q"] for q in POOL if _MATH.search(q["q"])]
assert not _math_q, "calculation question -- she said she will not make them do math: %r" % _math_q[:2]

# ---- Rule 3: slide 34's table is unreconstructable, so nothing may cite it ---
_s34 = [q["q"] for q in POOL if q["cite"].strip().endswith("Slide 34")]
assert not _s34, ("cites slide 34, whose two-column modality table does not survive "
                  "text extraction: %r" % _s34[:2])

# ---- every question carries an explicit fact slot ---------------------------
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260820)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (top_len, top_i), (runner, _) = lens[0], lens[1]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_IOS = set(q["io"] for q in POOL)
ALL_TOPICS = set(q["topic"] for q in POOL)


def score(setqs):
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    missing_topic = len(ALL_TOPICS - set(tops))
    lumpy = sum(max(0, n - 6) for n in ios.values())
    lumpy_t = sum(max(0, n - 5) for n in tops.values())
    lumpy_s = sum(max(0, n - 8) for n in slots.values())
    return (missing_io * 30 + missing_topic * 8 + lumpy * 3 + lumpy_t * 2
            + lumpy_s * 2 + gameable_pct(setqs) * 1.2)


def rotate_for_balance(qs):
    targets = [i % 4 for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
        q["c"] = t
    return qs


def validate(pool):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != 4: bad.append((i, "not 4 options"))
        if not (0 <= q["c"] <= 3): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != 4: bad.append((i, "duplicate option text"))
        for o in q["opts"]:
            if not o[1].strip(): bad.append((i, "option missing explanation"))
    return bad


if __name__ == "__main__":
    print("pool size:", len(POOL))
    print("schema problems:", validate(POOL) or "none")
    print("objectives:", len(ALL_IOS), " topics:", len(ALL_TOPICS),
          " slots:", len(set(q["slot"] for q in POOL)))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("Reynolds rule checks: number-context OK, no-math OK, slide 34 unused OK")
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best, idx = None, list(range(len(POOL)))
    for _ in range(30000):
        random.shuffle(idx)
        chosen = idx[:60]
        s1 = [POOL[i] for i in chosen[:30]]
        s2 = [POOL[i] for i in chosen[30:]]
        total = score(s1) + score(s2)
        if best is None or total < best[0]:
            best = (total, list(chosen))

    chosen = best[1]
    s1 = rotate_for_balance([POOL[i] for i in chosen[:30]])
    s2 = rotate_for_balance([POOL[i] for i in chosen[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        ios = Counter(q["io"] for q in s)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.1f%%" % gameable_pct(s))
        print("   objectives: %d of %d   topics: %d of %d   slots: %d"
              % (len(ios), len(ALL_IOS), len(set(q["topic"] for q in s)), len(ALL_TOPICS),
                 len(set(q["slot"] for q in s))))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "pdm_l2_sets.json"), "w"), ensure_ascii=False, indent=1)
    print("wrote pdm_l2_sets.json")
