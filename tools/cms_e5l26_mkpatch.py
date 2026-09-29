#!/usr/bin/env python3
"""Turn reviewer JSON (scratch) into tools/cms_e5l26_patch.py, keyed by the ORIGINAL stem.

    python3 tools/cms_e5l26_mkpatch.py judge_io.json:cms_e5l26_sets.json judge_vig.json:cms_e5l26_vig_sets.json [--skip io:3,vig:7]
The reviewer's (set, i) indexes point into the CURRENT sets file; the stem there identifies the pool question.
"""
import json, os, re, sys, pprint
HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
skip = set()
if "--skip" in args:
    k = args.index("--skip")
    skip = set(args[k + 1].split(","))
    args = args[:k] + args[k + 2:]
P = {}
try:
    sys.path.insert(0, HERE)
    import cms_e5l26_patch
    P = dict(cms_e5l26_patch.PATCHES)
except ImportError:
    pass
n = 0
for arg in args:
    jp, sp = arg.split(":")
    tag = "vig" if "vig" in sp else "io"
    sets = json.load(open(os.path.join(HERE, sp), encoding="utf-8"))
    for idx, it in enumerate(json.load(open(jp, encoding="utf-8"))["issues"]):
        if "%s:%d" % (tag, idx) in skip:
            continue
        q = sets[it["set"]][it["i"]]
        key = q["q"] if q["q"] not in [v.get("q") for v in P.values()] else [k for k, v in P.items() if v.get("q") == q["q"]][0]
        pt = P.setdefault(key, {})
        f = it["field"]
        if f == "stem": pt["q"] = it["fix"]
        elif f == "cite": pt["cite"] = it["fix"]
        elif f in ("opt_text", "opt_expl"):
            orig = q["opts"][it["opt"]][0]
            if orig in [v[0] for v in pt.get("opts", {}).values() if v[0]]:   # option text already replaced by an earlier fix
                orig = [k for k, v in pt["opts"].items() if v[0] == orig][0]
            cur = pt.setdefault("opts", {}).setdefault(orig, [None, None])
            fix = re.sub(r"\s*\((?:replace|replaces|replacing)[^)]*\)\s*$", "", it["fix"]).strip()
            cur[0 if f == "opt_text" else 1] = fix
        n += 1
open(os.path.join(HERE, "cms_e5l26_patch.py"), "w", encoding="utf-8").write(
    '# -*- coding: utf-8 -*-\n"""Independent-reviewer fixes for the Lecture 26 pools, applied by cms_e5_partition.py."""\nPATCHES = ' + pprint.pformat(P, width=140) + "\n")
print("patched", n, "items ->", len(P), "questions")
