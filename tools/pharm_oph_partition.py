#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the three Pharmacology Exam 2 ophthalmology pools.

SIZES ARE NOT 2x30 AND THAT IS DELIBERATE. Dr. Wood rules out dosing,
formulations, the indications table and which agent causes which adverse
effect; padding to the house 30 would have meant writing questions on exactly
the material he said he will not ask. Each pool is split in half instead:

    anti-infectives      40 -> 2 x 20
    allergy/inflammation 32 -> 2 x 16
    glaucoma/diagnostics 32 -> 2 x 16

Guards below are the ones this content can fail: a pharmacology question that
quizzes a number he excluded, a stem that cites the lecture, an uneven answer
distribution, or a key that is guessable by length.
"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_oph_pool_anti import QUESTIONS as ANTI
from pharm_oph_pool_inflam import QUESTIONS as INFLAM
from pharm_oph_pool_glauc import QUESTIONS as GLAUC

SEED, NOPT, BAR = 20260911, 4, 0.35
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|dr\.|this course|in class)\b")
# Things Dr. Wood said he will not ask. A milligram or a percent-concentration
# in a STEM means the question is testing a dose or a formulation.
DOSE = re.compile(r"(?i)\b\d+\s*(mg|milligram|microgram|unit|%\s*(solution|ointment|suspension))\b"
                  r"|\b(instil|apply)\b.*\b(times (a|per) day|daily|hourly)\b")


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= MARGIN_CHARS and L[c] >= runner * (1 + MARGIN_FRAC)


def check(pool, label):
    seen = set()
    for i, q in enumerate(pool):
        w = "%s[%d]" % (label, i)
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert q["c"] == 0, "%s: key must be authored first" % w
        assert "?" in q["q"], "%s: stem asks nothing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not DOSE.search(q["q"]), "%s: stem tests a dose or formulation" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        texts = [o[0] for o in q["opts"]]
        assert len(set(texts)) == NOPT, "%s: duplicate option text" % w
        for t, e in q["opts"]:
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            # EXPLANATIONS TOO, not just stems. Nineteen of these cited "this
            # lecture" or "this deck" on the first build: writing about the
            # teaching rather than about the medicine. A student revising in
            # March has no lecture in front of them.
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])


def split(pool, rng):
    idx = list(range(len(pool)))
    rng.shuffle(idx)
    half = len(pool) // 2
    return [pool[i] for i in idx[:half]], [pool[i] for i in idx[half:]]


def rotate(qs, rng):
    order = ([0, 1, 2, 3] * ((len(qs) // NOPT) + 1))[:len(qs)]
    rng.shuffle(order)
    out = []
    for q, want in zip(qs, order):
        o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
        r = dict(q); r["opts"] = o; r["c"] = want
        out.append(r)
    return out


def main():
    rng = random.Random(SEED)
    sets = {}
    for label, pool in (("anti", ANTI), ("inflam", INFLAM), ("glauc", GLAUC)):
        check(pool, label)
        a, b = split(pool, rng)
        for n, part in ((1, a), (2, b)):
            rot = rotate(part, rng)
            pos = {}
            for q in rot:
                pos[q["c"]] = pos.get(q["c"], 0) + 1
            assert max(pos.values()) - min(pos.values()) <= 1, \
                "%s%d: uneven positions %r" % (label, n, pos)
            frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
            assert frac <= BAR, "%s%d: key longest in %.0f%%" % (label, n, frac * 100)
            sets["%s%d" % (label, n)] = rot
            print("%-8s %2d questions  positions=%s  key-is-longest=%.0f%%"
                  % (label + str(n), len(rot),
                     {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100))
    out = os.path.join(HERE, "pharm_oph_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(out))


if __name__ == "__main__":
    main()
