#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Pharmacology Exam 3 topic pools (Lecture 9, Diuretics and Heart Failure Drugs).

One pool module per topic: tools/pharm_e3_pool_<key>.py exposes QUESTIONS (key authored FIRST, c == 0). This script holds
the guards (imported by the vignette partition too) and writes ONE sets file per topic, tools/pharm_e3_sets/<key>.json
(keys <key>1 and <key>2), so several topics can be built at once without writing the same file.

  1. NO DOSES. Dr. Wood does not test them (timings, routes, durations and clinical thresholds such as potassium or
     heart-rate cut-offs are allowed).
  2. DESCOPED: the digoxin target level (Dr. Wood: "I'm probably not going to quiz you specifically on the level")
     may not be a key; no key may BE a bare percentage or a bare number of liters (kidney-handling percentages are
     physiology to recognize, not figures to memorize).
  3. Dr. McInnis's weighting: per set, mechanism plus physiology items may not outnumber indications + education +
     adverse effects + contraindications + drug choice combined.
  4. Same house guards as every other build: four options, key first, stem asks one question, no course citations,
     explanation >= 60 characters and "Correct" marks only the key, answer positions rotated evenly, key not the
     longest option in more than 35 percent (warn over 10 percent).

Each pool is split in half rather than padded to the house 30: the pool is as large as the slides support.

    python3 tools/pharm_e3_partition.py <key> [<key> ...]
"""
import importlib, json, os, random, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _selfcontain_rx import RX
from _lecturers import citation_hits

SEED, NOPT, BAR, TARGET = 20261003, 4, 0.35, 0.10
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|dr\.|this course|in class)\b")
DOSE = re.compile(r"(?i)\b\d+\s*(mg|milligram|microgram|mcg|units?)\b(?!\s*/\s*(dl|g)\b)"
                  r"|\b\d+\s*%\s*(solution|ointment|suspension|saline)\b")
DESCOPED = re.compile(r"(?i)0\.5\s*(-|to)\s*1\s*ng|\bng\s*/\s*ml\b|therapeutic (level|range|window) of")
BAD_KEY = re.compile(r"^\s*(about |up to |roughly )?[\d.,]+\s*(-|to)?\s*[\d.,]*\s*(%|percent|liters?|l/day|liters per day)\s*$", re.I)
BREADTH = ("indication", "education", "adverse effect", "contraindication", "drug choice")
BACKGROUND = ("mechanism", "physiology")
SLOTS = set(BREADTH) | set(BACKGROUND) | {"class", "interaction", "monitoring", "protocol"}
CITE_RX = re.compile(r"^(Diuretics and Heart Failure Drugs|Antihypertensives|Myocardial Ischemia Drugs|Ophthalmology-2)\.pptx, Slide \d+$")   # a cross-lecture fact cites the deck that states it


def hard_cites(text):
    return bool(RX.search(text)) or any(h[0] != "review" for h in citation_hits(text))


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
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q.get("slot") in SLOTS, "%s: unknown slot %r" % (w, q.get("slot"))
        for s in [q["q"]] + [t for o in q["opts"] for t in o]:
            assert not CITES.search(s) and not hard_cites(s), "%s: cites the course: %r" % (w, s[:70])
        assert not DOSE.search(q["q"]), "%s: stem tests a dose" % w
        assert not DOSE.search(" ".join(o[0] for o in q["opts"])), "%s: option is a dose" % w
        assert not DESCOPED.search(q["q"] + " " + q["opts"][0][0]), "%s: descoped topic" % w
        assert not BAD_KEY.search(q["opts"][0][0]), "%s: the key is the five-minute number" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        texts = [o[0] for o in q["opts"]]
        assert len(set(texts)) == NOPT, "%s: duplicate option text" % w
        for k, (t, e) in enumerate(q["opts"]):
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            assert e.startswith("Correct") == (k == 0), "%s: 'Correct' marks the wrong option" % w
        assert CITE_RX.match(q["cite"]), "%s: cite %r" % (w, q["cite"])


def split(pool, rng):
    """Deal each topic's questions alternately into the two sets."""
    groups = OrderedDict()
    for q in pool:
        groups.setdefault(q["topic"], []).append(q)
    a, b = [], []
    for qs in groups.values():
        qs = qs[:]
        rng.shuffle(qs)
        for q in qs:
            (a if len(a) <= len(b) else b).append(q)
    rng.shuffle(a)
    rng.shuffle(b)
    return a, b


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
    keys = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not keys:
        sys.exit("usage: pharm_e3_partition.py <key> [<key> ...]   (pool module tools/pharm_e3_pool_<key>.py)")
    outdir = os.path.join(HERE, "pharm_e3_sets")
    os.makedirs(outdir, exist_ok=True)
    for key in keys:
        rng = random.Random(SEED + sum(map(ord, key)))     # own stream per topic: editing one pool never moves another
        pool = importlib.import_module("pharm_e3_pool_" + key.replace("-", "_")).QUESTIONS
        check(pool, key)
        a, b = split(pool, rng)
        sets = {}
        for n, part in ((1, a), (2, b)):
            rot = rotate(part, rng)
            pos = {}
            for q in rot:
                pos[q["c"]] = pos.get(q["c"], 0) + 1
            assert len(pos) == NOPT and max(pos.values()) - min(pos.values()) <= 1, \
                "%s%d: uneven positions %r" % (key, n, pos)
            frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
            assert frac <= BAR, "%s%d: key longest in %.0f%%" % (key, n, frac * 100)
            back = sum(q["slot"] in BACKGROUND for q in rot)
            broad = sum(q["slot"] in BREADTH for q in rot)
            assert back <= broad, "%s%d: mechanism+physiology %d outweighs breadth %d" % (key, n, back, broad)
            sets["%s%d" % (key, n)] = rot
            print("%-14s %2d questions  positions=%s  gameable=%.0f%%%s  mechanism+physiology=%d breadth=%d topics=%d"
                  % (key + str(n), len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100,
                     "  (over the 10%% target)" if frac > TARGET else "", back, broad, len({q["topic"] for q in rot})))
        json.dump(sets, open(os.path.join(outdir, key + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("wrote pharm_e3_sets/%s.json" % key)


if __name__ == "__main__":
    main()
