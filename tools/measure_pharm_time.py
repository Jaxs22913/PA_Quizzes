#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Measure how long Dr. Wood spent on each topic.

He said outright: "If I spend a lot of time talking about something, I'm
probably thinking about that when writing test questions." This turns that into
a number.

METHOD, and its limits. He works through each deck in order, so a topic runs
from its first substantive mention to the first substantive mention of the NEXT
topic. Boundaries come from the word-level timings in the .chunks.jsonl, not
from the rendered transcript, so they are audio-accurate to the segment.

That means the figure is TIME BETWEEN BOUNDARIES, not time strictly on-topic --
a digression inside a block counts toward that block. It is a proxy for weight,
which is exactly what he said to use it as, and it should not be read as
anything finer than "he spent much longer here than there".
"""
import json, os, re, sys

BASE = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/recordings/")

# Ordered as he teaches them. Each entry is (label, regex that marks the topic
# ACTUALLY starting -- deliberately specific, so a passing earlier reference
# does not open the block early).
TOPICS = {
 1: [("Antibiotic principles &amp; resistance", r"\bbacteriostatic\b|\bbactericidal\b"),
     ("Penicillins", r"\bnatural penicillins?\b|\bpenicillin g\b"),
     ("Cephalosporins", r"\bcephalosporins?\b"),
     ("Monobactams", r"\bmonobactam|\baztreonam\b"),
     ("Carbapenems", r"\bcarbapenem"),
     ("Vancomycin", r"\bvancomycin\b"),
     ("Macrolides", r"\bmacrolides?\b"),
     ("Tetracyclines", r"\btetracyclines?\b"),
     ("Aminoglycosides", r"\baminoglycosides?\b"),
     # the transcript renders "linezolid" as "linea", so match that too
     ("Linezolid &amp; daptomycin", r"\boxazolidin|\blinezolid\b|\blinea\b|\bdaptomycin\b"),
     ("Fluoroquinolones", r"\bfluoroquinolones?\b"),
     ("Clindamycin", r"\bclindamycin\b"),
     ("Trimethoprim/sulfamethoxazole", r"\bsulfamethoxazole\b|\bbactrim\b|\bseptra\b"),
     ("Metronidazole", r"\bmetronidazole\b|\bflagyl\b"),
     ("Polymyxins", r"\bpolymyxin|\bpolymixin"),
     ("Antifungals", r"\bantifungal|\bfungi\b"),
     ("Antivirals", r"\bantiviral|\bherpes\b"),
     ("Wrap-up &amp; questions", r"\bany questions\b|\bthat's antibiotics\b")],
 2: [("Topical drug delivery &amp; vehicles", r"\bvehicle|\bointment\b"),
     ("Acne &mdash; pathophysiology", r"\bmicrocomedone\b|\bacne\b"),
     ("Acne &mdash; topical therapy", r"\bbenzoyl peroxide\b"),
     ("Acne &mdash; systemic therapy", r"\bisotretinoin\b|\bisotritone\b|\bisotradenone\b"),
     ("Atopic dermatitis", r"\batopic dermatitis\b"),
     ("Topical corticosteroids", r"\btopical corticosteroids?\b|\bpotency\b"),
     ("Topical anti-infectives", r"\bbacitracin\b|\bmupirocin\b"),
     ("Topical antifungals &amp; antivirals", r"\bciclopirox\b|\bimiquimod\b")],
 3: [("ANS organisation &amp; receptors", r"\bautonomic nervous system\b|\bnicotinic\b"),
     ("Cholinergic agonists", r"\bcholinergic agonists?\b|\bbethanechol\b"),
     ("Cholinesterase inhibitors", r"\bacetylcholinesterase inhibitor|\bneostigmine\b"),
     ("Antimuscarinics", r"\bantimuscarinic|\batropine\b"),
     ("Neuromuscular blockers", r"\bneuromuscular.blocking\b|\bsuccinylcholine\b"),
     ("Adrenergic agonists", r"\badrenergic agonists?\b|\bepinephrine\b"),
     ("Adrenergic antagonists", r"\badrenergic antagonists?\b|\bphenoxybenzamine\b"),
     ("Beta blockers", r"\bbeta blockers?\b|\bpropranolol\b"),
     ("Q&amp;A and study advice", r"\bany advice for studying\b|\bdo i have any advice\b")],
}


def segments(lec):
    out = []
    with open(BASE + "pharm-lecture-%d.chunks.jsonl" % lec, encoding="utf-8") as fh:
        for line in fh:
            for s in json.loads(line)["segments"]:
                out.append((float(s["start"]), float(s["end"]), s["text"].lower()))
    out.sort()
    return out


def hhmm(sec):
    m, s = divmod(int(sec), 60)
    return "%d:%02d" % (m, s) if m < 60 else "%d:%02d:%02d" % (m // 60, m % 60, s)


def measure(lec):
    segs = segments(lec)
    total = segs[-1][1]
    # Boundaries must be MONOTONIC. The first attempt searched each topic
    # independently and opened cephalosporins at 18:25 -- where he name-drops it
    # while teaching penicillins -- which handed penicillins a NEGATIVE duration
    # and gave cephalosporins 42 minutes it never had. So each topic is searched
    # only AFTER the previous one opened, which is safe because he teaches the
    # deck in order.
    starts, floor = [], 0.0
    for label, pat in TOPICS[lec]:
        rx = re.compile(pat)
        hit = None
        for i, (st, _e, tx) in enumerate(segs):
            if st < floor + 20 or not rx.search(tx):
                continue
            # needs a second mention close by, so a passing reference does not
            # open the block. Thresholds are loose (20s floor, 240s window) because the
            # short topics are real: polymyxins genuinely get about a minute, and a
            # stricter rule swallowed them into the neighbouring block entirely.
            near = sum(1 for s2, _e2, t2 in segs[i:] if s2 < st + 240 and rx.search(t2))
            if near >= 2:
                hit = st
                break
        if hit is None:
            # Monobactams, polymyxins and linezolid get ONE mention at the point
            # he teaches them -- the two-mention rule dropped all three, and a
            # topic he covers in 90 seconds is still a topic. The monotonic floor
            # is what keeps a stray single mention from opening a block early.
            for st, _e, tx in segs:
                if st >= floor + 20 and rx.search(tx):
                    hit = st
                    break
        if hit is not None:
            floor = hit
        starts.append((label, hit))
    known = [(l, s) for l, s in starts if s is not None]
    rows = []
    for i, (label, st) in enumerate(known):
        end = known[i + 1][1] if i + 1 < len(known) else total
        rows.append((label, st, end, end - st))
    return rows, total


def main():
    allrows = {}
    for lec in (1, 2, 3):
        rows, total = measure(lec)
        allrows[lec] = rows
        print("\n===== LECTURE %d  (%s total) =====" % (lec, hhmm(total)))
        for label, st, en, dur in sorted(rows, key=lambda r: -r[3]):
            bar = "#" * max(1, int(dur / 60))
            print("  %-34s %5.1f min  %-6s  %s" % (re.sub(r"&\w+;", "-", label),
                                                   dur / 60, hhmm(st), bar))
    return allrows


if __name__ == "__main__":
    main()
