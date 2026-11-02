#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 7 Arcade decks (Respiratory Block Exam II, Lectures 39-45).

Exam 7 is built a lecture or two at a time by more than one builder, so deck content lives per lecture:
tools/cms_e7_arcade/lNN.json, each a list of {"id","name","color","icon","cards":[[prompt, answer], ...]},
authored from the slides only, ATOMIC FACTS ONLY per [[arcade_content_policy]]. Deck ids are
"cms-e7-lNN-<topic>". This script reads whichever lecture files exist, in lecture order.

Modeled on add_cms_e6_arcade.py. Idempotent: fenced between markers and re-runnable; registers an "Exam 7"
entry (id exam7) after Exam 6 INSIDE the CMS group only. ARCADE_JS=<path> points it at a different arcade.js
(used to test against a scratch copy). See tools/cms_e7_README.md.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ARCADE = os.environ.get("ARCADE_JS") or os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--CMSE7-DECKS-->", "  // <!--/CMSE7-DECKS-->"

DECKS = []
for _n in range(39, 46):
    _p = os.path.join(HERE, "cms_e7_arcade", "l%d.json" % _n)
    if os.path.exists(_p):
        for d in json.load(open(_p, encoding="utf-8")):
            assert d["id"].startswith("cms-e7-l%d-" % _n), "%s: deck id %r must start with cms-e7-l%d-" % (_p, d["id"], _n)
            DECKS.append((d["id"], d["name"], d["color"], d["icon"], [tuple(c) for c in d["cards"]]))
assert DECKS, "no lecture deck files in tools/cms_e7_arcade/"
assert len({d[0] for d in DECKS}) == len(DECKS), "duplicate deck ids"


def json_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def js(decks):
    out = []
    for did, name, colour, icon, cards in decks:
        rows = "\n".join('      [%s, %s],' % (json_str(q), json_str(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ]},\n" % (did, name, colour, icon, rows))
    return "\n".join(out)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(DECKS) + CLOSE

    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)
    else:
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]

    # Register under CMS I, Exam 7. SCOPED TO THE CMS GROUP ONLY -- a global
    # substitution on an exam id once rewrote three other classes' deck lists.
    exam7 = ('    { id: "exam7", name: "Exam 7", deckIds: [\n      %s\n    ] }'
             % ", ".join('"%s"' % d[0] for d in DECKS))
    g_start = src.index('  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 6"') == 1, "CMS group not isolated cleanly (Exam 6 must exist once)"
    if 'name: "Exam 7"' in group:
        group = re.sub(r'    \{ id: "exam7", name: "Exam 7", deckIds: \[.*?\] \}',
                       lambda _m: exam7, group, flags=re.S)
    else:
        e6 = group.rindex("] }")
        group = group[:e6 + len("] }")] + ",\n" + exam7 + group[e6 + len("] }"):]
    src = src[:g_start] + group + src[g_end:]

    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did, *_ in DECKS:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did

    open(ARCADE, "w", encoding="utf-8").write(src)
    n = sum(len(d[4]) for d in DECKS)
    print("wrote %d decks, %d cards into %s" % (len(DECKS), n, ARCADE))
    for did, name, _c, _i, cards in DECKS:
        print("   %-24s %-58s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))


if __name__ == "__main__":
    main()
