#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition an Interpretation of Medical Literature session pool into two 30s.

    python3 medlit_partition.py s1     # Session 1, Introduction, Bias and Validity

House format is 2x30 per topic. Anything above 60 in a pool is held back for a
cumulative exam rather than padded into the sets.

THIS COURSE DOES HAVE AN EXAM. The posted schedule lists no exam session, which
is easy to read as there being none, but the session 1 deck is explicit: a
computerised exam worth 40 per cent of the grade, covering the assigned readings
and the lecture material. The remaining 60 per cent is participation and the
group project, neither of which is examinable content.

COURSE MECHANICS ARE NOT CONTENT, so the grading weights, the required text and
the assignment structure are excluded at the pool level rather than filtered
here.

Guards, in the order this content could fail them: a stem or explanation that
cites the session, a thin explanation, a duplicate, an uneven answer
distribution, a key guessable by its length.
"""
import json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

WHICH = sys.argv[1] if len(sys.argv) > 1 else "s1"
SPECS = {
 "s1": (["medlit_s1_pool_a:POOL_A", "medlit_s1_pool_b:POOL_B"], "medlit_s1_sets.json"),
 "s2evid": (["medlit_s2evid_pool:POOL"], "medlit_s2evid_sets.json"),
 "s2design": (["medlit_s2design_pool:POOL"], "medlit_s2design_sets.json"),
 "s3rates": (["medlit_s3rates_pool:POOL"], "medlit_s3rates_sets.json"),
 "s3data": (["medlit_s3data_pool:POOL"], "medlit_s3data_sets.json"),
 "s4tests": (["medlit_s4tests_pool:POOL"], "medlit_s4tests_sets.json"),
}
if WHICH not in SPECS:
    sys.exit("unknown set %r -- use one of %s" % (WHICH, ", ".join(SPECS)))
mods, OUT = SPECS[WHICH]

POOL = []
for spec in mods:
    m, attr = spec.split(":")
    POOL.extend(getattr(__import__(m), attr))

SEED, NOPT, BAR, PER_SET = 20260918, 4, 0.35, 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|this course|in class|the session)\b")


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def check(pool):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d]" % i
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert q["c"] == 0, "%s: key must be authored first" % w
        assert "?" in q["q"], "%s: stem asks nothing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        for t, e in q["opts"]:
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])


def main():
    import random
    rng = random.Random(SEED)
    check(POOL)
    idx = list(range(len(POOL)))
    rng.shuffle(idx)
    idx = idx[:PER_SET * 2]
    sets = {}
    for n, part in ((1, idx[:PER_SET]), (2, idx[PER_SET:])):
        qs = [POOL[i] for i in part]
        order = ([0, 1, 2, 3] * ((len(qs) // NOPT) + 1))[:len(qs)]
        rng.shuffle(order)
        rot = []
        for q, want in zip(qs, order):
            o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
            r = dict(q); r["opts"] = o; r["c"] = want
            rot.append(r)
        pos = Counter(q["c"] for q in rot)
        assert max(pos.values()) - min(pos.values()) <= 1, \
            "set%d: uneven positions %r" % (n, pos)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: key longest in %.0f%%" % (n, frac * 100)
        sets["set%d" % n] = rot
        print("set%d  %d questions  positions=%s  key-is-longest=%.0f%%  topics=%d"
              % (n, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())},
                 frac * 100, len({q["topic"] for q in rot})))
    json.dump(sets, open(os.path.join(HERE, OUT), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT, "(%d held back)" % (len(POOL) - PER_SET * 2))


if __name__ == "__main__":
    main()
