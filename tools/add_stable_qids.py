#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Give every class-picks question a permanent id, so editing a stem no longer
throws away what the class answered.

The problem. answer_picks is keyed `<quizslug>__<hash of the stem>`, computed in
the page at read time. That is stable only while the stem is. Rewriting the
Pharmacology stems orphaned their history silently: 286 of 670 live documents no
longer join to any question in the repo, and the affected questions restarted at
zero responses with no sign anything had been lost.

The fix. Write the CURRENT hash into each question as a `qid` field and have the
page prefer it. Because the stored value equals what the page computes today,
every existing response keeps matching -- nothing is reset by this change -- and
from here the id survives any rewording.

Only the 38 files that actually record picks are touched, all of them Semester 2.
"""
import os, re, json, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fnv36(t):
    """Mirror of qidFor() in the quiz template: FNV-1a, base 36."""
    h = 2166136261
    for ch in t:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    if h == 0:
        return "0"
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = ""
    while h:
        out = digits[h % 36] + out
        h //= 36
    return out


BLOCK = re.compile(r'(const (?:QUESTIONS|DATA|QUIZ_DATA)\s*=\s*)(\[.*?\])(;\s*\n)', re.S)


def main():
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "*", "*.html"))
                   if "showClassPicks" in open(f, encoding="utf8", errors="ignore").read())
    total = added = already = 0
    for path in files:
        src = open(path, encoding="utf8").read()
        m = BLOCK.search(src)
        if not m:
            continue
        qs = json.loads(m.group(2))
        before = [(q.get("q"), q.get("c"), [o[0] for o in q.get("opts", [])]) for q in qs]
        n = 0
        for q in qs:
            total += 1
            if "qid" in q:
                already += 1
                continue
            q["qid"] = fnv36(q["q"])
            n += 1
        if not n:
            continue
        after = [(q.get("q"), q.get("c"), [o[0] for o in q.get("opts", [])]) for q in qs]
        assert before == after, "%s: adding an id changed a stem, option or key" % path
        out = src[:m.start(2)] + json.dumps(qs, ensure_ascii=False) + src[m.end(2):]
        open(path, "w", encoding="utf8").write(out)
        added += n
        print("  %-58s +%d" % (os.path.basename(path), n))
    print("\n%d questions across %d files; %d given an id, %d already had one"
          % (total, len(files), added, already))


if __name__ == "__main__":
    main()
