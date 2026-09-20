#!/usr/bin/env python3
"""Rewrite option EXPLANATIONS, addressed by (pool, stem, option index).

Matching an explanation by its own text does not scale: short distractor
explanations ("The deck says the opposite.") recur across many questions and
pools, so a text key is ambiguous exactly where it matters most. The stem is
unique within a pool, and the option index is unique within the question, so
this triple always names one explanation.

TSV: pool <TAB> stem <TAB> option_index <TAB> new explanation
"""
import ast, os, sys

TOOLS = "/Users/jaxonluke/Developer/PA_Quizzes/tools"
tsv, APPLY = sys.argv[1], "--apply" in sys.argv

rows = []
for i, line in enumerate(open(tsv, encoding="utf-8"), 1):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    p = line.split("\t")
    assert len(p) == 4, "line %d: want 4 fields, got %d" % (i, len(p))
    rows.append((p[0], p[1], int(p[2]), p[3]))

by_pool = {}
for pool, stem, idx, new in rows:
    by_pool.setdefault(pool, []).append((stem, idx, new))

total = 0
for pool, items in sorted(by_pool.items()):
    path = os.path.join(TOOLS, pool + ".py")
    raw = open(path, "rb").read()
    tree = ast.parse(raw.decode("utf-8"))

    # map stem text -> the List node holding that question's options
    qmap = {}
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Dict, ast.Call)):
            continue
        stem_node = opts_node = None
        pairs = (zip([k.value if isinstance(k, ast.Constant) else None
                      for k in n.keys], n.values) if isinstance(n, ast.Dict)
                 else [(kw.arg, kw.value) for kw in n.keywords])
        for k, v in pairs:
            if k == "q" and isinstance(v, ast.Constant):
                stem_node = v
            elif k == "opts":
                opts_node = v
        if stem_node is not None and isinstance(opts_node, ast.List):
            qmap.setdefault(stem_node.value, []).append(opts_node)

    targets = []
    for stem, idx, new in items:
        hits = qmap.get(stem, [])
        assert len(hits) == 1, "%s: stem matched %d questions: %r" % (pool, len(hits), stem[:60])
        opts = hits[0]
        assert idx < len(opts.elts), "%s: option %d out of range" % (pool, idx)
        pair = opts.elts[idx]
        assert isinstance(pair, ast.List) and len(pair.elts) == 2, "%s: option %d is not [text, expl]" % (pool, idx)
        node = pair.elts[1]
        assert isinstance(node, ast.Constant) and isinstance(node.value, str)
        targets.append((node, new))

    total += len(targets)
    if not APPLY:
        continue
    lines = raw.split(b"\n")
    for node, new in sorted(targets, key=lambda t: (t[0].lineno, t[0].col_offset), reverse=True):
        start = sum(len(l) + 1 for l in lines[:node.lineno - 1]) + node.col_offset
        end = sum(len(l) + 1 for l in lines[:node.end_lineno - 1]) + node.end_col_offset
        lit = raw[start:end].decode("utf-8")
        q = lit[0]
        assert q in "\"'", "%s: literal starts %r" % (pool, lit[:12])
        esc = new.replace("\\", "\\\\").replace(q, "\\" + q)
        raw = raw[:start] + (q + esc + q).encode("utf-8") + raw[end:]
    ast.parse(raw.decode("utf-8"))
    open(path, "wb").write(raw)

print("%s %d explanations across %d pools" % ("rewrote" if APPLY else "would rewrite", total, len(by_pool)))
