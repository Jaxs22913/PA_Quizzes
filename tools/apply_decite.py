#!/usr/bin/env python3
"""Rewrite citing STEMS across every question pool, in place.

Stems are identified by IMPORTING each pool (authoritative -- the pools use
half a dozen wrapper signatures and guessing arg positions is how you corrupt
one), then spliced by AST byte offset, because option text repeats and plain
string replacement cannot tell two identical strings apart.
"""
import ast, glob, importlib.util, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "/Users/jaxonluke/Developer/PA_Quizzes/tools")
from decite import rewrite
from check_pool_cites import CITES

TOOLS = "/Users/jaxonluke/Developer/PA_Quizzes/tools"
APPLY = "--apply" in sys.argv

def stems_of(path, mod):
    spec = importlib.util.spec_from_file_location(mod, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    out = []
    for attr in dir(m):
        P = getattr(m, attr)
        if isinstance(P, list) and P and isinstance(P[0], dict) and "opts" in P[0]:
            out += [q["q"] for q in P if CITES.search(q["q"])]
    return out

auto = hand = 0
notes, changed = {}, []
for path in sorted(glob.glob(os.path.join(TOOLS, "*pool*.py"))):
    mod = os.path.basename(path)[:-3]
    try:
        stems = stems_of(path, mod)
    except Exception as e:
        print("SKIP %s (%s)" % (mod, e)); continue
    if not stems:
        continue
    src = open(path, encoding="utf-8").read()
    raw = src.encode("utf-8")
    tree = ast.parse(src)
    want = {}
    for s in stems:
        new, note = rewrite(s)
        if note or new == s:
            hand += 1; notes[note or "unchanged"] = notes.get(note or "unchanged", 0) + 1
        else:
            want[s] = new
    # collect every string node whose value is a stem we want to rewrite
    spl = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value in want:
            spl.append(n)
    seen = {}
    for n in spl:
        seen[n.value] = seen.get(n.value, 0) + 1
    for k, c in seen.items():
        assert c == 1, "%s: stem appears %d times, ambiguous" % (mod, c)
    missing = set(want) - set(seen)
    assert not missing, "%s: %d stems not found in AST" % (mod, len(missing))
    auto += len(spl)
    if not APPLY:
        continue
    # splice from the END backwards so earlier offsets stay valid
    lines = raw.split(b"\n")
    for n in sorted(spl, key=lambda n: (n.lineno, n.col_offset), reverse=True):
        # byte offsets: ast gives line/col in bytes for utf-8 source
        start = sum(len(l) + 1 for l in lines[:n.lineno - 1]) + n.col_offset
        end = sum(len(l) + 1 for l in lines[:n.end_lineno - 1]) + n.end_col_offset
        lit = raw[start:end].decode("utf-8")
        q = lit[0]
        assert q in "\"'", "%s: literal does not start with a quote: %r" % (mod, lit[:20])
        new = want[n.value].replace("\\", "\\\\").replace(q, "\\" + q)
        raw = raw[:start] + (q + new + q).encode("utf-8") + raw[end:]
    ast.parse(raw.decode("utf-8"))          # must still parse
    open(path, "wb").write(raw)
    changed.append(mod)

print("auto %d  hand %d" % (auto, hand))
for k, v in sorted(notes.items(), key=lambda kv: -kv[1]):
    print("  %4d %s" % (v, k))
if APPLY:
    print("rewrote %d pools" % len(changed))
