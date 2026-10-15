#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the static data Pip (the study companion) reads: question banks, a guide
search index and a folder index.

    python3 tools/build_pip_data.py

Writes pip/data/ (git-ignored; regenerated, never hand-edited):

    index.json              folders -> class, exam, semester, quizzes, guides, cram sheets
    bank/<folder>.json      de-duplicated questions per folder + each page's id list
    guide/<folder>.json     searchable text blocks of every guide / cram sheet page

Scope: every <folder>/*.html whose source contains data-dark-kind="quiz" and a
`const QUESTIONS = [...]` array, in non-frozen (Semester 2+) folders. The frozen list
is the one in tools/check_exam_standard.py. Questions that carry an image, audio or
figure are left out of the bank but keep their slot (null) in the page's id list.

The class code and semester come from the site's own semesters.js, run in node, so the
folder->class mapping is never re-implemented here. Question ids are the `qid` fields
add_stable_qids.py maintains; guide links come from each folder's guide-links.json
(written by build_guide_links.py) joined on the same FNV-1a key theme.js computes.

stdlib only. Any parse problem it cannot handle stops the build with a clear message
and a non-zero exit; it never drops a page silently.
"""
import datetime, glob, html, json, os, re, subprocess, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
OUT = os.path.join(ROOT, "pip", "data")

import check_exam_standard as ces            # FROZEN list (import has no side effects)
from add_stable_qids import BLOCK, fnv36     # the exact array regex + the JS-mirroring hash

MEDIA_KEYS = ("img", "alt", "slide", "audio", "fig", "figure", "credit", "imgsrc")
MAX_BLOCK = 700
MIN_BLOCK = 12


def die(msg):
    sys.stderr.write("build_pip_data: ERROR: " + msg + "\n")
    sys.exit(1)


def dump(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)
    return len(s.encode("utf-8"))


def slug(s):
    """Same as build_group_quizzes.slug (and theme.js slugFromPath)."""
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def norm(t):
    return re.sub(r"\s+", " ", (t or "").replace(" ", " ")).strip()


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ------------------------------------------------------------------ registry (node)
def registry(folders):
    """{folder: {"cls":..., "sem":...}} from semesters.js, executed in node."""
    js = r"""
const fs=require('fs'),vm=require('vm');
const sb={window:{}};sb.window.window=sb.window;
vm.createContext(sb);
vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),sb);
const S=sb.window.Semesters;
const folders=JSON.parse(fs.readFileSync(0,'utf8'));
const out={};
for(const f of folders){const c=S.classOfPath(f+'/x.html');const s=c?S.ofClass(c):null;
 out[f]={cls:c||null,sem:s?s.id:null};}
process.stdout.write(JSON.stringify(out));
"""
    try:
        r = subprocess.run(["node", "-e", js, os.path.join(ROOT, "semesters.js")],
                           input=json.dumps(folders).encode("utf-8"),
                           capture_output=True, check=True)
    except FileNotFoundError:
        die("node is not installed; it is needed to read semesters.js")
    except subprocess.CalledProcessError as e:
        die("node failed reading semesters.js: " + e.stderr.decode("utf-8", "replace")[:400])
    return json.loads(r.stdout.decode("utf-8"))


# ------------------------------------------------------------------ html tree
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param",
        "source", "track", "wbr"}
# an open <x> is closed implicitly when one of these starts (scoped to its list/table/dl)
IMPLICIT = {
    "li": ({"li"}, {"ul", "ol"}),
    "dt": ({"dt", "dd"}, {"dl"}),
    "dd": ({"dt", "dd"}, {"dl"}),
    "tr": ({"tr", "td", "th"}, {"table", "thead", "tbody", "tfoot"}),
    "td": ({"td", "th"}, {"tr", "table"}),
    "th": ({"td", "th"}, {"tr", "table"}),
    "thead": ({"thead", "tbody", "tfoot", "tr", "td", "th"}, {"table"}),
    "tbody": ({"thead", "tbody", "tfoot", "tr", "td", "th"}, {"table"}),
    "option": ({"option"}, {"select"}),
}
P_CLOSERS = {"p", "div", "ul", "ol", "dl", "table", "h1", "h2", "h3", "h4", "h5", "h6",
             "blockquote", "section", "article", "aside", "figure", "pre", "details",
             "hr", "header", "footer", "nav", "form"}


class Node:
    __slots__ = ("tag", "attrs", "kids", "parent", "text")

    def __init__(self, tag, attrs=None, parent=None, text=None):
        self.tag, self.attrs, self.kids, self.parent, self.text = tag, attrs or {}, [], parent, text


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        self._open(tag, dict((k, v if v is not None else "") for k, v in attrs))
        if tag in VOID:
            self._close_to(tag, void=True)

    def handle_startendtag(self, tag, attrs):
        self._open(tag, dict((k, v if v is not None else "") for k, v in attrs))
        self._close_to(tag, void=True)

    def _open(self, tag, attrs):
        if tag in IMPLICIT:
            closes, stop = IMPLICIT[tag]
            n = self.cur
            while n is not self.root and n.tag not in stop:
                if n.tag in closes:
                    self.cur = n.parent
                    break
                n = n.parent
        if tag in P_CLOSERS:
            n = self.cur
            while n is not self.root and n.tag not in ("td", "th", "li", "dd", "div", "section", "body"):
                if n.tag == "p":
                    self.cur = n.parent
                    break
                n = n.parent
            else:
                pass
            if self.cur.tag == "p":
                self.cur = self.cur.parent
        node = Node(tag, attrs, self.cur)
        self.cur.kids.append(node)
        self.cur = node

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        n = self.cur
        while n is not self.root:
            if n.tag == tag:
                self.cur = n.parent
                return
            n = n.parent
        # a stray end tag with no open match is ignored

    def _close_to(self, tag, void=False):
        if self.cur.tag == tag:
            self.cur = self.cur.parent

    def handle_data(self, data):
        if data:
            self.cur.kids.append(Node("#text", parent=self.cur, text=data))


SKIP_TAGS = {"script", "style", "template", "svg", "nav", "button", "select", "option",
             "noscript", "textarea", "input", "audio", "video", "iframe", "canvas", "head", "title"}
SKIP_IDS = {"quiz-footer-logo", "pull-refresh"}
SKIP_CLASSES = {"guide-back-bar", "toc", "hdr-links", "hdr-save", "cmp-tools", "tbl-tools"}
EMIT_TAGS = {"p", "li", "dd", "dt", "h2", "h3", "h4", "h5", "h6", "blockquote", "figcaption",
             "summary", "caption"}
# elements that hold their own block-level content: their *own* text (outside any of
# these) is emitted too, so a bare "<div class=callout>text</div>" is not lost.
CONTAINER_TAGS = {"div", "section", "article", "aside", "main", "details", "dl", "ul", "ol",
                  "table", "thead", "tbody", "tfoot", "figure", "header", "footer", "form",
                  "pre", "tr", "td", "th", "hgroup", "body", "html", "address", "fieldset"}
BLOCKISH = EMIT_TAGS | CONTAINER_TAGS | {"h1"}
CHROME_TEXT = re.compile(r"click here to report|Back to Homepage|^Built from your PAJ|^← Back$", re.I)
CHROME_LINE = re.compile(r"^(?:PAJ\s*\d+\s+)?[^\n]{0,70}Class of 2028(?:\s*[·.][^\n]{0,60})?$", re.I)


def skipped(n):
    if n.tag in SKIP_TAGS:
        return True
    a = n.attrs
    if "hidden" in a or a.get("aria-hidden") == "true":
        return True
    if re.search(r"display\s*:\s*none", a.get("style", ""), re.I):
        return True
    if a.get("id") in SKIP_IDS:
        return True
    if SKIP_CLASSES & set(a.get("class", "").split()):
        return True
    return False


def own_text(n, descend_all=False):
    """Text of n's subtree. Unless descend_all, block-ish children are not entered (they
    are emitted on their own); a space stands where they were."""
    parts = []

    def walk(x):
        for k in x.kids:
            if k.tag == "#text":
                parts.append(k.text)
            elif skipped(k):
                parts.append(" ")
            elif k.tag == "br":
                parts.append(" ")
            elif not descend_all and k.tag in BLOCKISH:
                parts.append(" ")
            else:
                if k.tag in BLOCKISH:
                    parts.append(" ")
                walk(k)
                if k.tag in BLOCKISH:
                    parts.append(" ")

    walk(n)
    return norm("".join(parts))


def split_long(text):
    """Cut text longer than MAX_BLOCK into chunks at sentence boundaries."""
    if len(text) <= MAX_BLOCK:
        return [text]
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'“‘(\[★])", text)
    pieces = []
    for s in sents:
        while len(s) > MAX_BLOCK:                   # no sentence break: cut at a word boundary
            cut = s.rfind(" ", 0, MAX_BLOCK)
            if cut < MAX_BLOCK // 2:
                cut = MAX_BLOCK
            pieces.append(s[:cut].strip())
            s = s[cut:].strip()
        if s:
            pieces.append(s)
    out, cur = [], ""
    for p in pieces:
        if cur and len(cur) + 1 + len(p) > MAX_BLOCK:
            out.append(cur)
            cur = p
        else:
            cur = (cur + " " + p).strip()
    if cur:
        if out and len(cur) < MIN_BLOCK:
            out[-1] = out[-1] + " " + cur           # never drop a tiny tail; fold it back
        else:
            out.append(cur)
    return out


def parse_page(src):
    t = Tree()
    t.feed(src)
    t.close()
    return t.root


def find(n, tag):
    for k in n.kids:
        if k.tag == tag:
            return k
        r = find(k, tag)
        if r:
            return r
    return None


def page_title(root, src):
    h1 = find(root, "h1")
    if h1:
        t = own_text(h1, True)
        if t:
            return t
    m = re.search(r"<title>(.*?)</title>", src, re.S | re.I)
    t = norm(html.unescape(m.group(1))) if m else ""
    return re.split(r"\s+\|\s+", t)[0] if t else ""


def extract_blocks(root):
    """[(anchorId|None, sectionTitle, text)] in document order."""
    blocks = []
    # part: the page's current h2 (a lecture, "4 · Valvular Heart Disease"); sub: an h4-h6 item heading
    # ("Aortic stenosis") for the blocks inside the same container as it, so "the defining feature of
    # each valvular disease" can gather one line per condition
    state = {"last_id": None, "sec": "", "h3": "", "part": "", "sub": None}

    def sub_of(n):
        sb = state["sub"]
        if not sb or n is sb[1]:
            return ""
        x = n.parent
        while x is not None:
            if x is sb[2]:
                return sb[0]
            x = x.parent
        return ""

    def emit(n, text, sec_suffix=""):
        if not text:
            return
        if CHROME_TEXT.search(text):
            return
        if len(text) < 90 and CHROME_LINE.match(text):
            return
        anchor = n.attrs.get("id") or state["last_id"]
        sec = state["sec"] + sec_suffix
        sub = sub_of(n)
        for piece in split_long(text):
            if len(piece) >= MIN_BLOCK:
                blocks.append((anchor, sec, piece, state["part"], sub))

    def details_label(n):
        x = n.parent
        while x is not None and x is not root:
            if x.tag == "details":
                for k in x.kids:
                    if k.tag == "summary":
                        s = own_text(k, True)
                        return s
                return ""
            x = x.parent
        return ""

    def visit(n):
        if n.tag == "#text":
            return
        if skipped(n):
            return
        if n.attrs.get("id") and not n.attrs.get("data-gen"):
            # a line written into a section by apply_guide_additions.py (data-gen) anchors only
            # itself: the guide's own lines after it keep pointing at their section
            state["last_id"] = n.attrs["id"]
        tag = n.tag
        if tag == "tr":
            cells = [k for k in n.kids if k.tag in ("td", "th")]
            # a row may have been wrapped oddly; fall back to every descendant cell
            for c in cells:
                if c.attrs.get("id"):
                    state["last_id"] = c.attrs["id"]
            if cells and any(c.tag == "td" for c in cells):
                texts = [own_text(c, True) for c in cells]
                text = " — ".join(x for x in texts if x)
                suf = details_label(n)
                emit(n, text, (" › " + suf) if suf else "")
            elif cells:
                pass                                   # a header row of th only
            return                                     # a row is one unit; never emit inside it
        if tag in ("h2", "h3", "h4", "h5", "h6"):
            t = own_text(n, True)
            if tag in ("h2", "h3") and t:
                state["sec"] = t
                state["sub"] = None
                if tag == "h2":
                    state["part"] = t
            emit(n, t)
            if tag in ("h4", "h5", "h6") and t and n.parent is not None:
                state["sub"] = (t, n, n.parent)
            return
        if tag == "h1":
            return
        if tag in EMIT_TAGS or tag in CONTAINER_TAGS:
            t = own_text(n)
            if t:
                suf = ""
                if tag != "summary":
                    d = details_label(n)
                    if d:
                        suf = " › " + d
                emit(n, t, suf)
        for k in n.kids:
            visit(k)

    visit(root)
    return blocks


SMALL = {"of", "and", "the", "to", "in", "for", "on", "a", "an", "with", "by"}


EVERYDAY = set("as us id is or am it in on an at me my no so up we do go he if of to be by ok hi oh".split())


def abbreviations(texts):
    """{"pcr": "polymerase chain reaction", ...} from "Full Term (ABBR)" and "ABBR (full term)" in the text.
    The guides spell abbreviations out (no-abbreviations rule), so a student who types PCR
    would otherwise find nothing; Pip's search treats the two forms as the same words."""
    votes = {}
    def take(abbr, words):
        letters = re.sub(r"[^a-z0-9]", "", abbr.lower())
        if len(letters) < 2 or len(words) > 8:
            return
        ws = [w for w in words if w]
        # longest tail of the words whose initials (skipping small words) spell the abbreviation
        for k in range(min(len(ws), len(letters) + 3), 0, -1):
            tail = ws[-k:]
            ini = "".join(w[0] for w in tail if w.lower() not in SMALL)
            if ini.lower() == letters or (k <= len(letters) + 1 and tail[0][0].lower() == letters[0] and len(tail) >= 1 and ini.lower().startswith(letters[0])):
                while len(tail) > 1 and tail[0].lower() in SMALL:
                    tail = tail[1:]
                exp = " ".join(tail).lower()
                if exp != letters:
                    votes.setdefault(letters, {}).setdefault(exp, 0)
                    votes[letters][exp] += 1
                return
    for t in texts:
        for m in re.finditer(r"([A-Za-z][\w'\-]*(?:\s+[A-Za-z][\w'\-]*){0,7})\s*\(([A-Z][A-Za-z0-9]{1,7})\)", t):
            if sum(ch.isupper() for ch in m.group(2)) >= 2:
                take(m.group(2), re.split(r"[\s\-]+", m.group(1)))
        for m in re.finditer(r"\b([A-Z][A-Z0-9]{1,7})\s*\(([a-z][a-z'\- ]{3,80})\)", t):
            take(m.group(1), re.split(r"[\s\-]+", m.group(2)))
    # never Roman numerals ("type III (irreversible)" made "iii" an abbreviation) or everyday words
    # ("as" = aortic stenosis, "us" = ultrasound would rewrite "can you tell us")
    return {k: max(v.items(), key=lambda kv: kv[1])[0] for k, v in sorted(votes.items())
            if not re.match(r"^(i{1,3}|iv|vi{0,3}|ix|xi{0,3})$", k) and k not in EVERYDAY}


def build_guide_index(folder, files):
    docs, blocks, idsets, parts, pidx = [], [], {}, [], {}
    for f in files:
        src = read(os.path.join(ROOT, folder, f))
        m = re.search(r"<body[^>]*data-dark-kind=\"([^\"]*)\"", src)
        kind = m.group(1) if m else None
        try:
            root = parse_page(src)
            title = page_title(root, src) or f
            bl = extract_blocks(root)
        except Exception as e:
            die("cannot parse %s/%s: %r" % (folder, f, e))
        if not bl:
            die("no readable text blocks in %s/%s (parser likely failed)" % (folder, f))
        di = len(docs)
        docs.append({"file": f, "title": title, "kind": kind})
        seen = set()
        for anchor, sec, text, part, sub in bl:
            if text in seen:
                continue
            seen.add(text)
            b = [di, anchor or None, sec, text]
            # [4] the h2 part (an index into "p"), [5] the item heading: only when there is one
            if part or sub:
                if part and part not in pidx:
                    pidx[part] = len(parts)
                    parts.append(part)
                b.append(pidx[part] if part else -1)
                if sub:
                    b.append(sub)
            blocks.append(b)
        idsets[f] = set(re.findall(r"""\sid=["']([^"']+)["']""", src))
    return {"v": 1, "docs": docs, "b": blocks, "p": parts, "ab": abbreviations([x[3] for x in blocks])}, idsets


# ------------------------------------------------------------------ main
def ship_explain(fslug, gidx):
    """Pip explains: ship this exam's checked plain-language cards (pip/explain/<slug>.json, written and
    validated with tools/pip_explain.py) to pip/data/explain/<slug>.json, runtime fields only, plus a map
    from every anchor in a carded guide section to its unit, so a question's guide link finds its card.
    A card whose guide section changed since it was written still ships but is counted as stale."""
    src = os.path.join(ROOT, "pip", "explain", fslug + ".json")
    if not os.path.exists(src):
        return 0, 0, 0
    import pip_explain
    with open(src, encoding="utf-8") as fh:
        data = json.load(fh)
    us = {u["u"]: u for u in pip_explain.units(fslug)}
    have = {}
    for b in gidx["b"]:
        have.setdefault(gidx["docs"][b[0]]["file"], set()).add(b[1])
    cards, stale, dropped, carded = [], 0, 0, set()
    for c in data.get("cards", []):
        if c.get("doc") not in have or c.get("a") not in have[c["doc"]] or c.get("u") not in us:
            dropped += 1                              # its page or section is gone: never link to nowhere
            continue
        if c.get("h") != us[c["u"]]["h"]:
            stale += 1
        carded.add(c["u"])
        cards.append({k: c[k] for k in ("id", "u", "t", "k", "q", "doc", "a", "x")})
    amap = {}
    for u in us.values():
        if u["u"] in carded:
            for a in u["anchors"]:
                amap.setdefault(u["doc"] + "#" + a, u["u"])
    dump(os.path.join(OUT, "explain", fslug + ".json"), {"v": 1, "cards": cards, "m": amap})
    return len(cards), stale, dropped


def main():
    frozen_pages, pages_by_folder = 0, {}
    all_dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
    skipped_folders = []
    for d in all_dirs:
        files = sorted(f for f in os.listdir(os.path.join(ROOT, d)) if f.endswith(".html"))
        if not files:
            continue
        if ces.is_frozen(d + "/x.html"):
            skipped_folders.append(d)
            continue
        pages_by_folder[d] = files

    kinds, srcs = {}, {}
    for d, files in pages_by_folder.items():
        for f in files:
            s = read(os.path.join(ROOT, d, f))
            srcs[(d, f)] = s
            m = re.search(r"<body[^>]*data-dark-kind=\"([^\"]*)\"", s)
            kinds[(d, f)] = m.group(1) if m else None

    quiz_pages = {}
    for (d, f), s in srcs.items():
        if 'data-dark-kind="quiz"' not in s:
            continue
        m = BLOCK.search(s)
        if not m:
            die("%s/%s is a quiz page (data-dark-kind=\"quiz\") but has no const QUESTIONS array" % (d, f))
        try:
            qs = json.loads(m.group(2))
        except ValueError as e:
            die("%s/%s: QUESTIONS is not strict JSON: %s" % (d, f, e))
        if not isinstance(qs, list) or not qs:
            die("%s/%s: QUESTIONS is empty or not an array" % (d, f))
        quiz_pages.setdefault(d, {})[f] = (s, qs)

    folders = sorted(quiz_pages)
    if not folders:
        die("no quiz pages found")
    reg = registry(folders)

    try:
        group_ids = set(re.findall(r'^"([^"]+)":', read(os.path.join(ROOT, "group-quizzes", "index.js")), re.M))
    except OSError:
        group_ids = None

    built = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    index = {"v": 1, "built": built, "folders": []}
    ab_texts = []                     # every guide block and question, for the site-wide abbreviation list
    stats, misses = [], []
    explain_stats = []                # (folder, cards shipped, stale, dropped) per exam
    ab_by_exam = {}                   # slug -> that guide's own abbreviations, for exams with cards (cross-exam search)
    words = {}                        # word -> [count, exam bit mask], for pip/data/words.json
    all_ids = {}

    for folder in folders:
        fslug = slug(folder)
        r = reg[folder]
        if not r["cls"] or not r["sem"]:
            die("semesters.js does not classify folder %r (class=%r semester=%r)" % (folder, r["cls"], r["sem"]))
        m = re.search(r"\bExam\s+(\d+)\s*$", folder)
        exam = int(m.group(1)) if m else None
        base = re.sub(r"\s*Exam\s+\d+\s*$", "", folder).strip()
        if exam is not None:
            title = "%s · Exam %d" % (base, exam)
        elif base.endswith("Book Questions"):
            title = "%s · Book Questions" % base[: -len("Book Questions")].strip()
        else:
            title = folder

        # guide links for this folder
        gl_path = os.path.join(ROOT, folder, "guide-links.json")
        gl = None
        if os.path.exists(gl_path):
            gl = json.loads(read(gl_path))
            if gl.get("v") != 1 or "g" not in gl or "l" not in gl:
                die("%s: unexpected guide-links.json shape" % folder)

        # guide + cram pages (body data-dark-kind is the source of truth)
        gfiles = sorted(f for f in pages_by_folder[folder] if kinds[(folder, f)] == "guide")
        cfiles = sorted(f for f in pages_by_folder[folder] if kinds[(folder, f)] == "cram")
        gidx, idsets = build_guide_index(folder, gfiles + cfiles)

        # ---- questions
        pages_ids, quizzes = {}, []
        bank, order, variants = {}, [], {}
        raw = excluded = collisions = drift = 0
        for f in sorted(quiz_pages[folder]):
            src, qs = quiz_pages[folder][f]
            ids = []
            for i, q in enumerate(qs):
                raw += 1
                for key in ("q", "opts", "c", "qid"):
                    if key not in q:
                        die("%s/%s question %d lacks %r" % (folder, f, i, key))
                if any(k in q for k in MEDIA_KEYS):
                    excluded += 1
                    ids.append(None)
                    continue
                opts = q["opts"]
                if not (isinstance(opts, list) and all(isinstance(o, list) and len(o) == 2 and
                                                      all(isinstance(x, str) for x in o) for o in opts)):
                    die("%s/%s question %d: opts are not [text, explanation] pairs" % (folder, f, i))
                if not isinstance(q["c"], int) or isinstance(q["c"], bool) or not 0 <= q["c"] < len(opts):
                    die("%s/%s question %d: correct index %r out of range" % (folder, f, i, q["c"]))
                qid = q["qid"]
                if not isinstance(qid, str) or not qid:
                    die("%s/%s question %d has no usable qid" % (folder, f, i))
                # masters re-permute option order per form, so identity is order-free: the stem, the
                # SET of option texts and the correct option's text
                sig = (q["q"], tuple(sorted(o[0] for o in opts)), opts[q["c"]][0])
                vs = variants.setdefault(qid, [])
                aid = None
                for vsig, vid in vs:
                    if vsig == sig:
                        aid = vid
                        break
                if aid is None:
                    aid = qid if not vs else "%s~%d" % (qid, len(vs) + 1)
                    vs.append((sig, aid))
                    if len(vs) > 1:
                        collisions += 1
                        sys.stderr.write("  collision in %s: qid %s reused by a different question in %s -> %s\n"
                                         % (folder, qid, f, aid))
                    gtxt = q["q"] + "\n" + opts[q["c"]][0]
                    link = None
                    if gl:
                        L = gl["l"].get(fnv36(gtxt))
                        if L:
                            gi = L[0]
                            if not (isinstance(gi, int) and 0 <= gi < len(gl["g"])):
                                die("%s: guide-links index %r out of range" % (folder, gi))
                            link = [gl["g"][gi], L[1], L[2], L[3]]
                            if len(L) > 4 and L[4]:
                                link.append(1)         # "closest section" tier, as the quiz panel shows it
                    bank[aid] = {"id": aid, "q": q["q"], "o": opts, "c": q["c"], "io": q.get("io", ""),
                                 "t": q.get("topic", ""), "cite": q.get("cite", ""), "g": link, "p": []}
                    order.append(aid)
                else:
                    ob = {o[0]: o[1] for o in bank[aid]["o"]}
                    if ob != {o[0]: o[1] for o in opts}:
                        drift += 1
                if f not in bank[aid]["p"]:
                    bank[aid]["p"].append(f)
                ids.append(aid)
            if len(ids) != len(qs):
                die("%s/%s: id list length %d != QUESTIONS length %d" % (folder, f, len(ids), len(qs)))
            pages_ids[f] = ids
            qid_slug = slug(folder + "/" + f[:-5])
            if group_ids is not None and qid_slug not in group_ids:
                # build_group_quizzes skips image/audio pages entirely; anything else should be there
                has_media = any(any(k in q for k in MEDIA_KEYS) for q in qs)
                if not has_media:
                    sys.stderr.write("  note: %s/%s id %r is not in group-quizzes/index.js\n" % (folder, f, qid_slug))
            if qid_slug in all_ids:
                die("quiz id %r is not unique (%s/%s vs %s)" % (qid_slug, folder, f, all_ids[qid_slug]))
            all_ids[qid_slug] = folder + "/" + f
            h1 = find(parse_page(src), "h1")
            t = own_text(h1, True) if h1 else ""
            if not t:
                mt = re.search(r"<title>(.*?)</title>", src, re.S | re.I)
                t = re.split(r"\s+\|\s+", norm(html.unescape(mt.group(1))))[0] if mt else f[:-5]
            quizzes.append({"file": f, "id": qid_slug, "title": t, "n": len(qs),
                            "master": "master" in f.lower()})

        for b in bank.values():
            b["p"].sort()
        qlist = [bank[a] for a in order]
        joined = sum(1 for b in qlist if b["g"])

        # ---- validate anchors
        gmiss = []
        for b in qlist:
            if not b["g"]:
                continue
            gf, el = b["g"][0], b["g"][1]
            path = os.path.normpath(os.path.join(ROOT, folder, gf))
            if not os.path.exists(path):
                gmiss.append((b["id"], gf, "missing guide file"))
                continue
            gsrc = read(path)
            if not re.search(r"""\sid=["']%s["']""" % re.escape(el), gsrc):
                gmiss.append((b["id"], gf, el))
        imiss = []
        for di, anchor, sec, text, *_ in gidx["b"]:
            if anchor is not None and anchor not in idsets[gidx["docs"][di]["file"]]:
                imiss.append((gidx["docs"][di]["file"], anchor))
        misses.append((folder, gmiss, imiss))

        bank_kb = dump(os.path.join(OUT, "bank", fslug + ".json"),
                       {"v": 1, "f": folder, "pages": pages_ids, "q": qlist})
        guide_kb = dump(os.path.join(OUT, "guide", fslug + ".json"), gidx)
        ex_n, ex_stale, ex_drop = ship_explain(fslug, gidx)
        explain_stats.append((folder, ex_n, ex_stale, ex_drop))
        # every word this exam's guides and cards use (pip/data/words.json, below)
        fi = len(index["folders"])
        wtexts = [x[3] for x in gidx["b"]] + [x[2] for x in gidx["b"]] + gidx["p"]
        if ex_n:
            with open(os.path.join(OUT, "explain", fslug + ".json"), encoding="utf-8") as fh:
                for c in json.load(fh)["cards"]:
                    wtexts += [c["t"], c["x"]] + c["k"]
        for t in wtexts:
            # "P wave" -> "pwave wave", as letterTerms() in pip/pip-window.js reads it
            for w in re.findall(r"[a-z][a-z0-9]{2,}", re.sub(r"\b([pqrstuj])[\s-]+(waves?|points?)\b", r"\1\2 \2", t.lower())):
                e = words.setdefault(w, [0, 0])
                e[0] += 1
                e[1] |= 1 << fi
        if ex_n and gidx.get("ab"):
            ab_by_exam[fslug] = gidx["ab"]
        ab_texts.extend(x[3] for x in gidx["b"])
        for q in qlist:
            ab_texts.append(q["q"]); ab_texts.extend(o[0] + " " + o[1] for o in q["o"])
        index["folders"].append({"f": folder, "s": fslug, "c": r["cls"], "x": exam, "sem": r["sem"], "t": title,
                                 "guides": gfiles, "cram": cfiles, "quizzes": quizzes, "nq": len(qlist)})
        if ex_n:
            index["folders"][-1]["ex"] = ex_n
        stats.append({"f": folder, "pages": len(quiz_pages[folder]), "raw": raw, "uniq": len(qlist),
                      "excl": excluded, "coll": collisions, "drift": drift, "join": joined,
                      "bank_kb": bank_kb / 1024, "blocks": len(gidx["b"]), "guide_kb": guide_kb / 1024,
                      "bank_path": fslug, "docs": len(gidx["docs"])})

    # one list for the whole site: a guide that never writes "(PCR)" still answers "PCR"
    index["ab"] = abbreviations(ab_texts)
    index_size = dump(os.path.join(OUT, "index.json"), index)
    # Pip's spelling and routing list: every word of every exam's guides and cards, commonest first, with a
    # bit per exam (index.json folder order) saying where it occurs. A word known ANYWHERE is never
    # "corrected" (rythm -> rhythm, but never one exam's word into another's), and a question only loads
    # the exams that hold its words
    if len(index["folders"]) > 30:
        die("words.json masks assume at most 30 exam folders; there are %d" % len(index["folders"]))
    wl = sorted(words.items(), key=lambda kv: (-kv[1][0], kv[0]))
    words_kb = dump(os.path.join(OUT, "words.json"), {"v": 1, "w": " ".join(w for w, _ in wl),
                                                      "m": " ".join(format(e[1], "x") for _, e in wl)}) / 1024
    print("words.json: %d words, %.0f KB" % (len(wl), words_kb))
    ab_kb = dump(os.path.join(OUT, "ab.json"), ab_by_exam) / 1024
    print("per-exam abbreviations (%d exams with cards): %.1f KB" % (len(ab_by_exam), ab_kb))
    print("abbreviations (site-wide): %d" % len(index["ab"]))

    # ---- report
    W = max(len(s["f"]) for s in stats) + 1
    hdr = "%-*s %5s %6s %6s %5s %4s %7s %8s %7s %8s" % (W, "folder", "pages", "raw", "uniq", "excl", "coll",
                                                       "join%", "bank KB", "blocks", "guide KB")
    print(hdr)
    print("-" * len(hdr))
    tot = dict(pages=0, raw=0, uniq=0, excl=0, coll=0, join=0, bank_kb=0.0, blocks=0, guide_kb=0.0, drift=0)
    for s in stats:
        pct = 100.0 * s["join"] / s["uniq"] if s["uniq"] else 0.0
        print("%-*s %5d %6d %6d %5d %4d %6.1f%% %8.0f %7d %8.0f" % (
            W, s["f"], s["pages"], s["raw"], s["uniq"], s["excl"], s["coll"], pct, s["bank_kb"], s["blocks"], s["guide_kb"]))
        for k in tot:
            if k in s:
                tot[k] += s[k]
    print("-" * len(hdr))
    pct = 100.0 * tot["join"] / tot["uniq"] if tot["uniq"] else 0.0
    print("%-*s %5d %6d %6d %5d %4d %6.1f%% %8.0f %7d %8.0f" % (
        W, "TOTAL", tot["pages"], tot["raw"], tot["uniq"], tot["excl"], tot["coll"], pct, tot["bank_kb"], tot["blocks"], tot["guide_kb"]))
    print("\nindex.json: %.1f KB; %d folders, %d quiz pages" % (index_size / 1024, len(index["folders"]), tot["pages"]))
    print("same-qid questions whose explanations differ between pages (kept as one): %d" % tot["drift"])
    print("skipped (frozen Semester 1) folders: %d" % len(skipped_folders))
    ex = [e for e in explain_stats if e[1] or e[3]]
    print("Pip explains: %d cards in %d exams (%d stale: guide section changed since written; %d dropped: section gone)" % (
        sum(e[1] for e in ex), len(ex), sum(e[2] for e in ex), sum(e[3] for e in ex)))
    for f, n, st, dr in ex:
        if st or dr:
            print("  %s: %d stale, %d dropped (refresh with tools/pip_explain.py)" % (f, st, dr))

    gm = sum(len(m[1]) for m in misses)
    im = sum(len(m[2]) for m in misses)
    print("\nvalidation")
    print("  bank g elementId missing from its guide page: %d" % gm)
    print("  guide-index anchorId missing from its page:   %d" % im)
    print("  pages-list length == QUESTIONS length:        checked for %d pages, all equal" % tot["pages"])
    for folder, g, i in misses:
        for x in g[:5]:
            print("   MISS g  %s: %r" % (folder, x))
        for x in i[:5]:
            print("   MISS ix %s: %r" % (folder, x))
    if gm or im:
        die("anchor validation failed (%d bank, %d guide-index)" % (gm, im))


if __name__ == "__main__":
    main()
