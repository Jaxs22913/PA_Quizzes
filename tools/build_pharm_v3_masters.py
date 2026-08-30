#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble Master Exam set 2 (forms F-J) for Pharmacology I Exam 1.

Unlike build_master_exams.py, which samples questions already published in the
topic quizzes, this set is built from a pool written specifically for it -- the
first five forms had already consumed 300 of the 400 available questions, so a
second set drawn from the same pool would have repeated most of them.

Three things are enforced here rather than trusted:
  ROTATION. Every question is authored with its correct answer at index 0 so the
  author cannot drift towards a favourite position. The key is then moved to a
  rotating slot, giving a flat distribution by construction.
  NO REPEATS. Stems are checked against all 400 existing questions and against
  each other; a collision is a hard error, not a silent drop.
  PROPORTIONAL. Each form draws from all three lectures in the ratio the pool
  itself has, so all five are genuinely cumulative and comparable.
"""
import os, re, sys, json, random
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
D = os.path.join(ROOT, "Pharmacology I Exam 1")

POOLS = ["pharm_v3_pool_l1a", "pharm_v3_pool_l1b", "pharm_v3_pool_l1c",
         "pharm_v3_pool_l2", "pharm_v3_pool_l3a", "pharm_v3_pool_l3b"]

pool = []
for m in POOLS:
    mod = __import__(m)
    for q in mod.QUESTIONS:
        q = dict(q)
        q["_pool"] = m
        pool.append(q)
print("pool: %d questions from %d files" % (len(pool), len(POOLS)))

# ---- every question must be 4-option with an explanation on every choice ----
for q in pool:
    assert len(q["opts"]) == 4, "not four options: %s" % q["q"]
    for o in q["opts"]:
        assert len(o) == 2 and o[1].strip(), "option missing its explanation: %s" % q["q"]
    assert q["opts"][0][1].startswith(("Correct", "correct")), \
        "index 0 is meant to be the correct answer: %s" % q["q"]

# ---- no stem may repeat, inside the pool or against what is already published ----
existing = set()
SKIP = ("guide", "cram", "chart", "osce", "master", "what-to-star",
        "contraindications", "indications", "side-effects")
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".html") or any(k in fn for k in SKIP):
        continue
    s = open(os.path.join(D, fn), encoding="utf8").read()
    m = re.search(r'const (?:QUESTIONS|DATA|QUIZ_DATA)\s*=\s*(\[.*?\]);\s*\n', s, re.S)
    if m:
        for q in json.loads(m.group(1)):
            existing.add(re.sub(r"\W+", " ", q["q"].lower()).strip())

def norm(s):
    return re.sub(r"\W+", " ", s.lower()).strip()

seen, dupes = set(), []
for q in pool:
    n = norm(q["q"])
    if n in existing:
        dupes.append(("already published", q["q"]))
    if n in seen:
        dupes.append(("repeated in pool", q["q"]))
    seen.add(n)
if dupes:
    for why, s in dupes:
        print("  DUPLICATE (%s): %s" % (why, s))
    sys.exit("refusing to build on duplicated stems")
print("no duplicate stems against the 400 published questions or within the pool")

# ---- rotate the key off index 0 ----
rng = random.Random(20260830)
by_pool = defaultdict(list)
for q in pool:
    by_pool[q["_pool"]].append(q)
for name in POOLS:                       # rotate within each pool, offset per pool
    for i, q in enumerate(by_pool[name]):
        tgt = (i + POOLS.index(name)) % 4
        opts = q["opts"]
        correct = opts[0]
        rest = opts[1:]
        q["opts"] = rest[:tgt] + [correct] + rest[tgt:]
        q["c"] = tgt
        assert q["opts"][q["c"]] is correct

print("key distribution after rotation: %s" % sorted(Counter(q["c"] for q in pool).items()))

# ---- length bias: the key must not be uniquely longest by a gameable margin ----
def gameable(q):
    L = [len(re.sub(r"<[^>]+>", "", o[0])) for o in q["opts"]]
    k = L[q["c"]]
    others = [x for i, x in enumerate(L) if i != q["c"]]
    return k > max(others) and k - max(others) >= 8 and k >= 1.18 * max(others)
flagged = [q for q in pool if gameable(q)]
print("gameable by length: %d of %d (%.1f%%)" % (len(flagged), len(pool), 100.0*len(flagged)/len(pool)))
for q in flagged:
    print("   %s" % q["q"][:88])

# ---- split into five proportional forms ----
LEC = {"pharm_v3_pool_l1a": "L1", "pharm_v3_pool_l1b": "L1", "pharm_v3_pool_l1c": "L1",
       "pharm_v3_pool_l2": "L2", "pharm_v3_pool_l3a": "L3", "pharm_v3_pool_l3b": "L3"}
groups = defaultdict(list)
for q in pool:
    groups[LEC[q["_pool"]]].append(q)
for g in groups.values():
    rng.shuffle(g)
print("\nby lecture: %s" % {k: len(v) for k, v in sorted(groups.items())})

NFORMS, SIZE = 5, 60
quota = {}
total = sum(len(v) for v in groups.values())
for lec, qs in groups.items():
    quota[lec] = int(round(SIZE * len(qs) / float(total)))
while sum(quota.values()) > SIZE:
    quota[max(quota, key=quota.get)] -= 1
while sum(quota.values()) < SIZE:
    quota[min(quota, key=quota.get)] += 1
print("per-form quota: %s (sums to %d)" % (quota, sum(quota.values())))
for lec, n in quota.items():
    need = n * NFORMS
    assert len(groups[lec]) >= need, "%s: need %d, pool has %d" % (lec, need, len(groups[lec]))

forms = {}
cursor = defaultdict(int)
for idx, name in enumerate("FGHIJ"):
    form = []
    for lec, n in sorted(quota.items()):
        form += groups[lec][cursor[lec]:cursor[lec] + n]
        cursor[lec] += n
    rng.shuffle(form)
    # rebalance keys within the form so concatenation cannot clump them
    order = [0, 1, 2, 3] * (SIZE // 4 + 1)
    rng.shuffle(order)
    for q, tgt in zip(form, order):
        if q["c"] != tgt:
            opts = q["opts"]
            correct = opts[q["c"]]
            rest = [o for i, o in enumerate(opts) if i != q["c"]]
            q["opts"] = rest[:tgt] + [correct] + rest[tgt:]
            q["c"] = tgt
    forms[name] = [{k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite")} for q in form]
    print("form %s: %d questions, keys %s" % (name, len(form), sorted(Counter(q["c"] for q in form).items())))

allq = [q["q"] for f in forms.values() for q in f]
assert len(allq) == len(set(allq)), "a question landed in two forms"
print("\n%d distinct questions across the five forms" % len(allq))

out = os.path.join(D, "master-exams-set2.json")
json.dump(forms, open(out, "w", encoding="utf8"), ensure_ascii=False, indent=1)
print("wrote %s" % os.path.basename(out))
