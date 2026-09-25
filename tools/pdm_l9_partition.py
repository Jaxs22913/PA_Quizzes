#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 9 (Cardiac Biomarkers and Lipids) pool into two 30s.

House format is 2x30 per topic. The pool is larger than 60 so the remainder is
held back for the cumulative master exams, which cover Lectures 7-10 and Lab 2.

REYNOLDS' RULES, asserted rather than trusted:
  1. A laboratory value never appears in a stem without the scale that reads it
     (a reference limit, a desirable level, a named tier, or above/below).
  2. Her no-math rule is PER QUANTITY (Lecture 5: the anion gap was calculated,
     GFR and corrected sodium were not). This deck's own Quick Practice slide
     (43) asks for LDL-C and non-HDL-C to be calculated, so the two worked
     calculations in pool B are allowed -- and ONLY those two quantities. Any
     other "calculate" in a stem fails the build. CONFIRMED from the 21 September
     recording (2026-09-25, both transcripts, part 3 6:03-9:48): "there will be
     two things that you need to calculate ... for our purposes, we're gonna
     practice this", "You may use calculator[s]" (Notability adds "I'll allow
     it"), "So we had to do two calculations, and then we have to interpret." ALLOW_CALC stays True.

Selection is swap-based local search, as on the CMS and PDM L5 builds: it
spreads topics across both sets and holds the length-gameable share down. The
target is under 10% gameable per set (Jaxon, 2026-08-16); 35% is only the
failure bar.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l9_pool_a import POOL_A
from pdm_l9_pool_b import POOL_B

ALLOW_CALC = True
POOL = POOL_A + POOL_B
if not ALLOW_CALC:
    POOL = [q for q in POOL if q["slot"] != "calculation"]
SEED, NOPT, BAR, TARGET, PER_SET = 20260925, 4, 0.35, 0.10, 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slides?|deck|professor|this course|in class|syllabus)\b")
_NUM = re.compile(r"\b\d[\d,\.]*\s*(?:mg/dL|mg/L|ng/L|ng/mL|nmol/L|%)", re.I)
_SCALE = re.compile(r"(?i)\bnormal\b|\brange\b|\bdesirable\b|\blimit\b|\bpercentile\b|\btier\b|"
                    r"\babove\b|\bbelow\b|\bfavorable\b|\bconsidered elevated\b|\bgoal\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute(?!d tomography)|\bwork out\b|\bwhat is the (?:friedewald|non-hdl)")
_CALC_OK = re.compile(r"(?i)non-HDL-C|Friedewald LDL-C")


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def check(pool):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %s" % (i, q["q"][:50])
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert q["c"] == 0, "%s: key must be authored first" % w
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        if q["slot"] == "calculation":
            assert _CALC_OK.search(q["q"]), "%s: only LDL-C and non-HDL-C may be calculated" % w
        else:
            assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        if _NUM.search(q["q"]):
            assert _SCALE.search(q["q"]), "%s: number without its scale" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        assert q["opts"][0][1].startswith("Correct"), "%s: key explanation must open Correct" % w
        for j, (t, e) in enumerate(q["opts"]):
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            if j:
                assert not e.startswith("Correct"), "%s: distractor explanation opens Correct" % w
        assert q.get("cite", "").startswith("svCardiac Biomarkers and Lipids.pptx, Slide "), w


def score(sel):
    """Lower is better: gameable share over target, topic repeats, IO balance."""
    qs = [POOL[i] for i in sel]
    g = sum(gameable(q["opts"], 0) for q in qs) / len(qs)
    topics = Counter(q["topic"] for q in qs)
    rep = sum(v - 1 for v in topics.values() if v > 2)
    ios = Counter(q["io"] for q in qs)
    miss = 7 - len(ios)
    return max(0.0, g - TARGET) * 100 + rep * 0.5 + miss * 5


def main():
    rng = random.Random(SEED)
    check(POOL)
    n = len(POOL)
    assert n >= PER_SET * 2, "pool of %d cannot fill two sets of %d" % (n, PER_SET)
    best = None
    for _ in range(300):
        idx = list(range(n)); rng.shuffle(idx)
        s = idx[:PER_SET * 2]
        v = score(s[:PER_SET]) + score(s[PER_SET:])
        if best is None or v < best[0]:
            best = (v, s)
    v, sel = best
    rest = [i for i in range(n) if i not in sel]
    for _ in range(40000):
        a = rng.randrange(PER_SET * 2)
        if rest and rng.random() < 0.5:
            b = rng.randrange(len(rest))
            new = sel[:]; new[a], nr = rest[b], sel[a]
            nv = score(new[:PER_SET]) + score(new[PER_SET:])
            if nv <= v:
                sel, v = new, nv; rest[b] = nr
        else:
            b = rng.randrange(PER_SET * 2)
            new = sel[:]; new[a], new[b] = new[b], new[a]
            nv = score(new[:PER_SET]) + score(new[PER_SET:])
            if nv <= v:
                sel, v = new, nv

    sets = {}
    for k, part in ((1, sel[:PER_SET]), (2, sel[PER_SET:])):
        qs = [POOL[i] for i in part]
        order = ([0, 1, 2, 3] * ((len(qs) // NOPT) + 1))[:len(qs)]
        rng.shuffle(order)
        rot = []
        for q, want in zip(qs, order):
            o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
            r = {kk: vv for kk, vv in q.items() if kk != "slot"}
            r["opts"] = o; r["c"] = want
            rot.append(r)
        pos = Counter(q["c"] for q in rot)
        assert max(pos.values()) - min(pos.values()) <= 1, "set%d: uneven positions %r" % (k, pos)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: gameable %.0f%%" % (k, frac * 100)
        sets["set%d" % k] = rot
        print("set%d  %d questions  positions=%s  gameable=%.1f%%  topics=%d  objectives=%d"
              % (k, len(rot), {chr(65 + p): c for p, c in sorted(pos.items())}, frac * 100,
                 len({q["topic"] for q in rot}), len({q["io"] for q in rot})))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l9_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], 0) for q in POOL) / n
    print("pool %d (raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, raw * 100, os.path.basename(out), len(held)))


if __name__ == "__main__":
    main()
