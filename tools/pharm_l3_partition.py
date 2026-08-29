#!/usr/bin/env python3
"""Partition a Pharmacology I Lecture 3 pool into two 30s.

Parameterised over the lecture's two topics rather than duplicated, since the
ANS lecture is 124 slides and had to be split the way Lecture 1 was:

    python3 pharm_l3_partition.py chol    # ANS principles + cholinergic drugs
    python3 pharm_l3_partition.py adren   # adrenergic drugs

Same guarantees as the other pharmacology partitions: objective coverage and
length bias by selection, answer position by ROTATION, and the two course rules
enforced as assertions rather than trusted to the author -- Dr. Wood's no-dosage
rule, and Dr. McInnis's weighting (mechanism must not outweigh indications,
patient education, side effects and contraindications).
"""
import sys, os, json, random, re, difflib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

TOPIC = sys.argv[1] if len(sys.argv) > 1 else "chol"

if TOPIC == "chol":
    from pharm_l3_chol_pool import POOL as _A
    from pharm_l3_chol_pool_b import POOL_B as _B
    POOL, OUT_JSON = _A + _B, "pharm_l3_chol_sets.json"
    FIXES = {}
    # this pool's bias came from over-written ANSWERS, not thin distractors, so
    # it is fixed by trimming the answer back to the answer -- see the module
    from pharm_l3_chol_shortfix import SHORTEN, LENGTHEN
    for _i, _new in SHORTEN.items():
        _q = POOL[_i]
        assert len(_new) < len(_q["opts"][_q["c"]][0]), "shorten %d is not shorter" % _i
        _q["opts"][_q["c"]][0] = _new
    for _i, _map in LENGTHEN.items():
        _q = POOL[_i]
        for _j, _o in enumerate(_q["opts"]):
            if _j != _q["c"]:
                _o[0] = _map[_o[0]]
elif TOPIC == "adren":
    from pharm_l3_adren_pool import POOL as _A
    from pharm_l3_adren_pool_b import POOL_B as _B
    from pharm_l3_adren_pool_c import POOL_C as _C
    POOL, OUT_JSON = _A + _B + _C, "pharm_l3_adren_sets.json"
    FIXES = {}
    from pharm_l3_adren_shortfix import SHORTEN
    for _i, _new in SHORTEN.items():
        _q = POOL[_i]
        assert len(_new) < len(_q["opts"][_q["c"]][0]), "shorten %d is not shorter" % _i
        _q["opts"][_q["c"]][0] = _new
else:
    sys.exit("unknown topic %r -- use chol or adren" % TOPIC)

for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.20, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    assert _oi != _q["c"], "fix %d would overwrite the correct answer" % _idx
    _q["opts"][_oi][0] = _text

random.seed(20260829)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
MECH_IOS = ("2", "6")                    # transmission mechanism and transmitter fate
MCINNIS_IOS = ("4", "7", "8", "9", "10")  # predicted effects, and the drug-frame objectives


def io_num(q):
    return q["io"].split("—")[0].strip()


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rn, _) = lens[0], lens[1]
    return ti == q["c"] and (tl - rn) >= MARGIN_CHARS and tl >= rn * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def assert_no_dose_answers(pool):
    bare = re.compile(r"^\W*\d[\d\s.,%-]*\s*(mg|g|mcg|units|%|per cent)?\W*$", re.I)
    bad = [q["q"][:70] for q in pool if bare.match(q["opts"][q["c"]][0])]
    assert not bad, "a correct answer is a bare dose/strength: %r" % bad


def assert_mcinnis_weighting(qs, label):
    mech = sum(1 for q in qs if io_num(q) in MECH_IOS)
    four = sum(1 for q in qs if io_num(q) in MCINNIS_IOS)
    assert four > mech, ("%s: mechanism %d vs applied/drug objectives %d" % (label, mech, four))
    return mech, four


ALL_IOS = set(q["io"] for q in POOL)


def score(setqs):
    ios = Counter(q["io"] for q in setqs)
    missing = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 8) for n in ios.values())
    return missing * 25 + lumpy * 3 + gameable_pct(setqs) * 1.2


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
    print("topic: %s   pool size: %d" % (TOPIC, len(POOL)))
    print("schema problems:", validate(POOL) or "none")
    print("objectives covered:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    assert_no_dose_answers(POOL)
    print("Wood dosage rule: no correct answer is a bare dose or strength")
    m, f = assert_mcinnis_weighting(POOL, "pool")
    print("weighting (pool): mechanism %d vs applied/drug %d" % (m, f))
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best, idx = None, list(range(len(POOL)))
    for _ in range(40000):
        random.shuffle(idx)
        ch = idx[:60]
        total = score([POOL[i] for i in ch[:30]]) + score([POOL[i] for i in ch[30:]])
        if best is None or total < best[0]:
            best = (total, list(ch))

    ch = best[1]
    s1 = rotate_for_balance([POOL[i] for i in ch[:30]])
    s2 = rotate_for_balance([POOL[i] for i in ch[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        m, f = assert_mcinnis_weighting(s, name)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives: %d of %d" % (len(set(q["io"] for q in s)), len(ALL_IOS)))
        print("   mechanism %d vs applied/drug %d" % (m, f))
        print()

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, OUT_JSON), "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)
