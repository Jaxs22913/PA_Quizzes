#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split the CMS I Exam 5 "comorbidities, contraindications and scores" pools into two forms.

    python3 tools/cms_e5x2_partition.py            # build, report, write tools/cms_e5x2_sets.json
    python3 tools/cms_e5x2_partition.py --dry-run  # build and report, write nothing

Then tools/render_cms_e5x2.py renders the two pages.

WHY (2026-10-29, the night before the retest): Jaxon said the real Exam 5 had "vignettes with
patients with multiple comorbidities and then medications/diseases that were similar and we had
to know contraindications and what to pick instead", plus guideline questions: a vignette, then
"what's the score". He asked for two 70-question quizzes in that style. The items are NEW
(tools/cms_e5x2_pool_a.py for Lectures 29-32, tools/cms_e5x2_pool_b.py for 26-28), written to
tools/question_writing/EXPLAIN_DEEP.md, and never appear in the topic quizzes or masters.

Every usable item is used once: each lecture's items, grouped by kind (comorbid / score /
classify), alternate between the two forms, so each form gets half of every lecture and of every
kind. Items listed in tools/cms_e5x2_holds.json (review holds) are left out; a form is never
padded past what the pools hold (hold-not-force). Positions are permuted per form onto an even
A-D spread; a numeric option set keeps its values ascending, so its key sits where its value falls.
"""
import sys, os, json, random, re, copy
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

_argv = sys.argv
sys.argv = [_argv[0], "l27io"]            # cms_e5_partition reads argv[1] at import
import cms_e5_partition as P
sys.argv = _argv
import cms_e5x2_pool_a, cms_e5x2_pool_b

PER_FORM = 70
FORMS = ["1", "2"]
LECS = ["l26", "l27", "l28", "l29", "l30", "l31", "l32"]
SEED = int(os.environ.get("CMS_E5X2_SEED", "20261029"))
HOLDS = os.path.join(HERE, "cms_e5x2_holds.json")


def norm(t):
    return re.sub(r"\s+", " ", t).strip().lower()


def gameable(q):
    L = [len(o[0]) for o in q["opts"]]
    c = q["c"]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= P.MARGIN_CHARS and L[c] >= runner * (1 + P.MARGIN_FRAC)


def build(dry_run=False):
    rng = random.Random(SEED)
    holds = {norm(s) for s in json.load(open(HOLDS))} if os.path.exists(HOLDS) else set()
    pool = [q for q in cms_e5x2_pool_a.QUESTIONS + cms_e5x2_pool_b.QUESTIONS]
    for q in pool:                        # an `order` list of option texts fixes a non-numeric display order
        if q.get("order"):
            texts = [o[0] for o in q["opts"]]
            q["ordered"], q["asc"] = True, [texts.index(t) for t in q["order"]]
    stems = Counter(norm(q["q"]) for q in pool)
    assert max(stems.values()) == 1, "duplicate stem in the pools"
    held = [q for q in pool if norm(q["q"]) in holds]
    pool = [q for q in pool if norm(q["q"]) not in holds]
    assert len(held) == len(holds), "a hold matches no pool stem"
    print("pool %d usable, %d held" % (len(pool), len(held)))

    # alternate within each lecture x kind cell; which form starts each cell alternates too,
    # so odd cells do not all favor form 1
    cells = defaultdict(list)
    for q in pool:
        cells[(q["lec"], q["kind"])].append(q)
    forms, start = [[], []], 0
    for key in sorted(cells):
        items = cells[key][:]
        rng.shuffle(items)
        for n, q in enumerate(items):
            forms[(n + start) % 2].append(q)
        start += len(items) % 2
    # even the forms out, then cap at PER_FORM (spares are dropped from the bigger lecture cells)
    while abs(len(forms[0]) - len(forms[1])) > 1:
        big, small = (0, 1) if len(forms[0]) > len(forms[1]) else (1, 0)
        forms[small].append(forms[big].pop())
    for f in forms:
        while len(f) > PER_FORM:
            byl = Counter(q["lec"] for q in f)
            lec = byl.most_common(1)[0][0]
            drop = [q for q in f if q["lec"] == lec and q["kind"] == "comorbid"][-1]
            f.remove(drop)

    out, report = {}, {}
    for name, sel in zip(FORMS, forms):
        qs = [copy.deepcopy(q) for q in sel]
        rng.shuffle(qs)
        n = len(qs)
        fixed = {i: P.ascending(q).index(q["c"]) for i, q in enumerate(qs) if P.is_ordered(q)}
        base, extra = divmod(n, 4)
        f_ix = FORMS.index(name)
        want = {k: base + (1 if (k - 2 * f_ix) % 4 < extra else 0) for k in range(4)}
        free = []
        for k in range(4):
            free += [k] * (want[k] - sum(1 for t in fixed.values() if t == k))
        assert len(free) == n - len(fixed) and all(free.count(k) >= 0 for k in range(4)), "ordered sets crowd one letter"
        rng.shuffle(free)
        it = iter(free)
        targets = [fixed[i] if i in fixed else next(it) for i in range(n)]
        for q, t in zip(qs, targets):
            correct = q["opts"][q["c"]]
            if P.is_ordered(q):
                order = P.ascending(q)
                q["opts"] = [q["opts"][j] for j in order]
                q["c"] = order.index(q["c"])
                assert q["c"] == t
                continue
            rest = [o for j, o in enumerate(q["opts"]) if j != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:t] + [correct] + rest[t:]
            q["c"] = t
        for q in qs:
            assert re.match(r"correct\b", q["opts"][q["c"]][1], re.I), q["q"][:60]
            assert sum(1 for o in q["opts"] if re.match(r"correct\b", o[1].strip(), re.I)) == 1
        pos = Counter(q["c"] for q in qs)
        assert all(pos[k] == want[k] for k in range(4)), pos
        g = sum(gameable(q) for q in qs)
        print("  Form %s: %dq  pos %s  per lecture %s  kinds %s  length-gameable %d" % (
            name, n, "/".join(str(pos[k]) for k in range(4)),
            "/".join(str(sum(1 for q in qs if q["lec"] == l)) for l in LECS),
            dict(Counter(q["kind"] for q in qs)), g))
        out[name] = [{k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite", "img", "alt", "slide") if k in q}
                     for q in qs]
        report[name] = [{"lec": q["lec"], "kind": q["kind"], "c": q["c"], "q": q["q"][:90]} for q in qs]
    if dry_run:
        print("--dry-run: nothing written")
        return out
    json.dump(out, open(os.path.join(HERE, "cms_e5x2_sets.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote tools/cms_e5x2_sets.json")
    return out


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
