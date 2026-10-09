#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 11 (Rhythm Analysis and Sinus Rhythms) pool into two 30s.

House format is 2x30 per lecture (one topic per lecture, the L7-L10 pattern). The rest of the
pool is held back for the Exam 3 master forms (Lectures 11-16).

RULES, asserted rather than trusted:
  1. A measured value in a stem carries the scale that reads it (a normal range, "standard",
     or above/below). Rates and intervals are this lecture's material, so options carry them.
  2. No acronym outside the wave labels (P, QRS, ST, PR, QT, TP), the roman-numeral lead names
     and the ABBREV (full term) form.
  3. STRIPS HEAVY (Jaxon, 2026-10-08): every set carries at least IMG_MIN questions that show a
     strip, no tracing appears twice in one set (two crops of one picture count as one), every
     strip file exists, and no alt text names the keyed answer.
  4. The usual: four options, key authored first, one question mark, no course citations,
     every explanation at least 60 characters, balanced positions, gameable under 10% target.

EMPHASIS, from the 5 October recording (three clips, 102 minutes, distinct minutes per subject):
conduction system and action potential about 30, paper and waves about 27, rate, regularity and
the systematic approach about 19, leads about 9, the sinus rhythms about 18. The sinus rhythms
carry five of the nine objectives and all the strips, so they get the largest band per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUTDIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
sys.path.insert(0, HERE)
from pdm_l11_pool_a import POOL_A, SRC
from pdm_l11_pool_b import POOL_B

GROUPS = [
  ({"Conduction system", "Cardiac cell properties", "Action potential", "Refractory periods",
    "Conduction vector", "Ventricular filling"}, 6, 9),
  ({"Electrocardiogram paper", "Waves and intervals", "QRS duration", "PR interval"}, 5, 8),
  ({"Heart rate", "Regularity", "Systematic approach"}, 4, 7),
  ({"Lead placement"}, 2, 4),
  ({"Normal sinus rhythm", "Sinus bradycardia", "Sinus tachycardia", "Sinus rhythms compared",
    "Sinus arrhythmia", "Sinus exit block", "Sinus pause", "Sinus arrest", "Sick sinus syndrome"}, 9, 12),
]
BAN_STEMS = []
POOL = [q for q in POOL_A + POOL_B if not any(b in q["q"] for b in BAN_STEMS)]
N_IO = len({q["io"] for q in POOL})
# IMG_MIN was 14 until the 2026-10-08 fact-check retired the slide 87 (arrows draw the answer) and
# slide 93 (pause too close to a whole multiple) strips; the pool now has 14 distinct tracings, two
# of them with a single question, so 13 distinct tracings per set is the most both sets can carry.
SEED, NOPT, BAR, TARGET, PER_SET, IMG_MIN, TOPIC_CAP = 20261008, 4, 0.35, 0.10, 30, 13, 5
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slides?|deck|professor|this course|in class|syllabus)\b")
_UNIT = re.compile(r"\b\d[\d,\.]*\s*(?:per minute|seconds?|milliseconds?|millivolts?|millimeters?|percent)", re.I)
_SCALE = re.compile(r"(?i)\bnormal\b|\brange\b|\bstandard\b|\bresting\b|\bbelow\b|\babove\b|\blimit\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"QRS", "ST", "PR", "QT", "TP", "NOT", "DO"}


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def acronyms(txt):
    bad = []
    for m in _ACRO.finditer(txt):
        a = m.group(0)
        if a in _ACRO_OK or re.fullmatch(r"[IVX]+", a):
            continue
        if txt[m.end():m.end() + 2] == " (":         # ABBREV (full term)
            continue
        bad.append(a)
    return bad


def check(pool):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %s" % (i, q["q"][:50])
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert q["c"] == 0, "%s: key must be authored first" % w
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        if _UNIT.search(q["q"]):
            assert _SCALE.search(q["q"]), "%s: value without its scale" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        assert q["opts"][0][1].startswith("Correct"), "%s: key explanation must open Correct" % w
        for j, (t, e) in enumerate(q["opts"]):
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            assert len(t) <= 66, "%s: option over 66 characters: %r" % (w, t)
            if j:
                assert not e.startswith("Correct"), "%s: distractor explanation opens Correct" % w
        assert q.get("cite", "").startswith(SRC + ", Slide"), w
        for where, txt in [("stem", q["q"])] + [("option", o[0]) for o in q["opts"]] + \
                          [("explanation", o[1]) for o in q["opts"]]:
            bad = acronyms(txt)
            assert not bad, "%s: acronym %r in %s" % (w, bad, where)
        if "img" in q:
            assert os.path.exists(os.path.join(OUTDIR, q["img"])), "%s: missing %s" % (w, q["img"])
            assert q.get("alt") and q.get("slide"), "%s: picture without alt or slide" % w
            assert q["opts"][0][0].lower() not in q["alt"].lower(), "%s: alt text names the answer" % w


def tracing(q):
    """Two crops of one deck picture (the slide 89 strip with and without its second labels) are
    the same tracing, so a set may carry only one of them: key on the slide number in the name."""
    m = re.match(r"(l11-s\d+)", os.path.basename(q["img"]))
    return m.group(1) if m else q["img"]


def score(sel):
    """Lower is better."""
    qs = [POOL[i] for i in sel]
    g = sum(gameable(q["opts"], 0) for q in qs) / len(qs)
    topics = Counter(q["topic"] for q in qs)
    rep = sum(v - TOPIC_CAP for v in topics.values() if v > TOPIC_CAP)
    miss = N_IO - len({q["io"] for q in qs})
    short = 0
    for ts, lo, hi in GROUPS:
        k = sum(topics.get(t, 0) for t in ts)
        short += max(0, lo - k) + max(0, k - hi)
    imgs = [tracing(q) for q in qs if "img" in q]
    dup = len(imgs) - len(set(imgs))
    few = max(0, IMG_MIN - len(set(imgs)))
    return max(0.0, g - TARGET) * 100 + rep * 0.5 + miss * 5 + short * 3 + dup * 10 + few * 6


def main():
    rng = random.Random(SEED)
    check(POOL)
    n = len(POOL)
    assert n >= PER_SET * 2, "pool of %d cannot fill two sets of %d" % (n, PER_SET)
    best = None
    for _ in range(400):
        idx = list(range(n)); rng.shuffle(idx)
        s = idx[:PER_SET * 2]
        v = score(s[:PER_SET]) + score(s[PER_SET:])
        if best is None or v < best[0]:
            best = (v, s)
    v, sel = best
    rest = [i for i in range(n) if i not in sel]
    for _ in range(60000):
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
    assert v < 1, "could not satisfy every constraint (score %.2f)" % v

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
        imgs = [tracing(q) for q in rot if "img" in q]
        assert len(imgs) == len(set(imgs)) and len(imgs) >= IMG_MIN, "set%d: strips %d" % (k, len(imgs))
        sets["set%d" % k] = rot
        print("set%d  %d questions  positions=%s  gameable=%.1f%%  strips=%d  topics=%d  objectives=%d/%d"
              % (k, len(rot), {chr(65 + p): c for p, c in sorted(pos.items())}, frac * 100, len(imgs),
                 len({q["topic"] for q in rot}), len({q["io"] for q in rot}), N_IO))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l11_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], 0) for q in POOL) / n
    print("pool %d (%d with a strip; raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum(1 for q in POOL if "img" in q), raw * 100, os.path.basename(out), len(held)))


if __name__ == "__main__":
    main()
