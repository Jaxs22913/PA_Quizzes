#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split the Pharmacology Exam 2 myocardial ischemia VIGNETTE pool into two sets, and guard it.

Every guard is IMPORTED from pharm_mi_partition (check, split, rotate, gameable and the constants),
not restated, so the vignette pair is held to exactly the standard of the topic quizzes: four options,
key authored first, stem ends with a question mark, no course citations, no doses, nothing built on a
descoped slide claim, explanations of at least 60 characters, and mechanism + physiology never
outnumbering the breadth slots. This script adds the vignette-specific checks (a patient in every
stem, no patient names, one lead-in) and writes tools/pharm_mi_vignette_sets.json (keys set1, set2).
It never touches pharm_mi_sets.json.

    python3 tools/pharm_mi_vignette_partition.py
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_mi_partition import (check, split, rotate, gameable, BAR, TARGET, BREADTH, BACKGROUND,
                                NOPT, SEED)
from pharm_mi_vignette_pool import POOL

PATIENT = re.compile(r"\bA (\d{1,2}-year-old|newborn|toddler)\b")
ABBREV = re.compile(r"\b(BB|CCB|DHP|NDHP|PCI|CABG|ACEI|PDE|MI|EMS|tPA|rPA|TNK|STK|UA|NSTE|NSTEMI|STEMI|LV|HF|IHD|CHD|"
                    r"ECG|EKG|BP|HR|AV|SL|NTG|ACS|DM|CAD)\b")
LEADS = ("first-line treatment", "drug choice", "next step", "avoid", "adverse effect", "education",
         "interaction", "monitoring", "diagnosis", "mechanism", "benefit")
SEED_V = SEED + 8  # own stream, so this script never disturbs the topic-quiz selection


def guard_vignettes(pool):
    for i, q in enumerate(pool):
        w = "pool[%d]" % i
        assert PATIENT.match(q["q"]), "%s: stem does not open with a patient" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert q["lead"] in LEADS, "%s: unknown lead-in %r" % (w, q["lead"])
        blob = q["q"] + " " + " ".join(t for o in q["opts"] for t in o)
        assert not ABBREV.search(blob), "%s: abbreviation %r" % (w, ABBREV.search(blob).group(0))
        assert not re.search(r"(?i)\b(mr|mrs|ms)\.", blob), "%s: patient named" % w


def main():
    check(POOL, "vignette")
    guard_vignettes(POOL)
    # Choose, from a fixed list of seeds, the split whose two halves carry the most even spread of
    # lead-ins (so neither set is all "avoid" and no "diagnosis"), then the lowest length bias.
    def attempt(offset):
        rng = random.Random(SEED_V + offset)
        a, b = split(POOL, rng)
        ra, rb = rotate(a, rng), rotate(b, rng)
        la, lb = Counter(q["lead"] for q in ra), Counter(q["lead"] for q in rb)
        imbalance = sum(abs(la[k] - lb[k]) for k in LEADS)
        game = sum(gameable(q["opts"], q["c"]) for q in ra + rb)
        return imbalance + 2 * game, ra, rb

    best = min((attempt(o) for o in range(400)), key=lambda t: t[0])
    out = {}
    for n, rot in ((1, best[1]), (2, best[2])):
        pos = Counter(q["c"] for q in rot)
        assert len(pos) == NOPT and max(pos.values()) - min(pos.values()) <= 1, \
            "set%d: uneven positions %r" % (n, dict(pos))
        for q in rot:
            assert q["opts"][q["c"]][1].startswith("Correct")
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: key longest in %.0f%%" % (n, frac * 100)
        back = sum(q["slot"] in BACKGROUND for q in rot)
        broad = sum(q["slot"] in BREADTH for q in rot)
        assert back <= broad, "set%d: mechanism+physiology %d outweighs breadth %d" % (n, back, broad)
        leads = Counter(q["lead"] for q in rot)
        print("set%d  %2d questions  positions=%s  gameable=%.0f%%%s  mech+phys=%d breadth=%d topics=%d"
              % (n, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100,
                 "  (over the 10%% target)" if frac > TARGET else "", back, broad,
                 len({q["topic"] for q in rot})))
        print("       lead-ins:", dict(sorted(leads.items())))
        print("       topics  :", dict(Counter(q["topic"] for q in rot)))
        out["set%d" % n] = [{k: v for k, v in q.items() if k != "lead"} for q in rot]
    both = Counter(q["lead"] for q in POOL)
    print("pool   %d questions  lead-ins:" % len(POOL), dict(sorted(both.items())))
    print("       slots   :", dict(sorted(Counter(q["slot"] for q in POOL).items())))
    path = os.path.join(HERE, "pharm_mi_vignette_sets.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(path))
    from pharm_mi_course_extend import extend_vignettes     # course-keyed vignettes are appended, never split
    extend_vignettes()


if __name__ == "__main__":
    main()
