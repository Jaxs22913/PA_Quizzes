#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rotate answer positions and guard the two PDM lab-panel quizzes.

The pools author the correct answer FIRST so no author drifts toward a
favourite position; everything below moves it. Each 30-question set gets
8/8/7/7 across A-D -- the PD1 bug was a quiz where the answer was always A,
and [[answer_position_bias_check]] makes a distribution sweep mandatory on
every build.

The guards are the ones this kind of question can actually fail:

  every stem prints a reference range for every value it reports, because the
  whole premise is that nothing is recalled;
  every stem asks something (see check_leadin_present.py);
  no stem cites a lecture, slide or professor;
  the correct answer is not the longest option often enough to be guessable;
  no two options in an item are the same.
"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_lab_pool_cbc import QUESTIONS as CBC
from pdm_lab_pool_chem import QUESTIONS as CHEM

SEED = 20260910
NOPT = 4
BAR = 0.35            # share of items where the key is the longest option
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|prof\.|the course|in class)\b")
# Same rule as tools/check_leadin_present.py: a question mark, or an opening
# imperative that names the task. Two items here end "Calculate the anion gap
# and say what it means." -- an instruction, not a question, and perfectly clear.
IMPERATIVE = re.compile(r"(?i)\b(calculate|describe|rank|list|state|name|identify|select)\b")


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= MARGIN_CHARS and L[c] >= runner * (1 + MARGIN_FRAC)


def check(pool, label):
    for i, q in enumerate(pool):
        stem = q["q"]
        where = "%s[%d]" % (label, i)
        assert len(q["opts"]) == NOPT, "%s: %d options" % (where, len(q["opts"]))
        assert q["c"] == 0, "%s: key must be authored first" % where
        assert "?" in stem or IMPERATIVE.search(stem.split(". ")[-1]), \
            "%s: stem asks nothing" % where
        assert not CITES.search(stem), "%s: stem cites the course" % where
        # every reported value carries its range: count the parenthesised refs
        vals = stem.count(" · ") + 1
        refs = len(re.findall(r"\([^)]*\)", stem))
        assert refs >= vals - 1, \
            "%s: %d values but only %d reference ranges" % (where, vals, refs)
        texts = [o[0] for o in q["opts"]]
        assert len(set(texts)) == NOPT, "%s: duplicate option text" % where
        for t, e in q["opts"]:
            assert len(e) >= 60, "%s: explanation too thin: %r" % (where, e[:50])


def rotate(pool, rng):
    order = ([0, 1, 2, 3] * ((len(pool) // NOPT) + 1))[:len(pool)]
    rng.shuffle(order)
    out = []
    for q, want in zip(pool, order):
        opts = list(q["opts"])
        key = opts.pop(0)
        opts.insert(want, key)
        r = dict(q); r["opts"] = opts; r["c"] = want
        out.append(r)
    return out


def main():
    rng = random.Random(SEED)
    sets = {}
    for label, pool in (("cbc", CBC), ("chem", CHEM)):
        check(pool, label)
        rot = rotate(pool, rng)
        pos = {}
        for q in rot:
            pos[q["c"]] = pos.get(q["c"], 0) + 1
        game = sum(gameable(q["opts"], q["c"]) for q in rot)
        assert max(pos.values()) - min(pos.values()) <= 1, \
            "%s: uneven answer positions %r" % (label, pos)
        frac = game / len(rot)
        assert frac <= BAR, "%s: key is longest in %.0f%% of items" % (label, frac * 100)
        print("%-5s %d questions  positions=%s  key-is-longest=%.0f%%"
              % (label, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100))
        sets[label] = rot

    out = os.path.join(HERE, "pdm_lab_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(out))


if __name__ == "__main__":
    main()
