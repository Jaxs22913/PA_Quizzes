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
        qt[t] += 2.0
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


def build_folder(folder, dry=False):
    gpaths = sorted(g for g in glob.glob(os.path.join(folder, "*.html"))
                    if 'data-dark-kind="guide"' in open(g, encoding="utf-8").read()
                    and not re.search(r"osce|l3-review", g))
    quizzes = []
    for f in sorted(glob.glob(os.path.join(folder, "*.html"))):
        Q = load_questions(f)
        if Q:
            quizzes.append(Q)
    if not quizzes:
        return None
    idx = Index(gpaths) if gpaths else None
    if idx is None or not idx.secs:
        # A Semester 2 quiz folder with no anchored guide still gets a (empty)
        # file, so theme.js's fetch is a 200 and the console stays clean.
        if not dry:
            with open(os.path.join(folder, "guide-links.json"), "w", encoding="utf-8") as fh:
                json.dump({"v": 1, "g": [], "l": {}}, fh, separators=(",", ":"))
        return collections.Counter(), sum(len(Q) for Q in quizzes)
    guides, links, seen = [], {}, set()
    tiers = collections.Counter()
    for Q in quizzes:
        for q in Q:
            k = qkey(q)
            if k in seen:
                continue
            seen.add(k)
            sc, exact = match(idx, q)
            if sc is None:
                tiers["none"] += 1
                continue
            blk = best_block(idx, q, sc)
            b = idx.cov(q, set(toks(blk or "")))
            s = idx.cov(q, sc["tok"])
            snip = None
            if exact or (b is not None and b >= PASSAGE_MIN):
                tier, snip = "passage", (snippet(blk) if blk else "")
            elif b is not None and s is not None and b >= SECTION_PARA_MIN and s >= SECTION_MIN:
                tier, snip = "section", ""
            else:
                tiers["none"] += 1
                continue
            tiers[tier] += 1
            if sc["guide"] not in guides:
                guides.append(sc["guide"])
            links[k] = [guides.index(sc["guide"]), sc["id"], clean_title(sc["title"]), snip]
    out = {"v": 1, "g": guides, "l": links}
    if not dry:
        with open(os.path.join(folder, "guide-links.json"), "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    return tiers, len(seen)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    folders = [a for a in args] or sorted(
        d for d in os.listdir(_REPO)
        if os.path.isdir(os.path.join(_REPO, d)) and not d.startswith((".", "tools", "work", "group-", "audio", "icons")))
    total = collections.Counter()
    for d in folders:
        p = d if os.path.isabs(d) else os.path.join(_REPO, d)
        r = build_folder(p, dry)
        if r is None:
            continue
        tiers, n = r
        total.update(tiers)
        linked = tiers["passage"] + tiers["section"]
        print("%-52s %5d questions  %3d%% linked (%d passage, %d section)" % (
            os.path.basename(p), n, round(100 * linked / n), tiers["passage"], tiers["section"]))
    print("TOTAL", dict(total))


if __name__ == "__main__":
    main()
