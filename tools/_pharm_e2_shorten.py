#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shorten over-long correct answers in a pool (invoked for PD2 here).

101 of 150 questions had a length-gameable key: the correct answer carried the
full compound fact while the distractors were terse, so the longest option was
the answer and a student could score without reading. [[distractor_style_matching]]
says shorten the KEY, never pad the distractors.

The elaboration is not deleted -- it moves into the explanation, which is where
it belonged. "Correct" plus the detail teaches better than a long option does.

Only the leading clause is kept, and only where the key has a real separator to
cut at. Anything left gameable after this is reported for hand-editing rather
than being truncated blindly, because a key cut at the wrong place stops being
the right answer.
"""
import ast, io, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
import glob as _g
FILES = ["pharm_e2_vignette_pool.py"]
SEPS = [" — ", "; ", ", and ", ", "]


def split_key(text):
    """Leading clause, and the remainder that moves into the explanation."""
    for s in SEPS:
        i = text.find(s)
        # require the head to still be substantial and the tail to be worth moving
        if i > 12 and len(text) - i - len(s) > 8:
            return text[:i].rstrip(" ,;—"), text[i + len(s):].strip()
    return None, None


def gameable(opts):
    L = sorted(((len(o[0]), i) for i, o in enumerate(opts)), reverse=True)
    (t, ti), (r, _) = L[0], L[1]
    return ti == 0 and (t - r) >= 8 and t >= r * 1.18


def main():
    apply = "--apply" in sys.argv
    changed = total = 0
    leftover = []
    for fn in FILES:
        src = io.open(os.path.join(HERE, fn), encoding="utf-8").read()
        tree = ast.parse(src)
        raw = src.encode("utf-8")
        lines = raw.splitlines(keepends=True)
        starts = [0]
        for ln in lines:
            starts.append(starts[-1] + len(ln))

        def off(n, end=False):
            ln = (n.end_lineno if end else n.lineno) - 1
            col = n.end_col_offset if end else n.col_offset
            return starts[ln] + col

        edits = []
        for node in ast.walk(tree):
            if not isinstance(node, (ast.List, ast.Tuple)):
                continue
            e = node.elts
            ok = (len(e) == 4 and all(
                isinstance(x, (ast.List, ast.Tuple)) and len(x.elts) == 2
                and all(isinstance(y, ast.Constant) and isinstance(y.value, str)
                        for y in x.elts) for x in e))
            if not ok:
                continue
            opts = [[x.elts[0].value, x.elts[1].value] for x in e]
            if not re.match(r"\s*correct\b", opts[0][1], re.I):
                continue
            total += 1
            if not gameable(opts):
                continue
            head, tail = split_key(opts[0][0])
            if not head:
                leftover.append((fn, opts[0][0]))
                continue
            new_expl = opts[0][1].rstrip()
            if not new_expl.endswith((".", "!", "?")):
                new_expl += "."
            new_expl += " " + tail[0].upper() + tail[1:]
            if not new_expl.endswith((".", "!", "?")):
                new_expl += "."
            # check the shortened key actually fixes it
            trial = [[head, new_expl]] + opts[1:]
            if gameable(trial):
                leftover.append((fn, opts[0][0]))
                continue
            kt, ke = e[0].elts[0], e[0].elts[1]
            edits.append((off(kt), off(kt, True), head))
            edits.append((off(ke), off(ke, True), new_expl))
            changed += 1

        if apply and edits:
            out = raw
            for a, b, txt in sorted(edits, reverse=True):
                lit = ('"' + txt.replace("\\", "\\\\").replace('"', '\\"') + '"').encode("utf-8")
                out = out[:a] + lit + out[b:]
            text = out.decode("utf-8")
            ast.parse(text)                       # never write something unparseable
            io.open(os.path.join(HERE, fn), "w", encoding="utf-8").write(text)

    print("%s %d of %d question(s)" % ("shortened" if apply else "WOULD shorten",
                                       changed, total))
    print("left for hand-editing: %d" % len(leftover))
    for fn, k in leftover[:14]:
        print("   %-22s %s" % (fn, k[:72]))


if __name__ == "__main__":
    main()
