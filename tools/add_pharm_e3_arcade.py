#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Pharmacology I Exam 3 Arcade decks (Lecture 9, Diuretics and Heart Failure Drugs).

Six decks, one per Exam 3 topic quiz, authored in _pharm_e3_arcade_l9.py. ATOMIC FACTS ONLY per
[[arcade_content_policy]]. NOTHING HERE IS A DOSE: the assertions below refuse one.

REFUSES TO WRITE unless every card proves itself: each `verify` substring must be on the slide the card cites
(pharm_e3_lib.slide_text, picture-slide text included), each `tf` quote in the recording transcript, no card is a
dose, no duplicate question, every answer is short (Sprint is the most length-sensitive mode).

Idempotent: fenced between PHARME3 markers, re-runnable. Carries the guards the Exam 2 adder earned the hard way:
decks must land INSIDE DEMO_DECKS, and the exam registry edit is scoped to the Pharmacology group so it cannot
rewrite another class's deck list.

    python3 tools/add_pharm_e3_arcade.py --dry-run     # writes the result to the scratchpad, never touches arcade.js
    python3 tools/add_pharm_e3_arcade.py               # apply to arcade.js (coordinator only: it is a shared file)
"""
import os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pharm_e3_lib as L
import check_pharm_e3_wood as W
import _pharm_e3_arcade_l9 as A

DECKS = A.DECKS
ROOT = os.path.dirname(HERE)
ARCADE = os.path.join(ROOT, "arcade.js")
SCRATCH = "/private/tmp/claude-501/-Users-jaxonluke/8c127d8b-c2b9-43bc-94a9-c4dfe0f6e46d/scratchpad/arcade_e3_dryrun.js"
OPEN, CLOSE = "  // <!--PHARME3-DECKS-->", "  // <!--/PHARME3-DECKS-->"


def jstr(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def js(decks):
    out = []
    for did, name, color, icon, cards in decks:
        rows = "\n".join('      [%s, %s],' % (jstr(q), jstr(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ] }," % (did, name, color, icon, rows))
    return "\n".join(out) + "\n"


def prove():
    bad = re.compile(r"(?i)\b\d+\s*(mg(?!/dL)|milligram|microgram|mcg|unit)\b")
    fails = []
    byq = {}
    for deck, q, pairs, quotes in A.REG:
        byq[(deck, q)] = (pairs, quotes)
    seen = set()
    nsub = nq = 0
    for did, _n, _c, _i, cards in DECKS:
        answers = {}
        for q, a in cards:
            if (did, q) not in byq:
                fails.append("%s: card not registered with C(): %r" % (did, q)); continue
            if q in seen:
                fails.append("%s: duplicate question %r" % (did, q))
            seen.add(q)
            if bad.search(q + " " + a):
                fails.append("%s: dose or strength in card %r" % (did, q))
            if len(a.split()) > 18:
                fails.append("%s: answer too long for Sprint (%d words): %r" % (did, len(a.split()), q))
            if not q.rstrip().endswith(("?", ".")):
                fails.append("%s: question is not a sentence %r" % (did, q))
            answers.setdefault(a, 0); answers[a] += 1
            pairs, quotes = byq[(did, q)]
            for slide, subs in pairs:
                body = L.slide_text("L9", slide)
                if not body:
                    fails.append("%s: slide %d has no text" % (did, slide))
                for v in subs:
                    nsub += 1
                    if L.norm(v) not in body:
                        fails.append("%s: NOT ON SLIDE %d: %r (card %r)" % (did, slide, v, q))
            for qt in quotes:
                nq += 1
                if W.norm(qt) not in W.transcript("L9"):
                    fails.append("%s: NOT IN TRANSCRIPT: %r (card %r)" % (did, qt, q))
        dup = {a: n for a, n in answers.items() if n > 1}
        if dup:
            print("  note: %s has repeated answer values (engine groups them; not an error): %s" % (did, dup))
    return fails, nsub, nq


def main():
    dry = "--dry-run" in sys.argv
    fails, nsub, nq = prove()
    n = sum(len(d[4]) for d in DECKS)
    print("cards: %d   slide substrings: %d   transcript quotes: %d   %s" % (n, nsub, nq, "OK" if not fails else "FAILED %d" % len(fails)))
    for f in fails[:60]:
        print("   " + f)
    if fails:
        sys.exit("arcade verification failed -- refusing to write")

    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(DECKS) + CLOSE
    ids = [d[0] for d in DECKS]
    if OPEN not in src:
        for did in ids:
            assert 'id: "%s"' % did not in src, "deck id %s already exists outside the PHARME3 fence" % did

    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)
    else:
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]

    exam3 = '    { id: "exam3", name: "Exam 3", deckIds: [\n      %s\n    ] }' % ", ".join('"%s"' % i for i in ids)
    g_start = src.index('  { id: "pharm-1", name: "Pharmacology I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 1"') == 1 and group.count('name: "Exam 2"') == 1, "Pharmacology group not isolated cleanly"
    if 'name: "Exam 3"' in group:
        group = re.sub(r'    \{ id: "exam3", name: "Exam 3", deckIds: \[.*?\] \}', lambda _m: exam3, group, flags=re.S)
    else:
        e_last = group.rindex("] }")
        group = group[:e_last + len("] }")] + ",\n" + exam3 + group[e_last + len("] }"):]
    src = src[:g_start] + group + src[g_end:]

    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did in ids:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did

    target = SCRATCH if dry else ARCADE
    with open(target, "w", encoding="utf-8") as f:
        f.write(src)
    if dry:
        r = subprocess.run(["node", "--check", target], capture_output=True, text=True)
        print("node --check:", "OK" if r.returncode == 0 else "FAILED\n" + r.stderr[:600])
        if r.returncode:
            sys.exit(1)
        print("dry run: wrote %s (arcade.js untouched)" % target)
    print("%s %d decks, %d cards" % ("would add" if dry else "wrote", len(DECKS), n))
    for did, name, _c, _i, cards in DECKS:
        print("   %-26s %-60s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))


if __name__ == "__main__":
    main()
