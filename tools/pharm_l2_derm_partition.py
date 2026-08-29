#!/usr/bin/env python3
"""Partition the Pharmacology I Lecture 2 dermatology pool into two 30s.

Same machinery as pharm_l1_abx_partition.py: objective coverage and length bias
are optimised by selection, answer position is guaranteed by ROTATION rather
than by choosing an index while authoring (which is how the "always A" bug got
into 960 questions once already).

TWO RULES FROM THE COURSE ARE ENFORCED HERE RATHER THAN TRUSTED TO THE AUTHOR:

  Dr. Wood: no dosages. assert_no_dose_answers() fails the build if any correct
  answer is essentially a number -- a milligram figure, a percentage strength or
  a frequency standing alone. Potency CLASS and "start low and titrate" are
  technique and pass, which is the same line drawn for Lecture 1.

  Dr. McInnis, 2026-08-28: students over-invest in mechanism, so study the drug
  comprehensively -- indications, patient education, side effects and
  contraindications. assert_mcinnis_weighting() fails the build if mechanism
  questions outnumber those four combined, in the pool or in either set.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_l2_derm_pool_a import POOL_A
from pharm_l2_derm_pool_b import POOL_B

POOL = POOL_A + POOL_B

# length-bias remediation first, as a separate reviewable pass whose "never
# touch the correct option" assertion runs on every build
import difflib
from pharm_l2_derm_lengthfix import FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    assert _oi != _q["c"], "fix %d would overwrite the correct answer" % _idx
    _q["opts"][_oi][0] = _text

random.seed(20260829)

MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
MECH_IO = "2"                       # the mechanism objective
MCINNIS_IOS = ("3", "5", "6", "7", "10")   # indications, side effects, adverse, contra, education


def io_num(q):
    return q["io"].split("—")[0].strip()


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (top_len, top_i), (runner, _) = lens[0], lens[1]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def assert_no_dose_answers(pool):
    """Dr. Wood: the answer must never BE a number."""
    # a correct option that is mostly a figure -- "40 to 60 mg", "0.05% cream",
    # "twice daily for two weeks" standing alone
    bare = re.compile(r"^\W*\d[\d\s.,%-]*\s*(mg|g|mcg|units|%|per cent)?\W*$", re.I)
    bad = [q["q"][:70] for q in pool if bare.match(q["opts"][q["c"]][0])]
    assert not bad, "a correct answer is a bare dose/strength: %r" % bad
    return len(pool)


def assert_mcinnis_weighting(qs, label):
    mech = sum(1 for q in qs if io_num(q) == MECH_IO)
    four = sum(1 for q in qs if io_num(q) in MCINNIS_IOS)
    assert four > mech, (
        "%s is built the way Dr. McInnis told the class NOT to study: "
        "mechanism %d vs indications/education/side effects/contraindications %d"
        % (label, mech, four))
    return mech, four


ALL_IOS = set(q["io"] for q in POOL)


def score(setqs):
    """Lower is better. Position is not scored -- rotation guarantees it."""
    ios = Counter(q["io"] for q in setqs)
    missing = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 5) for n in ios.values())
    mech = sum(1 for q in setqs if io_num(q) == MECH_IO)
    four = sum(1 for q in setqs if io_num(q) in MCINNIS_IOS)
    # push each set toward her weighting, not just the pool as a whole
    skew = max(0, mech * 2 - four)
    return missing * 25 + lumpy * 3 + gameable_pct(setqs) * 1.2 + skew * 4


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
    print("objectives covered:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    assert_no_dose_answers(POOL)
    print("Wood dosage rule: no correct answer is a bare dose or strength")
    m, f = assert_mcinnis_weighting(POOL, "the pool")
    print("McInnis weighting (pool): mechanism %d vs her four %d" % (m, f))
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    best, idx = None, list(range(len(POOL)))
    for _ in range(40000):
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
        m, f = assert_mcinnis_weighting(s, name)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives: %d of %d" % (len(ios), len(ALL_IOS)))
        print("   mechanism %d vs indications/education/side effects/contra %d" % (m, f))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "pharm_l2_derm_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote pharm_l2_derm_sets.json")
