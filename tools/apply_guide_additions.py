#!/usr/bin/env python3
"""Write the facts a class study guide was missing INTO its sections.

Source of truth: tools/guide_additions/<folder-slug>.json, one file per exam
folder: {"folder", "guide", "items": [{"id", "section_id", "html", "keys",
"src": {question, key, explanation, also}}]}. `html` is one guide line (bold
topic phrase + the fact), composed from the quiz question's own vetted,
slide-cited explanation -- nothing beyond it (tools/verify_guide_additions.py
checks that). `keys` are the quiz questions the line answers.

Each line goes INTO its section's own text, next to the existing line it is
most about, styled like that text (Jaxon, 2026-10-15: no separate "Also
tested" box any more):

  region      from the heading id=section_id to the next heading that starts
              another linked section or another Pip unit (any h1-h3, or an h4
              with an id), never past the heading's own container
  candidates  every line of the section's own blocks (the container's direct
              children): an item of a plain <ul>, a plain <p>, a table row, a
              dt+dd pair, a figure caption, a line of a callout box
  score       BM25 over the words the line and the candidate share, rare words
              weighted by their idf over the guide's own text, the line's bold
              topic phrase counted twice
  insert      best is a <ul> item     -> <li id="ga-<id>" data-gen="1"> right after it
              best is a plain <p>     -> <p id="ga-<id>" data-gen="1"> right after it
              best is in a condition card (div.cond) -> a <p> inside the card,
                                         after its last line, before its slide cite
              best is in any other block (table, figure, callout/flag box, <ol>,
                <dl>) -> a <p> right after the whole block, never inside it
              nothing shares a rare word -> a <p> where the old box sat (the end
              of the section's opening text); counted as "fallback" in the output
              Never inside a table cell, <dl>, heading, <ol>, <nav>, a callout or
              flag box, or another generated line; a caption or lead-in paragraph
              (p.figgrid-h, one ending in ':', one sitting on top of its table or
              list) is never separated from the block it introduces, and a remark
              paragraph (p.muted, p.tag, ...) stays with the block it remarks on.
              Several lines after one spot follow the page order of what they
              matched (a drug table's facts in the table's row order).

Idempotent: every generated element (data-gen="1"), and any old
<div class="qa-also" data-gen="1"> box, is removed first, so re-running after a
guide REBUILD (which drops the lines, because the guides are generated)
restores them, and a second run is a no-op. The ids never change, so question
links (guide-links.json) and their audit records keep pointing at the same
line. tools/check_guide_additions_inline.py proves a run moved lines without
losing, duplicating or editing anything. Order after any guide or quiz rebuild:

    python3 tools/apply_guide_additions.py
    python3 tools/check_guide_additions_inline.py   # nothing lost, duplicated or edited
    python3 tools/build_guide_links.py
    python3 tools/check_guide_links.py --strict
    python3 tools/build_guide_docx.py <guide>.html  # the Word copies
    python3 tools/build_pip_data.py && python3 tools/pip_explain.py check
                                             # moved lines reorder a Pip unit's text: its cards
                                             # show stale until `pip_explain.py rehash` (only
                                             # after confirming the unit's set of lines is unchanged)

Usage: apply_guide_additions.py [--check] [--explain]
  --check    report guides whose lines are missing/stale (exit 1), write nothing
  --explain  print where each line went and the words that put it there
"""
import glob, html as H, json, math, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "tools", "guide_additions")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
TAG = re.compile(r"<!--.*?-->|<(script|style)\b.*?</\1>|<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(/?)>", re.S)
OLD_BOX = re.compile(r'<div class="qa-also" data-gen="1">.*?</div>\n?', re.S)
# a generated line: written below as "\n" + indent + element, right after an existing element
GEN_LINE = re.compile(r'\n[ \t]*<(li|p) id="ga-[^"]*" data-gen="1">.*?</\1>', re.S)

STOP = set("""the a an of and or to in on for with by is are was were be as at from that this these those it its
which what who whom not no than then into over under about after before during between both each most more less
other only also may can will should would could has have had their there they them his her he she when where
while how why all any some such one two three via per but if so do does did been being out up down off very
same own just like within without because until against among through whose upon onto use used using""".split())
K1, B = 1.2, 0.75
MIN_IDF = 1.5          # the best candidate must share at least one word this rare, else fallback


class Node:
    __slots__ = ("tag", "attrs", "start", "oend", "cstart", "end", "parent", "kids")

    def __init__(self, tag, attrs, start, oend, parent):
        self.tag, self.attrs, self.start, self.oend, self.parent, self.kids = tag, attrs, start, oend, parent, []
        self.cstart = self.end = None

    def attr(self, name):
        m = re.search(r'\b%s="([^"]*)"' % name, self.attrs)
        return m.group(1) if m else None


def parse(doc):
    """A tree of the page's elements with source offsets. The guides are generated and well
    formed; a mismatched close tag is an error rather than something to guess around."""
    root = Node("#root", "", 0, 0, None)
    root.cstart = root.end = len(doc)
    cur = root
    for t in TAG.finditer(doc):
        if t.group(1) or t.group(0).startswith("<!--"):
            continue
        close, name, attrs, selfc = t.group(2), t.group(3).lower(), t.group(4), t.group(5)
        if close:
            if cur.tag != name:
                raise ValueError("</%s> at offset %d closes <%s>" % (name, t.start(), cur.tag))
            cur.cstart, cur.end = t.start(), t.end()
            cur = cur.parent
        else:
            n = Node(name, attrs, t.start(), t.end(), cur)
            cur.kids.append(n)
            if name in VOID or selfc:
                n.cstart = n.end = t.end()
            else:
                cur = n
    if cur is not root:
        raise ValueError("<%s> at offset %d is never closed" % (cur.tag, cur.start))
    return root


def walk(n):
    for k in n.kids:
        yield k
        yield from walk(k)


def text_of(doc, n):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", doc[n.oend:n.cstart]))).strip()


def stem(w):
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 4 and (w.endswith(("ches", "shes", "sses", "xes", "zes"))):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def toks(text):
    out = []
    for w in re.findall(r"[a-z0-9]+", text.lower()):
        if w in STOP or (len(w) < 3 and not w.isdigit()) or len(w) < 2:
            continue
        out.append(stem(w))
    return out


def heading_section(root, sid):
    """(heading, container, region end) for the section headed by id=sid."""
    h = next((n for n in walk(root) if re.fullmatch(r"h[1-6]", n.tag) and n.attr("id") == sid), None)
    if h is None:
        return None
    cont, end = h.parent, h.parent.cstart
    for n in walk(cont):
        if n.start <= h.start:
            continue
        if n.start >= end:
            break
        if n.tag in ("h1", "h2", "h3") or (n.tag == "h4" and n.attr("id")):
            end = n.start
            break
    return h, cont, end


LABEL_P = {"figgrid-h", "txnote", "prof-lead"}           # a caption for the block AFTER it
NOTE_P = {"tag", "muted", "pearl", "callout", "note"}     # a remark on the block BEFORE it
LEAF = ("tr", "li", "dd", "p", "figcaption")
SKIP = {"script", "style", "nav", "button", "details", "form", "input", "template", "audio", "video",
        "header", "footer", "aside"}


def cls(n):
    return (n.attr("class") or "").split()


INTRODUCED = {"table", "ul", "ol", "dl", "figure"}


def is_label(doc, n, nxt=None):
    """A paragraph that introduces the next block: a caption class, a plain paragraph ending in
    ':', or a plain paragraph sitting directly on top of a table/list/figure it leads into."""
    if n.tag != "p":
        return False
    if set(cls(n)) & LABEL_P:
        return True
    if cls(n):
        return False
    if text_of(doc, n).endswith(":"):
        return True
    return nxt is not None and (nxt.tag in INTRODUCED or (nxt.tag == "div" and set(cls(nxt)) & {"figgrid", "fig-grid", "tbl-wrap"}))


def is_note(n):
    return n.tag == "p" and bool(set(cls(n)) & NOTE_P)


def leaves(doc, b):
    """The text lines inside a block (table rows, list items, dt+dd pairs, paragraphs,
    captions), outermost only; the block's own text when it has none."""
    out = []

    def rec(n):
        for k in n.kids:
            if k.tag in LEAF:
                t = text_of(doc, k)
                if k.tag == "dd":
                    prev = [x for x in n.kids if x.tag == "dt" and x.start < k.start]
                    t = (text_of(doc, prev[-1]) + " " + t) if prev else t
                if t:
                    out.append(t)
            elif k.tag not in SKIP:
                rec(k)
    rec(b)
    return out or [text_of(doc, b)]


def candidates(doc, h, cont, end):
    """Every line a fact could sit next to, as [(element to insert after, kind, text)]:

      a <li> of a plain <ul>      -> an <li> right after that item
      a plain <p>                 -> a <p> right after it
      a line of a condition card  -> a <p> inside the card, after its last line (before its slide cite)
      a line of anything else     -> a <p> right after the whole block: a table, figure, callout,
         (table row, figure caption, box, <ol>, <dl>; never inside it, and after any remark paragraph
          callout paragraph, ...)    that comments on it (p.muted, p.tag, ...)
    A caption paragraph (p.figgrid-h, or a plain one ending in ':') is read as part of the block it
    introduces and is never separated from it."""
    kids = [k for k in cont.kids if k.start > h.start and k.end <= end and not k.attr("data-gen")]
    out, label = [], ""
    for i, k in enumerate(kids):
        if k.tag in SKIP or re.fullmatch(r"h[1-6]", k.tag):
            label = ""                                 # a sub-heading or a button: never a spot
            continue
        if is_label(doc, k, kids[i + 1] if i + 1 < len(kids) else None):
            label += " " + text_of(doc, k)
            continue
        ctx, label = label, ""
        if 'href="#' in doc[k.start:k.end] and k.tag in ("ul", "ol", "p"):
            continue                                   # a strip of in-page links
        after = k
        for nxt in kids[i + 1:]:
            if not is_note(nxt):
                break
            after = nxt
        if k.tag == "ul" and not cls(k):
            for li in k.kids:
                if li.tag == "li":
                    out.append((li, "li", ctx + " " + text_of(doc, li)))
        elif k.tag == "p" and not cls(k):
            t = text_of(doc, k)
            if len(t) >= 20:
                out.append((after, "p", ctx + " " + t))
        elif k.tag == "div" and "cond" in cls(k):
            title = next((text_of(doc, x) for x in k.kids if re.fullmatch(r"h[1-6]", x.tag)), "")
            inner = [x for x in k.kids if not (x.tag == "p" and "src" in cls(x))]
            for t in leaves(doc, k):
                out.append((inner[-1], "p", " ".join((ctx, title, t))))
        elif k.tag == "p" and "src" in cls(k):
            continue                                   # a slide citation
        else:
            for t in leaves(doc, k):
                out.append((after, "p", ctx + " " + t))
    return out


def fallback_after(h, cont, end):
    """The element the old box followed: the last direct child before the section's first
    sub-heading (or the container's end), else the heading itself."""
    after = h
    for k in cont.kids:
        if k.start <= h.start:
            continue
        if re.fullmatch(r"h[1-6]", k.tag) or k.end > end:
            break
        if k.tag not in SKIP:
            after = k
    return after


def line_weights(item_html):
    m = re.match(r"\s*<b>(.*?)</b>", item_html, re.S)
    topic = toks(H.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))) if m else []
    rest = toks(H.unescape(re.sub(r"<[^>]+>", " ", item_html)))
    w = {t: 1.0 for t in rest}
    for t in topic:
        w[t] = 2.0
    return w


def guide_idf(doc, root):
    blocks = [set(toks(text_of(doc, n))) for n in walk(root)
              if n.tag in ("p", "li", "td", "th", "dd", "dt", "figcaption", "h2", "h3", "h4", "h5", "summary")]
    df = {}
    for b in blocks:
        for t in b:
            df[t] = df.get(t, 0) + 1
    n = len(blocks)
    return lambda t: math.log((n + 1) / (df.get(t, 0) + 0.5))


def place(doc, root, idf, sid, its, avg):
    """[(element to insert after, kind, item, score, shared words, rank)] for one section's lines.
    rank orders several lines that land after the same element: by the page order of the line
    each one matched (so facts after a drug table follow the table's row order)."""
    sec = heading_section(root, sid)
    if sec is None:
        return None
    h, cont, end = sec
    cands = candidates(doc, h, cont, end)
    ctoks = [toks(t) for _, _, t in cands]
    out = []
    for it in its:
        w = line_weights(it["html"])
        best = None
        for ci, ((node, kind, _), ct) in enumerate(zip(cands, ctoks)):
            tf = {}
            for t in ct:
                tf[t] = tf.get(t, 0) + 1
            norm = K1 * (1 - B + B * len(ct) / avg)
            shared = [t for t in w if t in tf]
            s = sum(w[t] * idf(t) * tf[t] * (K1 + 1) / (tf[t] + norm) for t in shared)
            if best is None or s > best[0]:
                best = (s, node, kind, shared, ci)
        if best and best[3] and max(idf(t) for t in best[3]) >= MIN_IDF:
            out.append((best[1], best[2], it, best[0], best[3], best[4]))
        else:
            out.append((fallback_after(h, cont, end), "fallback", it, 0.0, [], len(cands)))
    return out


def render(doc, after, kind, it):
    line_start = doc.rfind("\n", 0, after.start) + 1
    indent = doc[line_start:after.start]
    indent = indent if re.fullmatch(r"[ \t]*", indent) else ""
    tag = "li" if kind == "li" else "p"
    return '\n%s<%s id="ga-%s" data-gen="1">%s</%s>' % (indent, tag, it["id"], it["html"], tag)


def strip_generated(doc):
    return GEN_LINE.sub("", OLD_BOX.sub("", doc))


def apply_guide(gpath, datas, check=False, explain=False):
    """Write every additions file that targets this guide in ONE pass (the remover strips
    every generated line on the page before re-inserting)."""
    doc = open(gpath, encoding="utf-8").read()
    base = strip_generated(doc)
    root = parse(base)
    idf = guide_idf(base, root)
    lens = [len(toks(text_of(base, n))) for n in walk(root) if n.tag in ("p", "li")]
    avg = max(1.0, sum(lens) / max(1, len(lens)))
    by = {}
    for path, data in datas:
        for it in data["items"]:
            if it.get("html") and it["html"] != "SKIP":
                by.setdefault(it["section_id"], []).append(it)
    inserts, stats = [], {"li": 0, "p": 0, "fallback": 0}
    for sid, its in by.items():
        spots = place(base, root, idf, sid, its, avg)
        if spots is None:
            raise SystemExit("%s: section id %s not found in %s" % ([d[0] for d in datas], sid, gpath))
        for order, (after, kind, it, score, shared, rank) in enumerate(spots):
            inserts.append((after.end, (rank, order), render(base, after, kind, it)))
            stats[kind] += 1
            if explain:
                print("  %-9s %-8s %5.1f  %-40s -> %s" % (kind, sid[:8], score, re.sub(r"<[^>]+>", "", it["html"])[:40],
                      text_of(base, after)[:60] if after.tag != "#root" else ""))
    # insert from the bottom up so earlier offsets stay valid; at one spot the LAST line goes in first
    new = base
    for pos, order, frag in sorted(inserts, key=lambda x: (x[0], x[1]), reverse=True):
        new = new[:pos] + frag + new[pos:]
    if new != doc and not check:
        open(gpath, "w", encoding="utf-8").write(new)
    return new != doc, stats


def main():
    check = "--check" in sys.argv
    explain = "--explain" in sys.argv
    stale = 0
    files = {}
    for f in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        files.setdefault(os.path.join(ROOT, d["folder"], d["guide"]), []).append((f, d))
    for gpath, datas in files.items():
        if explain:
            print(os.path.relpath(gpath, ROOT))
        changed, st = apply_guide(gpath, datas, check, explain)
        for f, d in datas:
            n = len([1 for it in d["items"] if it.get("html") not in (None, "SKIP")])
            print("%-46s %4d lines  %s" % (os.path.basename(f)[:-5][:46], n, ("STALE/missing" if check else "written") if changed else "up to date"))
        print("%-46s       in lists %d, as paragraphs %d, fallback %d" % ("", st["li"], st["p"], st["fallback"]))
        stale += changed
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
