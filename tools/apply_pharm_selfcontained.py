#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make every Pharmacology I explanation self-contained.

Stems and options were cleared by the stem rewrites; this clears the
explanations. Edits parsed JSON, and asserts the answer key is untouched --
only opts[i][1] changes, never the option text or the correct index.

Archived v1 master forms are deliberately SKIPPED: they are a preserved
snapshot of the old bank, and rewriting them would defeat the point of keeping
them.
"""
import io, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_selfcontained import clean

FOLDER = os.path.join(ROOT, "Pharmacology I Exam 1")
PAT = re.compile(r"(const QUESTIONS\s*=\s*)(\[.*?\])(;\n)", re.S)
SRC = re.compile(r"\blectures?\b|\bthe decks?\b|\bDr\.\s", re.I)


def main():
    files = n = 0
    for fn in sorted(os.listdir(FOLDER)):
        if not fn.endswith(".html") or "-v1.html" in fn:
            continue
        p = os.path.join(FOLDER, fn)
        src = io.open(p, encoding="utf-8").read()
        m = PAT.search(src)
        if not m:
            continue
        qs = json.loads(m.group(2))
        before = [(q["q"], q["c"], [o[0] for o in q["opts"]]) for q in qs]
        c = 0
        for q in qs:
            for o in q["opts"]:
                if SRC.search(o[1]):
                    new = clean(o[1])
                    if new != o[1]:
                        o[1] = new
                        c += 1
        after = [(q["q"], q["c"], [o[0] for o in q["opts"]]) for q in qs]
        assert before == after, "%s: cleaning an explanation changed a stem or the key" % fn
        if c:
            io.open(p, "w", encoding="utf-8").write(
                src[:m.start(2)] + json.dumps(qs, ensure_ascii=False) + src[m.end(2):])
            files += 1
            n += c
            print("  %-46s %3d explanations cleaned" % (fn, c))
    print("\n%d explanation(s) cleaned across %d file(s)" % (n, files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
