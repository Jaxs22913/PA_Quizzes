#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify every quote on the Exam 2 "what he said to star" page against the recording transcripts.

Data: tools/pharm_e2/wood.json  {"entries":[{"lec","at","topic","kind","quote","verify":[raw substrings],"body"}]}
Each `verify` substring must appear in the transcript of the lecture it cites (timestamps stripped,
case/punctuation-insensitive). Transcripts stay in ~/Desktop and are never copied into the repo, so this
only runs on Jaxon's machine, like the deck-grounding checks.
"""
import html as H, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Pharmacology I Inbox/Exam 2/recordings/")
FILES = {"L4": "pharm-ophthalmology-wood-2026-09-03.transcript.txt",
         "L5": "pharm-ent-jax-2026-09-17.transcript.txt",
         "L6": "pharm-l6-antihypertensives-2026-09-22.transcript.txt",
         "L7": "pharm-l7-lipids-2026-09-22.transcript.txt"}
KINDS = {"marker", "rule", "shape", "scope", "emphasis"}
_cache = {}


def norm(s):
    s = H.unescape(re.sub(r"<[^>]+>", " ", s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("…", "..."), ("\xa0", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def transcript(lec):
    if lec not in _cache:
        p = BASE + FILES[lec]
        if not os.path.exists(p):
            sys.exit("transcript not found: %s" % p)
        raw = open(p, encoding="utf-8").read()
        _cache[lec] = norm(re.sub(r"\[\d+:\d+(?::\d+)?\]", " ", raw))
    return _cache[lec]


def main():
    p = os.path.join(HERE, "pharm_e2", "wood.json")
    if not os.path.exists(p):
        print("wood.json not written yet"); return 0
    d = json.load(open(p, encoding="utf-8"))
    fails, n = [], 0
    for i, e in enumerate(d["entries"]):
        n += 1
        for k in ("lec", "at", "topic", "kind", "quote", "verify", "body"):
            if not e.get(k):
                fails.append((i, e.get("topic", "?"), "missing " + k))
        if e.get("kind") not in KINDS:
            fails.append((i, e.get("topic", "?"), "bad kind %r" % e.get("kind")))
        if e.get("lec") not in FILES:
            fails.append((i, e.get("topic", "?"), "bad lec")); continue
        t = transcript(e["lec"])
        for v in e.get("verify", []):
            if norm(v) not in t:
                fails.append((i, e.get("topic", "?"), "NOT IN TRANSCRIPT %s: %r" % (e["lec"], v)))
        if re.search(r"\b\d+(\.\d+)?\s*(mg|mcg)\b", e.get("body", ""), re.I):
            fails.append((i, e.get("topic", "?"), "milligram dose in body"))
    print("entries: %d   %s" % (n, "OK" if not fails else "FAILED %d" % len(fails)))
    for i, t, why in fails[:40]:
        print("   [%d] %s -- %s" % (i, t, why))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
