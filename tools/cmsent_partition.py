#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five CMS I Exam 3 (ENT) Master Exams.

Loads every cmsent_*_pool.py and does the four things the pools cannot do for
themselves.

  ANSWER POSITIONS. Every question is authored with the correct choice first,
  because _cmsent_style.Q asserts the key's explanation opens "Correct".
  Rendering a pool straight out would make all five forms answerable without
  reading -- the PD1 bug, see [[answer_position_bias_check]]. Options are
  permuted here, PER FORM, so each form lands as close to even across A-D as
  fifty questions allow (13/13/12/12 rather than a national average that hides
  a skewed individual paper).

  STRATIFICATION. Each form draws from all five lectures in proportion, so
  every form is a genuine cumulative rehearsal rather than a sample of whichever
  lecture had the most questions written for it.

  NO REPEATS. No question appears in two forms, so working all five gives five
  times fifty distinct items.

  LENGTH BIAS. Reported, not silently accepted. The bar is the same as the other
  master sets; 0% is not the target, because a real answer is sometimes longer.

    python3 tools/cmsent_partition.py
"""
import importlib.util, os, json, random, re, collections, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FORMS = ["A", "B", "C", "D", "E"]
PER_FORM = 50
NOPT = 4
SEED = 20260908
MARGIN_CHARS, MARGIN_FRAC, BAR = 8, 0.18, 0.35

LECTURE = {"CMS I Disorders of the External and Middle Ear": "L15",
           "16. Disorders of Inner Ear": "L16",
           "hughie Nose & Paranasal Sinuses": "L17",
           "CMS I Neoplasms and Neck Masses": "L18",
           "CMS I Disorders of the Oral Cavity, Salivary Glands": "L19"}


def _load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.QUESTIONS


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= MARGIN_CHARS and L[c] >= runner * (1 + MARGIN_FRAC)


def build(strict=True):
    spec = importlib.util.spec_from_file_location(
        "shortfix", os.path.join(HERE, "cmsent_shortfix.py"))
    sf = importlib.util.module_from_spec(spec); spec.loader.exec_module(spec and sf)

    flat = []
    for f in sorted(glob.glob(os.path.join(HERE, "cmsent_*_pool.py"))):
        key = os.path.basename(f)[:-3]
        for i, q in enumerate(_load(f)):
            q["_lec"] = LECTURE[q["deck"]]
            # Shorten the key BEFORE anything else looks at option lengths. The
            # displaced clause is already in the key's own explanation, which is
            # where a reason belongs -- see cmsent_shortfix.py.
            new = sf.SHORT.get((key, i))
            if new:
                c = q["c"]
                assert len(new) < len(q["opts"][c][0]), "%s:%d not shorter" % (key, i)
                q["opts"][c][0] = new
                assert len({o[0].strip().lower() for o in q["opts"]}) == 4, \
                    "%s:%d shortened key collides with a distractor" % (key, i)
            flat.append(q)
    print("correct answers shortened: %d" % len(sf.SHORT))

    print("questions in the pools: %d   need %d" % (len(flat), PER_FORM * len(FORMS)))
    print("by lecture:", dict(sorted(collections.Counter(q["_lec"] for q in flat).items())))
    print("lead-ins:", dict(collections.Counter(q["lead"] for q in flat)))

    dup = [k for k, v in collections.Counter(q["q"] for q in flat).items() if v > 1]
    assert not dup, "duplicate stem: %r" % dup[:3]

    expl = [len(o[1]) for q in flat for o in q["opts"]]
    print("explanation length: min %d, mean %d, max %d"
          % (min(expl), sum(expl) // len(expl), max(expl)))

    before = sum(gameable(q["opts"], q["c"]) for q in flat)
    print("length-gameable: %d/%d = %.0f%%  (bar %.0f%%)"
          % (before, len(flat), 100 * before / len(flat), 100 * BAR))
    if before / len(flat) >= BAR:
        for q in flat:
            if gameable(q["opts"], q["c"]):
                r = max(len(o[0]) for i, o in enumerate(q["opts"]) if i != q["c"])
                print("   %d->%d  %s" % (len(q["opts"][q["c"]][0]), r, q["opts"][q["c"]][0][:70]))
        raise AssertionError("length bias over the bar -- shorten keys, never pad distractors")

    need = PER_FORM * len(FORMS)
    if len(flat) < need:
        msg = "pools hold %d questions, five forms of %d need %d" % (len(flat), PER_FORM, need)
        if strict:
            raise AssertionError(msg)
        print("!! %s -- building short forms for a pipeline check" % msg)

    rng = random.Random(SEED)
    per_form = min(PER_FORM, len(flat) // len(FORMS))

    # deal one continuous round-robin over (lecture, lead-in) cells, so the
    # leftovers rotate instead of always landing on Form A
    cells = collections.defaultdict(list)
    for q in flat:
        cells[(q["_lec"], q["lead"])].append(q)
    for v in cells.values():
        rng.shuffle(v)
    forms = {f: [] for f in FORMS}
    n = 0
    for key in sorted(cells):
        for q in cells[key]:
            forms[FORMS[n % len(FORMS)]].append(q)
            n += 1
    for f in FORMS:
        rng.shuffle(forms[f])
        forms[f] = forms[f][:per_form]

    # permute the key off position 0, within each form
    for f in FORMS:
        order = [i % NOPT for i in range(len(forms[f]))]
        rng.shuffle(order)
        for i, q in enumerate(forms[f]):
            target = order[i]
            correct = q["opts"][q["c"]]
            rest = [o for j, o in enumerate(q["opts"]) if j != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:target] + [correct] + rest[target:]
            q["c"] = target
            assert q["opts"][q["c"]] is correct

    seen = collections.Counter(id(q) for v in forms.values() for q in v)
    assert not seen or max(seen.values()) == 1, "a question landed in two forms"

    for f in FORMS:
        pos = collections.Counter(q["c"] for q in forms[f])
        lec = collections.Counter(q["_lec"] for q in forms[f])
        gm = sum(gameable(q["opts"], q["c"]) for q in forms[f])
        print("  Form %s: %2dq  lectures=%s  gameable=%.0f%%  pos=%s"
              % (f, len(forms[f]), dict(sorted(lec.items())),
                 100 * gm / max(1, len(forms[f])),
                 {"ABCD"[k]: v for k, v in sorted(pos.items())}))

    for v in forms.values():
        for q in v:
            q.pop("_lec", None)
            q.pop("deck", None)
            q.pop("lead", None)
    out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3", "master-exams.json")
    json.dump({f: forms[f] for f in FORMS}, open(out, "w"), indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(out, ROOT))
    return forms


if __name__ == "__main__":
    import sys
    build(strict="--allow-short" not in sys.argv)
