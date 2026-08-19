#!/usr/bin/env python3
"""Partition CMS I Lecture 2 Set 1 (General Dermatology I) into two 30s.

CMS format per [[cms_exam_spec]]: FOUR exams per topic -- Set 1 is 2 x 30 on the
instructional objectives, Set 2 is a separate 2 x 30 of vignettes. This builds
Set 1 only.

Objectives come from the SYLLABUS, not the slides, per the verbatim-IO rule.

Length-bias remediation runs first as a reviewable pass whose "never touch the
correct option" assertion executes every time. It needed three rounds here: the
raw pool was 66% gameable, the highest on the site, because this lecture's
correct answers are enumerations while the natural distractor is a single
clause. The fix widened the distractors rather than truncating the answers.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_l2_pool_a import POOL_A
from cms_l2_pool_b import POOL_B
from cms_l2_pool_c import POOL_C
from cms_l2_pool_d import POOL_D

# Pool D is APPENDED, never prepended. The length-fix maps below are keyed by
# index into POOL_A + POOL_B + POOL_C, so anything inserted ahead of them would
# silently rewrite the wrong questions.
POOL = POOL_A + POOL_B + POOL_C + POOL_D

import difflib
from cms_l2_lengthfix import FIXES, SLOT_FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    _q["opts"][_oi][0] = _text
for (_qi, _oi2), _text in SLOT_FIXES.items():
    assert _oi2 != POOL[_qi]["c"], "slot fix %d would overwrite the correct option" % _qi
    POOL[_qi]["opts"][_oi2][0] = _text

# CMS scope guard: Set 1 is objective-style, NOT vignettes. A stem that opens
# with a patient age and presentation belongs in Set 2, and mixing them would
# make the two sets indistinguishable.
import re as _re
_VIG = _re.compile(r"^A[n]? \d+[- ]year[- ]old|^A \d+[- ]month[- ]old", _re.I)
_v = [q["q"] for q in POOL if _VIG.search(q["q"])]
assert not _v, "vignette-style stem in the Set 1 pool: %r" % _v[:2]

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
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    missing_topic = len(ALL_TOPICS - set(tops))
    lumpy = sum(max(0, n - 5) for n in ios.values())
    lumpy_t = sum(max(0, n - 5) for n in tops.values())
    return missing_io * 30 + missing_topic * 8 + lumpy * 3 + lumpy_t * 2 + gameable_pct(setqs) * 1.2


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
    print("objectives:", len(ALL_IOS), " topics:", len(ALL_TOPICS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print("scope guard: no vignette stems in Set 1")
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
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives: %d of %d   topics: %d of %d"
              % (len(ios), len(ALL_IOS), len(set(q["topic"] for q in s)), len(ALL_TOPICS)))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "cms_l2_set1.json"), "w"), ensure_ascii=False, indent=1)
    print("wrote cms_l2_set1.json")
