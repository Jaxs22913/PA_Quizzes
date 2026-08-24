#!/usr/bin/env python3
"""Partition the PDM I Lecture 3 pool into two 30s.

House format for this class is 2x30 per topic plus 5x60 masters per exam.
MASTERS WAIT: Exam 1 covers Lectures 1-6 and Lab 1, and only Lectures 1-4 exist.

PROFESSOR REYNOLDS' RULES, asserted rather than trusted. Both carry over from her
2026-08-18 Lecture 1 recording:

  1. "I'm not going to just throw a random number at you and not give you context
     of whether that's high or low." -> A decibel level, a pressure, a millimetre
     measurement or a percentage may not appear without the scale that reads it.
  2. "We're not gonna do math, I'm not gonna make you do math." -> No question
     asks the student to calculate.

Note that rule 2 is SPECIFIC TO HER. The very next lecture in this course is
Shah's, whose objective (d) is literally "Calculate absolute white blood cell
counts" -- so the guard lives here, in Reynolds' partition, and NOT in the
shared machinery.

THIS IS THE STUDENT VERSION OF THE DECK. Slides 7, 21, 23, 28, 29, 30, 33 and 38
have had their licensed figures stripped and carry no picture at all. Where the
content survives in the slide's own text or notes it is quizzed and cited to the
notes; where it does not, it is not invented. Asserted: nothing cites a slide
whose content exists only in a picture that is not in the file.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l3_pool_a import POOL_A
from pdm_l3_pool_b import POOL_B
from pdm_l3_pool_c import POOL_C
from pdm_l3_pool_d import POOL_D
from pdm_l3_pool_e import POOL_E
from pdm_l3_lengthfix import FIXES

# D is APPENDED, never prepended: the length-fix keys are indices into A + B + C
# and prepending would silently retarget every one of them.
POOL = POOL_A + POOL_B + POOL_C + POOL_D + POOL_E

for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Rule 1: a number never appears without the scale that reads it ---------
# The units this deck actually uses: decibels, millimetres of mercury and of
# water, millimetres of tissue depth, and percentages.
_VALUE = re.compile(r"(?<![\w-])(?:\d+|one|two|three|five|ten|twenty|fifty|"
                    r"one hundred|two hundred)[- ](?:decibel|millimetre|per cent)", re.I)
_SCALE = re.compile(r"normal|range|threshold|upper limit|fail|gap|scale|"
                    r"greater than|less than|more than|up to|between|"
                    r"or more|or less|significant", re.I)
_offenders = [q["q"] for q in POOL
              if _VALUE.search(q["q"]) and not _SCALE.search(q["q"])]
assert not _offenders, ("a number without the scale that makes it readable -- Reynolds "
                        "supplies context on every exam: %r" % _offenders[:2])

# ---- Rule 2: no arithmetic --------------------------------------------------
# \b on "compute" matters: without it, every "computed tomography" question in
# the deck reads as a calculation, and this deck has dozens.
_MATH = re.compile(r"\bcalculate\b|\bcompute\b|\bworking out\b|"
                   r"how many .* would|what is the (sum|product|difference)", re.I)
_math_q = [q["q"] for q in POOL if _MATH.search(q["q"])]
assert not _math_q, "calculation question -- she said she will not make them do math: %r" % _math_q[:2]

# ---- Rule 3: the stripped figures -------------------------------------------
# These slides carry no picture in the student version. Citing one is only
# legitimate when the fact survives in the slide's own text or speaker notes,
# which is why the notes citations are written as "(speaker notes)". A bare
# citation to a picture-only slide would be a fact with no source.
_STRIPPED = {7, 21, 28, 30, 33}
_ghosts = [q["q"] for q in POOL
           if any(q["cite"].strip().endswith("Slide %d" % n) for n in _STRIPPED)]
assert not _ghosts, ("cites a slide whose content exists only in a figure that "
                     "is not in the student version: %r" % _ghosts[:2])

# ---- every question carries an explicit fact slot ---------------------------
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260824)
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
    print("Reynolds rule checks: number-context OK, no-math OK, stripped-figure slides not cited OK")
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
              open(os.path.join(HERE, "pdm_l3_sets.json"), "w"), ensure_ascii=False, indent=1)
    print("wrote pdm_l3_sets.json")
