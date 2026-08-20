#!/usr/bin/env python3
"""Partition CMS I Lecture 7 Set 1 (Benign Skin Lesions) into two 30s.

CMS format per [[cms_exam_spec]]: FOUR exams per topic -- Set 1 is 2 x 30 on the
instructional objectives, Set 2 is a separate 2 x 30 of vignettes. This builds
Set 1 only.

Objectives come from the SYLLABUS, not the slides, per the verbatim-IO rule.

LENGTH BIAS, and what actually worked. Raw rates by pool: A 23%, B 47%, C 41%,
D 53%, E 34%. Every one of those is the compare-and-contrast shape -- this deck
runs seventeen lesions past each other, so the correct answer is a compound
description and the natural distractor names a different lesion in fewer words.
Pools A to C were repaired by PADDING DISTRACTORS, which took 42 edits on pool B
alone. Pools D and E were repaired by TRIMMING THE CORRECT ANSWER instead and
moving the detail into its own explanation, which the student reads after
answering: 18 single edits took pool D from 53% to 0%. Trimming is roughly a
third of the work for the same result, and it is the direction to reach for
first. All five pools finish at 0%.

SLIDES 9, 24, 33, 34 AND 42 ARE IMAGES. The pressure injury staging system, the
keloid-versus-hypertrophic-scar comparison table, the sinus-versus-fistula
distinction and the keratolytic table exist nowhere in this deck's text --
slides 24, 33, 34 and 42 extract as bare titles or as "(no text)". They were read at
full size and are asked from here. See [[image-only-slides]].

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_l7_pool_a import POOL_A
from cms_l7_pool_b import POOL_B
from cms_l7_pool_c import POOL_C
from cms_l7_pool_d import POOL_D
from cms_l7_pool_e import POOL_E

POOL = POOL_A + POOL_B + POOL_C + POOL_D + POOL_E

# CMS scope guard: Set 1 is objective-style, NOT vignettes. A stem that opens
# with a patient age and presentation belongs in Set 2, and mixing them would
# make the two sets indistinguishable.
import re as _re
_VIG = _re.compile(r"^A[n]? \d+[- ]year[- ]old|^A \d+[- ]month[- ]old", _re.I)
_v = [q["q"] for q in POOL if _VIG.search(q["q"])]
assert not _v, "vignette-style stem in the Set 1 pool: %r" % _v[:2]

# every question carries an explicit fact slot
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
    missing_io = len(ALL_IOS - set(ios))
    missing_topic = len(ALL_TOPICS - set(tops))
    lumpy = sum(max(0, n - 5) for n in ios.values())
    lumpy_t = sum(max(0, n - 4) for n in tops.values())
    slots = Counter(q["slot"] for q in setqs)
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
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print("scope guard: no vignette stems in Set 1; every question carries a slot")
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
        print("   objectives: %d of %d   topics: %d of %d   slots: %d"
              % (len(ios), len(ALL_IOS), len(set(q["topic"] for q in s)), len(ALL_TOPICS),
                 len(set(q["slot"] for q in s))))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "cms_l7_set1.json"), "w"), ensure_ascii=False, indent=1)
    print("wrote cms_l7_set1.json")
