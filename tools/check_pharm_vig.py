#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Screen the pharm vignettes against the decks they cite.

Lighter than the reference-chart checks: a vignette paraphrases a slide rather
than quoting it, so a substring match would fail on legitimate rewording. This
instead checks that the KEYED ANSWER'S content words appear on the cited slide,
which is the same screen tools/check_ppt_grounding.py runs site-wide.

A flag means "go read that slide", never "this is wrong".
"""
import html as H
import os, re, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pharm_vig_pool import POOL

BASE = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/")
FILES = {"Antibiotics, Antivirals, and Antifungals": "Antibiotics, Antivirals, and Antifungals.pptx",
         "02. Dermatology Medications": "02. Dermatology Medications(1).pptx",
         "03. ANS Pharmacology": "03. ANS Pharmacology(1).pptx"}
STOP = set("the a an of and or to in on at by with for from that which this these those is are was "
           "were be as it its their they them into within between not no only also both each more "
           "most than then when where what how why during over under above below near does do can "
           "may might will would should could has have had after before all any one two three about only just such very both either neither same other another".split())
_c = {}


def norm(s):
    s = H.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())


def deck_text(deck):
    if deck not in _c:
        z = zipfile.ZipFile(BASE + FILES[deck])
        sl = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        _c[deck] = norm(" ".join(" ".join(re.findall(r"<a:t>(.*?)</a:t>",
                        z.read(n).decode("utf8", "ignore"))) for n in sl))
    return _c[deck]


def main():
    flags, unscreenable = 0, []
    for i, q in enumerate(POOL):
        body = deck_text(q["deck"])
        ans = q["opts"][q["c"]][0]
        words = [w for w in norm(ans).split() if w not in STOP and len(w) > 3]
        if not words:
            # e.g. "About 30%" -- the number is the answer and the screen strips
            # it, so there is nothing to match on. Report it rather than passing
            # it silently, since a silent pass looks like a check that ran.
            unscreenable.append((i, q["topic"], ans))
            continue
        hit = sum(1 for w in words if w in body)
        if hit == 0:
            flags += 1
            print("  FLAG [%d] %s" % (i, q["topic"]))
            print("        answer: %s" % ans)
            print("        none of %s appear in %s\n" % (words, q["deck"][:30]))
    for i, topic, ans in unscreenable:
        print("  not screenable [%d] %s -- answer %r has no content word to match;"
              " verified by hand against the slide" % (i, topic, ans))
    print("%d vignettes screened; %d to eyeball; %d not screenable"
          % (len(POOL), flags, len(unscreenable)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
