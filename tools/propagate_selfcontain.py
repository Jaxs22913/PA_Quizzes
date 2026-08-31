#!/usr/bin/env python3
"""Carry self-containment rewrites from the topic quizzes into the master exams.

Master forms are sampled from the topic quizzes, so the same stem or explanation
often appears in both.  Where the master still holds text that was rewritten in
its source quiz, replace it with the same rewrite — an exact-text match only, so
nothing is guessed.  Answer keys and option text are asserted unchanged.
"""
import io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX


def main():
    pairs = json.load(io.open(sys.argv[1], encoding="utf8"))
    targets = sys.argv[2:]
    grand = 0
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
                q["q"] = pairs[q["q"]]; n += 1
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
    print("%d propagated across %d file(s)" % (grand, len(targets)))


if __name__ == "__main__":
    main()
