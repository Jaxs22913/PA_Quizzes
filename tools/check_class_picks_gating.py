#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guard: class picks must never appear under an unanswered question.

Reported 2026-09-16 -- "the class stats were popping up even when I didn't
click an answer yet". Two independent causes, both in the paged quiz engine:

  1. PERSISTENCE. The "What the class picked" note is inserted as a SIBLING of
     #opts (host.parentNode.insertBefore(note, host.nextSibling)), but renderQ
     only does #opts.innerHTML = ''. The note therefore outlived the question
     it belonged to and sat under every later stem, showing a stale count.
     renderQ now removes it with the other per-question resets.

  2. RACE. ClassStats.getPicks is async. Answer a question, move on before it
     resolves, and the callback painted its percentages onto whichever option
     rows were on screen -- an unanswered one. The callback now bails unless
     the question it was called for is still displayed and still answered.

Both were reproduced in a headless browser against the pre-fix files and are
gone after it. This checker is the cheap static half: every rendered quiz
carries an inlined copy of the engine, so a quiz re-rendered from a stale
template, or an old file never re-rendered, silently loses the fix. It asserts
both guards are present wherever showClassPicks is.

    python3 tools/check_class_picks_gating.py            # whole site
    python3 tools/check_class_picks_gating.py "Some Exam" # one folder
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "__pycache__"}

# the two guards, matched on their load-bearing line rather than the comment
GUARDS = [
    ("renderQ removes the stale note",
     "document.getElementById('classpicks');"),
    ("the async callback bails if the user moved on",
     "if(QUESTIONS[order[idx]] !== q || answers[idx] === null) return;"),
]


def files(prefix=None):
    for dirpath, dirnames, names in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for n in names:
            if not n.endswith((".html",)):
                continue
            p = os.path.join(dirpath, n)
            rel = os.path.relpath(p, ROOT)
            if prefix and not rel.startswith(prefix):
                continue
            yield rel, p


def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else None
    checked = 0
    bad = []
    for rel, path in files(prefix):
        try:
            s = open(path, encoding="utf-8").read()
        except Exception:
            continue
        if "showClassPicks" not in s:
            continue
        checked += 1
        missing = [label for label, needle in GUARDS if needle not in s]
        if missing:
            bad.append((rel, missing))

    for rel, missing in bad:
        print("  %s" % rel)
        for m in missing:
            print("      missing guard: %s" % m)

    print()
    print("files carrying the quiz engine : %d" % checked)
    print("missing a class-picks guard    : %d" % len(bad))
    if not checked:
        print("\nNOTHING CHECKED -- the engine was not found in any file, which is "
              "itself a failure: this guard is meant to have something to guard.")
        return 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
