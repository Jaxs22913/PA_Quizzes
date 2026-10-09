#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 12 (Ectopy, Escape Rhythms and Supraventricular Dysrhythmias) pool
into two 30s.

House format is 2x30 per lecture. The remainder is held back for the Exam 3 master forms.

RULES, asserted rather than trusted (same contract as pdm_l11_partition.py):
  1. A measured value in a stem carries the scale that reads it (here the normal adult resting
     rate, 60 to 100 per minute, beside every stated rate).
  2. No acronym outside the wave labels (P, QRS, ST, PR, QT, TP, RP) and the ABBREV (full term)
     form.
  3. STRIPS HEAVY (Jaxon, 2026-10-08): at least IMG_MIN strip questions per set, no strip twice
     in one set, every strip file present, no alt text naming the keyed answer.
  4. Four options, key first, one question mark, no course citations, explanations of 60+
     characters, balanced positions, gameable under 10% target (35% bar).

EMPHASIS, from the 5 October recording (three clips, 84 minutes): ventricular beats and rhythms
about 20 minutes, junctional beats and rhythms about 17, atrioventricular nodal reentrant
tachycardia about 13, atrial flutter about 10, premature atrial complexes and their patterns
about 9, atrial fibrillation about 8, wandering atrial pacemaker and multifocal atrial
tachycardia about 5. The bands below follow those minutes.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUTDIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
sys.path.insert(0, HERE)
from pdm_l12_pool_a import POOL_A, SRC
from pdm_l12_pool_b import POOL_B

GROUPS = [
  ({"Premature atrial complex", "Premature beat patterns"}, 3, 5),
  ({"Premature junctional complex"}, 1, 3),
  ({"Premature ventricular complex"}, 3, 5),
  ({"Escape beats"}, 1, 3),
  ({"Junctional rhythm", "Junctional anatomy"}, 4, 7),
  ({"Idioventricular rhythm", "Junctional versus idioventricular"}, 3, 5),
  ({"Wandering atrial pacemaker", "Multifocal atrial tachycardia"}, 2, 4),
  ({"Atrial flutter"}, 3, 5),
  ({"Atrial fibrillation"}, 2, 4),
  ({"Reentry tachycardia"}, 3, 5),
]
BAN_STEMS = []
POOL = [q for q in POOL_A + POOL_B if not any(b in q["q"] for b in BAN_STEMS)]
N_IO = len({q["io"] for q in POOL})
SEED, NOPT, BAR, TARGET, PER_SET, IMG_MIN, TOPIC_CAP = 20261009, 4, 0.35, 0.10, 30, 18, 6
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slides?|deck|professor|this course|in class|syllabus)\b")
_UNIT = re.compile(r"\b\d[\d,\.]*\s*(?:per minute|seconds?|milliseconds?|millivolts?|millimeters?|percent)", re.I)
_SCALE = re.compile(r"(?i)\bnormal\b|\brange\b|\bstandard\b|\bresting\b|\bbelow\b|\babove\b|\blimit\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"QRS", "ST", "PR", "QT", "TP", "RP"}


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
    imgs = [q["img"] for q in qs if "img" in q]
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
        imgs = [q["img"] for q in rot if "img" in q]
        assert len(imgs) == len(set(imgs)) and len(imgs) >= IMG_MIN, "set%d: strips %d" % (k, len(imgs))
        sets["set%d" % k] = rot
        print("set%d  %d questions  positions=%s  gameable=%.1f%%  strips=%d  topics=%d  objectives=%d/%d"
              % (k, len(rot), {chr(65 + p): c for p, c in sorted(pos.items())}, frac * 100, len(imgs),
                 len({q["topic"] for q in rot}), len({q["io"] for q in rot}), N_IO))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l12_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], 0) for q in POOL) / n
    print("pool %d (%d with a strip; raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum(1 for q in POOL if "img" in q), raw * 100, os.path.basename(out), len(held)))


if __name__ == "__main__":
    main()
