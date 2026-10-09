#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 14 (Axis, Bundle Branch Blocks, and Chamber Enlargement) pool
into two 30s.

House format is 2x30 for the lecture (one topic pair per lecture). The remainder is held back for
the cumulative Exam 3 master forms (Lectures 11-16).

RULES, asserted rather than trusted (same as pdm_l13_partition.py):
  1. A value in a STEM always carries its normal range.  2. Nothing is calculated (the one sum
  question supplies both measurements and the normal sum, as the slide does).  3. No acronym
  outside the wave and interval names.  4. STRIPS HEAVY: at least MIN_IMG tracing questions per
  set, never the same tracing twice in one set.

EMPHASIS (the 6 October recording, parts 1-3; about 115 minutes of teaching, distinct minutes per
subject): the axis 24 plus most of the 18-minute run of practice 12-leads (which read axis and
bundle branch blocks again and again), right bundle branch block 19, left bundle branch block 17,
ventricular hypertrophy 17 (left 7.5, right 3, the hypertrophy mimic 2.5), the fascicular blocks
9, atrial enlargement 7. Spoken cues: the J point rule for V1, "easiest way to remember this"
(part 2, 2:48 and 12:35); the slide 22 correction (part 2, 42:28 and 44:31). No de-emphasis cue.
INCOMPLETE bundle branch block (objective d) is in neither the deck nor the recording.

Selection is swap-based local search, as on the L10 build. Target under 10% gameable per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
sys.path.insert(0, HERE)
from pdm_l14_pool_a import POOL_A, SRC
from pdm_l14_pool_b import POOL_B

GROUPS = [
  ({"Determining the axis", "Defining the axis", "Causes of axis deviation"}, 7, 10),
  ({"Left bundle branch block", "Right bundle branch block", "Bundle branch block criteria",
    "Where the ventricles depolarize"}, 7, 10),
  ({"Fascicular blocks"}, 2, 3),
  ({"Right atrial enlargement", "Left atrial enlargement", "Chamber enlargement"}, 4, 6),
  ({"Right ventricular hypertrophy", "Left ventricular hypertrophy"}, 4, 6),
  ({"Infarction mimics", "Systematic 12-lead read"}, 1, 3),
]
BAN_STEMS = []
POOL = [q for q in POOL_A + POOL_B if not any(b in q['q'] for b in BAN_STEMS)]
SEED, NOPT, BAR, TARGET, PER_SET = 20261014, 4, 0.35, 0.10, 30
MIN_IMG, MAX_IMG = 16, 20
N_IO = 9
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|lecturer|slides?|deck|professor|this course|in class|syllabus|mathis)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_LEADS = re.compile(r"\bV[1-6]\b|\b12-lead\b")       # lead names are not values
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"QRS", "QS", "PR", "QT", "ST", "NOT", "II", "III"}


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
        assert _AGE.search(q["q"]), "%s: stem names no patient" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        if re.search(r"\d", _LEADS.sub("", _AGE.sub("", q["q"]))):
            assert "(normal " in q["q"], "%s: value without its normal range" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        assert q["opts"][0][1].startswith("Correct"), "%s: key explanation must open Correct" % w
        for j, (t, e) in enumerate(q["opts"]):
            assert len(t) <= 66, "%s: option over 66 characters: %r" % (w, t)
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            if j:
                assert not e.startswith("Correct"), "%s: distractor explanation opens Correct" % w
        assert q.get("cite", "").startswith(SRC + ", Slide "), w
        for where, txt in [("stem", q["q"])] + [("option", o[0]) for o in q["opts"]] + [("explanation", o[1]) for o in q["opts"]]:
            bad = [a for a in _ACRO.findall(txt) if a not in _ACRO_OK]
            assert not bad, "%s: acronym %r in %s" % (w, bad, where)
        if "img" in q:
            assert os.path.exists(os.path.join(FOLDER, q["img"])), "%s: missing %s" % (w, q["img"])
            assert q.get("alt") and q.get("slide", "").startswith("Slide "), w
            key = q["opts"][0][0].lower()
            assert key not in q["alt"].lower(), "%s: alt text gives the answer away" % w


def score(sel):
    """Lower is better: gameable share over target, topic repeats, objective coverage, emphasis
    bounds, the strip quota, and the same strip twice in one set."""
    qs = [POOL[i] for i in sel]
    g = sum(gameable(q["opts"], 0) for q in qs) / len(qs)
    topics = Counter(q["topic"] for q in qs)
    rep = sum(v - 3 for v in topics.values() if v > 3)
    miss = N_IO - len({q["io"] for q in qs})
    short = 0
    for ts, lo, hi in GROUPS:
        k = sum(topics.get(t, 0) for t in ts)
        short += max(0, lo - k) + max(0, k - hi)
    imgs = [q["img"] for q in qs if "img" in q]
    quota = max(0, MIN_IMG - len(imgs)) + max(0, len(imgs) - MAX_IMG)
    dup = len(imgs) - len(set(imgs))
    return max(0.0, g - TARGET) * 100 + rep * 0.5 + miss * 5 + short * 3 + quota * 3 + dup * 4


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
    assert v < 1, "partition could not meet every constraint (score %.2f)" % v

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
        nimg = sum("img" in q for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  strips=%d  positions=%s  gameable=%.1f%%  topics=%d  objectives=%d"
              % (k, len(rot), nimg, {chr(65 + p): c for p, c in sorted(pos.items())}, frac * 100,
                 len({q["topic"] for q in rot}), len({q["io"] for q in rot})))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l14_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], 0) for q in POOL) / n
    print("pool %d (%d strips, raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum("img" in q for q in POOL), raw * 100, os.path.basename(out), len(held)))


if __name__ == "__main__":
    main()
