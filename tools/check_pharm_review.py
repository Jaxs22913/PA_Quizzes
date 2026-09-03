#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify every quote on the Dr. Wood exam review page against the recording.

Same contract as check_pharm_wood.py, pointed at the 3 September review session
instead of the three content lectures. Every entry carries `verify` substrings
that must appear in the transcript.

WHY THIS MATTERS MORE HERE THAN ANYWHERE ELSE ON THE SITE. A review session is
the one recording where the lecturer says what will and will not be on the
paper, and a page that misreports that sends people to revise the wrong thing
the night before. Nothing goes on the page that is not in the transcript.

The transcript stays in ~/Desktop and is never copied into this repo, so this
only runs on Jaxon's machine -- the same arrangement the PowerPoint-grounding
checks already use.
"""
import html as H
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _pharm_review_data as D

SRC = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/recordings/"
                         "pharm-exam-1-review-wood-2026-09-03.transcript.txt")
_cache = {}


def norm(s):
    s = H.unescape(re.sub(r"<[^>]+>", " ", s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("…", "..."), ("\xa0", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


# KNOWN MIS-HEARINGS, and why this list has to exist.
#
# The speech model renders several drug names wrongly and consistently --
# "Pfizer stigmine" for physostigmine, "immunopenicillins" for aminopenicillins.
# A page that quoted those verbatim would be unreadable and would look like the
# lecturer said something he did not. But silently rewriting a quote and then
# "verifying" it against the raw transcript would make the check meaningless.
#
# So the correction is declared here, applied to the TRANSCRIPT before matching,
# and listed on the page itself. The quote on the page is then still proved to
# be his words, with only the spelling of a drug name repaired.
ASR_FIXES = [
    ("pfizer stigmine", "physostigmine"),
    ("physostigmine", "physostigmine"),
    ("immunopenicillins", "aminopenicillins"),
    ("point by serial", "point-biserial"),
    ("rockuronium", "rocuronium"),
    ("the pants", "the pance"),
    ("our gastral", "ergosterol"),
    ("vecan rockuronium", "vecuronium and rocuronium"),
]


def transcript():
    if not _cache:
        if os.path.exists(SRC):
            raw = open(SRC, encoding="utf-8").read()
        else:
            # transcribe_long.py only writes the joined transcript when the whole
            # run finishes, but it appends each chunk as it lands. Falling back to
            # the chunk file lets the page be fact-checked against the part that
            # HAS transcribed, which matters when the exam is the next morning.
            import json
            chunks = SRC.replace(".transcript.txt", ".chunks.jsonl")
            if not os.path.exists(chunks):
                sys.exit("no transcript and no chunks yet: %s" % SRC)
            segs = []
            for line in open(chunks, encoding="utf-8"):
                for seg in json.loads(line).get("segments", []):
                    segs.append(seg["text"])
            raw = " ".join(segs)
            print("NOTE: verifying against %d partial chunk(s); the full transcript "
                  "is not written yet." % sum(1 for _ in open(chunks, encoding="utf-8")))
        t = norm(re.sub(r"\[\d+:\d+(?::\d+)?\]", " ", raw))
        for wrong, right in ASR_FIXES:
            t = t.replace(wrong, right)
        _cache["t"] = t
    return _cache["t"]


def main():
    t = transcript()
    entries = []
    for group, items in (("answer", D.ANSWERS), ("rule", D.RULES)):
        for it in items:
            entries.append(("%s: %s" % (group, it["title"]), it.get("quote", ""), it["verify"]))

    bad, checked = [], 0
    for name, quote, verify in entries:
        for v in verify:
            checked += 1
            if norm(v) not in t:
                bad.append("%s -- not in the recording: %r" % (name, v))
        # A quote is displayed in quotation marks, so it must be verbatim, not
        # merely paraphrase-adjacent. Punctuation and casing are normalised; the
        # words are not.
        if quote and norm(quote) not in t:
            bad.append("%s -- QUOTE is not verbatim in the recording" % name)
    print("checked %d verify strings across %d entries" % (checked, len(entries)))
    if bad:
        print("\nFAILED:")
        for b in bad:
            print("  " + b)
        return 1
    print("every quote and claim is grounded in the recording")
    return 0


if __name__ == "__main__":
    sys.exit(main())
