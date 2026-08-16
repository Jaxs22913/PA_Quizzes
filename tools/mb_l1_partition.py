#!/usr/bin/env python3
"""Partition the CMS Lecture 1 pool into two 30-question sets.

Optimises three things at once, which is why the pool is written oversized:
  - answer position balance (each of A-D near 25%)
  - instructional-objective coverage in BOTH sets
  - length bias (picking the longest option must not beat guessing)
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mb_l1_pool_a import POOL_A
from mb_l1_pool_b import POOL_B
from mb_l1_pool_c import POOL_C

POOL = POOL_A + POOL_B + POOL_C

# Apply the length-bias remediation before selecting. Written as a separate
# pass so the fixes are reviewable on their own, and so the applier's
# "never touch the correct option" assertion runs every time.
import difflib
from mb_l1_lengthfix import FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    # correct option excluded from candidates by construction -- a rewrite
    # cannot land on the answer regardless of how the similarity falls
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    _q["opts"][_oi][0] = _text

random.seed(20260816)   # deterministic: same pool -> same sets


def validate(pool):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != 4:
            bad.append((i, "not 4 options"))
        if not (0 <= q["c"] <= 3):
            bad.append((i, "answer index out of range"))
        if not q.get("cite"):
            bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != 4:
            bad.append((i, "duplicate option text"))
        for o in q["opts"]:
            if not o[1].strip():
                bad.append((i, "option missing explanation"))
    return bad


# Same definition tools/check_length_bias.py uses: longest by a MEANINGFUL
# margin -- at least MARGIN_CHARS longer AND MARGIN_FRAC longer than the
# runner-up. A two-character difference nobody eyeballs is not a tell.
MARGIN_CHARS = 8
MARGIN_FRAC = 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    top_len, top_i = lens[0]
    runner = lens[1][0]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    """Share of questions where picking the longest option reliably wins."""
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def score(setqs):
    """Lower is better."""
    pos = Counter(q["c"] for q in setqs)
    ideal = len(setqs) / 4.0
    pos_err = sum(abs(pos.get(i, 0) - ideal) for i in range(4))
    ios = Counter(q["io"] for q in setqs)
    missing = len(ALL_IOS - set(ios))
    # no free allowance on length bias -- every gameable question costs
    return pos_err * 2 + missing * 25 + gameable_pct(setqs) * 1.2


ALL_IOS = set(q["io"] for q in POOL)

if __name__ == "__main__":
    bad = validate(POOL)
    print("pool size:", len(POOL))
    print("schema problems:", bad if bad else "none")
    print("objectives:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print()

    # greedy + random restarts: pick 60 of the pool split into two 30s
    best = None
    idx = list(range(len(POOL)))
    for _ in range(30000):
        random.shuffle(idx)
        chosen = idx[:60]
        s1 = [POOL[i] for i in chosen[:30]]
        s2 = [POOL[i] for i in chosen[30:]]
        total = score(s1) + score(s2)
        if best is None or total < best[0]:
            best = (total, list(chosen))

    chosen = best[1]
    s1 = [POOL[i] for i in chosen[:30]]
    s2 = [POOL[i] for i in chosen[30:]]

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" %
              tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives covered: %d of %d" % (len(set(q["io"] for q in s)), len(ALL_IOS)))
        for io, n in sorted(Counter(q["io"] for q in s).items()):
            print("      %-58s %d" % (io[:58], n))
        print()

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "mb_l1_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote mb_l1_sets.json")
