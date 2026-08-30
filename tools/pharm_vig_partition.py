#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the pharm vignette pool into two 30s and render them.

Four options, matching the rest of Pharmacology I. Answer position is set by
ROTATION, never chosen while authoring -- the "always A" bug has happened twice
on this site.

Also enforces the length targets set for this bank, so a future addition
that reverts to paragraph-length options fails the build instead of shipping.
"""
import io, json, os, random, statistics, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from pharm_vig_pool import POOL
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 1")
PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
NOPT, PER = 4, 30
STEM_MAX, OPT_MAX, OPT_MED = 150, 42, 26
random.seed(20260830)


def gameable(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    return s[0][1] == q["c"] and (s[0][0] - s[1][0]) >= 8 and s[0][0] >= s[1][0] * 1.18


def validate(pool):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != NOPT: bad.append((i, "not four options"))
        if len(q["q"]) > STEM_MAX: bad.append((i, "stem %d chars" % len(q["q"])))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        w = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if len(set(w)) == 1: bad.append((i, "wrong choices share one explanation"))
        for o in q["opts"]:
            if len(o[0]) > OPT_MAX: bad.append((i, "option %d chars: %s" % (len(o[0]), o[0][:40])))
            if not o[1].strip(): bad.append((i, "option unexplained"))
    med = statistics.median([len(o[0]) for q in pool for o in q["opts"]])
    if med > OPT_MED: bad.append((-1, "option median %d over target %d" % (med, OPT_MED)))
    return bad


def rotate(qs):
    targets = [i % NOPT for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % NOPT
        if k: q["opts"] = q["opts"][-k:] + q["opts"][:-k]
        q["c"] = t
    return qs


def main():
    bad = validate(POOL)
    if bad:
        for i, m in bad: print("  [%s] %s" % (i, m))
        sys.exit("pool failed validation -- refusing to build")
    print("pool: %d  schema OK  gameable %d%%"
          % (len(POOL), 100 * sum(map(gameable, POOL)) // len(POOL)))

    answer = {id(q): q["opts"][q["c"]][0] for q in POOL}
    idx = list(range(len(POOL)))
    best = None
    for _ in range(20000):
        random.shuffle(idx)
        ch = idx[:PER * 2]
        sc = 0
        for half in (ch[:PER], ch[PER:]):
            t = Counter(POOL[i]["topic"] for i in half)
            d = Counter(POOL[i]["deck"] for i in half)
            sc += sum(max(0, n - 2) for n in t.values()) * 3
            sc += abs(d["Antibiotics, Antivirals, and Antifungals"] - 14) * 2
            sc += 100 * sum(gameable(POOL[i]) for i in half) // PER
        if best is None or sc < best[0]:
            best = (sc, list(ch))
    ch = best[1]
    sets = {"set1": rotate([POOL[i] for i in ch[:PER]]),
            "set2": rotate([POOL[i] for i in ch[PER:]])}
    for k, s in sets.items():
        for q in s:
            assert q["opts"][q["c"]][0] == answer[id(q)], "rotation moved an answer"
    for name, s in (("SET 1", sets["set1"]), ("SET 2", sets["set2"])):
        pos = Counter(q["c"] for q in s)
        ol = [len(o[0]) for q in s for o in q["opts"]]
        print("%s  n=%d  A/B/C/D %s  opt median %d max %d  gameable %d%%"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 statistics.median(ol), max(ol), 100 * sum(map(gameable, s)) // len(s)))

    CHIPS = ["Short clinical stems", "Antibacterials", "Antifungals &amp; antivirals",
             "Dermatology", "Autonomic"]
    INTRO = ("Short clinical vignettes for Pharmacology I Exam 1 &mdash; one or two sentences, four "
             "options, and options short enough to scan. Written to be to the point, with the "
             "reasoning in the answer explanation rather than crammed into the choices.")
    for n, (key, fname) in enumerate((("set1", "pharm-vignettes.html"),
                                      ("set2", "pharm-vignettes-version-2.html")), start=1):
        qs = [{"topic": q["topic"], "io": "Clinical application &mdash; Exam 1 lectures",
               "q": q["q"], "opts": q["opts"], "c": q["c"],
               "cite": "%s, Slide %d" % (q["deck"], q["slide"])} for q in sets[key]]
        html = render(title="Pharmacology I Vignettes %d &mdash; Exam 1" % n,
                      h1="Pharmacology I &mdash; Vignettes %d" % n,
                      sub="Pharmacology I &middot; Exam 1 &middot; Short clinical cases",
                      pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
                      questions=qs, already_converted=True, **PAL)
        io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
        print("wrote %-38s %d questions" % (fname, len(qs)))


if __name__ == "__main__":
    main()
