#!/usr/bin/env python3
"""Flag question SOURCES whose text still cites the course -- run before any render.

WHY THIS EXISTS. On 2026-09-20 I re-rendered Pharmacology Lecture 2
(dermatology medications) to pick up a one-word stem fix. The render replaced
1,570 lines with 104 and reintroduced course references into a shipped quiz
that had been hand-cleaned during the 2026-08-31 self-contained pass.

The cause is a divergence nothing was watching: the SHIPPED HTML was cleaned by
hand, but what it is generated FROM was not. check_self_contained reads the
rendered pages, so it reports clean right up until someone regenerates one.

WHAT IT READS -- every layer a renderer can read from:
  pools      tools/*pool*.py, tools/*_vig*.py (vignette banks have no "pool" in
             the name; 370 citations once hid there) and tools/*_gtd_bank.py
             (the Guess-that-Disease banks: cond/why/wrong, not opts).
  derived    tools/*_sets.json, tools/cms_l*_set*.json and <Exam>/master-exams*.json.
             Renderers read these DIRECTLY, so a clean pool does not protect a
             page: tools/cp_l3_sets.json still carried 8 "Professor Rappa" stems
             after the pools were cleaned, and render_cp_l3.py alone would have
             shipped them.
  Stems, option texts and explanations; `io` and `cite` are provenance.

WHAT COUNTS -- the site's own detectors, so this and check_self_contained cannot
disagree: _selfcontain_rx.RX plus _lecturers (hard), REVIEW_RX pronoun +
teaching verb (counted, listed with --review, never failing). This file used to
carry a private, narrower regex with no "Professor <Name>" pattern; it reported
"0 reference(s) across 0 pool(s)" while 73 sat in the pools (37 source phrases,
30 bare lecturer surnames, 6 in a Guess-that-Disease bank it never globbed;
measured 2026-09-22), and that "0 pool(s)" was pools-WITH-hits -- it never
printed what it had read. That private regex did catch a few shapes the site
detector then lacked ("this slide", "this course", "the material notes"); RX
was widened to cover them the same day (19 pool/sets strings), which with the
cross-lecture references it also gained ("from Lecture 2", "the same slide")
raised the pool count to 156.

    python3 tools/check_pool_cites.py             # counts per source + denominator
    python3 tools/check_pool_cites.py --detail    # with the offending text
    python3 tools/check_pool_cites.py --review    # also list pronoun candidates
    python3 tools/check_pool_cites.py --json out.json

Exit 1 on any hard reference, and on any module that fails to import -- a pool
that cannot be read has not been checked.
"""
import ast, glob, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)                 # pools import one another by bare name
from _lecturers import citation_hits

# Importing a module RUNS it. These are tooling, not banks: some download
# images, shell out to OCR, or write files at import time.
SKIP = re.compile(r"(partition|lengthfix|check_|render_|build_|dump_|apply_|_rx)")


def candidates():
    c = set()
    for pat in ("*pool*.py", "*_vig*.py", "*_gtd_bank.py"):
        c |= set(glob.glob(os.path.join(HERE, pat)))
    return sorted(c)


def string_lines(path):
    """{string literal: first line} from the module's source, to locate a hit."""
    out = {}
    try:
        tree = ast.parse(open(path, encoding="utf-8").read())
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.setdefault(node.value, node.lineno)
    return out


def q_fields(q):
    """[(field, text)] for a pool/sets question, or None for other dicts."""
    if isinstance(q.get("opts"), list) and isinstance(q.get("q"), str):
        out = [("stem", q["q"])]
        for j, o in enumerate(q["opts"]):
            if isinstance(o, (list, tuple)) and o:
                out.append(("option %d" % j, o[0]))
                if len(o) > 1:
                    out.append(("explanation %d" % j, o[1]))
            elif isinstance(o, str):
                out.append(("option %d" % j, o))
        return out
    if isinstance(q.get("cond"), str) and isinstance(q.get("wrong"), list):   # Guess that Disease
        out = [("key", q["cond"]), ("why", q.get("why", ""))]
        for j, w in enumerate(q["wrong"]):
            if isinstance(w, (list, tuple)) and w:
                out.append(("wrong %d" % j, w[0]))
                if len(w) > 1:
                    out.append(("wrong %d explanation" % j, w[1]))
        return out
    return None


scan_text = citation_hits          # one definition, shared with check_self_contained


def scan_pools():
    res = {"candidates": 0, "skipped_tooling": 0, "imported": 0, "import_failures": [],
           "banks": 0, "no_question_list": [], "questions": 0, "reexported": 0, "strings": 0,
           "hits": [], "review": []}
    cands = candidates()
    res["candidates"] = len(cands)
    loaded = []
    for f in cands:
        if SKIP.search(os.path.basename(f)):
            res["skipped_tooling"] += 1
            continue
        mod = os.path.basename(f)[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod, f)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        except BaseException as e:            # SystemExit too: a pool must not exit
            res["import_failures"].append({"module": mod, "error": "%s: %s" % (type(e).__name__, str(e)[:120])})
            continue
        res["imported"] += 1
        qs, seen = [], set()
        for attr in sorted(dir(m)):
            P = getattr(m, attr)
            if not (isinstance(P, list) and P and all(isinstance(x, dict) for x in P)):
                continue
            for i, q in enumerate(P):
                if id(q) in seen:
                    continue
                fields = q_fields(q)
                if fields is None:
                    break
                seen.add(id(q))
                qs.append(("%s[%d]" % (attr, i), q, fields))
        if not qs:
            res["no_question_list"].append(mod)
            continue
        loaded.append((f, mod, qs))

    # A module that imports another pool's list re-exposes the same questions.
    # Attribute each question to the file whose SOURCE holds its stem as a
    # literal, and drop the re-exports, so one citation is one entry.
    lits = {f: string_lines(f) for f, _, _ in loaded}
    owner = {}
    for f, _, qs in loaded:
        for loc, q, fields in qs:
            if fields[0][1] in lits[f]:
                owner.setdefault(fields[0][1], f)
    for f, mod, qs in loaded:
        res["banks"] += 1
        rel = os.path.relpath(f, ROOT)
        for loc, q, fields in qs:
            stem = fields[0][1]
            if stem not in lits[f] and stem in owner:
                res["reexported"] += 1
                continue                           # counted in the module that defines it
            res["questions"] += 1
            for field, text in fields:
                res["strings"] += 1
                for sev, det, frag in scan_text(text):
                    rec = {"file": rel, "index": loc, "line": lits[f].get(text), "field": field,
                           "text": text, "match": frag, "detector": det, "stem": stem[:160]}
                    (res["hits"] if sev == "hard" else res["review"]).append(rec)
    return res


def derived_files():
    fs = set(glob.glob(os.path.join(HERE, "*_sets.json")))
    fs |= set(glob.glob(os.path.join(HERE, "cms_l*_set*.json")))
    fs |= set(glob.glob(os.path.join(ROOT, "*", "master-exams*.json")))
    return sorted(fs)


def scan_derived():
    res = {"files": 0, "unreadable": [], "questions": 0, "strings": 0, "hits": [], "review": []}
    for f in derived_files():
        rel = os.path.relpath(f, ROOT)
        try:
            d = json.load(open(f, encoding="utf-8"))
        except ValueError as e:
            res["unreadable"].append({"file": rel, "error": str(e)[:100]})
            continue
        groups = d.items() if isinstance(d, dict) else [("", d)]
        n = 0
        for key, qs in groups:
            if not isinstance(qs, list):
                continue
            for i, q in enumerate(qs):
                fields = q_fields(q) if isinstance(q, dict) else None
                if fields is None:
                    continue
                n += 1
                for field, text in fields:
                    res["strings"] += 1
                    for sev, det, frag in scan_text(text):
                        rec = {"file": rel, "index": "%s[%d]" % (key, i) if key else "[%d]" % i,
                               "field": field, "text": text, "match": frag, "detector": det,
                               "stem": fields[0][1][:160]}
                        (res["hits"] if sev == "hard" else res["review"]).append(rec)
        if n == 0:
            res["unreadable"].append({"file": rel, "error": "no questions in the expected shape"})
            continue
        res["files"] += 1
        res["questions"] += n
    return res


def report(title, hits, detail, review_hits, show_review):
    by = {}
    for h in hits:
        by.setdefault(h["file"], []).append(h)
    if by:
        print(title)
    for f in sorted(by, key=lambda k: (-len(by[k]), k)):
        print("%5d  %s" % (len(by[f]), f))
        if detail:
            for h in by[f]:
                where = h["index"] + (" line %d" % h["line"] if h.get("line") else "")
                print("         %-22s %-16s %-17s %s" % (where, h["field"], h["detector"], h["text"][:90]))
    if show_review and review_hits:
        print(title.replace("HARD", "PRONOUN CANDIDATES (human review)"))
        for h in review_hits:
            print("         %-28s %-24s \"%s\"  %s" % (h["file"], h["index"], h["match"], h["text"][:70]))


def main(argv):
    detail = "--detail" in argv
    review = "--review" in argv
    json_out = argv[argv.index("--json") + 1] if "--json" in argv else None

    P = scan_pools()
    D = scan_derived()
    report("\nHARD REFERENCES IN POOLS", P["hits"], detail, P["review"], review)
    report("\nHARD REFERENCES IN DERIVED SETS (renderers read these directly)",
           D["hits"], detail, D["review"], review)
    for fl in P["import_failures"]:
        print("IMPORT FAILED -- NOT CHECKED: %s  %s" % (fl["module"], fl["error"]))
    for u in D["unreadable"]:
        print("UNREADABLE -- NOT CHECKED: %s  %s" % (u["file"], u["error"]))

    print("\npools: %d candidate module(s), %d skipped as tooling, %d imported, %d import failure(s)"
          % (P["candidates"], P["skipped_tooling"], P["imported"], len(P["import_failures"])))
    print("       %d with a question list: %d question(s) (+%d re-exported from another pool, "
          "counted once), %d string(s)%s"
          % (P["banks"], P["questions"], P["reexported"], P["strings"],
             ("; no question list in: " + ", ".join(P["no_question_list"])) if P["no_question_list"] else ""))
    print("derived sets: %d file(s), %d question(s), %d string(s), %d unreadable"
          % (D["files"], D["questions"], D["strings"], len(D["unreadable"])))
    pf = len({h["file"] for h in P["hits"]})
    df = len({h["file"] for h in D["hits"]})
    print("HARD references: %d in %d pool(s), %d in %d derived set file(s)"
          % (len(P["hits"]), pf, len(D["hits"]), df))
    print("pronoun candidates for review: %d in pools, %d in derived sets%s"
          % (len(P["review"]), len(D["review"]), "" if review else " (list with --review)"))
    if P["hits"] or D["hits"]:
        print("A non-zero count means the shipped page is cleaner than its source: clean the "
              "source before re-rendering, or the render puts the citation back.")
    if json_out:
        with open(json_out, "w", encoding="utf-8") as fh:
            json.dump({"pools": P, "derived": D}, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % json_out)
    bad = P["hits"] or D["hits"] or P["import_failures"] or D["unreadable"]
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
