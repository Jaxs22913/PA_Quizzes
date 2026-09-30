#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 10 (Coagulation and Hemostasis Testing) pool into two 30s.

House format is 2x30 for the lecture (the L7-L9 pattern: one topic per lecture). The pool is larger
than 60 so the remainder is held back for the cumulative master exams, which cover Lectures 7-10
and Lab 2.

REYNOLDS' RULES, asserted rather than trusted:
  1. A laboratory value never appears in a stem without the scale that reads it (a reference
     range, a goal, a named tier, or above/below).
  2. Nothing is calculated. Her no-math rule is PER QUANTITY, but this deck contains no worked
     calculation at all (no INR formula, no ratio), so ANY "calculate" in a stem fails the build.
  3. No acronym appears outside the roman-numeral factor names; write the full term.

EMPHASIS HOOKS (filled from the 30 September recording, never from off-deck content):
  GROUPS       topic groups with per-set minimum/maximum counts taken from the minutes each was
               spoken in; the local search is penalized for missing either bound.
  BAN_STEMS    substrings of stems the lecturer said are NOT examined; any pool question whose stem
               contains one is dropped before selection.

Selection is swap-based local search, as on the L5/L9 builds. The target is under 10% gameable
per set (Jaxon, 2026-08-16); 35% is only the failure bar.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l10_pool_a import POOL_A
from pdm_l10_pool_b import POOL_B
from pdm_l10_pool_c import POOL_C

# EMPHASIS WEIGHTS, measured as distinct MINUTES each subject was spoken in (whisper part 1 +
# part 2; 84 minutes of speech, words matched with \b boundaries): platelets 38, PT/INR 24,
# PTT 20, D-dimer 9, DIC 9, platelet count tiers 7, von Willebrand 6, bleeding time 6,
# fibrinogen 5, mixing studies 1. Each group below is (topics, minimum per set, maximum per set).
GROUPS = [
  ({"Platelet abnormalities", "Platelet count", "Bleeding time", "von Willebrand studies"}, 10, 13),
  ({"Prothrombin time", "International normalized ratio", "Activated partial thromboplastin time", "Thrombin time"}, 6, 9),
  ({"D-dimer"}, 3, 5),
  ({"Disseminated intravascular coagulation", "Pattern recognition"}, 3, 6),
  ({"Mixing study"}, 0, 2),
]
BAN_STEMS = []       # substrings of de-emphasized stems
POOL = [q for q in POOL_A + POOL_B + POOL_C if not any(b in q['q'] for b in BAN_STEMS)]
SEED, NOPT, BAR, TARGET, PER_SET = 20260930, 4, 0.35, 0.10, 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slides?|deck|professor|this course|in class|syllabus)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_SCALE = re.compile(r"(?i)\bnormal\b|\brange\b|\breference\b|\bdesirable\b|\blimit\b|\bgoal\b|\bbelow\b|\babove\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute(?!d tomography)|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ROMAN = {"II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII", "XIII"}
_ACRO_OK = {"NOT"}


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
        assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        if re.search(r"\d", _AGE.sub("", q["q"])):
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
        assert q.get("cite", "").startswith("Coagulation Studies 2026.pptx, Slide "), w
        for where, txt in [("stem", q["q"])] + [("option", o[0]) for o in q["opts"]] + [("explanation", o[1]) for o in q["opts"]]:
            bad = [a for a in _ACRO.findall(txt) if not re.fullmatch(r"[IVX]+[ab]?", a) and a not in _ACRO_OK]
            assert not bad, "%s: acronym %r in %s" % (w, bad, where)


def score(sel):
    """Lower is better: gameable share over target, topic repeats, IO balance."""
    qs = [POOL[i] for i in sel]
    g = sum(gameable(q["opts"], 0) for q in qs) / len(qs)
    topics = Counter(q["topic"] for q in qs)
    rep = sum(v - 1 for v in topics.values() if v > 2)
    ios = Counter(q["io"] for q in qs)
    miss = 6 - len(ios)
    short = 0
    for ts, lo, hi in GROUPS:
        k = sum(topics.get(t, 0) for t in ts)
        short += max(0, lo - k) + max(0, k - hi)
    return max(0.0, g - TARGET) * 100 + rep * 0.5 + miss * 5 + short * 3


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
    out = os.path.join(HERE, "pdm_l10_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], 0) for q in POOL) / n
    print("pool %d (raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, raw * 100, os.path.basename(out), len(held)))


if __name__ == "__main__":
    main()
