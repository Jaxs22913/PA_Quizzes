#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Microbiology Exam 3 Arcade decks -- Lecture 14 so far (Lectures 14 to 19 as they land).

One deck per lecture (arcade_content_policy), authored from the deck's slides by way of the Exam 3 study guide:
`cards` (Study/Learn/Sprint, one atomic fact each) and `matchCards` (Match: term -> short tag). Which-antibiotic
facts are left out, as in the quizzes. Cards live in tools/micro_e3/lN_cards.json, keyed by deck id, each
{"cards": [...], "matchCards": [...]}.

ATOMIC FACTS ONLY. Idempotent: fenced between markers, re-runnable.

    python3 tools/add_micro_e3_arcade.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from _arcade_add import apply, ARCADE

# a rod with one polar flagellum
GNR_ICON = ('<rect x="3" y="9" width="12" height="6" rx="3"/>'
            '<path d="M15 12c1.5-2 3-2 4 0s2 2 2 0"/>')

C = {}
for frag in ("l14_cards.json",):
    C.update(json.load(open(os.path.join(HERE, "micro_e3", frag), encoding="utf-8")))


def deck(did, name, colour, icon):
    d = C[did]
    return (did, name, colour, icon, [tuple(x) for x in d["cards"]], [tuple(x) for x in d["matchCards"]])


DECKS = [
    deck("micro-gram-negative-bacilli", "Gram-Negative Bacilli", "accent3", GNR_ICON),
]

if __name__ == "__main__":
    apply("MICROE3", DECKS, "microbiology", "Microbiology", "exam3", "Exam 3")
    src = open(ARCADE, encoding="utf-8").read()
    g = src[src.index('{ id: "microbiology", name: "'):]
    g = g[:g.index("\n  ]},")]
    for d in DECKS:
        assert src.count('id: "%s"' % d[0]) == 1, d[0] + " defined more than once (or not at all)"
        assert '"%s"' % d[0] in g[g.index('id: "exam3"'):], d[0] + " not grouped under Microbiology Exam 3"
    print("deck defined once and grouped under Microbiology / Exam 3")
