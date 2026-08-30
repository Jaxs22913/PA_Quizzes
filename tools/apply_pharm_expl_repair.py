# -*- coding: utf-8 -*-
"""Apply _pharm_expl_repair.REPAIRS to the live Pharmacology Exam 1 content.

Raw-text replacement (the strings are unique and contain no JSON escapes), then
a re-parse that asserts every stem, option and answer key is byte-identical to
what it was before -- only explanations may move. Archived v1 forms are a
deliberate snapshot and are skipped.
"""
import re, json, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pharm_expl_repair import REPAIRS

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "Pharmacology I Exam 1")
BLOCK = re.compile(r'const\s+(?:QUESTIONS|DATA|QUIZ_DATA)\s*=\s*(\[.*?\]);\s*\n', re.S)

def skeleton(qs):
    return [(q.get("q"), q.get("c"), [o[0] for o in q.get("opts", [])]) for q in qs]

def process(path, dumpjson=False):
    src = open(path, encoding="utf8").read()
    if dumpjson:
        before = skeleton(json.loads(src))
    else:
        m = BLOCK.search(src)
        if not m:
            return 0
        before = skeleton(json.loads(m.group(1)))
    n = 0
    out = src
    for bad, good in REPAIRS.items():
        if bad in out:
            n += out.count(bad)
            out = out.replace(bad, good)
    if not n:
        return 0
    after = skeleton(json.loads(out) if dumpjson else json.loads(BLOCK.search(out).group(1)))
    assert before == after, "%s: a repair changed a stem, option or key" % os.path.basename(path)
    open(path, "w", encoding="utf8").write(out)
    return n

total = 0
for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    if "-v1" in os.path.basename(path):
        continue
    n = process(path)
    if n:
        total += n
        print("  %-52s %d" % (os.path.basename(path), n))

mj = os.path.join(ROOT, "master-exams.json")
if os.path.exists(mj):
    src = open(mj, encoding="utf8").read()
    data = json.loads(src)
    def walk(o):
        c = 0
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, str) and v in REPAIRS:
                    o[k] = REPAIRS[v]; c += 1
                else: c += walk(v)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                if isinstance(v, str) and v in REPAIRS:
                    o[i] = REPAIRS[v]; c += 1
                else: c += walk(v)
        return c
    n = walk(data)
    if n:
        open(mj, "w", encoding="utf8").write(json.dumps(data, ensure_ascii=False, indent=1))
        total += n
        print("  %-52s %d" % ("master-exams.json", n))

print("\n%d replacements across the live Pharmacology Exam 1 content" % total)
