#!/usr/bin/env python3
"""Shared partition engine for Microbiology Lectures 15 (Fungi) and 16 (Food Safety): pool -> 2 x 30.

The same selection the Lecture 14 partition does (tools/micro_l14_partition.py), lifted into one function so the two
lecture scripts carry only their own weights, clusters and guards:

  * TARGET weights per topic over the 60 questions of both sets (within half a question of target is free; every
    topic weighted 2 or more appears in every set);
  * every set carries every objective, with a minimum for the transmission/source objective;
  * near-twins (CLUSTERS, plus every group of items sharing the same key text) at most N per set;
  * MUST_EACH groups in both sets, MUST_ANY groups in at least one;
  * length bias by selection (key uniquely longest in at most ~30%, "gameable" under 10%);
  * Set 1 TEXT-ONLY (it stays in Group Study), Set 2 carries exactly N_IMG pictures;
  * answer positions by ROTATION per set, balanced 8/8/7/7, EXCEPT ordered (numeric) option sets, which keep their
    ascending order (WRITER.md rule 8; the pool marks them ordered=True) and count toward the balance where they
    fall.
Carries the house 60-character explanation guard and the "Correct" opener contract that
check_answer_key_consistency.py reads.
"""
import json, os, random, re
from collections import Counter

NOPT = 4


def lens(q): return [len(o[0]) for o in q["opts"]]


def longest_is_correct(q):
    s = sorted(((l, i) for i, l in enumerate(lens(q))), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= 8 and tl >= rn * 1.18


def uniquely_longest(q):
    L = lens(q); c = L[q["c"]]
    return c > max(L[:q["c"]] + L[q["c"] + 1:])


def uniquely_shortest(q):
    L = lens(q); c = L[q["c"]]
    return c < min(L[:q["c"]] + L[q["c"] + 1:])


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def validate(pool, root, folder):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != NOPT: bad.append((i, "not four options"))
        if not (0 <= q["c"] < NOPT): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        for j, o in enumerate(q["opts"]):
            if len(o[1]) < 60:
                bad.append((i, "explanation under 60 chars: %r" % o[1][:40]))
            opens = o[1].lstrip().lower().startswith("correct")
            if (j == q["c"]) != opens:
                bad.append((i, "the 'Correct' opener must mark exactly the key"))
        wrong = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if len(set(wrong)) == 1:
            bad.append((i, "every wrong choice shares one explanation"))
        mis = q.get("mis") or {}
        if set(mis) != set(o[0] for j, o in enumerate(q["opts"]) if j != q["c"]):
            bad.append((i, "`mis` must name exactly the three distractors"))
        if not q["q"].rstrip().endswith("?"):
            bad.append((i, "stem does not ask a question"))
        if not q.get("ordered") and q["c"] != 0:
            bad.append((i, "a non-ordered item must be authored with its key at 0"))
        if q.get("img"):
            if not os.path.exists(os.path.join(root, folder, q["img"])):
                bad.append((i, "image file missing: " + q["img"]))
            if not q.get("alt") or not q.get("slide"):
                bad.append((i, "picture question without alt or slide caption"))
    stems = [q["q"] for q in pool]
    for s in set(stems):
        if stems.count(s) > 1:
            bad.append((stems.index(s), "duplicate stem"))
    return bad


def key_clusters(pool):
    """Items whose keys say the same thing give each other away: at most one per set."""
    by = {}
    for i, q in enumerate(pool):
        k = re.sub(r"[^a-z0-9 ]", "", q["opts"][q["c"]][0].lower()).strip()
        by.setdefault(k, []).append(i)
    return [(1, ids) for ids in by.values() if len(ids) > 1]


def rotate(qs, rng):
    """Balance positions per set: ordered items stay where their value falls; the rest are rotated so the set's
    totals come out as even as possible (8/8/7/7 for 30)."""
    n = len(qs)
    want = [n // NOPT + (1 if p < n % NOPT else 0) for p in range(NOPT)]
    order = list(range(NOPT)); rng.shuffle(order)          # which positions get the extra one
    want = [want[order.index(p)] for p in range(NOPT)]
    fixed = Counter(q["c"] for q in qs if q.get("ordered"))
    targets = []
    for p in range(NOPT):
        targets += [p] * max(0, want[p] - fixed.get(p, 0))
    free = [q for q in qs if not q.get("ordered")]
    while len(targets) < len(free):                        # only if ordered items overfill a position
        targets.append(min(range(NOPT), key=lambda p: targets.count(p) + fixed.get(p, 0)))
    targets = targets[:len(free)]
    rng.shuffle(targets)
    for q, t in zip(free, targets):
        k = (t - q["c"]) % NOPT
        q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
        q["c"] = t
    return qs


def partition(POOL, TARGET, CLUSTERS, MUST_EACH, MUST_ANY, io_min, n_img, seed, out_path, root, folder,
              iters=100000):
    """io_min: {objective prefix such as "2 ": minimum per set}. Returns (set1, set2)."""
    rng = random.Random(seed)
    print("pool:", len(POOL))
    probs = validate(POOL, root, folder)
    print("schema problems:", probs or "none")
    assert not probs, "fix the pool before partitioning"
    for t in TARGET:
        assert any(q["topic"] == t for q in POOL), "no question for " + t
    extra = set(q["topic"] for q in POOL) - set(TARGET)
    assert not extra, extra
    assert sum(TARGET.values()) == 60, sum(TARGET.values())
    ALL_IOS = set(q["io"] for q in POOL)
    print("objectives:", len(ALL_IOS), " pool per objective:",
          dict(sorted(Counter(q["io"].split(" ")[0] for q in POOL).items())))
    print("pool per topic:", dict(Counter(q["topic"] for q in POOL)))
    print("pool gameable: %.0f%%   pool key uniquely longest: %.0f%%"
          % (gameable_pct(POOL), 100.0 * sum(map(uniquely_longest, POOL)) / len(POOL)))
    clusters = list(CLUSTERS) + key_clusters(POOL)

    def io_count(qs, pre):
        return sum(1 for q in qs if q["io"].startswith(pre))

    def score(idx, set_no):
        qs = [POOL[i] for i in idx]
        top = Counter(q["topic"] for q in qs)
        s = 0.0
        for t, n in TARGET.items():
            d = abs(top.get(t, 0) - n / 2.0)
            s += max(0.0, d - 0.5) * 12
            if n >= 2 and top.get(t, 0) == 0:
                s += 40
        ios = set(q["io"] for q in qs)
        s += 40 * len(ALL_IOS - ios)
        for pre, m in io_min.items():
            s += max(0, m - io_count(qs, pre)) * 15
        s += gameable_pct(qs) * 3.0
        longest = 100.0 * sum(map(uniquely_longest, qs)) / len(qs)
        shortest = 100.0 * sum(map(uniquely_shortest, qs)) / len(qs)
        s += max(0.0, longest - 30.0) + max(0.0, shortest - 35.0)
        pics = sum(1 for q in qs if q.get("img"))
        s += (pics * 200) if set_no == 1 else abs(pics - n_img) * 30
        ids = set(idx)
        for n, cl in clusters:
            s += max(0, len(ids & set(cl)) - n) * 30
        for g in MUST_EACH:
            if not ids & set(g):
                s += 50
        return s

    def total(ch):
        return score(ch[:30], 1) + score(ch[30:], 2) + sum(50 for g in MUST_ANY if not set(ch) & set(g))

    best, idx = None, list(range(len(POOL)))
    for _ in range(400):
        rng.shuffle(idx)
        ch = idx[:60]
        t = total(ch)
        if best is None or t < best[0]:
            best = (t, list(ch))
    cur_t, cur = best
    for _ in range(iters):
        used = set(cur)
        out = [i for i in range(len(POOL)) if i not in used]
        k = rng.randrange(60)
        cand = list(cur)
        if rng.random() < 0.5 and out:
            cand[k] = rng.choice(out)
        else:
            j = rng.randrange(60)
            cand[k], cand[j] = cand[j], cand[k]
        t = total(cand)
        if t <= cur_t:
            cur_t, cur = t, cand
    print("selection score: %.1f" % cur_t)

    ch = cur
    s1 = rotate([json.loads(json.dumps(POOL[i])) for i in ch[:30]], rng)
    s2 = rotate([json.loads(json.dumps(POOL[i])) for i in ch[30:]], rng)
    texts = [POOL[i]["opts"][POOL[i]["c"]][0] for i in ch]
    for q, want in zip(s1 + s2, texts):
        assert q["opts"][q["c"]][0] == want, "rotation moved an answer!"
        assert q["opts"][q["c"]][1].startswith("Correct"), "key lost its Correct opener"
    print("rotation check: every correct answer still points at its own text\n")

    assert not set(ch[:30]) & set(ch[30:]), "a question landed in both sets"
    assert not any(q.get("img") for q in s1), "a picture question reached Set 1"
    for g in MUST_EACH:
        assert set(ch[:30]) & set(g) and set(ch[30:]) & set(g), "a set misses: " + POOL[g[0]]["q"]
    for g in MUST_ANY:
        assert set(ch) & set(g), "a flagged item is in neither set: " + POOL[g[0]]["q"]
    for name, s, part in (("SET 1", s1, ch[:30]), ("SET 2", s2, ch[30:])):
        assert set(q["io"] for q in s) == ALL_IOS, "%s misses an objective" % name
        for pre, m in io_min.items():
            assert io_count(s, pre) >= m, "%s has too few objective %s items" % (name, pre.strip())
        top = Counter(q["topic"] for q in s)
        for t, n in TARGET.items():
            if n >= 2:
                assert top.get(t, 0) >= 1, "%s has no %s question" % (name, t)
        for n, cl in clusters:
            assert len(set(part) & set(cl)) <= n, "%s carries too many of a twin cluster: %s" % (
                name, POOL[cl[0]]["q"][:60])
        pos = Counter(q["c"] for q in s)
        assert max(pos.values()) <= 9 and min(pos.get(p, 0) for p in range(NOPT)) >= 6, \
            "%s answer positions skewed %s" % (name, pos)
        assert gameable_pct(s) < 10, "%s length-gameable %.0f%%" % (name, gameable_pct(s))
        print("   per topic:", ", ".join("%s %d" % (t, top.get(t, 0)) for t in TARGET))
        print("%s  n=%d  positions A/B/C/D %s  key uniquely longest %.0f%%  uniquely shortest %.0f%%"
              "  gameable %.0f%%  objectives %s  pictures: %d  ordered: %d"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 100.0 * sum(map(uniquely_longest, s)) / len(s),
                 100.0 * sum(map(uniquely_shortest, s)) / len(s),
                 gameable_pct(s), dict(sorted(Counter(q["io"].split(" ")[0] for q in s).items())),
                 sum(1 for q in s if q.get("img")), sum(1 for q in s if q.get("ordered"))))
    assert sum(1 for q in s2 if q.get("img")) == n_img, "Set 2 should carry %d pictures" % n_img
    json.dump({"set1": s1, "set2": s2}, open(out_path, "w"), ensure_ascii=False, indent=1)
    print("\nwrote " + os.path.basename(out_path))
    return s1, s2
