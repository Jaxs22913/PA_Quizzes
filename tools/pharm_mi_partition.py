#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the two Pharmacology Exam 2 myocardial ischemia pools (Lecture 8).

Same guards as pharm_lipid_partition.py (the site course-citation detector, the dose guard that lets a lab or
vital-sign threshold through, the stratified-by-topic split, the answer-position rotation and the length guard),
restated for this lecture:

  1. NO DOSES. Dr. Wood does not test them. The aspirin chew dose, the nitroglycerin ointment inches and the
     tablet strengths are refused anywhere in a stem or an option. Timings and durations are allowed.
  2. A DESCOPED guard for slide claims a question must not be built on (the deck and the truth disagree, or the
     figure is a trial statistic): reteplase/tenecteplase "affinity for fibrin" (true only of tenecteplase),
     urokinase as an antigenic agent, the factor list plasmin lyses, the 75-year cut-off, the 10-day / 3-month /
     110 mmHg fibrinolytic contraindication figures, and the quoted risk-reduction percentages.
  3. The nitroglycerin five-minute instruction is a protocol to ACT on: a key may never BE the number of minutes.
  4. Dr. McInnis's weighting: per set, mechanism plus physiology items may not outnumber indications + education +
     adverse effects + contraindications + drug choice combined.

    antianginals    split in half (stable angina: beta blockers, calcium channel blockers, nitrates, add-ons)
    acs             split in half (acute coronary syndrome, thrombus formation, antiplatelets, fibrinolytics)

Each pool is split in half rather than padded to the house 30, as in the ENT, hypertension and lipid builds: the
pool is as large as the slides support. The length guard FAILS a set over 35 percent gameable (the house bar) and
WARNS over 10 percent (Jaxon's own target, 2026-08-16).

    python3 tools/pharm_mi_partition.py [--only anginal|acs]
"""
import importlib, json, os, random, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _selfcontain_rx import RX
from _lecturers import citation_hits

SEED, NOPT, BAR, TARGET = 20260930, 4, 0.35, 0.10
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|dr\.|this course|in class)\b")
DOSE = re.compile(r"(?i)\b\d+\s*(mg|milligram|microgram|mcg|units?)\b(?!\s*/\s*(dl|g)\b)"
                  r"|\b\d+\s*%\s*(solution|ointment|suspension|saline)\b")
DESCOPED = re.compile(r"(?i)affinity for fibrin|fibrin affinity|\burokinase\b|\bfactors? II, V|\b75 years\b"
                      r"|\b(10|ten) days\b|\b3 months\b|\b110 ?mm|\b325\b|\binch(es)?\b"
                      r"|\b(13|30|40) ?(%|percent)")
BAD_KEY = re.compile(r"(?i)\b(five|5)\s*minutes?\b|\bevery 5\b")
BREADTH = ("indication", "education", "adverse effect", "contraindication", "drug choice")
BACKGROUND = ("mechanism", "physiology")
SLOTS = set(BREADTH) | set(BACKGROUND) | {"class", "interaction", "monitoring", "protocol"}
CITE_RX = re.compile(r"^(Myocardial Ischemia Drugs|Antihypertensives|Lipids)\.pptx, Slide \d+$")   # cross-lecture facts (the CYP3A4 interactions) cite the deck that states them


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
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    rng = random.Random(SEED)
    sets = {}
    path = os.path.join(HERE, "pharm_mi_sets.json")
    if only and os.path.exists(path):
        sets = json.load(open(path, encoding="utf-8"))
    for label, modname in (("anginal", "pharm_mi_pool_anginal"), ("acs", "pharm_mi_pool_acs")):
        if only and only != label:
            continue
        pool = importlib.import_module(modname).QUESTIONS
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
            back = sum(q["slot"] in BACKGROUND for q in rot)
            broad = sum(q["slot"] in BREADTH for q in rot)
            assert back <= broad, "%s%d: mechanism+physiology %d outweighs breadth %d" % (label, n, back, broad)
            sets["%s%d" % (label, n)] = rot
            print("%-8s %2d questions  positions=%s  gameable=%.0f%%%s  mechanism+physiology=%d breadth=%d topics=%d"
                  % (label + str(n), len(rot),
                     {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100,
                     "  (over the 10%% target)" if frac > TARGET else "",
                     back, broad, len({q["topic"] for q in rot})))
    json.dump(sets, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(path))


if __name__ == "__main__":
    main()
