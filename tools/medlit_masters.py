#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Interpretation of Medical Literature Exam 1 master exams: five cumulative forms.

Every topic contributes the same number of questions to every form (five, with twelve topics), so
each form covers the whole block and no question appears in two forms. The questions are taken from
the topic quizzes' validated sets (tools/medlit_*_sets.json). Answer positions are re-permuted
PER FORM so a master's key is not in the same position as the same question's topic-quiz key.

    python3 tools/medlit_masters.py        # writes Interpretation of Medical Literature Exam 1/master-exams.json
"""
import json, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Interpretation of Medical Literature Exam 1", "master-exams.json")

# (label, sets file)
TOPICS = [("Bias and validity", "medlit_s1_sets.json"), ("Evidence", "medlit_s2evid_sets.json"),
          ("Study design", "medlit_s2design_sets.json"), ("Rates", "medlit_s3rates_sets.json"),
          ("Data and variation", "medlit_s3data_sets.json"), ("Diagnostic tests", "medlit_s4tests_sets.json"),
          ("Risk and ratios", "medlit_s7risk_sets.json"), ("Prognosis", "medlit_s7prog_sets.json"),
          ("Prevention and screening", "medlit_s8prev_sets.json"), ("Research and trials", "medlit_s8trials_sets.json"),
          ("Statistics and causation", "medlit_s9stats_sets.json"), ("Clinical questions and reviews", "medlit_s10reviews_sets.json")]
FORMS, PER, SEED = "ABCDE", 5, 20260928
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def main():
    rng = random.Random(SEED)
    forms = {f: [] for f in FORMS}
    missing = [f for _, f in TOPICS if not os.path.exists(os.path.join(HERE, f))]
    if missing:
        sys.exit("missing topic sets: %s" % ", ".join(missing))
    for label, fn in TOPICS:
        S = json.load(open(os.path.join(HERE, fn), encoding="utf-8"))
        qs = S["set1"] + S["set2"]
        assert len(qs) == 60, (fn, len(qs))
        # order by objective so an even stride samples every objective, then deal round-robin to the forms
        ios = []
        for q in qs:
            if q["io"] not in ios:
                ios.append(q["io"])
        qs = sorted(qs, key=lambda q: (ios.index(q["io"]), q["topic"]))
        take = [qs[round(k * len(qs) / (PER * len(FORMS)))] for k in range(PER * len(FORMS))]
        assert len({id(q) for q in take}) == PER * len(FORMS), "stride collided in " + fn
        for k, q in enumerate(take):
            forms[FORMS[k % len(FORMS)]].append(q)
    out = {}
    for f in FORMS:
        qs = forms[f]
        rng.shuffle(qs)                                   # mix the topics through the form
        order = ([0, 1, 2, 3] * (len(qs) // 4 + 1))[:len(qs)]
        rng.shuffle(order)
        rot = []
        for q, want in zip(qs, order):
            keytext = q["opts"][q["c"]]
            rest = [o for i, o in enumerate(q["opts"]) if i != q["c"]]
            rng.shuffle(rest)
            rest.insert(want, keytext)
            r = dict(q); r["opts"] = rest; r["c"] = want
            rot.append(r)
        pos = Counter(q["c"] for q in rot)
        assert max(pos.values()) - min(pos.values()) <= 1, (f, pos)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        print("form %s  %d questions  positions=%s  key-is-longest=%.0f%%  topics=%d"
              % (f, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100, len({q["topic"] for q in rot})))
        assert frac <= 0.13, "form %s: key longest in %.0f%%" % (f, frac * 100)
        out[f] = rot
    stems = [q["q"] for v in out.values() for q in v]
    assert len(set(stems)) == len(stems), "a question appears in two forms"
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.relpath(OUT, ROOT), "-", len(stems), "distinct questions")


if __name__ == "__main__":
    main()
