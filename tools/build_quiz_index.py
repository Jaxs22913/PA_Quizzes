#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emit quiz-index.json: which quiz files each exam folder holds.

The homepage could count quizzes by reading its own links out of the DOM. The
calendar page has no quiz links on it, so anything there that wants to say "3 of
29 done" needs the list shipped to it. Small enough to be one file: hrefs only,
no titles, since the caller only ever counts them and probes localStorage.
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ("guide", "cram", "chart", "osce", "index", "review", "progress",
        "class-traps", "calendar", "relax", "arcade", "group-")


def main():
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "*", "*.html"))):
        fn = os.path.basename(path)
        folder = os.path.basename(os.path.dirname(path))
        if any(k in fn for k in SKIP):
            continue
        src = open(path, encoding="utf8", errors="ignore").read()
        # a quiz is a page with a question bank, which is what "done" means here
        if not re.search(r'const (?:QUESTIONS|DATA|QUIZ_DATA)\s*=\s*\[', src):
            continue
        out.setdefault(folder, []).append(fn)
    dest = os.path.join(ROOT, "quiz-index.json")
    json.dump(out, open(dest, "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
    print("wrote quiz-index.json  %d folders, %d quizzes, %.1f KB"
          % (len(out), sum(len(v) for v in out.values()), os.path.getsize(dest) / 1024.0))
    for k in sorted(out, key=lambda k: -len(out[k]))[:6]:
        print("   %-46s %d" % (k, len(out[k])))


if __name__ == "__main__":
    main()
