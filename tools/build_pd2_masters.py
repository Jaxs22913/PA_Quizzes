#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 5 x 60 cumulative Master Exams for Physical Diagnosis 2 Exam 1.

WHY THIS EXISTS RATHER THAN build_master_exams.py. The generic builder harvests
questions from the RENDERED topic quizzes. For PD2 that yields only 195 -- the
two 30-question forms per lecture, plus Lecture 1's 15 -- which cannot fill
5 x 60 without repeating questions across forms.

But 371 questions are AUTHORED. The topic quizzes ship 60 per lecture out of
pools holding 114, 126 and 113, so more than half the written material never
reaches a student. Drawing the masters from the full pools uses that, and keeps
every design rule the generic builder states: questions are reused verbatim from
material that already passed the pool guards, no question appears in two forms,
and answer positions are rebalanced per form.

LECTURE 1 IS GENUINELY SMALL AND THAT IS NOT A DEFECT. Its source is a 24-page
introduction, much of it course mechanics -- the syllabus changes, who the
course directors are, how the labs run -- which the PD2 house rule excludes from
questions. 18 authored questions is an honest reflection of what is examinable
in it, so it contributes 3 per form while the other three contribute 19 each.
"""
import importlib, json, os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

FOLDER = "Physical Diagnosis 2 Exam 1"
FORMS = ["A", "B", "C", "D", "E"]
PER_FORM = 60

# lecture -> the pool modules that hold its questions
SOURCES = {
    "clinical-reasoning": ["pd2_l1_pool_a"],
    "dermatology":        ["pd2_l2_pool_a", "pd2_l2_pool_b", "pd2_l2_pool_c"],
    "ocular-exam":        ["pd2_l3_pool_a", "pd2_l3_pool_b", "pd2_l3_pool_c"],
    "ent-exam":           ["pd2_l4_pool_a", "pd2_l4_pool_b", "pd2_l4_pool_c"],
}
# Lecture 1 is small by nature; the rest split what is left evenly.
QUOTA = {"clinical-reasoning": 3, "dermatology": 19, "ocular-exam": 19, "ent-exam": 19}
assert sum(QUOTA.values()) == PER_FORM, "quotas do not add to a form"


def load(lecture):
    out = []
    for name in SOURCES[lecture]:
        mod = importlib.import_module(name)
        for v in vars(mod).values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "opts" in v[0]:
                out.extend(v)
    seen, uniq = set(), []
    for q in out:
        if q["q"] in seen:
            continue
        seen.add(q["q"])
        uniq.append(q)
    return uniq


def rebalance_positions(form, rng):
    """Spread correct answers across A/B/C/D. Slices of separately balanced
    pools do not stay balanced once concatenated."""
    targets = [i % 4 for i in range(len(form))]
    rng.shuffle(targets)
    for q, t in zip(form, targets):
        k = (t - q["c"]) % 4
        if k:
            q["opts"] = q["opts"][-k:] + q["opts"][:-k]
        q["c"] = t
    return form


def main():
    rng = random.Random(20260913)
    pools = {}
    for lec in SOURCES:
        qs = load(lec)
        for q in qs:
            q.setdefault("c", 0)
        rng.shuffle(qs)
        pools[lec] = qs

    print("authored pool: %d questions across %d lectures"
          % (sum(len(v) for v in pools.values()), len(pools)))
    for lec in sorted(pools):
        need = QUOTA[lec] * len(FORMS)
        print("   %-22s %3d authored   %2d per form   %3d needed" % (lec, len(pools[lec]), QUOTA[lec], need))
        assert len(pools[lec]) >= need, (
            "%s has %d questions but %d are needed -- shrinking the forms or repeating "
            "questions would both be worse than writing more" % (lec, len(pools[lec]), need))

    cursor = {k: 0 for k in pools}
    forms = []
    for _ in FORMS:
        form = []
        for lec in sorted(SOURCES):
            for _ in range(QUOTA[lec]):
                form.append(json.loads(json.dumps(pools[lec][cursor[lec]])))
                cursor[lec] += 1
        rng.shuffle(form)
        forms.append(rebalance_positions(form, rng))

    stems = [q["q"] for f in forms for q in f]
    print("\n%d forms x %d = %d questions; unique stems: %d"
          % (len(forms), PER_FORM, len(stems), len(set(stems))))
    assert len(set(stems)) == len(stems), "a question appears in more than one form"
    for name, f in zip(FORMS, forms):
        pos = Counter(q["c"] for q in f)
        assert len(f) == PER_FORM, "form %s has %d questions" % (name, len(f))
        assert all(len(q["opts"]) == 4 for q in f), "form %s has a non-four-option question" % name
        print("   Form %s: %d questions, answer positions A/B/C/D %d/%d/%d/%d"
              % (name, len(f), pos[0], pos[1], pos[2], pos[3]))

    out = os.path.join(ROOT, FOLDER, "master-exams.json")
    json.dump({n: f for n, f in zip(FORMS, forms)}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False)
    print("\nwrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
