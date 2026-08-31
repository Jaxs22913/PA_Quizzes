#!/usr/bin/env python3
"""Print every attribution-bearing stem/explanation in a quiz file, keyed by qid."""
import io, sys, os, json, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX as SRC
for path in sys.argv[1:]:
    s = io.open(path, encoding="utf8").read()
    qs = json.loads(re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n', s, re.S).group(1))
    hdr = False
    for _i, q in enumerate(qs):
        hits = []
        if SRC.search(q["q"]):
            hits.append(("q", q["q"]))
        for i, o in enumerate(q["opts"]):
            if len(o) > 1 and SRC.search(o[1]):
                hits.append((str(i), o[1]))
        if not hits:
            continue
        if not hdr:
            print("\n=== %s" % path); hdr = True
        print("%s |ANS=%s| %s" % ((q.get("qid") or "#%d" % _i), q["c"], q["q"] if not SRC.search(q["q"]) else ""))
        for k, t in hits:
            if k != "q":
                print("   [%s] %s :: %s" % (k, q["opts"][int(k)][0][:44], t))
            else:
                print("   [q] %s" % t)
