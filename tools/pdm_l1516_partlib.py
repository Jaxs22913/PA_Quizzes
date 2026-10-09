#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared partition logic for PDM I Exam 3, Lectures 15 and 16 (tools/pdm_l15_partition.py and
tools/pdm_l16_partition.py call it with their own pool, groups and output file).

Copied in shape from tools/pdm_l10_partition.py (seeded swap-based local search, keys rotated with
positions balanced per set), with three things added for the strip-heavy Exam 3 build:

  IMAGES   a picture appears at most ONCE per set (two questions on the same tracing in one quiz
           would let the first answer the second), and each set must carry at least MIN_IMG
           picture questions ("strips heavy", Jaxon 2026-10-08).
  NUMBERS  a stem value needs the scale that reads it (Reynolds' rule, also this class's spec:
           "you'll always have normal ranges"). Lead names (V1, V4R), "12-lead", ages and symptom
           durations are not values.
  ACRONYMS no abbreviation outside the wave and lead nomenclature (QRS, ST, PR, QT, QTc, TP, QS,
           S1Q3T3, aVR/aVL/aVF, V1-V9, V4R). The `io` field is the syllabus objective VERBATIM and
           keeps its "ECG"/"BER"/"COPD", so it is not checked.
"""
import json, os, random, re
from collections import Counter

NOPT, BAR, TARGET, PER_SET = 4, 0.35, 0.10, 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slides?|deck|professor|this course|in class|syllabus|lecturer)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_NOTVAL = re.compile(r"\bV\d+R?\b|\b1[25]-lead\b|\b\d+ (?:minutes|hours|days)\b|\bS1Q3T3\b")
_SCALE = re.compile(r"(?i)\bnormal\b|\brange\b|\breference\b|\blimit\b|\bthreshold\b|\bbelow\b|\babove\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute(?!d tomography)|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"QRS", "ST", "PR", "QT", "QTc", "TP", "QS", "NOT", "II", "III", "IV", "ALWAYS", "FRONT",
            "AFTER", "BEFORE", "UPSTROKE", "END", "LATERAL", "INFERIOR", "POSTERIOR", "DEPRESSION",
            "ELEVATION", "CLEAR", "SUBENDOCARDIAL", "ONLY", "ISOLATED", "WAS", "IS", "NO", "BOTH",
            "SHORT", "LONG", "WIDE", "NARROW", "UP", "DOWN", "DOES", "ARE", "LOW", "HIGH", "ONE",
            "AND", "OR", "PR", "FOUR", "TWO", "THREE"}


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def check(pool, src):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %s" % (i, q["q"][:60])
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert q["c"] == 0, "%s: key must be authored first" % w
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        bare = _NOTVAL.sub("", _AGE.sub("", q["q"]))
        if re.search(r"\d", bare):
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
        assert q.get("cite", "").startswith(src + ", Slide "), w
        if q.get("img"):
            assert q.get("alt") and q.get("slide"), "%s: picture without alt/slide" % w
        for where, txt in [("stem", q["q"])] + [("option", o[0]) for o in q["opts"]] + \
                          [("explanation", o[1]) for o in q["opts"]] + [("alt", q.get("alt", ""))]:
            bad = [a for a in _ACRO.findall(txt) if a not in _ACRO_OK and not re.fullmatch(r"[IVX]+", a)]
            assert not bad, "%s: acronym %r in %s" % (w, bad, where)


def _norm(t):
    t = t.lower(); t = re.sub(r"\([^)]*\)", "", t); t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\b(a|an|the|of|in|and|or|to|is|are|it|its)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def leak_pairs(pool, conflicts=()):
    """(i, j) pairs that must not share a set: question i's KEY text appears in question j's stem
    (the stem hands over the answer), plus the hand-listed semantic conflicts: each conflict is
    (stem substrings A, stem substrings B) and every A-question conflicts with every B-question."""
    bad = set()
    keys = [_norm(q["opts"][0][0]) for q in pool]
    stems = [_norm(q["q"]) for q in pool]
    for i, k in enumerate(keys):
        if len(k) < 6:
            continue
        for j, st in enumerate(stems):
            if i != j and re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", st):
                bad.add(frozenset((i, j)))
    for A, B in conflicts:
        ia = [i for i, q in enumerate(pool) if any(x in q["q"] for x in A)]
        ib = [i for i, q in enumerate(pool) if any(x in q["q"] for x in B)]
        assert ia and ib, "conflict matched nothing: %r / %r" % (A[:1], B[:1])
        for i in ia:
            for j in ib:
                if i != j:
                    bad.add(frozenset((i, j)))
    return bad


def run(pool, groups, n_io, out, seed, min_img, src, conflicts=()):
    check(pool, src)
    n = len(pool)
    LEAK = leak_pairs(pool, conflicts)
    partner = {}
    for pr in LEAK:
        a, b = tuple(pr)
        partner.setdefault(a, set()).add(b); partner.setdefault(b, set()).add(a)
    assert n >= PER_SET * 2, "pool of %d cannot fill two sets of %d" % (n, PER_SET)
    rng = random.Random(seed)

    def score(sel):
        qs = [pool[i] for i in sel]
        g = sum(gameable(q["opts"], 0) for q in qs) / len(qs)
        # the key being merely the LONGEST (any margin) is a softer cue; keep it near chance
        lg = sum(len(q["opts"][0][0]) > max(len(o[0]) for o in q["opts"][1:]) for q in qs) / len(qs)
        topics = Counter(q["topic"] for q in qs)
        miss = n_io - len({q["io"] for q in qs})
        imgs = Counter(q["img"] for q in qs if q.get("img"))
        dup_img = sum(v - 1 for v in imgs.values())
        few_img = max(0, min_img - sum(imgs.values()))
        short = 0
        for ts, lo, hi in groups:
            k = sum(topics.get(t, 0) for t in ts)
            short += max(0, lo - k) + max(0, k - hi)
        stems = Counter(q.get("twin") for q in qs if q.get("twin"))
        twins = sum(v - 1 for v in stems.values())
        ss = set(sel)
        leaks = sum(len(partner.get(i, set()) & ss) for i in sel) / 2
        return (max(0.0, g - TARGET) * 100 + max(0.0, lg - 0.30) * 40 + miss * 5 + short * 3 + dup_img * 20 + few_img * 4
                + twins * 15 + leaks * 15)

    # Simulated annealing with restarts (the plain greedy swap search stalls once twin, leak and
    # picture constraints interact). Seeded, so a rerun reproduces the same selection.
    import math
    gbest = None
    for restart in range(8):
        idx = list(range(n)); rng.shuffle(idx)
        sel = idx[:PER_SET * 2]; rest = idx[PER_SET * 2:]
        v = score(sel[:PER_SET]) + score(sel[PER_SET:])
        best_local = (v, sel[:])
        steps = 40000
        for it in range(steps):
            T = 4.0 * (1 - it / steps) + 0.01
            a = rng.randrange(PER_SET * 2)
            if rest and rng.random() < 0.5:
                b = rng.randrange(len(rest))
                new = sel[:]; new[a], nr = rest[b], sel[a]
            else:
                b = rng.randrange(PER_SET * 2); nr = None
                new = sel[:]; new[a], new[b] = new[b], new[a]
            nv = score(new[:PER_SET]) + score(new[PER_SET:])
            if nv <= v or rng.random() < math.exp(-(nv - v) / T):
                sel, v = new, nv
                if nr is not None:
                    rest[b] = nr
                if v < best_local[0]:
                    best_local = (v, sel[:])
        if gbest is None or best_local[0] < gbest[0]:
            gbest = best_local
    v, sel = gbest
    print("search score %.2f (0 = every soft target met)" % v)

    sets = {}
    for k, part in ((1, sel[:PER_SET]), (2, sel[PER_SET:])):
        qs = [pool[i] for i in part]
        imgs = Counter(q["img"] for q in qs if q.get("img"))
        assert all(x == 1 for x in imgs.values()), "set%d repeats a picture: %r" % (k, imgs)
        tw = Counter(pool[i].get("twin") for i in part if pool[i].get("twin"))
        assert all(x == 1 for x in tw.values()), "set%d keeps twins: %r" % (k, {a: b for a, b in tw.items() if b > 1})
        hit = [pr for pr in LEAK if pr <= set(part)]
        assert not hit, "set%d keeps %d leaking pair(s), e.g. %r" % (k, len(hit), [pool[i]["q"][:50] for i in hit[0]])
        assert sum(imgs.values()) >= min_img, "set%d has only %d picture questions" % (k, sum(imgs.values()))
        order = ([0, 1, 2, 3] * ((len(qs) // NOPT) + 1))[:len(qs)]
        rng.shuffle(order)
        rot = []
        for q, want in zip(qs, order):
            o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
            r = {kk: vv for kk, vv in q.items() if kk not in ("slot", "twin")}
            r["opts"] = o; r["c"] = want
            rot.append(r)
        pos = Counter(q["c"] for q in rot)
        assert max(pos.values()) - min(pos.values()) <= 1, "set%d: uneven positions %r" % (k, pos)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        longest = sum(len(q["opts"][q["c"]][0]) > max(len(o[0]) for j, o in enumerate(q["opts"]) if j != q["c"])
                      for q in rot) / len(rot)
        assert frac <= BAR, "set%d: gameable %.0f%%" % (k, frac * 100)
        topics = Counter(q["topic"] for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  pictures=%d  positions=%s  gameable=%.1f%%  key-longest=%.0f%%  objectives=%d/%d"
              % (k, len(rot), sum(imgs.values()), {chr(65 + p): c for p, c in sorted(pos.items())},
                 frac * 100, longest * 100, len({q["io"] for q in rot}), n_io))
        for ts, lo, hi in groups:
            got = sum(topics.get(t, 0) for t in ts)
            flag = "" if lo <= got <= hi else "   <-- outside %d-%d" % (lo, hi)
            print("      %-58s %2d%s" % (" / ".join(sorted(ts))[:58], got, flag))
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], 0) for q in pool) / n
    held = n - PER_SET * 2
    print("pool %d (raw gameable %.1f%%, %d picture questions)  wrote %s  (%d held back for the master exams)"
          % (n, raw * 100, sum(1 for q in pool if q.get("img")), os.path.basename(out), held))
