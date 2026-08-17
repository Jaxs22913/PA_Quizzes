#!/usr/bin/env python3
"""Partition the Pharmacology I Lecture 1 antibacterial pool into two 30s.

Three things are optimised at once, which is why the pool is written oversized:
  - instructional-objective coverage across both sets
  - length bias (picking the longest option must not beat guessing)
  - answer position, handled by ROTATION rather than by selection

The rotation is the part worth understanding. Every question in the pool is
authored with its correct answer first, because choosing the index by hand while
writing is exactly how the "always A" bug was introduced across 960 questions.
Each option is a [text, explanation] pair, so rotating the list carries each
explanation with its own choice -- the content is untouched and only the letter
changes. Rotation also cannot alter which option is longest, so it is safely
orthogonal to the length-bias work.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_l1_abx_pool_a import POOL_A
from pharm_l1_abx_pool_b import POOL_B
from pharm_l1_abx_pool_c import POOL_C

POOL = POOL_A + POOL_B + POOL_C

# length-bias remediation first, as a separate reviewable pass whose
# "never touch the correct option" assertion runs every time
import difflib
from pharm_l1_abx_lengthfix import FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    _q["opts"][_oi][0] = _text

# Dr. Wood told the class there is no need to memorise or know drug dosages
# (Jaxon, 2026-08-17). These four turn on a milligram figure or a regimen and
# are excluded from selection. Keyed on question text rather than index so the
# exclusion survives any edit to the pools.
#
# Two dose-adjacent questions are deliberately KEPT: when to draw a vancomycin
# trough, because syllabus objective 4 explicitly names "any needed laboratory
# monitoring"; and why aminoglycoside dosing moved to every 24 hours, whose
# answer is the post-antibiotic effect and concentration-dependent killing --
# the interval is only the setup for a mechanism question.
EXCLUDE_DOSAGE = [
    "What is the extended-infusion regimen given for piperacillin",
    "What is the ceftriaxone dose for meningitis",
    "Which carbapenem is dosed once daily",
    "What are the once-daily doses and trough targets for the aminoglycosides",
]
_before = len(POOL)
POOL = [q for q in POOL if not any(q["q"].startswith(p) for p in EXCLUDE_DOSAGE)]
assert len(POOL) == _before - len(EXCLUDE_DOSAGE), \
    "dosage exclusion matched %d, expected %d" % (_before - len(POOL), len(EXCLUDE_DOSAGE))

random.seed(20260817)

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


def score(setqs):
    """Lower is better. Position is not scored -- rotation guarantees it."""
    ios = Counter(q["io"] for q in setqs)
    missing = len(ALL_IOS - set(ios))
    # a set that piles six questions onto one objective is worse than one that
    # spreads them, even when both cover everything
    lumpy = sum(max(0, n - 4) for n in ios.values())
    return missing * 25 + lumpy * 3 + gameable_pct(setqs) * 1.2


def rotate_for_balance(qs):
    """Give each question a target answer position, evenly spread, then rotate."""
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
    print("objectives:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print()

    # the correct TEXT of each question, captured before rotation, so the
    # rotation can be proven not to have moved any answer onto a wrong option
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
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives: %d of %d" % (len(ios), len(ALL_IOS)))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "pharm_l1_abx_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote pharm_l1_abx_sets.json")
