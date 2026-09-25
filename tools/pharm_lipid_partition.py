#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the three Pharmacology Exam 2 lipid pools (Lecture 7).

Same guards as pharm_htn_partition.py (itself copied from
pharm_ent_partition.py); the four additions, restated for this lecture:

  1. The course-citation guard is the SITE detector (_selfcontain_rx.RX plus
     _lecturers' hard hits), not a private regex -- the private one in the ENT
     partition cannot see "Professor <Name>" and the pool checker was widened for
     exactly that on 2026-09-22.
  2. The dose guard lets a LAB VALUE through. "Triglycerides above 400 mg/dL"
     and "an albumin-to-creatinine ratio of 450 mg/g" are thresholds a question
     must be able to state; "10 mg" is a dose and is still refused.
  3. A DESCOPED guard for the caps said aloud and the deck's own conflict: no
     item may state the 7.5 percent risk threshold (slide 65 and the slide 66
     algorithm disagree, so no key may depend on it), ask for a 10-year risk
     CALCULATION, name orlistat (never on a slide), key ezetimibe to NPC1L1
     (the deck never links them), or reach past the CYP row of the statin
     pharmacokinetic table (prodrug status, bioavailability, protein binding).
     "Category X" is audio-only; the slides say "pregnancy".
  4. The split is STRATIFIED by topic rather than a plain shuffle, so both
     versions of a quiz cover every sub-topic of the pool, and each set is
     checked against Dr. McInnis's weighting: mechanism items may not outnumber
     indications + education + adverse effects + contraindications + drug
     choice combined.

    statins and statin guidelines           31 -> 16 + 15
    resins, ezetimibe, PCSK9 inhibitors     29 -> 15 + 14
    fibrates, niacin, lipid profiles        28 -> 2 x 14

Each pool is split in half rather than padded to the house 30, as in the ENT
and ophthalmology builds: the pool is as large as the slides support.

The length guard FAILS a set over 35 percent gameable (the house bar) and
WARNS over 10 percent (Jaxon's own target, 2026-08-16).
"""
import json, os, random, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _selfcontain_rx import RX
from _lecturers import citation_hits
from pharm_lipid_pool_statin import QUESTIONS as STATIN
from pharm_lipid_pool_ldl import QUESTIONS as LDL
from pharm_lipid_pool_tg import QUESTIONS as TG

SEED, NOPT, BAR, TARGET = 20260924, 4, 0.35, 0.10
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|dr\.|this course|in class)\b")
DOSE = re.compile(r"(?i)\b\d+\s*(mg|milligram|microgram|units?)\b(?!\s*/\s*(dl|g)\b)"
                  r"|\b\d+\s*%\s*(solution|ointment|suspension|saline)\b")
DESCOPED = re.compile(r"(?i)7\.5\s*%|\bcalculat|\borlistat\b|NPC1L1|\bprodrug|bioavailab"
                      r"|\bprotein[- ]binding|category x")
BAD_KEY = re.compile(r"(?i)NPC1L1|very liver toxic|not recommended together")
BREADTH = ("indication", "education", "adverse effect", "contraindication", "drug choice")


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
        for s in [q["q"]] + [t for o in q["opts"] for t in o]:
            assert not CITES.search(s) and not hard_cites(s), "%s: cites the course: %r" % (w, s[:70])
        assert not DOSE.search(q["q"]), "%s: stem tests a dose" % w
        assert not DOSE.search(" ".join(o[0] for o in q["opts"])), "%s: option is a dose" % w
        assert not DESCOPED.search(q["q"] + " " + q["opts"][0][0]), "%s: descoped topic" % w
        assert not BAD_KEY.search(q["opts"][0][0]), "%s: key states an audio-only overstatement" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        texts = [o[0] for o in q["opts"]]
        assert len(set(texts)) == NOPT, "%s: duplicate option text" % w
        for k, (t, e) in enumerate(q["opts"]):
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            assert e.startswith("Correct") == (k == 0), "%s: 'Correct' marks the wrong option" % w
        assert re.match(r"^Lipids\.pptx, Slide \d+$", q["cite"]), "%s: cite %r" % (w, q["cite"])


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
    rng = random.Random(SEED)
    sets = {}
    for label, pool in (("statin", STATIN), ("ldl", LDL), ("tg", TG)):
        check(pool, label)
        a, b = split(pool, rng)
        for n, part in ((1, a), (2, b)):
            rot = rotate(part, rng)
            pos = {}
            for q in rot:
                pos[q["c"]] = pos.get(q["c"], 0) + 1
            assert len(pos) == NOPT and max(pos.values()) - min(pos.values()) <= 1, \
                "%s%d: uneven positions %r" % (label, n, pos)
            frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
            assert frac <= BAR, "%s%d: key longest in %.0f%%" % (label, n, frac * 100)
            mech = sum(q["slot"] == "mechanism" for q in rot)
            broad = sum(q["slot"] in BREADTH for q in rot)
            assert mech <= broad, "%s%d: mechanism %d outweighs breadth %d" % (label, n, mech, broad)
            sets["%s%d" % (label, n)] = rot
            print("%-8s %2d questions  positions=%s  gameable=%.0f%%%s  mechanism=%d breadth=%d topics=%d"
                  % (label + str(n), len(rot),
                     {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100,
                     "  (over the 10%% target)" if frac > TARGET else "",
                     mech, broad, len({q["topic"] for q in rot})))
    out = os.path.join(HERE, "pharm_lipid_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(out))


if __name__ == "__main__":
    main()
