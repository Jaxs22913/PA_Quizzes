#!/usr/bin/env python3
"""Select the Physical Diagnosis 2 Lecture 1 quiz: ONE set of fifteen.

Not the house two-by-thirty. The lecture is largely course orientation, and with
that excluded there are about eighteen genuinely clinical questions in the
source. Fifteen selected from eighteen is what the material honestly supports.

Same machinery as the other partitions: length-bias remediation first, then
selection against objective coverage, then rotation to spread the answer
position. Every question is authored with its correct answer first, because
choosing the index by hand while writing is how the "always A" bug happened.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pd2_l1_pool_a import POOL_A as POOL

import difflib
from pd2_l1_lengthfix import FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    _q["opts"][_oi][0] = _text

# Jaxon's two rules for this lecture, asserted rather than trusted.
import re as _re
_CTX = _re.compile(r"according to the (powerpoint|slide|lecture)|in the (powerpoint|slide|example)|"
                   r"the sample (note|case)|as shown (on|in) the", _re.I)
assert not [q for q in POOL if _CTX.search(q["q"])], "question depends on having the deck open"
_MECH = _re.compile(r"percent of the (course|grade)|sequester|file nam|late assignment|dress code|"
                    r"how long does .* run|what may a student bring", _re.I)
assert not [q for q in POOL if _MECH.search(q["q"])], "course-mechanics question in the pool"

random.seed(20260818)
SET_SIZE = 15
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


def score(qs):
    ios = Counter(q["io"] for q in qs)
    missing = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 6) for n in ios.values())
    return missing * 25 + lumpy * 3 + gameable_pct(qs) * 1.2


def rotate_for_balance(qs):
    targets = [i % 4 for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        if k:
            q["opts"] = q["opts"][-k:] + q["opts"][:-k]
        q["c"] = t
    return qs


if __name__ == "__main__":
    print("pool size:", len(POOL))
    print("objectives:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    bad = [i for i, q in enumerate(POOL)
           if len(q["opts"]) != 4 or len(set(o[0] for o in q["opts"])) != 4 or not q.get("cite")]
    print("schema problems:", bad or "none")
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best, idx = None, list(range(len(POOL)))
    for _ in range(20000):
        random.shuffle(idx)
        chosen = [POOL[i] for i in idx[:SET_SIZE]]
        s = score(chosen)
        if best is None or s < best[0]:
            best = (s, list(idx[:SET_SIZE]))

    qs = rotate_for_balance([POOL[i] for i in best[1]])
    for q in qs:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    pos = Counter(q["c"] for q in qs)
    ios = Counter(q["io"] for q in qs)
    print("SET  n=%d" % len(qs))
    print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
    print("   length-gameable: %.0f%%" % gameable_pct(qs))
    print("   objectives: %d of %d" % (len(ios), len(ALL_IOS)))
    json.dump({"set1": qs}, open(os.path.join(HERE, "pd2_l1_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote pd2_l1_sets.json")
