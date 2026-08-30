#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply the rewritten stems to the Pharmacology I topic quizzes.

Same safety model as apply_pharm_shortening.py: edits the parsed QUESTIONS
JSON, never the surrounding HTML, and refuses to write if anything about the
answer key changes. Only q["q"] is touched -- options and the correct index are
left exactly as they were, so the rewrite cannot alter which answer is right.

Idempotent: a rewrite that does not fire is only stale if neither its old nor
its new stem is present anywhere in the folder.
"""
import io, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_stem_rewrite import REWRITE

FOLDER = os.path.join(ROOT, "Pharmacology I Exam 1")
PAT = re.compile(r"(const QUESTIONS\s*=\s*)(\[.*?\])(;\n)", re.S)


def main():
    used, files, n_total = set(), 0, 0
    for fn in sorted(os.listdir(FOLDER)):
        if "quiz" not in fn or not fn.endswith(".html"):
            continue
        p = os.path.join(FOLDER, fn)
        src = io.open(p, encoding="utf-8").read()
        m = PAT.search(src)
        if not m:
            continue
        qs = json.loads(m.group(2))
        before = [(q["c"], [o[0] for o in q["opts"]]) for q in qs]
        n = 0
        for q in qs:
            if q["q"] in REWRITE:
                used.add(q["q"])
                q["q"] = REWRITE[q["q"]]
                n += 1
        after = [(q["c"], [o[0] for o in q["opts"]]) for q in qs]
        assert before == after, "%s: a stem rewrite disturbed the answer key" % fn
        stems = [q["q"] for q in qs]
        assert len(set(stems)) == len(stems), "%s: rewrite made two stems identical" % fn
        if n:
            io.open(p, "w", encoding="utf-8").write(
                src[:m.start(2)] + json.dumps(qs, ensure_ascii=False) + src[m.end(2):])
            files += 1
            n_total += n
            print("  %-46s %3d stems rewritten" % (fn, n))
    corpus = "".join(io.open(os.path.join(FOLDER, f), encoding="utf-8").read()
                     for f in os.listdir(FOLDER) if "quiz" in f and f.endswith(".html"))
    already = {k for k in set(REWRITE) - used if REWRITE[k] in corpus}
    stale = set(REWRITE) - used - already
    print("\n%d stem(s) rewritten across %d file(s); %d already applied"
          % (n_total, files, len(already)))
    if stale:
        print("STALE entries matching neither old nor new text (%d):" % len(stale))
        for s in sorted(stale):
            print("   %s" % s[:95])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
