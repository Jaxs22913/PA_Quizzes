#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the "keyed as the course teaches" questions to the Pharmacology Exam 2 myocardial ischemia sets.

The questions live in pharm_mi_pool_course.py (see its docstring for the decision behind them). They are NOT
fed to the seeded splitters, because adding to a pool would reshuffle every question already shipped. Instead
this script runs AFTER pharm_mi_partition.py / pharm_mi_vignette_partition.py and APPENDS:

  * every existing question keeps its text, its options, its explanations and its key position;
  * each new question goes to the smaller of its two sets (alternating when equal), at a seeded random place;
  * its key is given the answer position that is least used in that set, so positions stay within one of even;
  * the same guards as the partitioners apply (four options, no course citations, no doses, descoped topics,
    explanations of at least 60 characters, the length-bias bar, mechanism + physiology never outweighing breadth).

Idempotent: a question whose stem is already in a set is skipped. Each partition script calls its extend_* function when it
finish, so re-running either one reproduces the same extended files.

    python3 tools/pharm_mi_course_extend.py
"""
import json, os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SEED = 20260930 + 77
NOPT = 4


def _pos_counts(qs):
    return Counter(q["c"] for q in qs)


def _place(qs, q, rng):
    """Move the (key-first) question's key to the least used position in the set; insert at a seeded place."""
    cnt = _pos_counts(qs)
    least = min(cnt.get(k, 0) for k in range(NOPT))
    choices = [k for k in range(NOPT) if cnt.get(k, 0) == least]
    want = rng.choice(choices)
    o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
    r = dict(q); r["opts"] = o; r["c"] = want
    r.pop("set", None)
    qs.insert(rng.randrange(len(qs) + 1), r)
    return r


def _report(label, qs):
    from pharm_mi_partition import gameable, BREADTH, BACKGROUND, BAR
    pos = _pos_counts(qs)
    assert max(pos.values()) - min(pos.values()) <= 1, "%s: uneven positions %r" % (label, dict(pos))
    frac = sum(gameable(q["opts"], q["c"]) for q in qs) / len(qs)
    assert frac <= BAR, "%s: key longest in %.0f%%" % (label, frac * 100)
    back = sum(q["slot"] in BACKGROUND for q in qs)
    broad = sum(q["slot"] in BREADTH for q in qs)
    assert back <= broad, "%s: mechanism+physiology %d outweighs breadth %d" % (label, back, broad)
    for q in qs:
        assert q["opts"][q["c"]][1].startswith("Correct")
    print("  %-9s %2d questions  positions=%s  gameable=%.0f%%  mech+phys=%d breadth=%d"
          % (label, len(qs), {chr(65 + k): pos.get(k, 0) for k in range(NOPT)}, frac * 100, back, broad))


def extend_topics(verbose=True):
    import pharm_mi_pool_course as pool
    from pharm_mi_partition import check

    rng = random.Random(SEED)
    check(pool.QUESTIONS, "course")

    # ---- topic quizzes -------------------------------------------------------------------
    path = os.path.join(HERE, "pharm_mi_sets.json")
    sets = json.load(open(path, encoding="utf-8"))
    added = 0
    for group in ("anginal", "acs"):
        a, b = sets[group + "1"], sets[group + "2"]
        for q in [x for x in pool.QUESTIONS if x["set"] == group]:
            if any(q["q"] == e["q"] for e in a + b):
                continue
            target = a if len(a) <= len(b) else b
            _place(target, q, rng)
            added += 1
    json.dump(sets, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if verbose:
        print("pharm_mi_sets.json: appended %d course-keyed questions" % added)
        for k in ("anginal1", "anginal2", "acs1", "acs2"):
            _report(k, sets[k])

    return added


def extend_vignettes(verbose=True):
    import pharm_mi_pool_course as pool
    from pharm_mi_partition import check
    from pharm_mi_vignette_partition import guard_vignettes

    rng = random.Random(SEED + 1)
    check(pool.VIGNETTES, "course-vig")
    guard_vignettes(pool.VIGNETTES)

    # ---- vignettes -----------------------------------------------------------------------
    vpath = os.path.join(HERE, "pharm_mi_vignette_sets.json")
    vs = json.load(open(vpath, encoding="utf-8"))
    vadded = 0
    for q in pool.VIGNETTES:
        if any(q["q"] == e["q"] for e in vs["set1"] + vs["set2"]):
            continue
        target = vs["set1"] if len(vs["set1"]) <= len(vs["set2"]) else vs["set2"]
        r = _place(target, {k: v for k, v in q.items() if k != "lead"}, rng)
        vadded += 1
    json.dump(vs, open(vpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if verbose:
        print("pharm_mi_vignette_sets.json: appended %d course-keyed vignettes" % vadded)
        for k in ("set1", "set2"):
            _report(k, vs[k])
    return vadded


if __name__ == "__main__":
    extend_topics()
    extend_vignettes()
