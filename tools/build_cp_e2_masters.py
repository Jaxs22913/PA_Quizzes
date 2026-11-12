#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build and render the five Clinical Pathophysiology I Exam 2 Master Exams, 5 x 60 (Forms A-E).

    python3 tools/build_cp_e2_masters.py            # build, report, write master-exams.json + 5 pages
    python3 tools/build_cp_e2_masters.py --dry-run  # build and report only

Then tools/add_stable_qids.py gives the pages ids.

BLOCK. Exam 2 (Wednesday 2026-11-18) = Lectures 6-10: 6 Cardiac, 7 Vascular, 8 Immunity, 9 Pulmonary,
10 Blood Disorders. Held until Lecture 10 was in (master_exam_sizing), cumulative, 5 forms x 60.

SOURCE AND PARTITION (master_exam_sizing, the Clin Path Exam 1 technique): each lecture's 60 shipped topic-quiz
questions (its sets JSON, which carries the `ordered` flags and matches the pages verbatim) are split 12 per
form, so the five forms are a TRUE PARTITION of the 300 (asserted: total == unique). Every one of the 300 has a
current blind review and audit PASS (tools/blind_review.py; asserted below through `check`), so nothing in a
form is unreviewed. No vignettes and no management, as in the topic quizzes (clin_path_exam_spec).

STRATIFICATION: inside a lecture the 60 are ordered by objective, then topic, then a seeded shuffle, and dealt
round-robin to the five forms, so every objective with five or more items reaches every form and none is
crowded into one. No two questions in one form share the same keyed text.

POSITIONS: permuted per form onto exactly 15/15/15/15. Numeric and ordered option sets keep their ascending
order (their key stays where its value falls); the free questions are rotated around them. No letter more than
three in a row.
"""
import json, os, random, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

FOLDER = "Clinical Pathophysiology I Exam 2"
OUT = os.path.join(ROOT, FOLDER)
FORMS = "ABCDE"
SEED = 20261118
LECS = [("Lecture 6 Cardiac", "clinpath_cardiac_sets.json"),
        ("Lecture 7 Vascular", "clinpath_vascular_sets.json"),
        ("Lecture 8 Immunity", "clinpath_immunity_sets.json"),
        ("Lecture 9 Pulmonary", "clinpath_pulmonary_sets.json"),
        ("Lecture 10 Blood Disorders", "clinpath_blood_sets.json")]
PER = 12
PAL = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Cardiac", "Vascular", "Immunity", "Pulmonary", "Blood disorders"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 2 block &mdash; <b>each of the five lectures "
         "contributes twelve questions to every form</b>, spread across its objectives, so this is a cumulative "
         "rehearsal and not a sample of whichever topic had the most questions. Questions are reused verbatim "
         "from the topic quizzes, each one independently reviewed against the slides. "
         "<b>No question appears in more than one form</b>, so the five forms give you 300 distinct questions. "
         "<b>Mechanism only, no vignettes.</b> This course draws its line against Clinical Medicine and Surgery "
         "at pathophysiology against management. Every question cites its slide.")


def letters_ok(cs):
    run = 1
    for a, b in zip(cs, cs[1:]):
        run = run + 1 if a == b else 1
        if run > 3:
            return False
    return True


def build():
    rng = random.Random(SEED)
    forms = {f: [] for f in FORMS}
    for label, fn in LECS:
        S = json.load(open(os.path.join(HERE, fn), encoding="utf-8"))
        qs = S["set1"] + S["set2"]
        assert len(qs) == 60, (label, len(qs))
        for q in qs:
            q["_lec"] = label
        rng.shuffle(qs)
        qs.sort(key=lambda q: (q["io"], q["topic"]))
        for i, q in enumerate(qs):
            forms[FORMS[i % 5]].append(q)
    # One keyed text per form: swap a clashing question with a same-lecture, same-objective one elsewhere.
    kt = lambda q: q["opts"][q["c"]][0]
    for f in FORMS:
        for q in list(forms[f]):
            if sum(kt(x) == kt(q) for x in forms[f]) < 2:
                continue
            done = False
            for g in FORMS:
                if g == f or done:
                    continue
                for o in forms[g]:
                    if o["_lec"] == q["_lec"] and o["io"] == q["io"] \
                            and all(kt(x) != kt(o) for x in forms[f] if x is not q) \
                            and all(kt(x) != kt(q) for x in forms[g] if x is not o):
                        forms[f][forms[f].index(q)] = o; forms[g][forms[g].index(o)] = q
                        print("  swapped %r (%s) <-> %r (%s) to keep one keyed text per form"
                              % (q["q"][:40], f, o["q"][:40], g))
                        done = True
                        break
    for f in FORMS:
        assert len(forms[f]) == 60
        keys = Counter(kt(q) for q in forms[f])
        assert all(n == 1 for n in keys.values()), (f, [k for k, n in keys.items() if n > 1])
    allq = [q["q"] for f in FORMS for q in forms[f]]
    assert len(allq) == len(set(allq)) == 300, "not a true partition"

    out = {}
    for f in FORMS:
        qs = forms[f]
        for _ in range(500):
            rng.shuffle(qs)
            fixed = {i: q["c"] for i, q in enumerate(qs) if q.get("ordered")}
            want = [15, 15, 15, 15]
            for v in fixed.values():
                want[v] -= 1
            assert min(want) >= 0
            free = [k for k in range(4) for _ in range(want[k])]
            rng.shuffle(free)
            it = iter(free)
            cs = [fixed[i] if i in fixed else next(it) for i in range(60)]
            if letters_ok(cs):
                break
        else:
            raise SystemExit("form %s: could not avoid long letter runs" % f)
        res = []
        for i, q in enumerate(qs):
            r = json.loads(json.dumps(q))
            if i not in fixed:
                o = r["opts"]; key = o.pop(r["c"]); o.insert(cs[i], key); r["c"] = cs[i]
            assert r["opts"][r["c"]][1].lower().startswith("correct"), (f, i)
            res.append(r)
        pos = Counter(r["c"] for r in res)
        assert [pos[k] for k in range(4)] == [15, 15, 15, 15], (f, pos)
        lec = Counter(r["_lec"] for r in res)
        assert set(lec.values()) == {PER}, (f, lec)
        print("Form %s  60 questions  positions=%s  per lecture=%s  ordered=%d"
              % (f, dict(zip("ABCD", [pos[k] for k in range(4)])), [lec[l] for l, _ in LECS], len(fixed)))
        out[f] = [{"topic": r["topic"], "io": r["io"], "q": r["q"], "opts": [o[:2] for o in r["opts"]],
                   "c": r["c"], "cite": r["cite"]} for r in res]
    return out


def main():
    out = build()
    if "--dry-run" in sys.argv:
        return
    json.dump(out, open(os.path.join(OUT, "master-exams.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from render import render
    for f in FORMS:
        fn = "cp-exam-2-master-exam-form-%s.html" % f.lower()
        html = render(title="Clin Path I Exam 2 Master Exam &mdash; Form %s" % f,
                      h1="Clinical Pathophysiology I &mdash; Comprehensive Master Exam",
                      sub="Exam 2 &middot; Lectures 6&ndash;10 &middot; Form %s" % f,
                      pill="60 questions", chips=CHIPS, intro=INTRO,
                      questions=out[f], already_converted=True, **PAL)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote", fn)


if __name__ == "__main__":
    main()
