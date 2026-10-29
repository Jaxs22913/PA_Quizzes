#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 6 Arcade decks (Respiratory Block Exam I, Lectures 33-38).

Exam 6 is built a lecture or two at a time by more than one builder, so deck content lives per lecture:
tools/cms_e6_arcade/lNN.json, each a list of {"id","name","color","icon","cards":[[prompt, answer], ...]},
authored from the slides only, ATOMIC FACTS ONLY per [[arcade_content_policy]]. Deck ids are
"cms-e6-lNN-<topic>". This script reads whichever lecture files exist, in lecture order.

Modeled on add_cms_e5_arcade.py. Idempotent: fenced between markers and re-runnable; registers an "Exam 6"
entry (id exam6) after Exam 5 INSIDE the CMS group only. ARCADE_JS=<path> points it at a different arcade.js
(used to test against a scratch copy). See tools/cms_e6_README.md.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ARCADE = os.environ.get("ARCADE_JS") or os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--CMSE6-DECKS-->", "  // <!--/CMSE6-DECKS-->"

DECKS = []
for _n in range(33, 39):
    _p = os.path.join(HERE, "cms_e6_arcade", "l%d.json" % _n)
    if os.path.exists(_p):
        for d in json.load(open(_p, encoding="utf-8")):
            assert d["id"].startswith("cms-e6-l%d-" % _n), "%s: deck id %r must start with cms-e6-l%d-" % (_p, d["id"], _n)
            DECKS.append((d["id"], d["name"], d["color"], d["icon"], [tuple(c) for c in d["cards"]]))
assert DECKS, "no lecture deck files in tools/cms_e6_arcade/"
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

    # Register under CMS I, Exam 6. SCOPED TO THE CMS GROUP ONLY -- a global
    # substitution on an exam id once rewrote three other classes' deck lists.
    exam6 = ('    { id: "exam6", name: "Exam 6", deckIds: [\n      %s\n    ] }'
             % ", ".join('"%s"' % d[0] for d in DECKS))
    g_start = src.index('  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 5"') == 1, "CMS group not isolated cleanly (Exam 5 must exist once)"
    if 'name: "Exam 6"' in group:
        group = re.sub(r'    \{ id: "exam6", name: "Exam 6", deckIds: \[.*?\] \}',
                       lambda _m: exam6, group, flags=re.S)
    else:
        e5 = group.rindex("] }")
        group = group[:e5 + len("] }")] + ",\n" + exam6 + group[e5 + len("] }"):]
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
