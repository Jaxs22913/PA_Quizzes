#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared helper: splice decks into arcade.js and register them under a class.

Every add_*_arcade.py script repeats the same three risky steps -- fence the
deck block, insert it INSIDE DEMO_DECKS, and edit only the target class group.
The two traps are recorded in add_cms_e3_arcade.py and both are guarded here:

  * a deck placed after DEMO_DECKS closes is valid JavaScript but invisible to
    findDeck(), so a parse check passes while the page throws on deck.cards;
  * a global re-sub on an exam id once rewrote three other classes' deck lists,
    so the group edit is cut out and applied to that group alone.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCADE = os.path.join(ROOT, "arcade.js")


def json_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def js(decks):
    out = []
    for did, name, colour, icon, cards in decks:
        rows = "\n".join("      [%s, %s]," % (json_str(q), json_str(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ]},\n" % (did, name, colour, icon, rows))
    return "\n".join(out)


def apply(tag, decks, group_id, group_name, exam_id, exam_name):
    """Idempotent: fenced by tag, re-runnable, verified before writing."""
    OPEN, CLOSE = "  // <!--%s-DECKS-->" % tag, "  // <!--/%s-DECKS-->" % tag
    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(decks) + CLOSE
    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)
    else:
        end = src.index("\n];", src.index("var DEMO_DECKS = ["))
        src = src[:end] + "\n\n" + block + src[end:]

    entry = ('    { id: "%s", name: "%s", deckIds: [\n      %s\n    ] }'
             % (exam_id, exam_name, ", ".join('"%s"' % d[0] for d in decks)))
    gpat = r'  \{ id: "%s", name: "[^"]+", exams: \[' % re.escape(group_id)
    m = re.search(gpat, src)
    if m:                                    # edit ONLY inside this group
        g_start = m.start()
        g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
        group = src[g_start:g_end]
        if 'id: "%s"' % exam_id in group:
            group = re.sub(r'    \{ id: "%s", name: "[^"]+", deckIds: \[.*?\] \}' % re.escape(exam_id),
                           lambda _m: entry, group, flags=re.S)
        else:
            last = group.rindex("] }") + len("] }")
            group = group[:last] + ",\n" + entry + group[last:]
        src = src[:g_start] + group + src[g_end:]
    else:                                    # class has no group yet -- create one
        anchor = '\n  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: ['
        assert src.count(anchor) == 1, "could not place the new group uniquely"
        newg = ('  { id: "%s", name: "%s", exams: [\n%s\n  ]},\n' % (group_id, group_name, entry))
        src = src.replace(anchor, "\n" + newg + anchor)

    d0 = src.index("var DEMO_DECKS = ["); d1 = src.index("\n];", d0)
    for did, *_ in decks:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s landed OUTSIDE the DEMO_DECKS array" % did
    assert src.index('id: "%s"' % group_id) > d1, "the group landed INSIDE DEMO_DECKS"

    open(ARCADE, "w", encoding="utf-8").write(src)
    n = sum(len(d[4]) for d in decks)
    print("wrote %d deck(s), %d cards -> %s / %s" % (len(decks), n, group_name, exam_name))
    for did, name, _c, _i, cards in decks:
        print("   %-24s %-42s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))
