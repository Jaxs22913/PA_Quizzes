#!/usr/bin/env python3
"""Dump attribution-bearing STEMS with their full option list, for hand-rewriting."""
import io, sys, os, json, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX as SRC
for path in sys.argv[1:]:
    s = io.open(path, encoding="utf8").read()
    m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n', s, re.S)
    if not m:
        continue
    try:
        qs = [q for q in json.loads(m.group(1))
              if isinstance(q, dict) and "q" in q and "opts" in q]
    except Exception:
        continue
    print("\n=== %s" % path)
    for _i, q in enumerate(qs):
        if not SRC.search(q["q"]):
            continue
        print('"%s": {"q": "%s"},' % ((q.get("qid") or "#%d" % _i), q["q"]))
        for i, o in enumerate(q["opts"]):
            print("      %s%d %s" % ("*" if i == q["c"] else " ", i, o[0]))
