#!/usr/bin/env python3
"""Apply a hand-written stem mapping (TSV: old<TAB>new) to the pools.

Same AST byte-offset splice as apply_decite.py: option text repeats inside a
pool, so a string replacement cannot tell two identical strings apart.
"""
import ast, glob, os, sys
TOOLS = "/Users/jaxonluke/Developer/PA_Quizzes/tools"
tsv, APPLY = sys.argv[1], "--apply" in sys.argv

want = {}
for i, line in enumerate(open(tsv, encoding="utf-8"), 1):
    line = line.rstrip("\n")
    if not line.strip():
        continue
    p = line.split("\t")
    assert len(p) == 2, "line %d: expected 2 tab-separated fields, got %d" % (i, len(p))
    assert p[0] != p[1], "line %d: replacement identical to original" % i
    want[p[0]] = p[1]
print("mapping: %d entries" % len(want))

# global uniqueness check FIRST -- a per-file check passes happily while the
# same string is being replaced in three other pools it does not belong to.
where = {}
for path in sorted(set(glob.glob(os.path.join(TOOLS, "*pool*.py")))
                   | set(glob.glob(os.path.join(TOOLS, "*_vig*.py")))):
    if __import__("re").search(r"(partition|lengthfix|check_|render_|build_|dump_|apply_|_rx)", os.path.basename(path)):
        continue
    try:
        tree = ast.parse(open(path, encoding="utf-8").read())
    except SyntaxError:
        continue
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value in want:
            where.setdefault(n.value, []).append(os.path.basename(path))
dupes = {k: v for k, v in where.items() if len(v) > 1}
if dupes:
    for k, v in dupes.items():
        print("AMBIGUOUS: %r appears in %s" % (k[:60], ", ".join(v)))
    sys.exit("refusing to apply: %d mapping entries are not unique" % len(dupes))

hit, files = 0, 0
import re as _re
_cands = sorted(set(glob.glob(os.path.join(TOOLS, "*pool*.py")))
                | set(glob.glob(os.path.join(TOOLS, "*_vig*.py"))))
_skip = _re.compile(r"(partition|lengthfix|check_|render_|build_|dump_|apply_|_rx)")
for path in _cands:
    if _skip.search(os.path.basename(path)):
        continue
    src = open(path, encoding="utf-8").read()
    if not any(k in src for k in want):
        continue
    raw = src.encode("utf-8")
    spl = [n for n in ast.walk(ast.parse(src))
           if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value in want]
    if not spl:
        continue
    seen = {}
    for n in spl:
        seen[n.value] = seen.get(n.value, 0) + 1
    for k, c in seen.items():
        assert c == 1, "%s: %r appears %d times" % (os.path.basename(path), k[:50], c)
    hit += len(spl); files += 1
    if not APPLY:
        continue
    lines = raw.split(b"\n")
    for n in sorted(spl, key=lambda n: (n.lineno, n.col_offset), reverse=True):
        start = sum(len(l) + 1 for l in lines[:n.lineno - 1]) + n.col_offset
        end = sum(len(l) + 1 for l in lines[:n.end_lineno - 1]) + n.end_col_offset
        lit = raw[start:end].decode("utf-8")
        q = lit[0]
        assert q in "\"'", "%s: literal starts %r" % (os.path.basename(path), lit[:12])
        new = want[n.value].replace("\\", "\\\\").replace(q, "\\" + q)
        raw = raw[:start] + (q + new + q).encode("utf-8") + raw[end:]
    ast.parse(raw.decode("utf-8"))
    open(path, "wb").write(raw)

print("matched %d stems in %d pools" % (hit, files))
missing = len(want) - hit
if missing:
    print("WARNING: %d mapping entries matched nothing" % missing)
