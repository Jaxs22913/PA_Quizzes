#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build and render the 5 x 60 cumulative Master Exams for Physical Diagnosis 2 Exam 2
(Lectures 5-7: Advanced Cardiovascular & Peripheral Vascular, Thorax & Lungs, Hematology).

SOURCE. The full authored pools (shipped and held items), like the Exam 1 masters
(tools/build_pd2_masters.py), but only items holding a CURRENT blind + audit PASS in
tools/blind_review.json (tools/_pd2_e2_review_status.py applies the same tests as
`blind_review.py check`). The heart-sound listening quiz is left out, as Exam 1 had no
equivalent.

SPLIT. Weighting by scheduled hours (calendar-data.js: Lecture 5 3 h, Lecture 6 2 h, Lecture 7 1 h)
would give 30/20/10 per 60-question form, which needs 150 Lecture 5 items; only about 100 of its
119 pool items hold a pass. So each lecture is filled toward its hour weight as far as its reviewed
pool allows: Lecture 5 at 20 per form, Lecture 6 at 23 and Lecture 7 the remaining 17.
QUOTA is asserted against the pass counts, so a lost pass fails the build.

PARTITION. Each lecture's passed items are ordered by topic and dealt round-robin to the five
forms, so every form gets the same spread of topics; no item appears twice (asserted).
POSITIONS. Exactly 15/15/15/15 per form. Numeric option sets stay ascending with the key where
its value falls (WRITER.md rule 8, tools/_option_order.py); the rest fill the remaining
positions to reach 15 each (asserted).
"""
import json, os, random, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from _pd2_e2_review_status import pools, status
from _option_order import option_values, order_options
from render import render

FOLDER = "Physical Diagnosis 2 Exam 2"
OUT = os.path.join(ROOT, FOLDER)
FORMS = "ABCDE"
PER_FORM = 60
QUOTA = {"L5": 20, "L6": 23, "L7": 17}
assert sum(QUOTA.values()) == PER_FORM
NAMES = {"L5": "cardiovascular", "L6": "thorax and lungs", "L7": "hematology"}
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Cardiovascular &amp; peripheral vascular", "Thorax &amp; lungs", "Hematology"]
WORDS = {17: "seventeen", 20: "twenty", 23: "twenty-three"}


def clean(q):
    q = {k: v for k, v in q.items() if k not in ("mis",)}
    return json.loads(json.dumps(q))


def main():
    rng = random.Random(20261120)
    P = pools()
    passed = {lec: [q for q in qs if status(q) == "pass"] for lec, qs in P.items()}
    for lec, qs in passed.items():
        need = QUOTA[lec] * len(FORMS)
        print("%s  pool %3d  passed %3d  per form %2d  needed %3d" % (lec, len(P[lec]), len(qs), QUOTA[lec], need))
        assert len(qs) >= need, "%s has %d passed items for %d places" % (lec, len(qs), need)

    forms = {f: [] for f in FORMS}
    for lec in ("L5", "L6", "L7"):
        qs = passed[lec][:]
        rng.shuffle(qs)
        # topic-stratified: group by topic, then interleave so a cut keeps every topic spread
        by_t = defaultdict(list)
        for q in qs:
            by_t[q.get("topic", "")].append(q)
        order = []
        topics = sorted(by_t, key=lambda t: -len(by_t[t]))
        while any(by_t.values()):
            for t in topics:
                if by_t[t]:
                    order.append(by_t[t].pop())
        chosen = order[:QUOTA[lec] * len(FORMS)]
        # the items left out are the tail of the interleave: the largest topics' extras
        for i, q in enumerate(chosen):
            forms[FORMS[i % len(FORMS)]].append((lec, clean(q)))

    # identity = stem + picture + option texts (several picture items share a stem)
    stems = [(q["q"], q.get("img", ""), tuple(sorted(o[0] for o in q["opts"])))
             for f in forms.values() for _l, q in f]
    assert len(stems) == len(set(stems)) == PER_FORM * len(FORMS), "not a true partition"

    out = {}
    for name in FORMS:
        items = forms[name]
        rng.shuffle(items)
        qs = []
        fixed = {}
        for n, (_lec, q) in enumerate(items):
            if option_values([o[0] for o in q["opts"]]) is not None:
                q = order_options(q)
                fixed[n] = q["c"]
            qs.append(q)
        want = Counter({k: PER_FORM // 4 for k in range(4)})
        for t in fixed.values():
            want[t] -= 1
        assert min(want.values()) >= 0, "too many ordered keys in one position"
        free = [k for k in range(4) for _ in range(want[k])]
        rng.shuffle(free)
        it = iter(free)
        for n, q in enumerate(qs):
            if n in fixed:
                continue
            t = next(it)
            key = q["opts"][q["c"]]
            rest = [o for i, o in enumerate(q["opts"]) if i != q["c"]]
            rng.shuffle(rest)
            rest.insert(t, key)
            q["opts"], q["c"] = rest, t
        pos = Counter(q["c"] for q in qs)
        assert all(pos[k] == PER_FORM // 4 for k in range(4)), pos
        assert all(len(q["opts"]) == 4 for q in qs)
        lec = Counter(l for l, _q in items)
        assert all(lec[k] == QUOTA[k] for k in QUOTA), lec
        out[name] = qs
        print("Form %s: %d questions  positions A/B/C/D %d/%d/%d/%d  L5/L6/L7 %d/%d/%d  topics %d  ordered %d"
              % (name, len(qs), pos[0], pos[1], pos[2], pos[3], lec["L5"], lec["L6"], lec["L7"],
                 len(set(q.get("topic") for q in qs)), len(fixed)))

    json.dump(out, open(os.path.join(OUT, "master-exams.json"), "w", encoding="utf-8"), ensure_ascii=False)
    total = sum(len(v) for v in out.values())
    for name in FORMS:
        intro = (
            "Sixty questions drawn from all three lectures of the Exam 2 block, in proportion: "
            "cardiovascular and peripheral vascular contributes %s, thorax and lungs %s and hematology %s. "
            "<b>Weighted toward the longer lectures</b> as far as the reviewed questions allow (Lecture 5 was "
            "three hours, Lecture 6 two and Lecture 7 one). "
            "<b>No question appears in more than one form</b>, so all five give you %d distinct questions, drawn "
            "from the full written pools, not only the topic quizzes. Every question here passed an independent "
            "blind review and audit against its slides. "
            "<b>This is a physical diagnosis course</b>: the questions ask what you find, how you find it and "
            "what the finding means. Every question cites its slide."
            % (WORDS[QUOTA["L5"]], WORDS[QUOTA["L6"]], WORDS[QUOTA["L7"]], total))
        fn = "pd2-exam-2-master-exam-form-%s.html" % name.lower()
        html = render(title="PD2 Exam 2 Master Exam &mdash; Form %s" % name,
                      h1="Physical Diagnosis 2 &mdash; Comprehensive Master Exam",
                      sub="Exam 2 &middot; Lectures 5&ndash;7 &middot; Form %s" % name,
                      pill="%d questions" % len(out[name]), chips=CHIPS, intro=intro,
                      questions=out[name], already_converted=True, **PAL)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote", fn)


if __name__ == "__main__":
    main()
