#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse the Interpretation of Medical Literature "Clinical Epidemiology Study Questions" document
(183 textbook questions, 14 chapters) into tools/medlit_book_sets.json and copy its figures into
"Interpretation of Medical Literature Book Questions/images/".

    python3 tools/build_medlit_book.py [path-to.docx]    # default ~/Downloads/Clinical_Epidemiology_Questions_and_Answers.docx
    python3 tools/render_medlit_book.py                  # then write the 14 chapter quizzes

The document is textbook material and is reproduced as given:
  * one quiz per chapter; question text and answer choices verbatim (3 to 5 choices, as in the book);
  * a scenario that several questions share ("Questions 1.1-1.6 are based on...") is put in front of EACH of
    those questions, so every question reads on its own (the site's self-contained rule);
  * figures go on the questions they belong to; the small data table becomes a plain text line;
  * the book gives ONE explanation, for the correct answer. Each wrong choice shows it behind "Not the best
    answer" (what the legacy converter did) rather than inventing per-choice refutations the book lacks;
  * instructions that only say "select the best answer" are dropped.
"""
import json, os, re, sys
from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Downloads/Clinical_Epidemiology_Questions_and_Answers.docx")
FOLDER = os.path.join(ROOT, "Interpretation of Medical Literature Book Questions")
OUT = os.path.join(HERE, "medlit_book_sets.json")
DASH = "–-"

ALT = {
    1: "Distribution of vitamin D levels: a right-skewed curve for participants in the United States peaking near 18 and a right-skewed curve for participants in Ghana peaking near 29.",
    2: "Three histograms of the error of hospital-staff fetal heart rate measurements against the electronic monitor, for monitored rates of 130 to 150 (A), under 130 (B) and over 150 (C).",
    3: "Calibration of a risk model. A: observed and predicted event rates by 10-year risk category. B and C: predicted probability against observed proportion, with the points above the diagonal line of perfect calibration.",
    4: "Distributions of estimated 5-year breast cancer risk for women who did and did not develop breast cancer; the two curves overlap almost completely.",
    5: "Health-care-associated MRSA infections per 1,000 patient-days from October 2005 to June 2010, falling after the program was introduced across the VA hospitals.",
}
CAPTION = {1: "Figure 3.13", 2: "Figure 3.14", 3: "Figure 5.4", 4: "Figure 5.3B", 5: "MRSA infections graph"}
# scenarios whose range the document does not state
RANGE_OVERRIDE = {"A study was conducted to determine whether a fecal": ((10, 1), (10, 3)),
                  "In a randomized controlled trial of screening": ((10, 4), (10, 6))}

doc = Document(SRC)
rels = doc.part.rels


def text_of(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


items, nimg = [], 0
os.makedirs(os.path.join(FOLDER, "images"), exist_ok=True)
for el in doc.element.body.iterchildren():
    tag = el.tag.split("}")[1]
    if tag == "p":
        pp = el.find(qn("w:pPr"))
        st = pp.find(qn("w:pStyle")) if pp is not None else None
        style = st.get(qn("w:val")) if st is not None else ""
        for b in el.iter(qn("a:blip")):
            nimg += 1
            part = rels[b.get(qn("r:embed"))].target_part
            fn = "book-figure-%d.%s" % (nimg, part.partname.split(".")[-1])
            open(os.path.join(FOLDER, "images", fn), "wb").write(part.blob)
            items.append(("img", (nimg, fn)))
        t = text_of(el).strip()
        if t:
            items.append(({"Heading1": "h1", "Heading2": "h2", "Title": "title"}.get(style, "p"), t))
    elif tag == "tbl":
        items.append(("tbl", [[text_of(c).strip() for c in r.iter(qn("w:tc"))] for r in el.iter(qn("w:tr"))]))

OPT = re.compile(r"^([A-H])\.\s+(.*)$", re.S)
GENERIC = re.compile(r"(select|choose|mark) the (one )?best (answer|response)\.?$|^Read the (following|related)|^Questions? [\d.]+.*are based on|^For questions?\b", re.I)
KEEP = re.compile(r"^For each of the (following|numbered)", re.I)


def qnum(s):
    a, b = s.split(".")
    return (int(a), int(b))


def rng(text):
    m = re.search(r"[Qq]uestions?\s+(\d+\.\d+)\s*[%s]\s*(\d+\.\d+)" % DASH, text) or re.search(r"\((\d+\.\d+)\s*[%s]\s*(\d+\.\d+)\)" % DASH, text)
    return (qnum(m.group(1)), qnum(m.group(2))) if m else None


def clean(t):
    t = re.sub(r"\s*Questions?\s+[\d.]+\s*[%s]\s*[\d.]+\s+relate to the figure\.\s*For each question, choose the best answer\." % DASH, "", t)
    return t.replace("circle the one response", "select the one response")


def table_line(rows):
    hdr = rows[0]
    return "; ".join("%s: %s" % (r[0], ", ".join("%s %s" % (hdr[k], r[k]) for k in range(1, len(r)))) for r in rows[1:])


def ask_of(instruction):
    if "threat to validity" in instruction:
        return "Which response best represents the corresponding threat to validity?"
    if "type of data" in instruction:
        return "Which is the most appropriate term for this type of data?"
    raise SystemExit("no question wording for instruction: " + instruction)


def context_of(grp):
    """A run of items that sets the scene for later questions -> {lo, hi, text[], imgs[]} or None."""
    paras = [v for k, v in grp if k == "p"]
    r = None
    for p in paras:
        r = r or rng(p)
    text, imgs, asks = [], [], []
    for k, v in grp:
        if k == "p":
            cv = clean(v)
            if KEEP.match(cv):
                asks.append(ask_of(cv))          # an instruction that names the task becomes the question that ends the stem
                continue
            if GENERIC.search(cv):
                continue
            text.append(cv)
        elif k == "tbl":
            text.append(table_line(v) + ".")
        elif k == "img":
            imgs.append(v)
    for p in paras:
        for lead, span in RANGE_OVERRIDE.items():
            if p.startswith(lead):
                r = span
    if not (text or asks) or not r:
        return None
    return {"lo": r[0], "hi": r[1], "text": text, "imgs": imgs, "asks": asks}


TOC = {}
for kk, vv in items:
    m = re.match(r"^(\d+)\s+(.+?)\s+\u00b7\s+\d+ questions$", vv) if kk == "p" else None
    if m:
        TOC[int(m.group(1))] = m.group(2).strip()      # the contents list keeps the colons ("Risk: Basic Principles")
chapters, ctxs, cur, i, n = [], [], None, 0, len(items)
while i < n:
    k, v = items[i]
    if k == "h1":
        m = re.match(r"Chapter (\d+)\s+(.*)", v)
        cur = {"n": int(m.group(1)), "title": TOC.get(int(m.group(1)), m.group(2).strip()), "questions": []}
        chapters.append(cur)
        j = i + 1
        grp = []
        while j < n and items[j][0] not in ("h2", "h1"):
            grp.append(items[j]); j += 1
        c = context_of(grp)
        if c:
            ctxs.append(c)
        i = j
    elif k == "h2" and v.startswith("Question "):
        num = v.split()[-1]
        stem, opts, img, ans = [], [], None, None
        j = i + 1
        while j < n and items[j][0] not in ("h2", "h1"):
            kk, vv = items[j]; j += 1
            if kk == "img":
                img = vv
            elif kk == "p":
                mo = OPT.match(vv)
                if re.match(r"Answer [A-H]\b", vv):
                    ans = vv; break
                if mo:
                    opts.append((mo.group(1), mo.group(2).strip()))
                else:
                    stem.append(clean(vv))
        assert ans and opts, "question %s did not parse" % num
        letter = re.match(r"Answer ([A-H])", ans).group(1)
        rest = re.sub(r"^Answer [A-H]\.?\s*", "", ans).strip()
        ci = [o[0] for o in opts].index(letter)
        otext = opts[ci][1]
        if rest.lower().rstrip(".") == otext.lower().rstrip("."):
            rest = ""
        elif rest.lower().startswith(otext.lower()):
            rest = rest[len(otext):].lstrip(". ").strip()
        grp = []
        while j < n and items[j][0] not in ("h2", "h1"):
            grp.append(items[j]); j += 1
        expl = rest
        first = grp[0][1] if grp and grp[0][0] == "p" else ""
        if grp and re.match(r"^(Questions? \d|For questions?|Figure \d|In a randomized controlled trial of screening)", first):
            c = context_of(grp)
            if c:
                ctxs.append(c)
        else:
            for kk, vv in grp:
                add = (table_line(vv) + ".") if kk == "tbl" else vv
                expl += (" " if expl else "") + add
        q = {"num": num, "stem": stem, "opts": opts, "c": ci, "img": img, "expl": expl.strip()}
        cur["questions"].append(q)
        i = j
    else:
        i += 1

# ---- assemble
EXPL_PATH = os.path.join(ROOT, "tools", "medlit_book_explanations.json")
EXPL = json.load(open(EXPL_PATH, encoding="utf-8")) if os.path.exists(EXPL_PATH) else {}
out = []
for ch in chapters:
    qs = []
    for q in ch["questions"]:
        num = qnum(q["num"])
        pre, imgs, asks = [], [], []
        for c in ctxs:
            if c["lo"] <= num <= c["hi"]:
                pre += c["text"]; imgs += c["imgs"]; asks += c["asks"]
        img = q["img"] or (imgs[0] if imgs else None)
        letter = q["opts"][q["c"]][0]
        otext = q["opts"][q["c"]][1]
        good = "Correct. " + (q["expl"] if q["expl"] else otext.rstrip(".") + ".")
        # no letter in the wording: the choices can be reordered, and the page prints the right letter itself
        bad = "Not the best answer. The best answer is: %s. See the explanation under it." % otext.rstrip(".")
        opts = [[t, good if idx == q["c"] else bad] for idx, (l, t) in enumerate(q["opts"])]
        cite = "Clinical Epidemiology Study Questions, Question %s" % q["num"]
        ex = EXPL.get(q["num"])
        if ex:
            # per-choice explanations written from the lecture decks (tools/medlit_book_explanations.json),
            # keyed by choice TEXT so the answer-position balancing below can move choices safely
            assert [t for _, t in q["opts"]] and all(t in ex["expls"] for _, t in q["opts"]), q["num"]
            opts = [[t, ex["expls"][t]] for _, t in q["opts"]]
            assert opts[q["c"]][1].startswith("Correct"), q["num"]
            cite = "; ".join(ex["cites"] + [cite])
        d = {"num": q["num"], "c0": q["c"], "expl_src": q["expl"], "topic": ch["title"], "io": "Chapter %d · %s" % (ch["n"], ch["title"]),
             "q": "\n\n".join(pre + [" ".join(q["stem"])] + asks[:1]), "opts": opts, "c": q["c"],
             "cite": cite}
        if img:
            d["img"] = "images/" + img[1]; d["alt"] = ALT[img[0]]; d["slide"] = CAPTION[img[0]]
        qs.append(d)
    out.append({"n": ch["n"], "title": ch["title"], "questions": qs})
# ---- answer positions: the book's keys are what they are, so only choices that can move are moved.
# Not moved: choices that name other choices ("A and B", "all of the above"), numeric/percent lists (ordered
# by size), and the same lettered list repeated across a chapter's questions.
import collections
REF = re.compile(r"\b[A-E]\b(,| and | or )|^[A-E]$", 0)
REF_LOWER = re.compile(r"(all|none) of the above|\b(both|neither) [ab]\b", re.I)


LETTER_IN_TEXT = re.compile(r"(?:Answers?|Choices?|Options?|Statements?|Items?)\s+[A-E]\b|\b(?:in|of|for|to|by)\s+[A-E]\b(?![\w'])|\b[A-E],\s+(?:and\s+)?[A-E]\b|\b[A-E]\s+(?:and|or)\s+[A-E]\b|\([A-E]\)")


def movable(q, shared):
    if LETTER_IN_TEXT.search(q["expl_src"]) or LETTER_IN_TEXT.search(q["q"]):
        return False
    texts = [o[0] for o in q["opts"]]
    if any(REF.search(t) or REF_LOWER.search(t) for t in texts):
        return False
    if all(re.fullmatch(r"[~\u223c<>=\s\d.,%/\u2013\u2212-]+(mg|mm|hg|cm|g|/[\w,]+)?[/\w ,]*", t) or re.search(r"\d", t) and len(t) < 14 for t in texts):
        return False
    return tuple(texts) not in shared


rng_ = __import__("random").Random(20260929)
for ch in out:
    seen = collections.Counter(tuple(o[0] for o in q["opts"]) for q in ch["questions"])
    shared = {k for k, v in seen.items() if v >= 3}
    qs = ch["questions"]
    for _ in range(60):
        cnt = collections.Counter(q["c"] for q in qs)
        span = max(len(q["opts"]) for q in qs)
        hi = max(range(span), key=lambda p: cnt.get(p, 0))
        cand = []
        for lo in sorted(range(span), key=lambda p: cnt.get(p, 0)):
            if cnt.get(hi, 0) - cnt.get(lo, 0) <= 1:
                break
            cand = [q for q in qs if q["c"] == hi and lo < len(q["opts"]) and movable(q, shared)]
            if cand:
                break
        if not cand:
            break
        q = rng_.choice(cand)
        key = q["opts"].pop(q["c"]); q["opts"].insert(lo, key); q["c"] = lo
# a question whose text points at lettered choices must still have the book's letters
for ch in out:
    for q in ch["questions"]:
        if LETTER_IN_TEXT.search(q["expl_src"]) or LETTER_IN_TEXT.search(q["q"]) or any(REF.search(o[0]) for o in q["opts"]):
            assert q["c"] == q["c0"], "question %s cites letters but its choices were reordered" % q["num"]
        del q["c0"], q["expl_src"]
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
tot = sum(len(c["questions"]) for c in out)
print("wrote", os.path.relpath(OUT, ROOT), "-", len(out), "chapters,", tot, "questions,", nimg, "figures")
for c in out:
    print("  %2d %-28s %2d questions" % (c["n"], c["title"], len(c["questions"])))
