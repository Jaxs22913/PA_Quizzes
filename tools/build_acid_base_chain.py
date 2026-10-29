#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Acid-Base Case Chain data: tools/abchain_<set>.py -> arcade-chain/<set>.json (+ the arcade.js registry).

    python3 tools/build_acid_base_chain.py          # writes both sets, then run tools/check_acid_base_cases.py

Layers: the case files hold the patient, the numbers, the declared intent and the hand-written clinical steps;
tools/abchain_common.py turns the numbers into the arithmetic steps; this script orders the options, balances the
key positions, writes the JSON the page reads, and refreshes the CHAIN_SETS block in arcade.js (between the
ABCHAIN-SETS markers) so the Arcade card counts never drift from the data. Never hand-edit the JSON.

Option order: number sets (Winter range, anion gap) stay ascending with the key where its value falls (WRITER.md
rule 8); every other step gets a key position from a balanced, seeded list, so each of A-D is keyed about equally
often across a set, and the distractors are shuffled with the same seed.
"""
import hashlib, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from abchain_common import (Ctx, GEN, NUMERIC, COURSES, LABEL, UNIT, ORDER, computed_answers, chron_prompt, cite,
                            f, fph, ag_read_prompt, ag_calc_prompt)
import abchain_pdm_e4
import abchain_cms_e6

MODULES = [abchain_pdm_e4, abchain_cms_e6]
OUT = os.path.join(ROOT, "arcade-chain")
# word labels for the phone lab strip (the full table keeps LABEL's "ABBREV (full term)" form)
SHORT = {"ph": "pH", "pco2": "Carbon dioxide", "hco3": "Bicarbonate", "po2": "Oxygen", "na": "Sodium",
         "cl": "Chloride", "k": "Potassium", "alb": "Albumin"}
SEED = 20261029


def lab_rows(course, labs):
    cfg = COURSES[course]
    rows = []
    for k in ORDER:
        if k not in labs:
            continue
        v = labs[k]
        if k == "ph":
            vs = fph(v)
        elif k in ("k", "alb"):
            vs = "%.1f" % v
        else:
            vs = f(v)
        lo, hi = cfg[k]
        rtext = ("greater than %s" % f(lo)) if hi is None else "%s to %s" % (
            fph(lo) if k == "ph" else ("%.1f" % lo if k in ("k", "alb") else f(lo)),
            fph(hi) if k == "ph" else ("%.1f" % hi if k in ("k", "alb") else f(hi)))
        rows.append(dict(k=k, label=LABEL[k], short=SHORT[k], v=vs, n=v, unit=UNIT[k], range=rtext, lo=lo, hi=hi))
    return rows


def raw_steps(mod, case):
    x = Ctx(mod.COURSE, case)
    got = computed_answers(x)
    for k, v in case["expect"].items():
        assert got.get(k) == v, "%s: declared %s=%r but the numbers give %r" % (case["id"], k, v, got.get(k))
    out = []
    for st in case["steps"]:
        kind, arg = (st if isinstance(st, tuple) else (st, None))
        if kind in ("cause", "next"):
            d = case[kind]
            opts = [(t, e) for (t, cat, e) in d["options"]]
            cats = [cat for (t, cat, e) in d["options"]]
            key, walk, slides, prompt = d["key"], d["walk"], d["slides"], d["prompt"]
            label = "Cause" if kind == "cause" else "Next step"
        else:
            label, prompt, gen = GEN[kind]
            if kind == "chronicity":
                prompt = chron_prompt(x)
            elif kind == "ag_read":
                prompt = ag_read_prompt(x)
            elif kind == "ag_calc":
                prompt = ag_calc_prompt(x)
            if kind in NUMERIC:
                opts, key, walk, slides = gen(x, arg)
            elif kind == "alk_comp":
                opts, key, walk, slides = gen(x, case.get("alk_tail", ""))
            else:
                opts, key, walk, slides = gen(x)
            cats = None
        texts = [t for t, _ in opts]
        assert len(opts) == 4 and len(set(texts)) == 4, "%s/%s: need four distinct options: %s" % (case["id"], kind,
                                                                                                  texts)
        assert key in texts, "%s/%s: key %r not among options" % (case["id"], kind, key)
        for t, e in opts:
            if t == key:
                assert e.startswith("Correct."), "%s/%s: key explanation must open 'Correct.'" % (case["id"], kind)
            else:
                assert not e.startswith("Correct"), "%s/%s: wrong option opens 'Correct'" % (case["id"], kind)
        out.append(dict(kind=kind, label=label, prompt=prompt, opts=opts, cats=cats, key=key, walk=walk,
                        cite=cite(COURSES[mod.COURSE], slides)))
    return out


def build_set(mod):
    rnd = random.Random("%s-%s" % (SEED, mod.SET["id"]))
    cases = [(c, raw_steps(mod, c)) for c in mod.CASES]
    n_label = sum(1 for _, steps in cases for s in steps if s["kind"] not in NUMERIC)
    positions = [i % 4 for i in range(n_label)]
    rnd.shuffle(positions)
    pi = 0
    out_cases = []
    nsteps = 0
    for n, (c, steps) in enumerate(cases, 1):
        js = []
        for i, s in enumerate(steps, 1):
            opts = list(s["opts"])
            cats = list(s["cats"]) if s["cats"] else None
            if s["kind"] in NUMERIC:
                order = list(range(4))            # generator already sorted ascending
            else:
                kidx = [t for t, _ in opts].index(s["key"])
                others = [j for j in range(4) if j != kidx]
                rnd.shuffle(others)
                pos = positions[pi]
                pi += 1
                order = others[:pos] + [kidx] + others[pos:]
            o = [opts[j] for j in order]
            cj = [cats[j] for j in order] if cats else None
            key = [t for t, _ in o].index(s["key"])
            step = dict(id="s%d" % i, kind=s["kind"], label=s["label"], prompt=s["prompt"],
                        options=[dict(t=t, e=e) for t, e in o], key=key, walk=s["walk"], cite=s["cite"])
            if cj:
                for od, cat in zip(step["options"], cj):
                    od["cat"] = cat
            js.append(step)
        nsteps += len(js)
        oc = dict(id=c["id"], n=n, title="Case %d" % n, who=c["who"], vignette=c["vignette"],
                  labs=lab_rows(mod.COURSE, c["labs"]), steps=js, summary=c["summary"])
        for k in ("urine_cl", "volume"):
            if k in c:
                oc[k] = c[k]
        out_cases.append(oc)
    data = dict(mod.SET)
    data.update(course_code=mod.COURSE, deck=COURSES[mod.COURSE]["deck"], cases=out_cases, version=1)
    return data, len(out_cases), nsteps


def write_registry(meta):
    path = os.path.join(ROOT, "arcade.js")
    src = open(path, encoding="utf-8").read()
    a, b = "  // <!--ABCHAIN-SETS-->", "  // <!--/ABCHAIN-SETS-->"
    assert a in src and b in src, "arcade.js is missing the ABCHAIN-SETS markers"
    lines = [a, "  // written by tools/build_acid_base_chain.py from arcade-chain/*.json; do not hand-edit"]
    for m in meta:
        lines.append('  { id: "%s", name: "%s", course: "%s", exam: "%s", color: "accent3", cases: %d, steps: %d, '
                     'ver: "%s" },' % (m["id"], m["name"], m["course"], m["exam"], m["cases"], m["steps"], m["ver"]))
    lines.append(b)
    new = re.sub(re.escape(a) + r".*?" + re.escape(b), lambda _: "\n".join(lines), src, flags=re.S)
    if new != src:
        open(path, "w", encoding="utf-8").write(new)
    return new != src


def main():
    os.makedirs(OUT, exist_ok=True)
    meta = []
    for mod in MODULES:
        data, nc, ns = build_set(mod)
        path = os.path.join(OUT, data["id"] + ".json")
        s = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        open(path, "w", encoding="utf-8").write(s)
        meta.append(dict(id=data["id"], name=data["name"], course=data["course"], exam=data["exam"], cases=nc,
                         steps=ns, ver=hashlib.sha1(s.encode("utf-8")).hexdigest()[:10]))
        print("wrote %-28s %2d cases, %3d steps, %5.1f KB" % (os.path.relpath(path, ROOT), nc, ns, len(s) / 1024.0))
    changed = write_registry(meta)
    print("arcade.js CHAIN_SETS", "updated" if changed else "unchanged")


if __name__ == "__main__":
    main()
