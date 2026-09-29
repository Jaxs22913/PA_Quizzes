#!/usr/bin/env python3
"""Build <exam folder>/guide-links.json: for each Semester 2+ quiz question, the
study-guide passage that teaches it. theme.js reads the file and puts a
"See it in the study guide" button under the explanation, which opens that
passage in a panel INSIDE the quiz (so the student never loses their place).

Why matching, not a hand-kept table: 10,000+ questions and ~20 guides that are
rebuilt often. The guides do not share one structure (some cite slides, some do
not), so the link is found by content:

  1. EXACT   the guide prints "<deck>.pptx, Slide N" for the question's own
             deck and slide -> that section. Deterministic.
  2. TEXT    BM25 over the guide's id'd sections, weighting the question stem
             and the correct answer, with a small bonus when the section cites
             the question's slide number.

A match is only KEPT when the guide really contains the answer, because a link
to the wrong paragraph is worse than no link (these are study aids for graded
exams):

  passage  >= 85% of the correct answer's distinctive terms sit in ONE
           paragraph of the section (or the EXACT rule fired)  -> the panel
           scrolls to and highlights that paragraph
  section  >= 60% in the best paragraph AND >= 85% in the section -> the panel
           opens at the section, no highlight
  (none)   anything weaker -> no button. Coverage is ~50% of questions, on
           purpose; the rest simply have no link.

Keys: the question is identified by an FNV-1a hash of "<stem>\\n<correct
option text>" (same function as QSIG in the quiz engine, over UTF-16 code
units), so an edited question silently loses its link instead of pointing at
stale content. Re-run this after ANY quiz or guide rebuild, then run
tools/check_guide_links.py.

Scope: pages carrying data-dark-kind="quiz" (Semester 2+ generated quizzes);
Semester 1 is frozen and is never read or written.

Usage:  python3 tools/build_guide_links.py [--dry-run] [folder ...]
"""
import collections
import glob
import html
import json
import math
import os
import re
import sys

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASSAGE_MIN = 0.85       # answer-term coverage of the best paragraph
SECTION_PARA_MIN = 0.60  # ... for the section tier
SECTION_MIN = 0.85       # ... plus coverage of the whole section
EXPLAINED_MIN = 0.80     # a closest section 'explains it, in other words' at this key coverage
W_ANSWER, W_STEM, W_EXPL = 1.5, 2.0, 1.0
SLIDE_BONUS = 1.15

STOP = set("""the a an of and or to in on for with by is are was were be as at from that this these those it
its which what who whom not no than then into over under about after before during between both each most more
less other only also may can will should would could has have had their there they them his her he she when where
while because since if but so such any all one two three four first second per via vs""".split())
NUMW = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12"}
NUMW_RE = re.compile(r"\b(" + "|".join(NUMW) + r")\b")


def toks(text):
    t = html.unescape(re.sub(r"<[^>]+>", " ", text)).lower()
    t = NUMW_RE.sub(lambda m: NUMW[m.group(1)], t)
    t = t.replace("naevus", "nevus").replace("naevi", "nevi").replace("haem", "hem").replace("oedema", "edema")
    out = []
    for w in re.findall(r"[a-z][a-z0-9\-]{2,}|\d+(?:\.\d+)?", t):
        if w in STOP:
            continue
        w = re.sub(r"(ies)$", "y", w)
        w = re.sub(r"(es|s)$", "", w) if len(w) > 4 else w
        out.append(w)
    return out


def acronyms(text):
    ws = [w for w in re.findall(r"[A-Za-z][A-Za-z\-]+", html.unescape(text)) if w.lower() not in STOP]
    out = set()
    for n in range(2, 6):
        for i in range(len(ws) - n + 1):
            out.add("".join(w[0] for w in ws[i:i + n]).lower())
    return out


def fnv(s):
    """Same hash the quiz engine's QSIG uses (JS: charCodeAt = UTF-16 units)."""
    h = 0x811C9DC5
    b = s.encode("utf-16-le")
    for i in range(0, len(b), 2):
        h ^= b[i] | (b[i + 1] << 8)
        h = (h * 0x01000193) & 0xFFFFFFFF
    n, out = h, ""
    if n == 0:
        return "0"
    while n:
        out = "0123456789abcdefghijklmnopqrstuvwxyz"[n % 36] + out
        n //= 36
    return out


def qkey(q):
    return fnv(q["q"] + "\n" + q["opts"][q["c"]][0])


def slides_in(text):
    nums = set()
    for m in re.finditer(r"[Ss]lides?\s*((?:\d+(?:\s*(?:&ndash;|–|-|and|,|&amp;)\s*\d+)*)(?:\s*,\s*\d+(?:\s*(?:&ndash;|–|-)\s*\d+)?)*)", text):
        g = html.unescape(m.group(1))
        for a in re.finditer(r"(\d+)\s*(?:–|-)\s*(\d+)", g):
            lo, hi = int(a.group(1)), int(a.group(2))
            if 0 < hi - lo < 80:
                nums.update(range(lo, hi + 1))
        nums.update(int(x) for x in re.findall(r"\d+", g))
    return nums


def ensure_heading_ids(path):
    """Give every id-less <h2>-<h4> in a guide a stable id (gh-<slug>[-n]).
    Some guides (Medical Literature) ship headings with no ids, so nothing in
    them can be linked to. Only ADDS id attributes, idempotent, and a rebuilt
    guide simply gets them again on the next run of this tool."""
    s = open(path, encoding="utf-8").read()
    # Only for guides that ship (almost) no heading ids at all. Guides with ids on
    # their real sections are left byte-for-byte alone; a few id-less sub-headings
    # there are not worth editing a generated page for.
    if len(re.findall(r'\bid="', s)) >= 12:      # ids already sit on its real sections/cards
        return 0
    used = set(re.findall(r'\bid="([^"]+)"', s))
    n = [0]

    def sub(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        if re.search(r'\bid=', attrs):
            return m.group(0)
        text = html.unescape(re.sub(r"<[^>]+>", "", inner))
        slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48] or "section"
        cand, k = "gh-" + slug, 2
        while cand in used:
            cand, k = "gh-%s-%d" % (slug, k), k + 1
        used.add(cand)
        n[0] += 1
        return "<%s%s id=\"%s\">%s</%s>" % (tag, attrs, cand, inner, tag)

    new = re.sub(r"<(h[2-4])([^>]*)>(.*?)</\1>", sub, s, flags=re.S)
    if n[0]:
        open(path, "w", encoding="utf-8").write(new)
    return n[0]


def parse_guide(path):
    s = open(path, encoding="utf-8").read()
    body = s[s.find("<body"):]
    body = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>", "", body, flags=re.S)
    marks = [(m.start(), m.end(), m.group(2), re.sub(r"<[^>]+>", "", m.group(3)))
             for m in re.finditer(r"<(h[1-4])([^>]*)>(.*?)</\1>", body, re.S)]
    merged = []
    for i, (st, en, attrs, title) in enumerate(marks):
        nxt = marks[i + 1][0] if i + 1 < len(marks) else len(body)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm is None:
            if merged:
                merged[-1]["html"] += " " + title + " " + body[en:nxt]
            continue
        merged.append({"id": idm.group(1), "title": html.unescape(title).strip(), "html": body[en:nxt]})
    return merged


BLOCK = re.compile(r"</(?:li|p|tr|dd|dt|blockquote|figcaption|summary)>|<br\s*/?>|</h[1-6]>", re.I)


def blocks_of(sc):
    out = []
    for p in BLOCK.split(sc["html"]):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", p))).strip()
        if len(t) >= 25:
            out.append(t)
    return out


class Index:
    def __init__(self, guides):
        self.secs = []
        for g in guides:
            for sc in parse_guide(g):
                sc["guide"] = os.path.basename(g)
                sc["tok"] = collections.Counter(toks(sc["html"] + " " + sc["title"]))
                sc["len"] = sum(sc["tok"].values())
                plain = html.unescape(re.sub(r"<[^>]+>", " ", sc["html"]))
                sc["plain"] = plain
                sc["slides"] = slides_in(plain)
                self.secs.append(sc)
        df = collections.Counter()
        for sc in self.secs:
            for t in sc["tok"]:
                df[t] += 1
        n = len(self.secs)
        self.idf = {t: math.log((n + 1) / (c + 0.5)) for t, c in df.items()}
        self.avg = sum(sc["len"] for sc in self.secs) / max(1, n)

    def score(self, w, sc):
        tot = 0.0
        for t, wt in w.items():
            if t in sc["tok"]:
                tf = sc["tok"][t]
                tot += wt * self.idf[t] * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * sc["len"] / self.avg))
        return tot

    def cov(self, q, tokens):
        txt = q["opts"][q["c"]][0]
        base = set(toks(txt))
        tot = sum(self.idf.get(t, 0) for t in base)
        if tot == 0:
            return None
        if any(a in tokens for a in acronyms(txt) if a in self.idf and a not in base and len(a) >= 2):
            return 1.0
        return sum(self.idf.get(t, 0) for t in base if t in tokens) / tot


def deck_of(cite):
    m = re.match(r"(.*?\.pptx?)", cite, re.I)
    return m.group(1) if m else cite.split(", Slide")[0]


def slide_of(cite):
    m = re.search(r"Slides?\s*(\d+)", cite)
    return int(m.group(1)) if m else None


def weights(q):
    ans = q["opts"][q["c"]]
    w = collections.Counter()
    for t in toks(ans[0]):
        w[t] += W_ANSWER
    for t in toks(q["q"]):
        w[t] += W_STEM
    for t in toks(ans[1]):
        w[t] += W_EXPL
    return w


def best_block(idx, q, sc):
    ans = q["opts"][q["c"]]
    qt = collections.Counter()
    for t in toks(ans[0]):
        qt[t] += 3.0          # the KEY picks the paragraph (a stem-word pick chose the wrong one)
    for t in toks(q["q"]):
        qt[t] += 1.0
    best, text = 0.0, None
    for b in blocks_of(sc):
        bt = set(toks(b))
        s = sum(w * idx.idf.get(t, 0) for t, w in qt.items() if t in bt) / (len(bt) ** 0.25 or 1)
        if s > best:
            best, text = s, b
    return text


def match(idx, q):
    w = weights(q)
    deck, n = deck_of(q["cite"]), slide_of(q["cite"])
    exact = []
    if n is not None:
        key = re.compile(re.escape(deck[-25:]) + r"[^<]{0,3},?\s*Slides?\s*" + str(n) + r"\b")
        exact = [sc for sc in idx.secs if key.search(sc["plain"])]
    if 1 <= len(exact) <= 2:
        return max(exact, key=lambda c: idx.score(w, c)), True
    best, top = 0.0, None
    for sc in idx.secs:
        s = idx.score(w, sc) * (SLIDE_BONUS if n is not None and n in sc["slides"] else 1)
        if s > best:
            best, top = s, sc
    return top, False


def snippet(text):
    text = text[:90]
    if len(text) == 90 and " " in text:
        text = text[:text.rfind(" ")]
    return text.strip()


def clean_title(t):
    t = re.sub(r"^\s*\d+(?:\.\d+)*\s*[·.\-–—]\s*", "", t)
    return (t[:72].rsplit(" ", 1)[0] + "…") if len(t) > 74 else t


def load_questions(path):
    s = open(path, encoding="utf-8").read()
    if 'data-dark-kind="quiz"' not in s:
        return None
    m = re.search(r"const QUESTIONS = (\[.*?\]);\n", s, re.S)
    return json.loads(m.group(1)) if m else None


def near_window(idx, anchors, deck, slide):
    """(lo, hi) section indexes between the confident links of the slides on
    either side of `slide`, in the deck's main guide; None if unknowable."""
    if slide is None:
        return None
    mine = [(s_, p) for d, s_, p in anchors if d == deck]
    if not mine:
        return None
    guide = collections.Counter(idx.secs[p]["guide"] for _, p in mine).most_common(1)[0][0]
    mine = [(s_, p) for s_, p in mine if idx.secs[p]["guide"] == guide]
    before = [x for x in mine if x[0] <= slide]
    after = [x for x in mine if x[0] >= slide]
    cands = []
    if before:
        cands.append(max(before)[1])
    if after:
        cands.append(min(after)[1])
    lo, hi = min(cands), max(cands)
    if hi - lo > 10:                      # neighbors far apart: use the nearer one only
        near = (max(before) if before else min(after))[1]
        lo = hi = near
    return lo, hi


def near_section(idx, anchors, q, deck, slide):
    """Tier 3 -- the section a slide lives in, from its NEIGHBORS.

    Slides are taught in order and the guides follow slide order, so a question
    citing slide 43 belongs between the sections that slides 41 and 45 already
    link to. `anchors` = [(deck, slide, section index)] from confident links.
    Restricted to the guide most of that deck's anchors point at; among the
    sections between the two neighbors the question's own words choose.
    Validated by hiding each confident link and predicting it back: ~84% the
    exact section (~90% when another question cites the same slide)."""
    if slide is None:
        return None
    mine = [(s_, p) for d, s_, p in anchors if d == deck]
    if not mine:
        return None
    guide = collections.Counter(idx.secs[p]["guide"] for _, p in mine).most_common(1)[0][0]
    mine = [(s_, p) for s_, p in mine if idx.secs[p]["guide"] == guide]
    same = [p for s_, p in mine if s_ == slide]
    if same:
        return collections.Counter(same).most_common(1)[0][0]
    before = [x for x in mine if x[0] < slide]
    after = [x for x in mine if x[0] > slide]
    cands = []
    if before:
        cands.append(max(before)[1])
    if after:
        cands.append(min(after)[1])
    lo, hi = min(cands), max(cands)
    if hi - lo > 8:                       # neighbors far apart in the guide: trust the nearer slide only
        lo = hi = (max(before)[1] if before else min(after)[1])
    w = weights(q)
    return max(range(lo, hi + 1), key=lambda i: idx.score(w, idx.secs[i]))


def load_additions(folder):
    """{question key: (line id, section title, plain text)} for lines written into the
    guide by tools/apply_guide_additions.py -- those questions link straight to
    their own line (the fact was written FOR them, so no guessing)."""
    out = {}
    p = os.path.join(_REPO, "tools", "guide_additions",
                     re.sub(r"[^a-z0-9]+", "-", os.path.basename(folder).lower()).strip("-") + ".json")
    if not os.path.exists(p):
        return out
    d = json.load(open(p, encoding="utf-8"))
    for it in d["items"]:
        if not it.get("html") or it["html"] == "SKIP":
            continue
        plain = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", it["html"]))).strip()
        for k in it["keys"]:
            out[k] = ("ga-" + it["id"], d["guide"], it.get("section_title", ""), plain)
    return out


def external_guides(folder):
    """Guide paths a quiz folder borrows from another folder (tools/guide_external.json)."""
    p = os.path.join(_REPO, "tools", "guide_external.json")
    if not os.path.exists(p):
        return []
    rel = json.load(open(p, encoding="utf-8")).get(os.path.basename(folder))
    return [os.path.join(_REPO, rel)] if rel else []


def build_folder(folder, dry=False):
    gpaths = sorted(g for g in glob.glob(os.path.join(folder, "*.html"))
                    if 'data-dark-kind="guide"' in open(g, encoding="utf-8").read()
                    and not re.search(r"osce|l3-review", g)) or external_guides(folder)
    # a guide's identity is its file name everywhere; guide-links.json stores the path from this folder
    relpath = {os.path.basename(g): os.path.relpath(g, folder) for g in gpaths}
    quizzes = []
    for f in sorted(glob.glob(os.path.join(folder, "*.html"))):
        Q = load_questions(f)
        if Q:
            quizzes.append(Q)
    if not quizzes:
        return None
    if not dry:
        for g in gpaths:
            ensure_heading_ids(g)
    idx = Index(gpaths) if gpaths else None
    if idx is None or not idx.secs:
        # A Semester 2 quiz folder with no anchored guide still gets a (empty)
        # file, so theme.js's fetch is a 200 and the console stays clean.
        if not dry:
            with open(os.path.join(folder, "guide-links.json"), "w", encoding="utf-8") as fh:
                json.dump({"v": 1, "g": [], "l": {}}, fh, separators=(",", ":"))
        return collections.Counter(), sum(len(Q) for Q in quizzes), []
    pos = {(sc["guide"], sc["id"]): i for i, sc in enumerate(idx.secs)}
    items, seen = [], set()
    for Q in quizzes:
        for q in Q:
            k = qkey(q)
            if k in seen:
                continue
            seen.add(k)
            items.append({"q": q, "k": k, "deck": deck_of(q["cite"]), "slide": slide_of(q["cite"]), "link": None})
    # pass 0: a question whose fact was written into the guide FOR it links to that line
    adds = load_additions(folder)
    for it in items:
        a = adds.get(it["k"])
        if a and any(sc["guide"] == a[1] for sc in idx.secs):
            it["link"] = ("passage", {"guide": a[1], "id": a[0], "title": a[2], "tok": collections.Counter()}, snippet(a[3]))
    # pass 0b: a link an independent judge PASSED (tools/audit_guide_links.py) is used exactly
    # as audited, provided the paragraph it quoted still exists in the guide
    audit = {}
    ap = os.path.join(_REPO, "tools", "guide_link_audit.json")
    if os.path.exists(ap):
        audit = json.load(open(ap, encoding="utf-8"))
    by_id = {(sc["guide"], sc["id"]): sc for sc in idx.secs}
    for it in items:
        r = audit.get(os.path.basename(folder) + "|" + it["k"])
        if it["link"] or not r or r.get("v") != "PASS":
            continue
        sc = by_id.get((os.path.basename(r["g"]), r["a"]))
        if sc and any(fnv(re.sub(r"\s+", " ", b).strip()) == r["p"] for b in blocks_of(sc)):
            it["link"] = ("passage", sc, r["s"])
    # pass 1: direct matches (the key is really in the guide)
    for it in items:
        if it["link"]:
            continue
        q = it["q"]
        sc, exact = match(idx, q)
        if sc is None:
            continue
        blk = best_block(idx, q, sc)
        b = idx.cov(q, set(toks(blk or "")))
        s = idx.cov(q, sc["tok"])
        if exact or (b is not None and b >= PASSAGE_MIN):
            it["link"] = ("passage", sc, snippet(blk) if blk else "")
        elif b is not None and s is not None and b >= SECTION_PARA_MIN and s >= SECTION_MIN:
            it["link"] = ("section", sc, "")
    # pass 2: the sections that CONTAIN the key, nearest to where the slide sits.
    # Direct matching missed these because the question's own words outweighed
    # the key when choosing a section (a nail in the eye, key "leave it in
    # place", is taught in "The disposition ladder" but its stem words pulled a
    # neighbour). Candidates = sections holding >=85% of the key's terms; among
    # them BM25 chooses, with a boost inside the window the slide's neighbors
    # define. A candidate far outside that window is not trusted.
    anchors = [(it["deck"], it["slide"], pos[(it["link"][1]["guide"], it["link"][1]["id"])])
               for it in items if it["link"] and it["link"][0] == "passage" and it["slide"] is not None
               and (it["link"][1]["guide"], it["link"][1]["id"]) in pos]
    for it in items:
        if it["link"]:
            continue
        q = it["q"]
        win = near_window(idx, anchors, it["deck"], it["slide"])
        w = weights(q)
        best, bs = None, 0.0
        for i, sc in enumerate(idx.secs):
            c = idx.cov(q, sc["tok"])
            if c is None or c < SECTION_MIN:
                continue
            in_win = win is not None and win[0] - 2 <= i <= win[1] + 2
            if win is not None and not in_win:
                continue
            sco = idx.score(w, sc) * (1.6 if win is not None and win[0] <= i <= win[1] else 1.0)
            if sco > bs:
                best, bs = i, sco
        if best is not None:
            sc = idx.secs[best]
            blk = best_block(idx, q, sc)
            b = idx.cov(q, set(toks(blk or "")))
            if b is not None and b >= PASSAGE_MIN:
                it["link"] = ("passage", sc, snippet(blk))
            else:
                it["link"] = ("section", sc, "")
    # pass 3: still nothing -> the closest section by slide position
    gaps = []
    for it in items:
        if it["link"]:
            continue
        p = near_section(idx, anchors, it["q"], it["deck"], it["slide"])
        if p is None:
            # no slide neighbors at all: the best text match anywhere still
            # names the right neighborhood far more often than not
            sc, _ = match(idx, it["q"])
            if sc is not None:
                p = pos[(sc["guide"], sc["id"])]
        if p is not None:
            sc = idx.secs[p]
            if (idx.cov(it["q"], sc["tok"]) or 0) >= EXPLAINED_MIN:
                it["link"] = ("section", sc, "")     # the section holds >=80% of the key: it explains it, in other words
            else:
                it["link"] = ("near", sc, "")
                gaps.append((it["q"], sc))           # the guide does not teach this fact: write it in
    guides, links, tiers = [], {}, collections.Counter()
    for it in items:
        if not it["link"]:
            tiers["none"] += 1
            continue
        tier, sc, snip = it["link"]
        tiers[tier] += 1
        gp = relpath.get(sc["guide"], sc["guide"])
        if gp not in guides:
            guides.append(gp)
        row = [guides.index(gp), sc["id"], clean_title(sc["title"]), snip]
        if tier == "near":
            row.append(1)
        links[it["k"]] = row
    out = {"v": 1, "g": guides, "l": links}
    if not dry:
        with open(os.path.join(folder, "guide-links.json"), "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    return tiers, len(items), gaps


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    folders = [a for a in args] or sorted(
        d for d in os.listdir(_REPO)
        if os.path.isdir(os.path.join(_REPO, d)) and not d.startswith((".", "tools", "work", "group-", "audio", "icons")))
    total = collections.Counter()
    allgaps = []
    for d in folders:
        p = d if os.path.isabs(d) else os.path.join(_REPO, d)
        r = build_folder(p, dry)
        if r is None:
            continue
        tiers, n, gaps = r
        total.update(tiers)
        allgaps.extend((os.path.basename(p), q, sc) for q, sc in gaps)
        linked = n - tiers["none"]
        print("%-46s %5d q  %3d%% linked (%d passage, %d section, %d closest, %d none)" % (
            os.path.basename(p), n, round(100 * linked / max(1, n)), tiers["passage"], tiers["section"],
            tiers["near"], tiers["none"]))
    print("TOTAL", dict(total), "| probably-not-in-the-guide:", len(allgaps))
    if "--gaps" in sys.argv:
        for folder, q, sc in allgaps:
            print("GAP\t%s\t%s\t%s\t-> %s" % (folder, q["opts"][q["c"]][0][:60], q["cite"][-50:], sc["title"][:40]))


if __name__ == "__main__":
    main()
