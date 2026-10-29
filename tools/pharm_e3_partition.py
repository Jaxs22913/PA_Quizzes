#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Pharmacology Exam 3 topic pools (Lectures 9, 10 and 11).

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

WRITER RULES (tools/question_writing/WRITER.md v1, 2026-10-15) apply to the pools written after that date (WRITER_RULES
below; Lecture 10 onward): every distractor carries its misconception as a THIRD element of the option,
[text, explanation, "<category from MIS>"], kept in the sets JSON (blind_review.py reads it) and stripped from the
pages by render_pharm_e3.py; numeric option sets (tools/_option_order.py) are shown ASCENDING and not shuffled, the
key sitting where its value falls, and the other questions' positions are balanced around them. Lecture 9 pools are
untouched by this (their sets are never re-partitioned).

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
CITE_RX = re.compile(r"^(Diuretics and Heart Failure Drugs|Antiarrhythmics|Pulmonology-2|Antihypertensives|Myocardial Ischemia Drugs|Ophthalmology-2)\.pptx, (Slide \d+|Slides \d+(, \d+)+)$")   # a cross-lecture fact cites the deck that states it; "Slides 89, 71" when the deciding fact spans slides (primary first)


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
        for k, o in enumerate(q["opts"]):
            t, e = o[0], o[1]
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            assert e.startswith("Correct") == (k == 0), "%s: 'Correct' marks the wrong option" % w
            if len(o) > 2:
                assert k > 0 and o[2] in MIS, "%s: misconception tag %r (key carries none; distractors one of MIS)" % (w, o[2])
            assert len(o) <= 3, "%s: option has %d fields" % (w, len(o))
        assert CITE_RX.match(q["cite"]), "%s: cite %r" % (w, q["cite"])


MIS = ("competing diagnosis", "wrong stage or severity", "ruled out by a stated finding",
       "confused mechanism or drug class", "adjacent fact", "reversed direction or value", "common lay belief")
WRITER_RULES = {"aa1a", "aa1bc", "aa24", "aa3", "aamisc"}      # Lecture 10 pools (WRITER.md v1)
WRITER_RULES |= {"pucap", "puhap", "putb", "puana", "pubd", "puctl", "puinh", "pucopd"}   # Lecture 11 pools
_ABSOL = re.compile(r"\b(always|never|only|all|none)\b", re.I)


def writer_check(pool, label):
    """WRITER.md v1 extras: every distractor tagged, no absolute word only in distractors."""
    for i, q in enumerate(pool):
        w = "%s[%d]" % (label, i)
        assert all(len(o) == 3 for o in q["opts"][1:]), "%s: every distractor needs a misconception tag" % w
        assert len(q["opts"][0]) == 2, "%s: the key carries no misconception tag" % w
        key_abs = bool(_ABSOL.search(q["opts"][0][0]))
        for o in q["opts"][1:]:
            assert key_abs or not _ABSOL.search(o[0]), "%s: absolute word only in a distractor: %r" % (w, o[0])


def rotate_balanced(qs, rng):
    """Like rotate(), but numeric option sets are sorted ascending (tools/_option_order.py) and keep the key where
    its value falls; the remaining questions are placed so the four positions stay within one of each other."""
    from _option_order import order_options, option_values
    fixed = {}
    for n, q in enumerate(qs):
        if option_values([o[0] for o in q["opts"]]) is not None:
            fixed[n] = order_options(q)
    want = [len(qs) // NOPT + (1 if k < len(qs) % NOPT else 0) for k in range(NOPT)]
    rng.shuffle(want)
    for q in fixed.values():
        want[q["c"]] -= 1
    free = [k for k in range(NOPT) for _ in range(max(0, want[k]))]
    while len(free) < len(qs) - len(fixed):
        free.append(min(range(NOPT), key=lambda k: want[k] + free.count(k)))
    rng.shuffle(free)
    it = iter(free)
    out = []
    for n, q in enumerate(qs):
        if n in fixed:
            out.append(fixed[n]); continue
        tgt = next(it)
        o = list(q["opts"]); key = o.pop(0); o.insert(tgt, key)
        r = dict(q); r["opts"] = o; r["c"] = tgt
        out.append(r)
    return out


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
        if key in WRITER_RULES:
            writer_check(pool, key)
        a, b = split(pool, rng)
        sets = {}
        for n, part in ((1, a), (2, b)):
            rot = rotate_balanced(part, rng) if key in WRITER_RULES else rotate(part, rng)
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
