#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 7 (Electrocardiography) pool into two 30s.

THE COURSE NUMBER RULE IS RELAXED FOR THIS LECTURE, deliberately. Elsewhere in
Principles of Diagnostic Medicine a figure never appears without the scale that
reads it and nothing is calculated -- a rule that belongs to a different
lecturer. Here the objectives are "Determine heart rate using an
electrocardiogram" and "Measure and interpret" the PR interval and the rest, so
intervals, thresholds and the two rate methods ARE the material. Asking a
student to multiply a six-second count by ten is the objective, not a breach of
it.

What the questions still do is supply what a clinician would actually have --
the strip, the counts, the measured interval in small boxes -- and ask what
follows. So the numeric guard here checks that a figure is accompanied by
something that reads it, and the calculation guard is dropped rather than
worked around.

The pool is 62, so two are held back for the cumulative masters covering
Lectures 7-10 and Lab 2.

THE TRANSCRIPT IS NOT IN YET. Queued behind the exams that come sooner, so
every question comes off the slides and cites the slide it came from.
"""
import json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l7_pool_a import POOL_A
from pdm_l7_pool_b import POOL_B

POOL = POOL_A + POOL_B
SEED, NOPT, BAR, PER_SET = 20260919, 4, 0.35, 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|this course|in class)\b")
# A figure with a unit needs a word that reads it. "58 per cent" is fine when the
# stem also says what a normal ratio looks like or asks what it suggests.
_NUM = re.compile(r"\b\d[\d,\.]*\s*(?:mg|mmHg|per cent|%|beats|bpm|minutes?|hours?)", re.I)
_SCALE = re.compile(r"(?i)\bnormal\b|\brange\b|\braised\b|\bhigh\b|\blow\b|\babove\b|\bbelow\b|"
                    r"\bsuggest|\bindicat|\bexceed|\breach|\bpredicted\b|\bthreshold\b|\bvalid\b")


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
        if _NUM.search(q["q"]):
            assert _SCALE.search(q["q"]), "%s: number without its scale: %r" % (w, q["q"][:70])
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
    out = os.path.join(HERE, "pdm_l7_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(out), "(%d held back for the master exams)"
          % (len(POOL) - PER_SET * 2))


if __name__ == "__main__":
    main()
