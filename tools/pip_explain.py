#!/usr/bin/env python3
"""Pip's plain-language explanations ("Pip explains").

Jaxon, 2026-10-09: when someone asks for help, Pip should not just hand them the guide; he should
explain the concept in easier language (no word limit, but never a whole page).

Source of truth: pip/explain/<folder slug>.json (committed, hand-checked content). Each card explains
ONE concept from ONE section of that exam's study guide, in plain words, and links to that section.
tools/build_pip_data.py ships the cards to pip/data/explain/<slug>.json (git-ignored, generated).

  python3 tools/pip_explain.py units <slug> [--out DIR]   the guide's sections, for whoever writes cards
  python3 tools/pip_explain.py check [<slug> ...]         validate cards (all files when no slug given)
  python3 tools/pip_explain.py lint <slug> DRAFT.json      check a writer's draft before it is merged
  python3 tools/pip_explain.py rehash <slug> u12 [u13 ...] after a guide edit, mark those units' cards current
                                                          (only once someone has re-read them against the new text)
  python3 tools/pip_explain.py assemble <slug> PART.json [PART.json ...]
                                                          merge written cards ({id,u,t,k,q,x}) into
                                                          pip/explain/<slug>.json, adding h, doc and a

A card (pip/explain/<slug>.json -> {"v": 1, "s": slug, "cards": [...]}):
  id   kebab-case, unique in the file
  u    the unit id it was written from ("u12", from `units`)
  h    that unit's text hash when the card was written (a changed guide section makes the card stale)
  doc  the guide page file;  a  the section anchor on that page (the card's "Open in the guide" link)
  t    the concept's name (<= 80 characters)
  k    1-8 other names a student might use (synonyms, the abbreviation, an eponym)
  q    2-4 ways a student might ask about it ("why does nephrotic syndrome cause edema")
  x    the explanation: plain words, about 60-180 words, no headings or bold
Run tools/build_pip_data.py first: `units` and `check` read pip/data/guide/<slug>.json.
Writing spec (voice, grounding, length, the two example cards): tools/pip_explain_STYLE.md. The pipeline that built
the first cards (2026-10-09): one writer per exam from `units`, `lint` per part, then an INDEPENDENT fact-checker
who verifies every sentence against its unit, fixes, adds missing concepts, then `assemble` + `check`.
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GUIDE = os.path.join(ROOT, "pip", "data", "guide")
SRC = os.path.join(ROOT, "pip", "explain")


def die(msg):
    sys.stderr.write("pip_explain: " + msg + "\n")
    sys.exit(2)


def load_guide(slug):
    p = os.path.join(GUIDE, slug + ".json")
    if not os.path.exists(p):
        die("no %s (run tools/build_pip_data.py first)" % os.path.relpath(p, ROOT))
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def units(slug):
    """The study guide's sections in page order: one unit per (page, heading), cram sheets left out
    (they repeat the guide). The link anchor is the section's own id, not a question-link id."""
    g = load_guide(slug)
    out, by = [], {}
    for b in g["b"]:
        doc = g["docs"][b[0]]
        if doc.get("kind") == "cram" or not b[2]:
            continue
        key = (doc["file"], b[2])
        u = by.get(key)
        if u is None:
            u = by[key] = {"u": "u%d" % len(out), "doc": doc["file"], "page": doc.get("title", ""),
                           "heading": b[2], "anchors": [], "lines": []}
            out.append(u)
        if b[1] and b[1] not in u["anchors"]:
            u["anchors"].append(b[1])
        if b[3] not in u["lines"]:
            u["lines"].append(b[3])
    for u in out:
        own = [a for a in u["anchors"] if not a.startswith("ga-")]
        u["a"] = (own or u["anchors"] or ["top"])[0]
        u["text"] = "\n".join(u.pop("lines"))
        u["h"] = hashlib.sha1(u["text"].encode("utf-8")).hexdigest()[:10]
        u["chars"] = len(u["text"])
    return out


# ------------------------------------------------------------------ checks
BANNED = re.compile(r"\b(lectures?|lecturers?|slides?|professors?|instructors?|Dr\.|recordings?|transcripts?|syllabus|"
                    r"instructional objectives?|decks?|timestamps?|in class)\b", re.I)
BRITISH = re.compile(r"\b(\w*(haem(?!ophil|olyticus)|tumour|colour|behaviour|favour|labour|centre|fibre|litre|metre|anaem|leukaem|"
                     r"paediatr|oesophag|orthopaed|foetal|foetus|oestrogen|diarrhoea|haemorrhag|ischaem|analys(e|ed|ing)\b)\w*|"
                     r"oedem\w*|(recogn|organ|minim|maxim|real|util|stabil|immun|sensit|neutral|character)is(e|ed|es|ing|ation)\b)", re.I)
ABBR = re.compile(r"(?<![\w])([A-Z][A-Z0-9]{1,5})s?(?![\w])")
ROMAN = re.compile(r"^[IVX]+$")
OK_ABBR = {"DNA", "RNA", "HIV", "AIDS", "OK", "TV", "US",
           # electrocardiogram wave and interval names: they are the names, with nothing to spell out
           "QRS", "PR", "QT", "ST", "RR", "PP", "QTC", "V1", "V2", "V3", "V4", "V5", "V6"}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def words(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", s))


def abbr_problems(x):
    """An abbreviation must be spelled out where it first appears: "ECG (electrocardiogram)" or
    "electrocardiogram (ECG)" (the site's no-abbreviations rule)."""
    bad, seen = [], set()
    for m in ABBR.finditer(x):
        a = m.group(1)
        if a in seen or a in OK_ABBR or ROMAN.match(a):
            continue
        seen.add(a)
        after = x[m.end():m.end() + 2]
        before = x[max(0, m.start() - 1):m.start()]
        if not (after.startswith(" (") or before == "("):
            bad.append(a)
    return bad


def check_file(slug, strict_stale=False, data=None):
    p = os.path.join(SRC, slug + ".json")
    errs, warns = [], []
    if data is None:
        try:
            with open(p, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError) as e:
            return ["%s: cannot read (%s)" % (slug, e)], [], 0
    us = {u["u"]: u for u in units(slug)}
    g = load_guide(slug)
    anchors = {}
    for b in g["b"]:
        anchors.setdefault(g["docs"][b[0]]["file"], set()).add(b[1])
    if data.get("v") != 1 or data.get("s") != slug:
        errs.append("header must be {\"v\": 1, \"s\": \"%s\"}" % slug)
    cards = data.get("cards") or []
    ids = set()
    for i, c in enumerate(cards):
        w = "%s #%d %s" % (slug, i, c.get("id", "?"))
        for f in ("id", "u", "h", "doc", "a", "t", "k", "q", "x"):
            if f not in c:
                errs.append(w + ": missing " + f)
        if not all(f in c for f in ("id", "u", "doc", "a", "t", "k", "q", "x")):
            continue
        if not KEBAB.match(c["id"]):
            errs.append(w + ": id must be kebab-case")
        if c["id"] in ids:
            errs.append(w + ": duplicate id")
        ids.add(c["id"])
        if c["u"] not in us:
            errs.append(w + ": unknown unit " + c["u"])
        elif c.get("h") != us[c["u"]]["h"]:
            (errs if strict_stale else warns).append(w + ": stale (its guide section changed since it was written)")
        if c["doc"] not in anchors:
            errs.append(w + ": unknown page " + c["doc"])
        elif c["a"] not in anchors[c["doc"]]:
            errs.append(w + ": anchor %r not on %s" % (c["a"], c["doc"]))
        if not isinstance(c["t"], str) or not (2 <= len(c["t"]) <= 80):
            errs.append(w + ": t must be 2-80 characters")
        if not (isinstance(c["k"], list) and len(c["k"]) <= 8 and all(isinstance(s, str) and s for s in c["k"])):
            errs.append(w + ": k must be a list of up to 8 strings")
        if not (isinstance(c["q"], list) and 2 <= len(c["q"]) <= 4 and all(isinstance(s, str) and s for s in c["q"])):
            errs.append(w + ": q must be a list of 2-4 strings")
        x = c["x"] if isinstance(c["x"], str) else ""
        n = words(x)
        if n < 35 or n > 230:
            errs.append(w + ": explanation is %d words (35-230 allowed, aim for 60-180)" % n)
        elif n > 190:
            warns.append(w + ": explanation is %d words (aim for 60-180)" % n)
        if re.search(r"\*\*|^#|\n#|<[a-z/]", x):
            errs.append(w + ": no markdown or HTML in x")
        m = BANNED.search(x)
        if m:
            errs.append(w + ": mentions %r (explain the fact itself)" % m.group(0))
        m = BRITISH.search(x)
        if m:
            errs.append(w + ": British spelling %r (US spelling)" % m.group(0))
        bad = abbr_problems(x)
        if bad:
            errs.append(w + ": spell out on first use: " + ", ".join(bad))
    covered = {c.get("u") for c in cards}
    for u in us.values():
        if u["u"] not in covered and u["chars"] >= 800 and not re.search(r"objectives|how to use", u["heading"], re.I):
            warns.append("%s %s: no card yet for %r (%d characters)" % (slug, u["u"], u["heading"][:60], u["chars"]))
    return errs, warns, len(cards)


def assemble(slug, parts):
    """Merge card files written from `units` into pip/explain/<slug>.json. The writer gives
    {id, u, t, k, q, x}; the unit decides h (its text hash), doc and a (the section link)."""
    us = {u["u"]: u for u in units(slug)}
    path = os.path.join(SRC, slug + ".json")
    old = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            old = json.load(fh).get("cards", [])
    fresh = []
    for p in parts:
        with open(p, encoding="utf-8") as fh:
            fresh.extend(json.load(fh).get("cards", []))
    redo = {c["u"] for c in fresh}
    cards = [c for c in old if c["u"] not in redo]      # a rewritten unit replaces all its old cards
    ids = {c["id"] for c in cards}
    for c in fresh:
        u = us.get(c.get("u"))
        if not u:
            die("card %s names unknown unit %s" % (c.get("id"), c.get("u")))
        cid, n = c["id"], 2
        while cid in ids:
            cid, n = "%s-%d" % (c["id"], n), n + 1
        ids.add(cid)
        cards.append({"id": cid, "u": u["u"], "h": u["h"], "doc": u["doc"], "a": u["a"],
                      "t": c["t"], "k": c["k"], "q": c["q"], "x": c["x"].strip()})
    order = {u: i for i, u in enumerate(us)}
    cards.sort(key=lambda c: order.get(c["u"], 1e9))
    os.makedirs(SRC, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"v": 1, "s": slug, "cards": cards}, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("%s: %d cards (%d new or rewritten) -> %s" % (slug, len(cards), len(fresh), os.path.relpath(path, ROOT)))


def lint(slug, draft):
    """Check a writer's draft ({"cards": [{id, u, t, k, q, x}]}) with the same rules as `check`."""
    with open(draft, encoding="utf-8") as fh:
        cards = json.load(fh).get("cards", [])
    us = {u["u"]: u for u in units(slug)}
    for c in cards:
        u = us.get(c.get("u"))
        if u:
            c.setdefault("h", u["h"]); c.setdefault("doc", u["doc"]); c.setdefault("a", u["a"])
    errs, warns, n = check_file(slug, data={"v": 1, "s": slug, "cards": cards})
    warns = [w for w in warns if "no card yet" not in w]
    print("%s: %d cards, %d errors" % (draft, n, len(errs)))
    for e in errs:
        print("  ERROR " + e)
    for w in warns:
        print("  warn  " + w)
    return 1 if errs else 0


def rehash(slug, which):
    path = os.path.join(SRC, slug + ".json")
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    us = {u["u"]: u for u in units(slug)}
    n = 0
    for c in data["cards"]:
        if c["u"] in which and c["u"] in us and c.get("h") != us[c["u"]]["h"]:
            c["h"] = us[c["u"]]["h"]; n += 1
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("%s: %d cards marked current (units %s)" % (slug, n, ", ".join(which)))
    return 0


def main(argv):
    if len(argv) >= 4 and argv[1] == "rehash":
        return rehash(argv[2], set(argv[3:]))
    if len(argv) == 4 and argv[1] == "lint":
        return lint(argv[2], argv[3])
    if len(argv) >= 4 and argv[1] == "assemble":
        assemble(argv[2], argv[3:])
        return 0
    if len(argv) < 2 or argv[1] not in ("units", "check"):
        die(__doc__.strip().split("\n\n")[2] if __doc__ else "usage")
    if argv[1] == "units":
        if len(argv) < 3:
            die("units <slug> [--out DIR]")
        slug, out = argv[2], None
        if "--out" in argv:
            out = argv[argv.index("--out") + 1]
        us = units(slug)
        body = json.dumps({"s": slug, "units": us}, ensure_ascii=False, indent=1)
        if out:
            os.makedirs(out, exist_ok=True)
            path = os.path.join(out, slug + ".units.json")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(body)
            print("%s: %d units, %d characters -> %s" % (slug, len(us), sum(u["chars"] for u in us), path))
        else:
            print(body)
        return 0
    slugs = argv[2:] or sorted(f[:-5] for f in os.listdir(SRC) if f.endswith(".json")) if os.path.isdir(SRC) else argv[2:]
    total_e = total = 0
    for s in slugs:
        errs, warns, n = check_file(s)
        total += n
        total_e += len(errs)
        print("%s: %d cards, %d errors, %d warnings" % (s, n, len(errs), len(warns)))
        for e in errs:
            print("  ERROR " + e)
        for w in warns:
            print("  warn  " + w)
    print("total: %d cards, %d errors" % (total, total_e))
    return 1 if total_e else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
