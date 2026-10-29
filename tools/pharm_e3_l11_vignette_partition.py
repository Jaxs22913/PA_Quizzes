#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split the Pharmacology Exam 3 PULMONARY vignette pool (Lecture 11: pulmonary infections, asthma and chronic
obstructive pulmonary disease) into two sets, and guard it.

Same standard as the Lecture 9 vignettes (pharm_e3_vignette_partition.py): every guard is IMPORTED from
pharm_e3_partition (check, split, gameable, the WRITER.md v1 writer_check and rotate_balanced) and from the Lecture 9
vignette partitioner (a patient opens every stem, one question, a known lead-in, no patient names). The abbreviation
list keeps the Lecture 10 terms and is widened for this lecture's pneumonia, tuberculosis, asthma, inhaler and
smoking cessation shorthand. Writes tools/pharm_e3_l11_vignette_sets.json (keys set1, set2), with `lead` stripped
(`mis` is kept for the blind review; the renderer strips it). Never touches any other sets file.

    python3 tools/pharm_e3_l11_vignette_partition.py
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_e3_partition import (check, split, rotate_balanced, writer_check, gameable, BAR, TARGET, BREADTH,
                                BACKGROUND, NOPT, SEED)
import pharm_e3_vignette_partition as V9
from pharm_e3_l11_vignette_pool import POOL

ABBREV = re.compile(r"\b(PSVT|SVT|VT|VF|WPW|PAC|PVCs?|AF|AFib|CHF|MI|IV|EKG|ECG|AV|SA|ICU|ER|ED|BB|CCB|NAPA|CYP\w*|ACLS|"
                    r"HFrEF|EF|LV|BP|HR|NSR|"
                    r"CAP|HAP|VAP|HCAP|MDR|MRSA|PO|IM|SC|SQ|COPD|COLD|FEV1|FVC|ICS|LABA|SABA|SAMA|LAMA|LTRA|OCS|CAT|"
                    r"TB|MTB|LTBI|HIV|IgE|IL|NRT|OTC|MDI|DPI|VHC|MAOIs?|TCAs?|NMDA|CNS|GI|UTI|CAD|DM|PDE|cAMP|cGMP|"
                    r"INH|RIF|EMB|PZA|ABX|SR|ADR|N/V|HA)\b")
SEED_V = SEED + 11   # own stream: never disturbs the topic quizzes or the Lecture 9 and 10 vignettes


def guard(pool):
    for i, q in enumerate(pool):
        w = "pool[%d]" % i
        assert V9.PATIENT.match(q["q"]), "%s: stem does not open with a patient" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert q["lead"] in V9.LEADS, "%s: unknown lead-in %r" % (w, q["lead"])
        blob = q["q"] + " " + " ".join(t for o in q["opts"] for t in o[:2])
        m = ABBREV.search(blob)
        assert not m, "%s: abbreviation %r" % (w, m.group(0))
        assert not re.search(r"(?i)\b(mr|mrs|ms)\.", blob), "%s: patient named" % w


def main():
    check(POOL, "l11-vignette")
    writer_check(POOL, "l11-vignette")
    guard(POOL)

    def attempt(offset):
        rng = random.Random(SEED_V + offset)
        a, b = split(POOL, rng)
        ra, rb = rotate_balanced(a, rng), rotate_balanced(b, rng)
        la, lb = Counter(q["lead"] for q in ra), Counter(q["lead"] for q in rb)
        ta, tb = Counter(q["topic"] for q in ra), Counter(q["topic"] for q in rb)
        imbalance = sum(abs(la[k] - lb[k]) for k in V9.LEADS) + sum(abs(ta[k] - tb[k]) for k in set(ta) | set(tb))
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
        print("set%d  %2d questions  positions=%s  gameable=%.0f%%%s  mech+phys=%d breadth=%d topics=%d"
              % (n, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100,
                 "  (over the 10%% target)" if frac > TARGET else "", back, broad,
                 len({q["topic"] for q in rot})))
        print("       lead-ins:", dict(sorted(Counter(q["lead"] for q in rot).items())))
        print("       topics  :", dict(Counter(q["topic"] for q in rot)))
        out["set%d" % n] = [{k: v for k, v in q.items() if k != "lead"} for q in rot]
    print("pool   %d questions  lead-ins:" % len(POOL), dict(sorted(Counter(q["lead"] for q in POOL).items())))
    path = os.path.join(HERE, "pharm_e3_l11_vignette_sets.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(path))


if __name__ == "__main__":
    main()
