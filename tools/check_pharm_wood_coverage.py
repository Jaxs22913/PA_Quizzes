#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Completeness sweep for the Dr. Wood emphasis page.

check_pharm_wood.py proves every quote on the page is real. This proves the
page is not MISSING one: it scans all three transcripts for emphasis language,
then reports every hit that no entry on the page already covers.

Matching is positional, not textual -- for each hit it takes a window of the
transcript and asks whether any entry's verify string falls inside it. An entry
therefore "covers" the moment it was drawn from, and anything left over is a
moment the page never looked at.
"""
import html as H
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _pharm_wood_data as D

BASE = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/recordings/")

# Deliberately wider than the page's own marker: anything that reads as "this
# one matters" should surface here even if he never said the word notable.
SIGNAL = re.compile(
    r"\bnotable\b|\bstar(?:red|ring)?\b|\bunderlin\w*|\bhighlight\w*|"
    r"\btest question\b|\bon the (?:exam|test|pance)\b|\bclassic\b|\bbuzzword\b|"
    r"\bhallmark\b|\bmake sure you (?:know|remember)\b|\bdon'?t forget\b|"
    r"\bremember (?:this|that)\b|\bkey (?:point|thing)\b|\bmost important\b|"
    r"\bpay attention\b|\bwatch out\b|\bthe one thing\b|\bgold standard\b", re.I)

# Reviewed and excluded, keyed by the phrase that trips the scan, with a reason.
EXCLUDE = {
 "star wars": "a joke about Rise of the Resistance, not an emphasis marker",
 "we'll kind of highlight those as we go": "housekeeping -- promising to flag things later",
 "we'll highlight those as they pop up": "housekeeping",
 "we'll highlight those as we get to it": "housekeeping",
 "we'll kind of highlight that as we go through": "housekeeping",
 "i just highlight the big ones": "housekeeping about the size of the azole list",
 "the reason why i highlight this is just because": "L2 housekeeping about targeting acne",
 "always like to highlight that first": "L2, non-pharmacologic therapy generally",
 "a couple of things i kind of want to highlight": "L3 housekeeping on a review slide",
 "we're gonna be highlighting primarily here": "L3 housekeeping -- what the next slides cover",
 "good luck on the test on monday": "sign-off at the end of Lecture 3",
 "nothing too notable there": "a NEGATIVE -- oseltamivir, he is saying there is nothing to flag",
 "so it's something to watch out for. and then again, adverse reactions": "generic renal-dosing caution, no drug named",
 "you do have to watch out for renal adjustments as well": "generic renal caution for the fluoroquinolone class",
 "it's also how well can the patient actually tolerate": "general point about tolerability, not a drug fact",
 "remember that tug of war": "restates the sympathetic/parasympathetic framing from earlier in the lecture",
}


def norm(s):
    s = H.unescape(re.sub(r"<[^>]+>", " ", s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("…", "..."), ("\xa0", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def load(lec):
    p = BASE + "pharm-lecture-%d.transcript.txt" % lec
    if not os.path.exists(p):
        sys.exit("transcript not found: %s" % p)
    return norm(re.sub(r"\[\d+:\d+(?::\d+)?\]", " ", open(p, encoding="utf-8").read()))


def covered_spans(text, lec):
    """Character ranges of the transcript this page already quotes from."""
    spans = []
    groups = ([(D.MARKER["lec"], D.MARKER["verify"])] +
              [(r["lec"], r["verify"]) for r in D.RULES] +
              [(p["lec"], p["verify"]) for p in D.PATTERNS] +
              [(s["lec"], s["verify"]) for s in D.STRATEGY] +
              [(s[3], s[4]) for s in D.STARRED])
    for l, verify in groups:
        if l != lec:
            continue
        for v in verify:
            i = text.find(norm(v))
            if i >= 0:
                spans.append((i - 700, i + len(norm(v)) + 700))
    return spans


def main():
    total_hits = gaps = 0
    for lec in (1, 2, 3):
        text = load(lec)
        spans = covered_spans(text, lec)
        seen, unc = set(), []
        for m in SIGNAL.finditer(text):
            total_hits += 1
            if any(a <= m.start() <= b for a, b in spans):
                continue
            ctx = text[max(0, m.start() - 170): m.start() + 230]
            if any(k in ctx for k in EXCLUDE):
                continue
            key = ctx[140:230]
            if key in seen:
                continue
            seen.add(key)
            unc.append((m.group(0), ctx))
        print("\n===== LECTURE %d =====  %d uncovered emphasis moment(s)" % (lec, len(unc)))
        for word, ctx in unc:
            gaps += 1
            print("  [%s] ...%s...\n" % (word, ctx.strip()[:300]))
    print("\nscanned %d emphasis hits across 3 transcripts; %d reviewed-and-excluded phrases; "
          "%d uncovered" % (total_hits, len(EXCLUDE), gaps))
    return 0


if __name__ == "__main__":
    sys.exit(main())
