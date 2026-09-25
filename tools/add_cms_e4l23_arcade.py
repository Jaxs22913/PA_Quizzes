#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 4 Lecture 23 (Valvular Heart Disease, Carter) Arcade decks.

Deck content lives in cms_e4l23_arcade_decks.json ({"id","name","color","icon",
"cards":[[prompt, answer], ...]}), slides only, atomic facts, his two slide
corrections applied, nothing from the unkeyed list (see cms_e4l23_scope.py).

Idempotent. Each deck object is inserted just before the closing
"// <!--/CMSE4-DECKS-->" fence (replaced in place if its id is already there),
and the three ids are added to the CMS I "exam4" deckIds list after
"cms-lipids-drugs", i.e. in lecture order before the heart failure decks.
ARCADE_JS=<path> points it at a different arcade.js (used to test on a copy).
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ARCADE = os.environ.get("ARCADE_JS") or os.path.join(os.path.dirname(HERE), "arcade.js")
CLOSE = "  // <!--/CMSE4-DECKS-->"
DECKS = json.load(open(os.path.join(HERE, "cms_e4l23_arcade_decks.json"), encoding="utf-8"))


def q(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def deck_js(d):
    rows = "\n".join("      [%s, %s]," % (q(a), q(b)) for a, b in d["cards"])
    return ('  { id: "%s", name: "%s", color: "%s",\n    icon: \'%s\',\n    cards: [\n%s\n    ]},\n'
            % (d["id"], d["name"], d["color"], d["icon"], rows))


def main():
    src = open(ARCADE, encoding="utf-8").read()
    assert src.count(CLOSE) == 1, "CMSE4 fence not found exactly once"
    for d in DECKS:
        block = deck_js(d)
        pat = re.compile(r'  \{ id: "%s",.*?\n    \]\},\n' % re.escape(d["id"]), re.S)
        if pat.search(src):
            src = pat.sub(lambda _m: block, src, count=1)
        else:
            src = src.replace(CLOSE, block + CLOSE)
    g0 = src.index('  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: [')
    e4 = src.index('{ id: "exam4", name: "Exam 4", deckIds: [', g0)
    e4_end = src.index("] }", e4)
    lst = src[e4:e4_end]
    ids = [d["id"] for d in DECKS]
    if not all('"%s"' % i in lst for i in ids):
        anchor = '"cms-lipids-drugs",'
        assert anchor in lst, "exam4 deck list has no cms-lipids-drugs anchor"
        lst = lst.replace(anchor, anchor + "\n      " + ", ".join('"%s"' % i for i in ids) + ",", 1)
        src = src[:e4] + lst + src[e4_end:]
    open(ARCADE, "w", encoding="utf-8").write(src)
    print("wrote %d decks, %d cards into %s" % (len(DECKS), sum(len(d["cards"]) for d in DECKS), ARCADE))


if __name__ == "__main__":
    main()
