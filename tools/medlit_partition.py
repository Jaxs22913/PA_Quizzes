#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition an Interpretation of Medical Literature session pool into two 30s.

    python3 medlit_partition.py s1     # Session 1, Introduction, Bias and Validity

House format is 2x30 per topic. Anything above 60 in a pool is held back for a
cumulative exam rather than padded into the sets.

THIS COURSE DOES HAVE AN EXAM. The posted schedule lists no exam session, which
is easy to read as there being none, but the session 1 deck is explicit: a
computerised exam worth 40 percent of the grade, covering the assigned readings
and the lecture material. The remaining 60 percent is participation and the
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
 # Sessions 7-10 (added 2026-09-28)
 "s7risk": (["medlit_s7risk_pool:POOL"], "medlit_s7risk_sets.json"),
 "s7prog": (["medlit_s7prog_pool:POOL"], "medlit_s7prog_sets.json"),
 "s8prev": (["medlit_s8prev_pool:POOL"], "medlit_s8prev_sets.json"),
 "s8trials": (["medlit_s8trials_pool:POOL"], "medlit_s8trials_sets.json"),
 "s9stats": (["medlit_s9stats_pool:POOL"], "medlit_s9stats_sets.json"),
 "s10reviews": (["medlit_s10reviews_pool:POOL"], "medlit_s10reviews_sets.json"),
 # "Reading a Study" (added 2026-10-27): application items for syllabus units 12-13. Built by
 # main_apply() below, NOT main(): it ships the non-reserve items per skill TARGET, keeps numeric and
 # ordered option sets in their written order, and refuses a stem that repeats any other Med Lit pool.
 "s11apply": (["medlit_s11apply_pool:POOL"], "medlit_s11apply_sets.json"),
}
APPLY = {"s11apply"}
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


def _norm_stem(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def main_apply():
    """Application quiz: every pool item carries `skill`, `unit` and `reserve`; the pool module carries
    TARGET {skill: shipped count}. Items flagged numeric/fixed keep their written option order and key
    index (WRITER.md rule 8: ascending values are not shuffled); every other key is authored at 0 and
    rotated. Positions are balanced AROUND the fixed keys, so each set's A-D counts differ by at most 1.
    Skills are dealt alternately into the two sets (sorted by unit, so units spread too). A reserve item
    replaces a failed shipped item by swapping the two `reserve` flags, which leaves the pool order --
    and so every other item's set and position -- unchanged."""
    import random, glob
    sys.path.insert(0, HERE)
    from _option_order import ordered_kind, option_values
    pm = __import__(mods[0].split(":")[0])
    target = pm.TARGET
    order = list(pm.TOPIC)
    rng = random.Random(SEED)

    # 1. item guards (the same as check(), with the key-first rule relaxed for fixed option orders)
    seen = set()
    for i, q in enumerate(POOL):
        w = "pool[%d]" % i
        fixed = q.get("numeric") or q.get("fixed")
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert q["skill"] in target and isinstance(q["unit"], int), "%s: skill/unit" % w
        assert "?" in q["q"], "%s: stem asks nothing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert _norm_stem(q["q"]) not in seen, "%s: duplicate stem" % w
        seen.add(_norm_stem(q["q"]))
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        assert set(q.get("mis", {})) == {o[0] for k, o in enumerate(q["opts"]) if k != q["c"]}, \
            "%s: mis must name every distractor" % w
        kind = ordered_kind([o[0] for o in q["opts"]])
        if kind:
            assert q.get("numeric"), "%s: numeric options would be rotated; write them ascending, numeric=True" % w
            v = option_values([o[0] for o in q["opts"]])
            assert v == sorted(v), "%s: numeric options not ascending" % w
        if not fixed:
            assert q["c"] == 0, "%s: key must be authored first" % w
        assert q["opts"][q["c"]][1].startswith("Correct"), "%s: key explanation must open with Correct" % w
        for k, (t, e) in enumerate(q["opts"]):
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            if k != q["c"]:
                assert not e.startswith("Correct"), "%s: distractor explanation opens with Correct" % w

    # 2. no stem may repeat another Med Lit pool (the masters generator breaks on duplicates)
    others = set()
    for f in sorted(glob.glob(os.path.join(HERE, "medlit_*_pool*.py"))):
        m = os.path.basename(f)[:-3]
        if m == mods[0].split(":")[0]:
            continue
        mod = __import__(m)
        for attr in ("POOL", "POOL_A", "POOL_B"):
            for q in getattr(mod, attr, []):
                others.add(_norm_stem(q["q"]))
    clash = [q["q"][:70] for q in POOL if _norm_stem(q["q"]) in others]
    assert not clash, "stem repeats another Med Lit pool: %r" % clash

    # 3. shipped items per skill, dealt alternately into the two sets
    ship = [q for q in POOL if not q.get("reserve")]
    got = Counter(q["skill"] for q in ship)
    assert got == Counter(target), "shipped per skill %r != TARGET %r" % (dict(got), target)
    # Each skill is split as evenly as possible (an odd count gives its extra item to alternate sets, so
    # the sets come out 30/30); within a skill, items go rarest unit first to whichever set holds fewer
    # items of that unit, so a unit with two or more shipped items reaches both sets.
    parts, start = ([], []), 0
    ucount = Counter(q["unit"] for q in ship)
    for sk in order:
        items = sorted((q for q in ship if q["skill"] == sk),
                       key=lambda q: (ucount[q["unit"]], q["unit"], POOL.index(q)))
        quota = [len(items) // 2, len(items) // 2]
        if len(items) % 2:
            quota[start] += 1
            start = 1 - start
        for q in items:
            have = [sum(1 for x in parts[s] if x["unit"] == q["unit"]) for s in (0, 1)]
            pick = 0 if (have[0], len(parts[0])) <= (have[1], len(parts[1])) else 1
            if quota[pick] == 0:
                pick = 1 - pick
            quota[pick] -= 1
            parts[pick].append(q)
    sets = {}
    for n, qs in ((1, parts[0]), (2, parts[1])):
        assert len(qs) == PER_SET, "set%d has %d questions" % (n, len(qs))
        qs = list(qs)
        rng.shuffle(qs)
        fixed_pos = Counter(q["c"] for q in qs if q.get("numeric") or q.get("fixed"))
        base, extra = divmod(len(qs), NOPT)
        ranked = sorted(range(NOPT), key=lambda k: (-fixed_pos[k], rng.random()))
        want = {k: base + (1 if k in ranked[:extra] else 0) for k in range(NOPT)}
        assert all(want[k] >= fixed_pos[k] for k in range(NOPT)), "set%d: fixed keys crowd one position" % n
        free = [k for k in range(NOPT) for _ in range(want[k] - fixed_pos[k])]
        rng.shuffle(free)
        rot = []
        for q in qs:
            r = {k: v for k, v in q.items() if k not in ("reserve", "numeric", "fixed")}
            if not (q.get("numeric") or q.get("fixed")):
                o = list(q["opts"]); key = o.pop(0); p = free.pop(); o.insert(p, key)
                r["opts"] = o; r["c"] = p
            rot.append(r)
        pos = Counter(q["c"] for q in rot)
        assert max(pos.values()) - min(pos.values()) <= 1, "set%d: uneven positions %r" % (n, pos)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: key longest in %.0f%%" % (n, frac * 100)
        sets["set%d" % n] = rot
        print("set%d  %d questions  positions=%s  key-is-longest=%.0f%%  skills=%s  units=%s"
              % (n, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100,
                 dict(Counter(q["skill"] for q in rot)), dict(sorted(Counter(q["unit"] for q in rot).items()))))
    json.dump(sets, open(os.path.join(HERE, OUT), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", OUT, "(%d reserve held back)" % (len(POOL) - len(ship)))


if __name__ == "__main__":
    main_apply() if WHICH in APPLY else main()
