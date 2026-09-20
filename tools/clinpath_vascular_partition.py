#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Clinical Pathophysiology Lecture 7 pool into 2 x 30.

Vascular Pathophysiology. 92 questions written across two files -- anatomy,
endothelium and blood pressure regulation in part A, arteriosclerosis through
venous disease in part B -- and split in half here, so each set is drawn from
the whole lecture rather than from one half of it.

NO RECORDING EXISTS for this lecture, so every question comes off the slides.

Guards, in the order this content could have failed them:

  NO MANAGEMENT. [[clin_path_exam_spec]] draws the line between this course and
  CMS I at mechanism against management. A vascular deck is full of conditions
  that have obvious treatments, and naming one even in a WRONG option still
  teaches management, so the guard checks every option rather than just the key.
  NO VIGNETTES, also per the spec.
  Stems ask something, cite nothing, and explanations do the same.
  Answer positions even; key not guessable by length.
"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clinpath_vascular_pool_a import QUESTIONS as POOL_A
from clinpath_vascular_pool_b import QUESTIONS as POOL_B
POOL = POOL_A + POOL_B

SEED, NOPT, BAR = 20260918, 4, 0.35
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|this course|in class)\b")
# Management terms for a CARDIAC deck. Deliberately NOT the ENT list this file
# was adapted from: that one catches "drainage", which here appears innocently
# as venous and lymphatic drainage, and it misses everything a vascular lecture
# would actually be treated with.
MGMT = re.compile(r"(?i)\b(treat with|first-line|first line|prescrib|therapy is|managed with|"
                  r"stent|angioplasty|bypass graft|thrombolysis|thrombolytic|revascularis|"
                  r"revasculariz|valve replacement|valvuloplasty|pacemaker|defibrillat|"
                  r"pericardiocentesis|statin|beta blocker|beta-blocker|ace inhibitor|"
                  r"nitrate|nitroglycerin|anticoagulat|antiplatelet therapy|diuretic therapy)\b")
VIGNETTE = re.compile(r"(?i)^\s*(a|an)\s+\d{1,3}[- ]year[- ]old|^\s*a\s+patient\b|^\s*a\s+\d")


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
        assert not VIGNETTE.search(q["q"]), "%s: stem is a vignette" % w
        # Mechanism only. The key carries the teaching, so it is the one that
        # matters most -- a distractor naming a treatment as a wrong answer is
        # still teaching management.
        for t, e in q["opts"]:
            assert not MGMT.search(t), "%s: management in an option: %r" % (w, t[:60])
            assert not CITES.search(e), "%s: explanation cites the course" % w
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option" % w


def main():
    rng = random.Random(SEED)
    check(POOL)
    # 2 x 30 per [[clin_path_exam_spec]]. The pool is 94, deliberately larger:
    # the surplus is not waste, it is what the cumulative master exams draw on
    # later, and writing it now while the deck is open is cheaper than coming
    # back for it. Shuffled first, so the two sets and the reserve are each
    # drawn from the whole lecture rather than from one section of it.
    idx = list(range(len(POOL))); rng.shuffle(idx)
    PER_SET = 30
    idx = idx[:PER_SET * 2]
    half = PER_SET
    sets = {}
    for n, part in ((1, idx[:half]), (2, idx[half:])):
        qs = [POOL[i] for i in part]
        order = ([0, 1, 2, 3] * ((len(qs) // NOPT) + 1))[:len(qs)]
        rng.shuffle(order)
        rot = []
        for q, want in zip(qs, order):
            o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
            r = dict(q); r["opts"] = o; r["c"] = want
            rot.append(r)
        pos = {}
        for q in rot:
            pos[q["c"]] = pos.get(q["c"], 0) + 1
        assert max(pos.values()) - min(pos.values()) <= 1, "set%d uneven: %r" % (n, pos)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: key longest in %.0f%%" % (n, frac * 100)
        sets["set%d" % n] = rot
        print("set%d  %d questions  positions=%s  key-is-longest=%.0f%%"
              % (n, len(rot), {chr(65 + k): v for k, v in sorted(pos.items())}, frac * 100))
    out = os.path.join(HERE, "clinpath_vascular_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(out))


if __name__ == "__main__":
    main()
