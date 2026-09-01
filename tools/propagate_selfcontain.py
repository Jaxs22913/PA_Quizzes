#!/usr/bin/env python3
"""Carry self-containment rewrites from the topic quizzes into the master exams.

Master forms are sampled from the topic quizzes, so the same stem or explanation
often appears in both.  Where the master still holds text that was rewritten in
its source quiz, replace it with the same rewrite — an exact-text match only, so
nothing is guessed.  Answer keys and option text are asserted unchanged.
"""
import glob, io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX


def build_guard(paths):
    """stem -> set of option-sets, taken from the files the map came from.

    A stem is only safe to propagate into a target if the target's options
    still match the source question's options.  Without this, replacing a stem
    whose OPTIONS also changed leaves the target asking a new question over the
    old answers -- which is exactly what happened once, silently.
    """
    guard = {}
    for p in paths:
        try:
            s = io.open(p, encoding="utf8").read()
        except Exception:
            continue
        m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n', s, re.S)
        if not m:
            continue
        try:
            qs = json.loads(m.group(1))
        except Exception:
            continue
        for q in qs:
            if isinstance(q, dict) and "opts" in q:
                guard.setdefault(q["q"], set()).add(
                    frozenset(o[0] for o in q["opts"]))
    return guard


def main():
    pairs = json.load(io.open(sys.argv[1], encoding="utf8"))
    targets = sys.argv[2:]
    guard = build_guard(glob.glob(os.path.join(
        os.path.dirname(targets[0]) or ".", "*.html")) if targets else [])
    grand = skipped = 0
    for path in targets:
        s = io.open(path, encoding="utf8").read()
        m = re.search(r'(const QUESTIONS\s*=\s*)(\[.*?\])(;\s*\n)', s, re.S)
        if not m:
            continue
        qs = json.loads(m.group(2))
        before = [(q["c"], [o[0] for o in q["opts"]]) for q in qs]
        n = 0
        for q in qs:
            if q["q"] in pairs:
                new = pairs[q["q"]]
                here = frozenset(o[0] for o in q["opts"])
                if new in guard and here not in guard[new]:
                    skipped += 1                      # options moved with the stem
                    print("     SKIP (options differ from the source question): %s"
                          % q["q"][:70])
                else:
                    q["q"] = new; n += 1
            for o in q["opts"]:
                if len(o) > 1 and o[1] in pairs:
                    o[1] = pairs[o[1]]; n += 1
        assert before == [(q["c"], [o[0] for o in q["opts"]]) for q in qs]
        if n:
            io.open(path, "w", encoding="utf8").write(
                s[:m.start(2)] + json.dumps(qs, ensure_ascii=False, indent=2) + s[m.end(2):])
        left = sum(1 for q in qs if RX.search(q["q"])) + \
               sum(1 for q in qs for o in q["opts"] if len(o) > 1 and RX.search(o[1]))
        print("  %-46s %3d propagated, %3d left" % (path.split("/")[-1][:46], n, left))
        grand += n
    print("%d propagated across %d file(s); %d skipped by the option guard"
          % (grand, len(targets), skipped))


if __name__ == "__main__":
    main()
