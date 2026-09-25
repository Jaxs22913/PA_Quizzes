#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 5 Arcade decks -- Lecture 27 (Arterial Occlusive Disease
and Aortic Aneurysm) and Lecture 28 (Cardiomyopathy), both Carter.

Deck content lives in cms_e5_arcade_decks.json (a list of
{"id","name","color","icon","cards":[[prompt, answer], ...]}), authored from
the slides only, ATOMIC FACTS ONLY per [[arcade_content_policy]]. Five decks:
three for Lecture 27, two for Lecture 28.

Modeled on add_cms_e4_arcade.py. Idempotent: fenced between markers and
re-runnable; registers an "Exam 5" entry (id exam5) after Exam 4 INSIDE the CMS
group only. ARCADE_JS=<path> points it at a different arcade.js (used to test
against a scratch copy).
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ARCADE = os.environ.get("ARCADE_JS") or os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--CMSE5-DECKS-->", "  // <!--/CMSE5-DECKS-->"

DECKS = [(d["id"], d["name"], d["color"], d["icon"], [tuple(c) for c in d["cards"]])
         for d in json.load(open(os.path.join(HERE, "cms_e5_arcade_decks.json"), encoding="utf-8"))]


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

    # Register under CMS I, Exam 5. SCOPED TO THE CMS GROUP ONLY -- a global
    # substitution on an exam id once rewrote three other classes' deck lists.
    exam5 = ('    { id: "exam5", name: "Exam 5", deckIds: [\n      %s\n    ] }'
             % ", ".join('"%s"' % d[0] for d in DECKS))
    g_start = src.index('  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 4"') == 1, "CMS group not isolated cleanly (Exam 4 must exist once)"
    if 'name: "Exam 5"' in group:
        group = re.sub(r'    \{ id: "exam5", name: "Exam 5", deckIds: \[.*?\] \}',
                       lambda _m: exam5, group, flags=re.S)
    else:
        e4 = group.rindex("] }")
        group = group[:e4 + len("] }")] + ",\n" + exam5 + group[e4 + len("] }"):]
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
