# -*- coding: utf-8 -*-
"""Assemble the five Updated CMS derm Master Exams (65 questions each).

Loads every cmsderm_l*_pool.py, applies the distractor padding in
cmsderm_lengthfix.py, then does three things the source pools cannot do for
themselves:

  ANSWER POSITIONS. Every question was authored with the correct choice first,
  which would make all five forms answerable without reading (see
  [[answer_position_bias_check]] -- this is exactly the PD1 bug). Options are
  permuted so the key lands on a balanced A-E cycle.

  STRATIFICATION. Each form draws proportionally from all nine lectures, so all
  five are genuinely cumulative and comparable rather than over-weighting
  whichever lecture happened to get the most questions.

  NO REPEATS. 326 questions, 325 slots -- no question appears in two forms.

    python3 tools/cmsderm_partition.py
"""
import importlib.util, glob, os, json, random, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FORMS = ["A", "B", "C", "D", "E"]
PER_FORM = 65
SEED = 20260826

MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def _load(path, attr):
    spec = importlib.util.spec_from_file_location("m", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= MARGIN_CHARS and L[c] >= runner * (1 + MARGIN_FRAC)


def build():
    fixes = _load(os.path.join(HERE, "cmsderm_lengthfix.py"), "FIX")
    pools = {}
    for f in sorted(glob.glob(os.path.join(HERE, "cmsderm_l*_pool.py"))):
        key = os.path.basename(f).replace("cmsderm_", "").replace("_pool.py", "")
        pools[key] = _load(f, "QUESTIONS")

    stems = _load(os.path.join(HERE, "cmsderm_stemfix.py"), "STEM")
    for (key, qi), new_stem in stems.items():
        q = pools[key][qi]
        assert q["q"].endswith("?"), f"{key}:{qi} stem has no lead-in"
        assert new_stem.rstrip().endswith("?"), f"{key}:{qi} rewrite has no lead-in"
        q["q"] = new_stem
    print(f"stems rewritten as patient vignettes: {len(stems)}")

    short = _load(os.path.join(HERE, "cmsderm_shortfix.py"), "OPTS")
    leads = _load(os.path.join(HERE, "cmsderm_shortfix.py"), "LEAD")
    for (key, qi), new_lead in leads.items():
        q = pools[key][qi]
        parts = re.split(r"(?<=[.!?])\s+", q["q"].strip())
        assert parts[-1].endswith("?"), f"{key}:{qi} final sentence is not the lead-in"
        q["q"] = " ".join(parts[:-1] + [new_lead])
    for (key, qi), texts in short.items():
        q = pools[key][qi]
        assert len(texts) == 5, f"{key}:{qi}"
        assert len({t.strip().lower() for t in texts}) == 5, f"{key}:{qi} duplicate option"
        q["opts"] = [[t, q["opts"][i][1]] for i, t in enumerate(texts)]
    print(f"option sets cut to reference length: {len(short)}  (lead-ins narrowed: {len(leads)})")

    expl = _load(os.path.join(HERE, "cmsderm_explfix.py"), "EXPL")
    for (key, qi, oi), new_e in expl.items():
        q = pools[key][qi]
        assert oi != q["c"], f"explfix would rewrite the KEYED answer at {key}:{qi}"
        assert not new_e.startswith("Correct"), f"{key}:{qi}:{oi} distractor must not read as correct"
        q["opts"][oi][1] = new_e
    print(f"thin refutations strengthened: {len(expl)}")

    # Padding retired 2026-08-27. It was the wrong fix: the bias came from
    # over-long CORRECT answers, so cmsderm_shortfix.py cures both at once.
    # cmsderm_lengthfix.py is kept in the tree only as a record of what was tried.
    _ = fixes


    flat = [(k, i, q) for k, v in pools.items() for i, q in enumerate(v)]
    vig = [q for _, _, q in flat if re.match(r"A(n)? \d+-(year|month|week|day)-old|A newborn|The mother of a \d+", q["q"])]
    print(f"patient vignettes: {len(vig)}/{len(flat)} = {len(vig)/len(flat):.0%}")
    before = sum(gameable(q["opts"], q["c"]) for _, _, q in flat)
    print(f"gameable after padding: {before}/{len(flat)} = {before/len(flat):.1%}  (bar 35%)")

    # --- permute options onto a balanced A-E cycle ---
    rng = random.Random(SEED)
    order = list(range(5)) * (len(flat) // 5 + 1)
    rng.shuffle(order)
    for n, (_, _, q) in enumerate(flat):
        target = order[n]
        correct = q["opts"][q["c"]]
        rest = [o for i, o in enumerate(q["opts"]) if i != q["c"]]
        rng.shuffle(rest)
        q["opts"] = rest[:target] + [correct] + rest[target:]
        q["c"] = target
        assert q["opts"][q["c"]] is correct

    after = sum(gameable(q["opts"], q["c"]) for _, _, q in flat)
    assert after == before, "permutation must not change the length-bias count"
    print("answer positions:", dict(collections.Counter("ABCDE"[q["c"]] for _, _, q in flat)))

    # --- stratified partition, no repeats ---
    by_pool = collections.defaultdict(list)
    for k, i, q in flat:
        by_pool[k].append(q)
    for k in by_pool:
        rng.shuffle(by_pool[k])

    total = sum(len(v) for v in by_pool.values())
    quota = {k: round(len(v) / total * PER_FORM) for k, v in by_pool.items()}
    forms = {f: [] for f in FORMS}
    cursor = {k: 0 for k in by_pool}
    for f in FORMS:
        for k, n in quota.items():
            take = by_pool[k][cursor[k]:cursor[k] + n]
            cursor[k] += len(take)
            forms[f].extend(take)
        # top up or trim to exactly PER_FORM from the deepest remaining pool
        while len(forms[f]) < PER_FORM:
            k = max(by_pool, key=lambda k: len(by_pool[k]) - cursor[k])
            forms[f].append(by_pool[k][cursor[k]]); cursor[k] += 1
        forms[f] = forms[f][:PER_FORM]
        rng.shuffle(forms[f])

    seen = collections.Counter(id(q) for v in forms.values() for q in v)
    assert max(seen.values()) == 1, "a question landed in two forms"
    for f in FORMS:
        assert len(forms[f]) == PER_FORM, (f, len(forms[f]))
        pos = collections.Counter(q["c"] for q in forms[f])
        gm = sum(gameable(q["opts"], q["c"]) for q in forms[f])
        lec = len({q["cite"].split(",")[0] for q in forms[f]})
        print(f"  Form {f}: {len(forms[f])}q  decks={lec}  gameable={gm/PER_FORM:.0%}  "
              f"positions={ {'ABCDE'[k]: v for k, v in sorted(pos.items())} }")

    out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1", "master-exams-updated.json")
    json.dump({f: forms[f] for f in FORMS}, open(out, "w"), indent=1, ensure_ascii=False)
    print("wrote", out)
    return forms


if __name__ == "__main__":
    build()
