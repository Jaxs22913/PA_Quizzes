#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five Updated CMS I Exam 2 ophthalmology Master Exams (65 each).

Loads all fifteen cmsophtho_*_pool.py files -- 325 questions written from the
five ophthalmology decks -- and does the three things the pools cannot do for
themselves:

  ANSWER POSITIONS. Every question is authored with the correct choice FIRST,
  because _cmsophtho_style.Q asserts the key's explanation opens "Correct".
  Rendering a pool straight out would make all five forms answerable without
  reading -- the PD1 bug, see [[answer_position_bias_check]]. Options are
  permuted here onto a balanced A-E cycle.

  STRATIFICATION. Each form draws proportionally from all five lectures and
  carries a fixed quota of diagnosis and treatment lead-ins, so every form is a
  genuine cumulative rehearsal weighted the way Jaxon asked -- "mostly vignettes
  and geared towards treatments and diagnosis" -- rather than over-weighting
  Lecture 10 simply because it is the biggest deck.

  NO REPEATS. 325 questions, 325 slots: each question appears in exactly one
  form, so working all five gives 325 distinct items.

    python3 tools/cmsophtho_partition.py
"""
import importlib.util, os, json, random, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FORMS = ["A", "B", "C", "D", "E"]
PER_FORM = 65
DIAG_PER_FORM = 11          # 56 diagnosis items / 5 forms, floored
TX_PER_FORM = 15            # 78 treatment items / 5 forms, floored
SEED = 20260906

POOLS = ["l10", "l10b", "l10c", "l10d", "l11", "l11b", "l12", "l12b", "l12c",
         "l13", "l13b", "l13c", "l14", "l14b", "l14c"]
LECTURE = {"l10": "10", "l11": "11", "l12": "12", "l13": "13", "l14": "14"}

# Same bar as the derm masters. 0% is NOT the target: the reference questions
# Jaxon supplied sit at 13%, because a real answer is sometimes just longer.
MARGIN_CHARS, MARGIN_FRAC, BAR = 8, 0.18, 0.35


def _load(name, attr="QUESTIONS"):
    path = os.path.join(HERE, "cmsophtho_%s_pool.py" % name)
    spec = importlib.util.spec_from_file_location("m_" + name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


def gameable(opts, c):
    """True if the key is long enough to be picked without reading the stem."""
    L = [len(o[0]) for o in opts]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= MARGIN_CHARS and L[c] >= runner * (1 + MARGIN_FRAC)


def build():
    pools = {k: _load(k) for k in POOLS}

    # --- shorten over-long correct answers ---------------------------------
    # Displaced detail is appended to the KEY's own explanation, so nothing the
    # slides taught disappears -- it just stops being visible in the option list,
    # where its length was the giveaway.
    spec = importlib.util.spec_from_file_location(
        "shortfix", os.path.join(HERE, "cmsophtho_shortfix.py"))
    sf = importlib.util.module_from_spec(spec); spec.loader.exec_module(sf)
    for (k, i), (text, extra) in sf.SHORT.items():
        q = pools[k][i]
        c = q["c"]
        assert len(text) < len(q["opts"][c][0]), "%s:%d shortfix is not shorter" % (k, i)
        q["opts"][c][0] = text
        if extra:
            q["opts"][c][1] = q["opts"][c][1].rstrip() + " " + extra
        assert len({o[0].strip().lower() for o in q["opts"]}) == 5, \
            "%s:%d shortened key collides with a distractor" % (k, i)
    print("correct answers shortened: %d" % len(sf.SHORT))

    flat = [q for k in POOLS for q in pools[k]]
    assert len(flat) == PER_FORM * len(FORMS), \
        "%d questions for %d slots" % (len(flat), PER_FORM * len(FORMS))

    for q in flat:                                     # lecture number for stratifying
        q["_lec"] = LECTURE[re.match(r"(l\d+)", [k for k in POOLS
                                                 if q in pools[k]][0]).group(1)] \
                    if False else None
    for k in POOLS:                                    # cheaper, and unambiguous
        lec = LECTURE[re.match(r"(l\d+)", k).group(1)]
        for q in pools[k]:
            q["_lec"] = lec

    vig = re.compile(r"\b\d{1,2}-(year|month|week|day)-old\b|\bnewborn\b|\binfant\b")
    nv = sum(bool(vig.search(q["q"])) for q in flat)
    print("questions: %d   patient vignettes: %d = %.0f%%" % (len(flat), nv, 100 * nv / len(flat)))
    print("lead-ins:", dict(collections.Counter(q["lead"] for q in flat)))
    print("lectures:", dict(sorted(collections.Counter(q["_lec"] for q in flat).items())))

    before = sum(gameable(q["opts"], q["c"]) for q in flat)
    print("length-gameable: %d/%d = %.0f%%  (bar %.0f%%)"
          % (before, len(flat), 100 * before / len(flat), 100 * BAR))
    if before / len(flat) >= BAR:
        for k in POOLS:
            for i, q in enumerate(pools[k]):
                if gameable(q["opts"], q["c"]):
                    r = max(len(o[0]) for j, o in enumerate(q["opts"]) if j != q["c"])
                    print('  ("%s", %d): %d->%d  %s' % (k, i, len(q["opts"][q["c"]][0]), r,
                                                      q["opts"][q["c"]][0]))
        raise AssertionError("length bias over the bar -- shorten keys, never pad distractors")

    # --- partition -------------------------------------------------------
    # Group into (lecture, lead-in) cells, then deal ONE continuous round-robin
    # across the cells laid end to end. Each cell of size n therefore gives every
    # form either floor(n/5) or ceil(n/5) items, and because the cursor carries
    # over between cells the leftovers rotate instead of always landing on Form A.
    # 325 = 5 x 65 exactly, so every form fills without a top-up pass -- and no
    # form can miss a lecture, which a per-quota draw did (Form A lost Lecture 11,
    # the smallest deck, because its diagnosis and treatment quotas were filled
    # from the big decks first).
    rng = random.Random(SEED)
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

    # --- permute options onto a balanced A-E cycle, WITHIN each form -------
    # Every question is authored with the correct choice first (_cmsophtho_style.Q
    # asserts the key's explanation opens "Correct"), so rendering a pool straight
    # out would make all five forms answerable without reading -- the PD1 bug, see
    # [[answer_position_bias_check]]. Doing this per form rather than across the
    # whole bank is what makes each form land on exactly 13 of each letter; a
    # single global cycle left Form A with 18 A's and 7 B's.
    assert PER_FORM % 5 == 0, "per-form balance needs a multiple of five"
    before = sum(gameable(q["opts"], q["c"]) for q in flat)
    for f in FORMS:
        order = list(range(5)) * (PER_FORM // 5)
        rng.shuffle(order)
        for n, q in enumerate(forms[f]):
            target = order[n]
            correct = q["opts"][q["c"]]
            rest = [o for i, o in enumerate(q["opts"]) if i != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:target] + [correct] + rest[target:]
            q["c"] = target
            assert q["opts"][q["c"]] is correct
    after = sum(gameable(q["opts"], q["c"]) for q in flat)
    assert after == before, "permutation must not change the length-bias count"

    seen = collections.Counter(id(q) for v in forms.values() for q in v)
    assert max(seen.values()) == 1, "a question landed in two forms"
    assert len(seen) == len(flat), "%d of %d questions used" % (len(seen), len(flat))

    for f in FORMS:
        assert len(forms[f]) == PER_FORM, (f, len(forms[f]))
        pos = collections.Counter(q["c"] for q in forms[f])
        lead = collections.Counter(q["lead"] for q in forms[f])
        lec = collections.Counter(q["_lec"] for q in forms[f])
        gm = sum(gameable(q["opts"], q["c"]) for q in forms[f])
        nvg = sum(bool(vig.search(q["q"])) for q in forms[f])
        assert len(lec) == 5, "form %s misses a lecture: %s" % (f, sorted(lec))
        print("  Form %s: dx=%-2d tx=%-2d  lectures=%s  vignettes=%.0f%%  gameable=%.0f%%  pos=%s"
              % (f, lead["diagnosis"], lead["treatment"],
                 dict(sorted(lec.items())), 100 * nvg / PER_FORM, 100 * gm / PER_FORM,
                 {"ABCDE"[k]: v for k, v in sorted(pos.items())}))

    for v in forms.values():
        for q in v:
            q.pop("_lec", None)
    out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2", "master-exams-updated.json")
    json.dump({f: forms[f] for f in FORMS}, open(out, "w"), indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(out, ROOT))
    return forms


if __name__ == "__main__":
    build()
