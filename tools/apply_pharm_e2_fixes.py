#!/usr/bin/env python3
"""Apply reviewer fixes (scratch JSON) to tools/pharm_e2/<Lx>.json, then re-run the checker.

    python3 tools/apply_pharm_e2_fixes.py L6 path/to/judge.json [--skip N,N]   # N = issue index to leave alone
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
lec, jp = sys.argv[1], sys.argv[2]
skip = set()
if "--skip" in sys.argv:
    skip = {int(x) for x in sys.argv[sys.argv.index("--skip") + 1].split(",") if x}
p = os.path.join(HERE, "pharm_e2", lec + ".json")
d = json.load(open(p, encoding="utf-8"))
issues = json.load(open(jp, encoding="utf-8"))["issues"]
applied = 0
for n, it in enumerate(issues):
    if n in skip:
        continue
    where, i, field = it["where"], it["i"], it["field"]
    if where.startswith("kcz."):
        row = d["kcz"][where.split(".")[1]][i]
    elif where == "chart":
        row = d["chart"]["rows"][i]
    else:
        row = d[where][i]
    fix = it["fix"]
    m = re.fullmatch(r"cells\[(\d+)\]", field)
    if m:
        row["cells"][int(m.group(1))] = fix
    elif field == "bbw":
        row["bbw"] = fix in (True, "true", "True")
    else:
        row[field] = fix
    for v in it.get("verify", []):
        if v not in row["verify"]:
            row["verify"].append(v)
    applied += 1
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("applied", applied, "of", len(issues))
