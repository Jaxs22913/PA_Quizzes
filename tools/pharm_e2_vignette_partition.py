#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split the Pharm Exam 2 vignette pool into 2 x 21, and guard it.

Guards: four options, key authored first, no doses (Dr. Wood does not ask for
them), no course citations, no thin explanations, and no question built on
anything he de-scoped.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_e2_vignette_pool import POOL

# Dr. Wood does not ask for doses. A concentration quoted inside a product name
# is not a dose, so the pattern targets amounts and frequencies.
DOSE = re.compile(r"\b\d+\s*(?:mg|mcg|µg|g|units)\b|\b\d+\s*times (?:a|per) day\b|"
                  r"\bq\d+h\b|\bevery \d+ hours\b", re.I)
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|this course|in class|the syllabus)\b")
# The four things he took off the table.
# A flat length bar is the wrong test, as this session already established on
# the PD2 pools: "An antifungal." is fourteen characters and names the thing
# completely, while "Not the stated reason." is longer and names nothing. What
# is tested is the DEFECT -- an explanation that negates without naming what the
# distractor actually is.
BARE_NEG = re.compile(r"^(?:not\b|neither\b|it does not\b|reversed\.$|the opposite\b|"
                      r"no such\b|unrelated\.$|incorrect\.$|wrong\.$)", re.I)

DESCOPED = re.compile(r"which (?:agent|antibiotic) causes (?:eye |ocular )?irritation|"
                      r"which formulation|brand name|which combination product", re.I)


def check(pool):
    for i, q in enumerate(pool):
        w = "pool[%d]" % i
        assert len(q["opts"]) == 4, "%s: not four options" % w
        assert q["c"] == 0, "%s: key must be authored first" % w
        assert len({o[0] for o in q["opts"]}) == 4, "%s: duplicate option" % w
        assert not DESCOPED.search(q["q"]), "%s: built on de-scoped material" % w
        for o in q["opts"]:
            assert not DOSE.search(o[0]), "%s: a dose reached an option" % w
            assert not CITES.search(o[1]), "%s: explanation cites the course" % w
            assert not (BARE_NEG.match(o[1].strip()) and len(o[1].strip()) < 52), \
                "%s: explanation only NEGATES: %r" % (w, o[1][:48])
        assert not DOSE.search(q["q"]), "%s: a dose reached the stem" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
    # The promised item must survive into the pool.
    blob = " ".join(q["q"] + " ".join(o[0] + o[1] for o in q["opts"]) for q in pool)
    assert "rebound hyperaemia" in blob.lower(), "the item he promised to ask is missing"


def rotate(qs, rng):
    targets = [i % 4 for i in range(len(qs))]
    rng.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        if k:
            q["opts"] = q["opts"][-k:] + q["opts"][:-k]
        q["c"] = t
    return qs


def gameable_pct(qs):
    n = 0
    for q in qs:
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (t, ti), (r, _) = L[0], L[1]
        if ti == q["c"] and (t - r) >= 8 and t >= r * 1.18:
            n += 1
    return 100.0 * n / len(qs)


def main():
    check(POOL)
    rng = random.Random(20260913)
    answer = {id(q): q["opts"][q["c"]][0] for q in POOL}
    idx = list(range(len(POOL)))
    rng.shuffle(idx)
    half = len(POOL) // 2
    out = {}
    for n, part in ((1, idx[:half]), (2, idx[half:])):
        qs = rotate([POOL[i] for i in part], rng)
        for q in qs:
            assert q["opts"][q["c"]][0] == answer[id(q)], "rotation moved an answer!"
        g = gameable_pct(qs)
        assert g <= 35.0, "set%d: key longest in %.0f%%" % (n, g)
        pos = Counter(q["c"] for q in qs)
        print("set%d  %d questions  positions=%s  gameable=%.0f%%  topics=%d"
              % (n, len(qs), dict(sorted(pos.items())), g, len({q["topic"] for q in qs})))
        out["set%d" % n] = qs
    json.dump(out, open(os.path.join(HERE, "pharm_e2_vignette_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote pharm_e2_vignette_sets.json")


if __name__ == "__main__":
    main()
