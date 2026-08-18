#!/usr/bin/env python3
"""Partition the Physical Diagnosis 2 Lecture 2 (Dermatology) pool into two 30s.

Four things are optimised at once, which is why the pool is written oversized at
114 questions:
  - instructional-objective coverage across both sets
  - TOPIC spread, which matters more here than in most decks: the lecture runs
    from skin anatomy through history, technique, the descriptive vocabulary and
    then the abnormal findings, and a set that lands entirely on morphology
    would cover every objective while still being a bad exam
  - length bias (picking the longest option must not beat guessing)
  - answer position, handled by ROTATION rather than by selection

Every question is authored with its correct answer first, because choosing the
index by hand while writing is exactly how the "always A" bug was introduced.
Each option is a [text, explanation] pair, so rotating the list carries each
explanation with its own choice.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pd2_l2_pool_a import POOL_A
from pd2_l2_pool_b import POOL_B
from pd2_l2_pool_c import POOL_C

POOL = POOL_A + POOL_B + POOL_C

# length-bias remediation first, as a separate reviewable pass whose
# "never touch the correct option" assertion runs every time
import difflib
from pd2_l2_lengthfix import FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    _q["opts"][_oi][0] = _text

# Jaxon's rule for this course, asserted rather than trusted: no question may
# depend on having the deck open, and none may test course mechanics.
import re as _re
_CTX = _re.compile(r"according to the (powerpoint|slide|lecture)|in the (powerpoint|slide|example)|"
                   r"the sample (note|case)|as shown (on|in) the|pictured (above|below)|this image", _re.I)
assert not [q for q in POOL if _CTX.search(q["q"])], "question depends on having the deck open"
_MECH = _re.compile(r"percent of the (course|grade)|sequester|file nam|late assignment|dress code|"
                    r"how long does .* run|what may a student bring", _re.I)
assert not [q for q in POOL if _MECH.search(q["q"])], "course-mechanics question in the pool"

random.seed(20260818)

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
    """Lower is better. Position is not scored -- rotation guarantees it."""
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    missing_topic = len(ALL_TOPICS - set(tops))
    lumpy_io = sum(max(0, n - 10) for n in ios.values())
    lumpy_topic = sum(max(0, n - 6) for n in tops.values())
    return (missing_io * 30 + missing_topic * 12
            + lumpy_io * 3 + lumpy_topic * 3 + gameable_pct(setqs) * 1.2)


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
    print("objectives:", len(ALL_IOS), " topics:", len(ALL_TOPICS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
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
        tops = Counter(q["topic"] for q in s)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives: %d of %d" % (len(ios), len(ALL_IOS)))
        print("   topics: %d of %d  %s" % (len(tops), len(ALL_TOPICS), dict(tops)))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "pd2_l2_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote pd2_l2_sets.json")
