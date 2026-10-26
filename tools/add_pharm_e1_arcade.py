#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Pharmacology I Exam 1 Arcade decks for Lecture 2 (Dermatology Medications) and Lecture 3 (ANS
Pharmacology). Lecture 1 already has its three decks; this adds the nine in _pharm_e1_arcade_l2l3.py.

Modeled on add_pharm_e3_arcade.py. ATOMIC FACTS ONLY per [[arcade_content_policy]]. NOTHING HERE IS A DOSE.

REFUSES TO WRITE unless every card AND every Match pair proves itself:
  - each `verify` substring is on the cited slide's VISIBLE text (runs and table cells; speaker notes are
    deliberately NOT read, per the slides-only rule) or in that slide's PICTURE transcription;
  - no dose or strength, no bare abbreviation (two or more capitals), no British spelling, no citation of the
    lecture, slide or lecturer inside card text;
  - no duplicate question, no two answers in a deck that differ only by plural or punctuation (Learn would
    show both), answers short enough for Sprint, Match tags under about eight words;
  - 8 to 20 cards and 10 to 13 Match pairs per deck.

Idempotent: fenced between PHARME1 markers, re-runnable. Carries the guards the Exam 2 and 3 adders earned:
decks must land INSIDE DEMO_DECKS, and the registry edit is scoped to the Pharmacology group's Exam 1 entry
(Lecture 1's decks and any other deck already listed there are kept, in order).

    python3 tools/add_pharm_e1_arcade.py --dry-run [--out PATH]   # writes the result elsewhere, never touches arcade.js
    python3 tools/add_pharm_e1_arcade.py               # apply to arcade.js
"""
import html as H, os, re, subprocess, sys, tempfile, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _pharm_e1_arcade_l2l3 as A

ROOT = os.path.dirname(HERE)
ARCADE = os.path.join(ROOT, "arcade.js")
BASE = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Pharmacology I Inbox/Exam 1/")
FILES = {"L2": "02. Dermatology Medications(1).pptx", "L3": "03. ANS Pharmacology(1).pptx"}
OPEN, CLOSE = "  // <!--PHARME1-DECKS-->", "  // <!--/PHARME1-DECKS-->"
_cache = {}


def norm(s):
    s = H.unescape(s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
                 ("−", "-"), ("\xa0", " "), ("…", "..."), ("​", ""), ("®", ""), ("→", "->")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def slide_text(lec, n):
    """Visible slide text only: every <a:t> run on the slide (table cells included), runs separated AND runs
    joined (PowerPoint splits words mid-run), plus the slide's PICTURE transcription. Never the notes."""
    key = (lec, n)
    if key not in _cache:
        z = zipfile.ZipFile(BASE + FILES[lec])
        member = "ppt/slides/slide%d.xml" % n
        parts = []
        if member in z.namelist():
            runs = [H.unescape(r) for r in re.findall(r"<a:t>(.*?)</a:t>", z.read(member).decode("utf-8", "ignore"), re.S)]
            parts += [" ".join(runs), "".join(runs)]
        if (lec, n) in A.PICTURE:
            parts.append(A.PICTURE[(lec, n)])
        _cache[key] = norm(" ".join(parts))
    return _cache[key]


def jstr(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def js(decks):
    out = []
    for did, name, color, icon, cards, match in decks:
        rows = "\n".join("      [%s, %s]," % (jstr(q), jstr(a)) for q, a in cards)
        mrows = "\n".join("      [%s, %s]," % (jstr(t), jstr(d)) for t, d in match)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ],\n"
                   "    matchCards: [\n%s\n    ] }," % (did, name, color, icon, rows, mrows))
    return "\n".join(out) + "\n"


DOSE = re.compile(r"(?i)\b\d+(\.\d+)?\s*(%|percent|mg\b|milligram|microgram|mcg|units?\b|grams?\b|g\b|ml\b|milliliter)")
ABBREV = re.compile(r"\b(?![IVX]+\b)[A-Z]{2,}[a-z]?\b(?! \()")     # ABBREV (full term) is the allowed form; Roman numerals are not abbreviations
BRITISH = re.compile(r"(?i)(oedema|anaemi|haem(?!ophilus)|oesoph|colour|behaviour|tumour|paediatr|labour|fibre|centre|"
                     r"isation|minimis|recognis|organis(?!m)|metabolis|sensitis|characteris|utilis|stabilis|neutralis|"
                     r"hydrolys|paralys(?!is)|analys(?!is)|localis|immunis|sterilis|desensitis)")
CITE = re.compile(r"(?i)\b(slide|lecture|deck|professor|syllabus|dr\.|wood|mcinnis)\b")
MATCH_FAMILY = {"mydriasis", "miosis"}     # single-word answers that are distinct terms, not plurals


def key_of(a):
    return re.sub(r"[^a-z0-9 ]", "", a.lower()).rstrip("s").strip()


def prove():
    fails, notes = [], []
    reg = {(kind, deck, front): pairs for kind, deck, front, pairs in A.REG}
    seen_q = set()
    nsub = 0
    ids = [d[0] for d in A.DECKS]
    if len(ids) != len(set(ids)):
        fails.append("duplicate deck id")
    for did, name, _c, _i, cards, match in A.DECKS:
        lec = A.LECTURE[did]
        if not 8 <= len(cards) <= 20:
            fails.append("%s: %d cards (need 8 to 20)" % (did, len(cards)))
        if not 10 <= len(match) <= 13:
            fails.append("%s: %d Match pairs (need 10 to 13)" % (did, len(match)))
        if ABBREV.search(name.replace("&amp;", "&")):
            fails.append("%s: bare abbreviation in deck name %r" % (did, name))
        keys = {}
        for kind, rows in (("card", cards), ("match", match)):
            for front, back in rows:
                pairs = reg.get((kind, did, front))
                if pairs is None:
                    fails.append("%s: %s not registered with C()/M(): %r" % (did, kind, front)); continue
                text = front + " " + back
                if DOSE.search(text):
                    fails.append("%s: dose or strength in %r" % (did, front))
                if ABBREV.search(text):
                    fails.append("%s: bare abbreviation %r in %r" % (did, ABBREV.search(text).group(0), front))
                if BRITISH.search(text):
                    fails.append("%s: British spelling %r in %r" % (did, BRITISH.search(text).group(0), front))
                if CITE.search(text):
                    fails.append("%s: cites the source inside card text: %r" % (did, front))
                if kind == "card":
                    if front in seen_q:
                        fails.append("%s: duplicate question %r" % (did, front))
                    seen_q.add(front)
                    if not front.rstrip().endswith(("?", ".")):
                        fails.append("%s: question is not a sentence %r" % (did, front))
                    if len(back.split()) > 18:
                        fails.append("%s: answer too long for Sprint (%d words): %r" % (did, len(back.split()), front))
                    if ";" in back:
                        fails.append("%s: answer has two clauses (semicolon): %r" % (did, front))
                    k = key_of(back)
                    if k in keys and keys[k] != back and k not in MATCH_FAMILY:
                        fails.append("%s: answers %r and %r differ only by plural or punctuation" % (did, keys[k], back))
                    keys.setdefault(k, back)
                else:
                    if len(back.split()) > 8:
                        fails.append("%s: Match tag over eight words: %r -> %r" % (did, front, back))
                    if len(front.split()) > 4:
                        fails.append("%s: Match term is not a short name: %r" % (did, front))
                for slide, subs in pairs:
                    body = slide_text(lec, slide)
                    if not body:
                        fails.append("%s: %s slide %d has no visible text" % (did, lec, slide))
                    if not subs:
                        fails.append("%s: %r cites slide %d with nothing to verify" % (did, front, slide))
                    for v in subs:
                        nsub += 1
                        if norm(v) not in body:
                            fails.append("%s: NOT ON %s SLIDE %d: %r (%s %r)" % (did, lec, slide, v, kind, front))
        dup = {a: n for a, n in ((a, sum(1 for _q, b in cards if b == a)) for a in {b for _q, b in cards}) if n > 1}
        if dup:
            notes.append("  note: %s has repeated answer values (engine groups them; not an error): %s" % (did, dup))
    return fails, notes, nsub


def main():
    dry = "--dry-run" in sys.argv
    fails, notes, nsub = prove()
    nc = sum(len(d[4]) for d in A.DECKS)
    nm = sum(len(d[5]) for d in A.DECKS)
    print("decks: %d   cards: %d   match pairs: %d   slide substrings: %d   %s"
          % (len(A.DECKS), nc, nm, nsub, "OK" if not fails else "FAILED %d" % len(fails)))
    for n in notes:
        print(n)
    for f in fails[:80]:
        print("   " + f)
    if fails:
        sys.exit("arcade verification failed -- refusing to write")

    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(A.DECKS) + CLOSE
    ids = [d[0] for d in A.DECKS]
    if OPEN not in src:
        for did in ids:
            assert 'id: "%s"' % did not in src, "deck id %s already exists outside the PHARME1 fence" % did
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]
    else:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)

    # registry: the Pharmacology group's Exam 1 entry only
    g_start = src.index('  { id: "pharm-1", name: "Pharmacology I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 1"') == 1, "Pharmacology group not isolated cleanly"
    m = re.search(r'\{ id: "exam1", name: "Exam 1", deckIds: \[(.*?)\] \}', group, flags=re.S)
    assert m, "Pharmacology Exam 1 entry not found"
    current = re.findall(r'"([a-z0-9-]+)"', m.group(1))
    keep = [i for i in current if i not in ids]
    assert {"pharm-antibacterials", "pharm-antivirals", "pharm-antifungals"} <= set(keep), "Lecture 1 decks missing from Exam 1"
    exam1 = '{ id: "exam1", name: "Exam 1", deckIds: [\n      %s\n    ] }' % ", ".join('"%s"' % i for i in keep + ids)
    group = group[:m.start()] + exam1 + group[m.end():]
    src = src[:g_start] + group + src[g_end:]

    # guards: inside DEMO_DECKS, and both structures carry every deck
    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did in ids:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did
    defined = set(re.findall(r'\{ id: "([a-z0-9-]+)", name: "[^"]+", color:', src))
    grouped = set(re.findall(r'"([a-z0-9-]+)"', src[src.index("exams: ["):]))
    for did in ids:
        assert did in defined and did in grouped, "%s missing from the deck list or the exam grouping" % did

    if dry:
        if "--out" in sys.argv:
            target = sys.argv[sys.argv.index("--out") + 1]
        else:
            fd, target = tempfile.mkstemp(prefix="arcade_e1_dryrun_", suffix=".js")
            os.close(fd)
    else:
        target = ARCADE
    with open(target, "w", encoding="utf-8") as f:
        f.write(src)
    r = subprocess.run(["node", "--check", target], capture_output=True, text=True)
    print("node --check:", "OK" if r.returncode == 0 else "FAILED\n" + r.stderr[:600])
    if r.returncode:
        sys.exit(1)
    if dry:
        print("dry run: wrote %s (arcade.js untouched)" % target)
    print("%s %d decks, %d cards, %d match pairs" % ("would add" if dry else "wrote", len(A.DECKS), nc, nm))
    for did, name, _c, _i, cards, match in A.DECKS:
        print("   %-36s %-58s %2d cards  %2d match" % (did, re.sub("&[a-z]+;", "&", name), len(cards), len(match)))


if __name__ == "__main__":
    main()
