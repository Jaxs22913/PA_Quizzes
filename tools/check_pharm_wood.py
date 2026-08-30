#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify every quote on the Dr. Wood emphasis page against the recordings.

Same contract as the deck-based charts, with the transcripts as the source
instead of the PowerPoints. Every entry carries `verify` substrings that must
appear in the lecture it cites.

The transcripts stay in ~/Desktop and are never copied into this repo, so this
only runs on Jaxon's machine -- which is the same arrangement the PPT-grounding
checks already use.
"""
import html as H
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _pharm_wood_data as D

BASE = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/recordings/")
_cache = {}


def norm(s):
    s = H.unescape(re.sub(r"<[^>]+>", " ", s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("…", "..."), ("\xa0", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def transcript(lec):
    if lec not in _cache:
        p = BASE + "pharm-lecture-%d.transcript.txt" % lec
        if not os.path.exists(p):
            sys.exit("transcript not found: %s" % p)
        raw = open(p, encoding="utf-8").read()
        _cache[lec] = norm(re.sub(r"\[\d+:\d+(?::\d+)?\]", " ", raw))
    return _cache[lec]


def main():
    entries = ([("marker", D.MARKER["quote"], D.MARKER["lec"], D.MARKER["verify"])] +
               [("rule: " + r["title"], r["quote"], r["lec"], r["verify"]) for r in D.RULES] +
               [("pattern: " + p["title"], p["quote"], p["lec"], p["verify"]) for p in D.PATTERNS] +
               [("strategy: " + s["title"], s["quote"], s["lec"], s["verify"]) for s in D.STRATEGY] +
               [("starred: " + s[0], s[1], s[3], s[4]) for s in D.STARRED])
    fails, checked = [], 0
    for label, _quote, lec, verify in entries:
        body = transcript(lec)
        missing = [v for v in verify if norm(v) not in body]
        checked += len(verify)
        if missing:
            fails.append((label, lec, missing))
    plain = re.compile(r"<[^>]+>")
    print("entries: %d   substrings checked: %d   %s"
          % (len(entries), checked, "OK" if not fails else "FAILED %d" % len(fails)))
    for label, lec, missing in fails:
        print("  %s  (lecture %d)" % (plain.sub("", label), lec))
        for m in missing:
            print("      NOT IN TRANSCRIPT: %r" % m)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
