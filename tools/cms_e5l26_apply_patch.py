#!/usr/bin/env python3
"""Apply tools/cms_e5l26_patch.py straight onto the shipped Lecture 26 sets (no re-partition, so the
questions that were reviewed stay the questions that ship). Idempotent.

    python3 tools/cms_e5l26_apply_patch.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_e5l26_patch import PATCHES
byq = {}
for k, v in PATCHES.items():
    byq[k] = v
    if "q" in v:
        byq[v["q"]] = v
n = 0
for f in ("cms_e5l26_sets.json", "cms_e5l26_vig_sets.json"):
    p = os.path.join(HERE, f)
    d = json.load(open(p, encoding="utf-8"))
    for key in d:
        for q in d[key]:
            pt = byq.get(q["q"])
            if not pt:
                continue
            if "q" in pt: q["q"] = pt["q"]
            if "cite" in pt: q["cite"] = pt["cite"]
            for old, (txt, ex) in pt.get("opts", {}).items():
                hit = [o for o in q["opts"] if o[0] in (old, txt)]
                assert len(hit) == 1, "option %r not found in %r" % (old, q["q"][:60])
                if txt is not None: hit[0][0] = txt
                if ex is not None: hit[0][1] = ex
            n += 1
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("patched", n, "shipped questions")
