#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply the shortened options to the Pharmacology I topic quizzes.

Edits the embedded QUESTIONS JSON rather than the surrounding HTML, so the file
is re-serialised from parsed data and cannot be corrupted by a stray string
match. Safety checks, all of which abort the write:

  * the correct-answer INDEX is never touched, and the keyed answer's text is
    compared before and after so a replacement cannot silently move the answer
  * options within a question must stay unique -- shortening two different
    options into the same string would make a question unanswerable
  * every replacement must actually fire somewhere, so a stale entry in the
    table is reported rather than ignored
"""
import io, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_option_shorten import SHORTEN

FOLDER = os.path.join(ROOT, "Pharmacology I Exam 1")
PAT = re.compile(r"(const QUESTIONS\s*=\s*)(\[.*?\])(;\n)", re.S)


def main():
    used = set()
    changed_files = 0
    total_opts = 0
    for fn in sorted(os.listdir(FOLDER)):
        if "quiz" not in fn or not fn.endswith(".html"):
            continue
        p = os.path.join(FOLDER, fn)
        src = io.open(p, encoding="utf-8").read()
        m = PAT.search(src)
        if not m:
            continue
        qs = json.loads(m.group(2))
        before_answers = [q["opts"][q["c"]][0] for q in qs]
        n = 0
        for q in qs:
            for o in q["opts"]:
                if o[0] in SHORTEN:
                    used.add(o[0])
                    o[0] = SHORTEN[o[0]]
                    n += 1
            texts = [o[0] for o in q["opts"]]
            assert len(set(texts)) == len(texts), \
                "%s: shortening made two options identical: %s" % (fn, q["q"][:60])
        after_answers = [q["opts"][q["c"]][0] for q in qs]
        for b, a in zip(before_answers, after_answers):
            assert a == SHORTEN.get(b, b), "%s: the keyed answer moved" % fn
        if n:
            io.open(p, "w", encoding="utf-8").write(
                src[:m.start(2)] + json.dumps(qs, ensure_ascii=False) + src[m.end(2):])
            changed_files += 1
            total_opts += n
            print("  %-46s %3d options shortened" % (fn, n))
    # An entry that did not fire is fine IF its replacement is already in the
    # files -- this script is meant to be re-runnable. Only an entry whose old
    # AND new text are both absent is genuinely stale.
    corpus = "".join(io.open(os.path.join(FOLDER, f), encoding="utf-8").read()
                     for f in os.listdir(FOLDER) if "quiz" in f and f.endswith(".html"))
    already = {k for k in set(SHORTEN) - used if SHORTEN[k] in corpus}
    stale = set(SHORTEN) - used - already
    print("\n%d option(s) shortened across %d file(s); %d already applied"
          % (total_opts, changed_files, len(already)))
    if stale:
        print("STALE table entries matching neither old nor new text (%d):" % len(stale))
        for s in sorted(stale):
            print("   %s" % s[:90])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
