#!/usr/bin/env python3
"""INDEPENDENT audit that each question's guide link lands on the CONCEPT.

Why this exists: build_guide_links.py picks a passage by word overlap, and
check_guide_links.py can only prove the passage CONTAINS the answer's words. Neither
proves the passage EXPLAINS the concept that makes the answer right. This tool adds a
second, independent reader and a hard rule (Jaxon, 2026-09-28: "make sure they are
linked to the correct concepts ... make it a rule going forward for all questions").

The protocol
  1. `export`  writes judge batches: for each link needing audit, the question, the
     correct answer, its vetted explanation, and up to 6 candidate paragraphs from
     the linked guide section (the current target is always among them).
  2. A judge (a separate model reading ONLY that text) answers per item:
        PASS     a paragraph STATES the fact that makes the answer correct
        PARTIAL  right topic, but the fact itself is not stated
        FAIL     no paragraph is about this concept
     and for PASS must give the paragraph number and a VERBATIM quote of the
     sentence that states it. The quote is machine-checked against the paragraph
     text at `import`, so a PASS cannot be given on impression.
  3. `import`  writes tools/guide_link_audit.json {question key: record}. A PASS
     also re-points the link at the exact paragraph the judge quoted, so
     section-level links become highlighted passages. PARTIAL/FAIL are listed for
     repair (write the fact into the guide: tools/guide_additions/) -- never left.
  4. `authored` records the lines written FOR a question as AUTHORED (correct by
     construction; a control sample of them is judged like everything else).
  5. check_guide_links.py --strict fails unless EVERY link has a current PASS or
     AUTHORED record whose target text still exists in the guide.

Usage:
  audit_guide_links.py status
  audit_guide_links.py authored
  audit_guide_links.py export --set section|closest|extras|passage|added|new --out DIR
                              [--sample 0.2] [--seed N] [--size 50]
  audit_guide_links.py import DIR
  audit_guide_links.py export-pins --pins FILE --out DIR [--size 50]
      FILE = {"<exam folder>": {"<question key>": "<guide heading id>"}}. For questions whose best
      passage the word-overlap matcher misses, name the guide subsection that states the fact;
      the judges then see THAT subsection's paragraphs. A PASS re-points the link there at `import`.
"""
import glob
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_guide_links as B

ROOT = B._REPO
AUDIT = os.path.join(ROOT, "tools", "guide_link_audit.json")
PARAS = 6            # candidate paragraphs shown to a judge
PARA_WORDS = 110     # each truncated to this many words


def norm(t):
    return re.sub(r"\s+", " ", t).strip()


def pkey(text):
    return B.fnv(norm(text))


def folders():
    for d in sorted(os.listdir(ROOT)):
        if os.path.exists(os.path.join(ROOT, d, "guide-links.json")) and d.startswith(
                ("Clinical", "Microbiology", "Pharmacology I", "Physical Diagnosis 2", "Principles", "Interpretation")):
            yield d


def akey(folder, k):
    """Audit records are per exam folder: the same question text can sit in two exams."""
    return "%s|%s" % (os.path.basename(folder), k)


def load_audit():
    return json.load(open(AUDIT, encoding="utf-8")) if os.path.exists(AUDIT) else {}


def save_audit(a):
    json.dump(a, open(AUDIT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"), sort_keys=True)


class Folder:
    def __init__(self, d):
        self.d = d
        self.path = os.path.join(ROOT, d)
        self.data = json.load(open(os.path.join(self.path, "guide-links.json"), encoding="utf-8"))
        self.guides = {}
        self.questions = {}
        for f in sorted(glob.glob(os.path.join(self.path, "*.html"))):
            for q in B.load_questions(f) or []:
                self.questions.setdefault(B.qkey(q), q)

    def guide(self, name):
        if name not in self.guides:
            secs = {sc["id"]: sc for sc in B.parse_guide(os.path.join(self.path, name))}
            html = open(os.path.join(self.path, name), encoding="utf-8").read()
            self.guides[name] = (secs, html)
        return self.guides[name]

    def blocks(self, guide, anchor):
        """Paragraph texts of the section (or added line) the link points at."""
        secs, html = self.guide(guide)
        if anchor.startswith("ga-"):
            m = re.search(r'<li id="%s">(.*?)</li>' % re.escape(anchor), html, re.S)
            return [norm(re.sub(r"<[^>]+>", " ", B.html.unescape(m.group(1))))] if m else []
        sc = secs.get(anchor)
        return B.blocks_of(sc) if sc else []


def candidates(q, blocks, snippet):
    """Top paragraphs for this question; the linked paragraph is always included."""
    ans = q["opts"][q["c"]]
    w = B.toks(ans[0]) * 3 + B.toks(q["q"]) + B.toks(ans[1])
    idf_like = {}
    for b in blocks:
        for t in set(B.toks(b)):
            idf_like[t] = idf_like.get(t, 0) + 1
    n = max(1, len(blocks))
    import math
    scored = []
    for i, b in enumerate(blocks):
        bt = set(B.toks(b))
        s = sum(math.log((n + 1) / (idf_like[t] + 0.5)) for t in set(w) if t in bt) / (len(bt) ** 0.25 or 1)
        scored.append((s, i))
    scored.sort(reverse=True)
    pick = [i for _, i in scored[:PARAS]]
    if snippet:
        cur = [i for i, b in enumerate(blocks) if norm(snippet)[:60] in norm(b)]
        for i in cur[:1]:
            if i not in pick:
                pick = pick[:-1] + [i]
    pick.sort()
    out = []
    for i in pick:
        words = norm(blocks[i]).split()
        out.append({"n": len(out) + 1, "text": " ".join(words[:PARA_WORDS]) + (" ..." if len(words) > PARA_WORDS else ""), "_full": norm(blocks[i])})
    return out


def link_kind(F, k, v, first_members):
    if v[1].startswith("ga-"):
        return "added" if k in first_members else "extras"
    if len(v) > 4:
        return "closest"
    return "passage" if v[3] else "section"


def first_members_of(d):
    p = os.path.join(ROOT, "tools", "guide_additions", re.sub(r"[^a-z0-9]+", "-", d.lower()).strip("-") + ".json")
    out = set()
    if os.path.exists(p):
        for it in json.load(open(p, encoding="utf-8"))["items"]:
            if it.get("html") not in (None, "SKIP") and it["keys"]:
                out.add(it["keys"][0])
    return out


def record_current(F, k, v, rec):
    """Is the audit record still valid for the link as built today?"""
    if not rec or rec["v"] not in ("PASS", "AUTHORED"):
        return False
    guide = F.data["g"][v[0]]
    if rec.get("g") != guide or rec.get("a") != v[1]:
        return False
    if rec["v"] == "AUTHORED":
        blocks = F.blocks(guide, v[1])
        return bool(blocks) and pkey(blocks[0]) == rec["p"]
    if rec.get("s") != v[3]:
        return False
    return any(pkey(b) == rec["p"] for b in F.blocks(guide, v[1]))


def cmd_authored():
    audit = load_audit()
    n = 0
    for d in folders():
        F = Folder(d)
        fm = first_members_of(d)
        for k, v in F.data["l"].items():
            if not v[1].startswith("ga-"):
                continue
            if k not in fm:                      # a merged EXTRA member: a judge must confirm the shared line states ITS fact
                if audit.get(akey(d, k), {}).get("v") == "AUTHORED":
                    del audit[akey(d, k)]
                continue
            guide = F.data["g"][v[0]]
            blocks = F.blocks(guide, v[1])
            if blocks:
                audit[akey(d, k)] = {"v": "AUTHORED", "g": guide, "a": v[1], "p": pkey(blocks[0])}
                n += 1
    save_audit(audit)
    print("recorded %d authored lines" % n)


def cmd_status():
    audit = load_audit()
    tot = {}
    for d in folders():
        F = Folder(d)
        fm = first_members_of(d)
        for k, v in F.data["l"].items():
            kind = link_kind(F, k, v, fm)
            ok = record_current(F, k, v, audit.get(akey(d, k)))
            t = tot.setdefault(kind, [0, 0])
            t[0] += 1
            t[1] += ok
    for kind, (n, ok) in sorted(tot.items()):
        print("%-9s %5d links, %5d audited (%d%%)" % (kind, n, ok, round(100 * ok / max(1, n))))
    print("ALL       %5d links, %5d audited" % (sum(t[0] for t in tot.values()), sum(t[1] for t in tot.values())))


def cmd_export(args):
    which = args[args.index("--set") + 1]
    out = args[args.index("--out") + 1]
    frac = float(args[args.index("--sample") + 1]) if "--sample" in args else 1.0
    seed = int(args[args.index("--seed") + 1]) if "--seed" in args else 1
    size = int(args[args.index("--size") + 1]) if "--size" in args else 50
    os.makedirs(out, exist_ok=True)
    audit = load_audit()
    rnd = random.Random(seed)
    items, manifest = [], {}
    for d in folders():
        F = Folder(d)
        fm = first_members_of(d)
        for k, v in F.data["l"].items():
            kind = link_kind(F, k, v, fm)
            if which == "new":
                want = not record_current(F, k, v, audit.get(akey(d, k)))
            else:
                fresh = "--include-audited" in args or not record_current(F, k, v, audit.get(akey(d, k)))
                want = kind == which and fresh and (frac >= 1 or rnd.random() < frac)
            if not want:
                continue
            q = F.questions.get(k)
            if not q:
                continue
            guide = F.data["g"][v[0]]
            cands = candidates(q, F.blocks(guide, v[1]), v[3])
            if not cands:
                continue
            ans = q["opts"][q["c"]]
            items.append({"id": k, "question": q["q"], "answer": ans[0], "explanation": ans[1], "paragraphs": [{"n": c["n"], "text": c["text"]} for c in cands]})
            manifest[k] = {"folder": d, "guide": guide, "anchor": v[1], "kind": kind, "paras": [c["_full"] for c in cands]}
    rnd.shuffle(items)
    for i in range(0, len(items), size):
        json.dump(items[i:i + size], open(os.path.join(out, "judge-%03d.json" % (i // size + 1)), "w"), ensure_ascii=False, indent=1)
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w"), ensure_ascii=False)
    print("exported %d items in %d batches -> %s" % (len(items), (len(items) + size - 1) // size, out))


def cmd_export_pins(args):
    pins = json.load(open(args[args.index("--pins") + 1], encoding="utf-8"))
    out = args[args.index("--out") + 1]
    size = int(args[args.index("--size") + 1]) if "--size" in args else 50
    os.makedirs(out, exist_ok=True)
    items, manifest = [], {}
    for d, m in pins.items():
        F = Folder(d)
        for k, anchor in m.items():
            q = F.questions.get(k)
            v = F.data["l"].get(k)
            if not q or not v:
                print("skip (unknown question):", d, k)
                continue
            guide = F.data["g"][v[0]]
            cands = candidates(q, F.blocks(guide, anchor), "")
            if not cands:
                print("skip (no paragraphs under %s):" % anchor, k)
                continue
            ans = q["opts"][q["c"]]
            items.append({"id": k, "question": q["q"], "answer": ans[0], "explanation": ans[1], "paragraphs": [{"n": c["n"], "text": c["text"]} for c in cands]})
            manifest[k] = {"folder": d, "guide": guide, "anchor": anchor, "kind": "pinned", "paras": [c["_full"] for c in cands]}
    for i in range(0, len(items), size):
        json.dump(items[i:i + size], open(os.path.join(out, "judge-%03d.json" % (i // size + 1)), "w"), ensure_ascii=False, indent=1)
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w"), ensure_ascii=False)
    print("exported %d pinned items in %d batches -> %s" % (len(items), (len(items) + size - 1) // size, out))


def cmd_import(args):
    dirp = args[0]
    manifest = json.load(open(os.path.join(dirp, "manifest.json"), encoding="utf-8"))
    audit = load_audit()
    res = {"PASS": 0, "PARTIAL": 0, "FAIL": 0, "BADQUOTE": 0, "MISSING": 0}
    repair = []
    seen = set()
    for f in sorted(glob.glob(os.path.join(dirp, "verdict-*.json"))):
        for e in json.load(open(f, encoding="utf-8")):
            k = e.get("id")
            m = manifest.get(k)
            if not m:
                continue
            seen.add(k)
            v = e.get("verdict")
            if v == "PASS":
                n = e.get("para")
                quote = norm(e.get("quote", ""))
                paras = m["paras"]
                def enough(par):
                    # a short paragraph may be quoted whole; otherwise 5+ words
                    return len(quote.split()) >= min(5, len(par.split()))
                ok = isinstance(n, int) and 1 <= n <= len(paras) and enough(paras[n - 1]) and \
                    quote.lower().replace("’", "'") in paras[n - 1].lower().replace("’", "'")
                if not ok:
                    # allow the quote to sit in ANY candidate paragraph
                    hit = [i for i, p in enumerate(paras) if enough(p) and quote.lower().replace("’", "'") in p.lower().replace("’", "'")]
                    if hit:
                        n, ok = hit[0] + 1, True
                if not ok:
                    res["BADQUOTE"] += 1
                    repair.append((k, m, "PASS with an unverifiable quote"))
                    continue
                para = paras[n - 1]
                audit[akey(m["folder"], k)] = {"v": "PASS", "g": m["guide"], "a": m["anchor"], "s": B.snippet(para), "p": pkey(para), "q": quote[:200]}
                res["PASS"] += 1
            elif v in ("PARTIAL", "FAIL"):
                res[v] += 1
                repair.append((k, m, v))
                audit.pop(akey(m["folder"], k), None)
    res["MISSING"] = len(set(manifest) - seen)
    save_audit(audit)
    json.dump([{"id": k, "folder": m["folder"], "kind": m["kind"], "why": w} for k, m, w in repair],
              open(os.path.join(dirp, "repair.json"), "w"), indent=1)
    print("imported:", res, "| need repair:", len(repair))


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    {"status": lambda: cmd_status(), "authored": lambda: cmd_authored(),
     "export": lambda: cmd_export(a), "export-pins": lambda: cmd_export_pins(a), "import": lambda: cmd_import(a[1:])}[a[0]]()


if __name__ == "__main__":
    main()
