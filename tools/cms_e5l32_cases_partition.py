#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split the Lecture 32 case-vignette pool into the two 30-question "Case Vignettes" quizzes.

    python3 tools/cms_e5l32_cases_partition.py            # build, report, write tools/cms_e5l32_cases_sets.json
    python3 tools/cms_e5l32_cases_partition.py --dry-run  # build and report, write nothing

Then tools/render_cms_e5l32_cases.py renders the two pages.

WHY (2026-10-29): Professor Reynolds' four practice cases ("IE Missing Slide and Cases.pptx", slides
2-5) show how her questions are written; Jaxon asked for two quizzes in that style. The pool
(tools/cms_e5l32_cases_pool.py) assigns every item to form "1", "2" or "S" (spare) by hand, so the
pairs that teach the same point from opposite sides (enterococci with chronic kidney disease vs acute
kidney injury, HACEK with and without allergy, the two culture-negative causes, the two halves of the
"Application of Duke Criteria" slide) land in different forms, and two of her four cases sit in each.

An item listed in tools/cms_e5l32_cases_holds.json (a review hold) is dropped and replaced by the first
spare with the same `ask`, else the first "other" spare, else the first spare left (hold-not-force: a form is never padded past what
the pool holds). Order within a form is a seeded shuffle; answer positions are permuted onto an even
A-D spread (8/8/7/7, the extra letters differing between forms). Ordered option sets keep their order
and their key sits where its value falls: numeric sets ascend (WRITER.md rule 8), and an `order` list
fixes a chronological display order.
"""
import sys, os, json, random, re, copy
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cms_e5l32_cases_pool as POOL
from _option_order import option_values

PER_FORM = 30
FORMS = ["1", "2"]
SEED = int(os.environ.get("CMS_E5L32_CASES_SEED", "20261029"))
HOLDS = os.path.join(HERE, "cms_e5l32_cases_holds.json")
OUT = os.path.join(HERE, "cms_e5l32_cases_sets.json")
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def norm(t):
    return re.sub(r"\s+", " ", t).strip().lower()


def ordered_idx(q):
    """Option indices in display order for an ordered set, else None."""
    texts = [o[0] for o in q["opts"]]
    if q.get("order"):
        assert sorted(q["order"]) == sorted(texts), "order must list the option texts: %r" % q["q"][:60]
        return [texts.index(t) for t in q["order"]]
    vals = option_values(texts)
    if vals is None:
        return None
    return sorted(range(4), key=lambda j: (vals[j], j))


def gameable(q):
    L = [len(o[0]) for o in q["opts"]]
    c = q["c"]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= MARGIN_CHARS and L[c] >= runner * (1 + MARGIN_FRAC)


def build(dry_run=False):
    rng = random.Random(SEED)
    pool = copy.deepcopy(POOL.QUESTIONS)
    stems = Counter(norm(q["q"]) for q in pool)
    assert max(stems.values()) == 1, "duplicate stem in the pool"
    holds = {norm(s) for s in json.load(open(HOLDS))} if os.path.exists(HOLDS) else set()
    assert holds <= set(stems), "a hold matches no pool stem"
    spares = [q for q in pool if q["form"] == "S" and norm(q["q"]) not in holds]
    forms = {f: [q for q in pool if q["form"] == f] for f in FORMS}
    for f in FORMS:
        kept = []
        for q in forms[f]:
            if norm(q["q"]) not in holds:
                kept.append(q)
                continue
            same = ([s for s in spares if s["ask"] == q["ask"]] or [s for s in spares if s["ask"] == "other"]
                    or spares)
            if same:
                rep = same[0]
                spares.remove(rep)
                kept.append(rep)
                print("  form %s: hold %r -> spare %r" % (f, q["q"][:50], rep["q"][:50]))
            else:
                print("  form %s: hold %r, no spare left (form shrinks)" % (f, q["q"][:50]))
        forms[f] = kept[:PER_FORM]
    print("pool %d items, %d held, %d spares unused" % (len(pool), len(holds), len(spares)))

    out, report = {}, {}
    for fi, name in enumerate(FORMS):
        qs = forms[name]
        rng.shuffle(qs)
        n = len(qs)
        fixed = {}
        for i, q in enumerate(qs):
            oi = ordered_idx(q)
            if oi is not None:
                fixed[i] = oi.index(q["c"])
        base, extra = divmod(n, 4)
        want = {k: base + (1 if (k - 2 * fi) % 4 < extra else 0) for k in range(4)}
        free = []
        for k in range(4):
            free += [k] * (want[k] - sum(1 for t in fixed.values() if t == k))
        assert len(free) == n - len(fixed), "ordered sets crowd one letter: %s" % want
        rng.shuffle(free)
        it = iter(free)
        for i, q in enumerate(qs):
            correct = q["opts"][q["c"]]
            oi = ordered_idx(q)
            if oi is not None:
                q["opts"] = [q["opts"][j] for j in oi]
                q["c"] = oi.index(q["c"])
                assert q["c"] == fixed[i]
                continue
            t = next(it)
            rest = [o for j, o in enumerate(q["opts"]) if j != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:t] + [correct] + rest[t:]
            q["c"] = t
        for q in qs:
            assert re.match(r"correct\b", q["opts"][q["c"]][1], re.I), q["q"][:60]
            assert sum(1 for o in q["opts"] if re.match(r"correct\b", o[1].strip(), re.I)) == 1, q["q"][:60]
        pos = Counter(q["c"] for q in qs)
        assert all(pos[k] == want[k] for k in range(4)), pos
        g = sum(gameable(q) for q in qs)
        cases = sorted(q["case"] for q in qs if q.get("case"))
        print("  Quiz %s: %dq  pos A/B/C/D %s  asks %s  her cases %s  length-gameable %d" % (
            name, n, "/".join(str(pos[k]) for k in range(4)), dict(Counter(q["ask"] for q in qs)), cases, g))
        out[name] = [{k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite") if k in q} for q in qs]
        report[name] = [{"ask": q["ask"], "case": q.get("case"), "c": "ABCD"[q["c"]], "q": q["q"][:90]} for q in qs]
    if dry_run:
        print("--dry-run: nothing written")
        return out
    json.dump(out, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote tools/cms_e5l32_cases_sets.json")
    return out


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
