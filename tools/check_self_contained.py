#!/usr/bin/env python3
"""Fail any question that cites its own source.

A question has to stand on its own: a student reading it should never need to
know which lecture, deck, slide, syllabus or professor it came from.  Deleting
the attribution is the fix — relabelling it "the material" was tried and
rejected.  Deletion strands verbs and genitives, so rewrite the sentence rather
than snipping the phrase out.

  python3 tools/check_self_contained.py                   # every live folder
  python3 tools/check_self_contained.py "Some Exam 2"     # one folder (or file)
  python3 tools/check_self_contained.py --review          # also LIST the pronoun
                                                          # candidates to eyeball
  python3 tools/check_self_contained.py --json hits.json  # every hit, for fixing
  python3 tools/check_self_contained.py --include-frozen  # Semester 1 as well

WHAT IT READS. Every .html under the chosen folders, and in each one:
  - the page's `const QUESTIONS = [...]` quiz bank, and
  - any `var TEST_YOURSELF = {...}` self-test bank (study guides, the Micro
    review page) -- these used to be skipped by FILENAME ("guide", "cram"...),
    so the self-tests on eleven Semester 2 pages were never looked at: 52
    citations on ten of them by the detector of 2026-09-22, 59 once RX was
    widened the same day (see _selfcontain_rx.py).
  Stems, option texts and explanations are checked; `io` and `cite` are
  provenance metadata and deliberately are not.

WHAT COUNTS.
  HARD    _selfcontain_rx.RX ("the lecture", "the deck", "Professor X"...) and
          _lecturers ("Why did Beck ask...", "Webster tied...", "Dr. Fair").
          Any hard hit fails the run.
  REVIEW  _selfcontain_rx.REVIEW_RX, a pronoun + teaching verb ("she said").
          Human-judged, because patients are "she" too ("she prefers"). The
          COUNT is always printed; --review lists them.

WHAT IT CANNOT READ IS COUNTED, NEVER SKIPPED. The first version cut the bank
out with a non-greedy regex and swallowed the JSON error, so any array holding
"];" inside a string silently left the scan (16 Semester 1 files did). Banks are
now decoded properly; a bank that still cannot be parsed, or an entry whose
shape is not recognised, is reported and fails the run for a live folder.

SCOPE. Semester 1 is frozen (Jaxon, 2026-08-27) and is skipped using the FROZEN
list in check_exam_standard.py, which is checked against semesters.js. This file
used to keep its own list, which had drifted: it skipped the Semester 2 course
Interpretation of Medical Literature and scanned four Semester 1 folders.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _lecturers import citation_hits, unclassified_calendar_names
from check_exam_standard import is_frozen

# Top-level folders that are not course content.
NOT_CONTENT = ("tools", "group-quizzes", "icons", "audio", "rpg", "node_modules")

BANK_DECL = re.compile(r"\b(?:const|let|var)\s+(QUESTIONS|TEST_YOURSELF)\s*=\s*")
# Other question-bank shapes that exist on Semester 1 pages. They are not read;
# finding one in a live folder is reported rather than passed over.
OTHER_DECL = re.compile(r"\b(?:const|let|var)\s+(ITEMS|questions|DECK|BANK|Q)\s*=\s*\[")


# --------------------------------------------------------------------------
# Reading JavaScript literals. The quiz banks are JSON, but the TEST_YOURSELF
# banks are JS object literals: unquoted keys, single-quoted strings, trailing
# commas, and <!--MARKER--> lines (an HTML-like comment, legal inside a classic
# script). Validated 2026-09-22: equal to json.loads on all 525 QUESTIONS arrays
# and to node's own eval on all 25 TEST_YOURSELF banks.
# --------------------------------------------------------------------------
class JSLiteralError(ValueError):
    pass


_NUM = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?")
_IDENT = re.compile(r"[A-Za-z_$][A-Za-z0-9_$]*")
_ESC = {"n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f", "v": "\v", "0": "\0"}


def parse_js_literal(text, pos=0):
    """-> (value, end). Raises JSLiteralError on anything that is not a plain
    literal: a variable, a function call, string concatenation, ${...}."""
    n = len(text)

    def skip(i):
        while i < n:
            ch = text[i]
            if ch in " \t\r\n\ufeff\u00a0":
                i += 1
            elif text.startswith("//", i) or text.startswith("<!--", i):
                j = text.find("\n", i)
                i = n if j < 0 else j + 1
            elif text.startswith("/*", i):
                j = text.find("*/", i + 2)
                if j < 0:
                    raise JSLiteralError("unterminated comment at %d" % i)
                i = j + 2
            elif text.startswith("-->", i):
                k = i - 1                      # "-->" opens a comment only at a line start
                while k >= 0 and text[k] in " \t":
                    k -= 1
                if k >= 0 and text[k] not in "\n\r":
                    return i
                j = text.find("\n", i)
                i = n if j < 0 else j + 1
            else:
                return i
        return i

    def string(i):
        q = text[i]
        i += 1
        out = []
        while i < n:
            ch = text[i]
            if ch == "\\":
                nx = text[i + 1] if i + 1 < n else ""
                if nx in _ESC:
                    out.append(_ESC[nx]); i += 2
                elif nx == "u":
                    if text[i + 2:i + 3] == "{":
                        j = text.index("}", i)
                        out.append(chr(int(text[i + 3:j], 16))); i = j + 1
                    else:
                        out.append(chr(int(text[i + 2:i + 6], 16))); i += 6
                elif nx == "x":
                    out.append(chr(int(text[i + 2:i + 4], 16))); i += 4
                elif nx in "\r\n":
                    i += 2
                    if nx == "\r" and text[i:i + 1] == "\n":
                        i += 1
                else:
                    out.append(nx); i += 2
            elif ch == q:
                return "".join(out), i + 1
            elif q == "`" and text.startswith("${", i):
                raise JSLiteralError("template substitution at %d" % i)
            elif ch in "\r\n" and q != "`":
                raise JSLiteralError("newline in string at %d" % i)
            else:
                out.append(ch); i += 1
        raise JSLiteralError("unterminated string at %d" % i)

    def value(i):
        i = skip(i)
        if i >= n:
            raise JSLiteralError("unexpected end of input")
        ch = text[i]
        if ch == "{":
            obj = {}
            i += 1
            while True:
                i = skip(i)
                if text[i] == "}":
                    return obj, i + 1
                if text[i] in "\"'":
                    key, i = string(i)
                else:
                    m = _IDENT.match(text, i) or _NUM.match(text, i)
                    if not m:
                        raise JSLiteralError("bad key at %d: %r" % (i, text[i:i + 20]))
                    key, i = m.group(0), m.end()
                i = skip(i)
                if text[i] != ":":
                    raise JSLiteralError("expected ':' at %d: %r" % (i, text[i:i + 20]))
                obj[key], i = value(i + 1)
                i = skip(i)
                if text[i] == ",":
                    i += 1
                elif text[i] != "}":
                    raise JSLiteralError("expected ',' or '}' at %d: %r" % (i, text[i:i + 20]))
        if ch == "[":
            arr = []
            i += 1
            while True:
                i = skip(i)
                if text[i] == "]":
                    return arr, i + 1
                v, i = value(i)
                arr.append(v)
                i = skip(i)
                if text[i] == ",":
                    i += 1
                elif text[i] != "]":
                    raise JSLiteralError("expected ',' or ']' at %d: %r" % (i, text[i:i + 20]))
        if ch in "\"'`":
            s, j = string(i)
            k = skip(j)
            if k < n and text[k] == "+":
                raise JSLiteralError("string concatenation at %d" % k)
            return s, j
        m = _NUM.match(text, i)
        if m:
            s = m.group(0)
            return (float(s) if any(c in s for c in ".eE") else int(s)), m.end()
        m = _IDENT.match(text, i)
        if m and m.group(0) in ("true", "false", "null", "undefined"):
            return {"true": True, "false": False}.get(m.group(0)), m.end()
        raise JSLiteralError("not a literal at %d: %r" % (i, text[i:i + 30]))

    try:
        return value(pos)
    except IndexError:
        raise JSLiteralError("unexpected end of input")


def read_literal(text, pos):
    """JSON first (fast, C), the JS reader for what JSON cannot take."""
    try:
        return json.JSONDecoder().raw_decode(text, pos)[0]
    except ValueError:
        return parse_js_literal(text, pos)[0]


# --------------------------------------------------------------------------
# The text a student reads, per question shape.
# --------------------------------------------------------------------------
# Keys that hold provenance or bookkeeping, not text a student reads as part of
# the question. `io` is the verbatim syllabus objective and `cite` the slide
# provenance; both are meant to name their source.
METADATA = {"io", "cite", "topic", "slot", "lead", "qid", "deck", "img", "slide", "alt",
            "chart", "kfe", "src", "id", "c", "a", "answer", "type", "tags"}
OPTION_KEYS = ("opts", "o", "choices", "options")


def question_fields(q):
    """[(field, text)] for one question, or None if its shape is unknown.

    Shapes seen: {q, opts:[[text, explanation], ...]} (every Semester 2 quiz);
    {q, choices, answer, correct, why} (legacy); TEST_YOURSELF entries
    {q, o|choices:[text...], a|correct, why|explain|expl}. Every OTHER string
    key is read too, under its own name, so a new explanation key cannot slip
    past -- the first version of this function knew why/explain and missed
    "expl", which hid 12 citations in three guides' self-tests."""
    if not isinstance(q, dict) or not isinstance(q.get("q"), str):
        return None
    out = [("stem", q["q"])]
    key = next((k for k in OPTION_KEYS if k in q), None)
    opts = q.get(key)
    if not isinstance(opts, list):
        return None
    for j, o in enumerate(opts):
        if isinstance(o, str):
            out.append(("option %d" % j, o))
        elif isinstance(o, list) and o and all(isinstance(x, str) for x in o):
            out.append(("option %d" % j, o[0]))
            if len(o) > 1:
                out.append(("explanation %d" % j, o[1]))
        elif isinstance(o, dict) and isinstance(o.get("t", o.get("text")), str):
            out.append(("option %d" % j, o.get("t", o.get("text"))))
        else:
            return None
    for k, v in q.items():
        if k not in METADATA and k != "q" and k != key and isinstance(v, str):
            out.append((k, v))
    return out


def page_banks(path):
    """-> (banks, problems). banks: [(bank name, [(location, question), ...])];
    problems: [str] -- anything in the page that holds questions and could not
    be read."""
    text = open(path, encoding="utf-8").read()
    banks, problems = [], []
    for m in BANK_DECL.finditer(text):
        name = m.group(1)
        try:
            val = read_literal(text, m.end())
        except (JSLiteralError, ValueError) as e:
            problems.append("%s: cannot parse (%s)" % (name, str(e)[:70]))
            continue
        if name == "QUESTIONS":
            if not isinstance(val, list):
                problems.append("QUESTIONS is not an array")
                continue
            banks.append(("QUESTIONS", [("#%d" % i, q) for i, q in enumerate(val)]))
        else:
            if not isinstance(val, dict):
                problems.append("TEST_YOURSELF is not an object")
                continue
            for sec, qs in val.items():
                if not isinstance(qs, list):
                    problems.append("TEST_YOURSELF.%s is not an array" % sec)
                    continue
                banks.append(("TEST_YOURSELF.%s" % sec,
                              [("%s[%d]" % (sec, i), q) for i, q in enumerate(qs)]))
    for m in OTHER_DECL.finditer(text):
        problems.append("%s: a question bank shape this checker does not read" % m.group(1))
    return banks, problems


scan_text = citation_hits          # one definition, shared with check_pool_cites


def resolve_roots(args, include_frozen=False):
    """Folder/file arguments, relative to cwd or to the repo root."""
    if args:
        out = []
        for a in args:
            p = a if os.path.exists(a) else os.path.join(ROOT, a)
            if not os.path.exists(p):
                sys.exit("no such folder or file: %s" % a)
            out.append(os.path.abspath(p))
        return out, []
    roots, frozen = [], []
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p) or d.startswith(".") or d in NOT_CONTENT:
            continue
        if is_frozen(d) and not include_frozen:
            frozen.append(d)
            continue
        roots.append(p)
    return roots, frozen


def html_files(roots):
    for r in roots:
        if os.path.isfile(r):
            yield r
        else:
            yield from sorted(glob.glob(os.path.join(r, "**", "*.html"), recursive=True))


def scan(roots, review=False, quiet=False):
    """Scan and print. Returns the result dict (also what --json writes)."""
    res = {"files_scanned": 0, "files_with_banks": 0, "quiz_banks": 0, "ty_pages": 0, "ty_banks": 0,
           "questions": 0, "ty_questions": 0, "strings": 0, "problems": [],
           "hits": [], "review": []}
    by_file = {}
    for path in html_files(roots):
        rel = os.path.relpath(path, ROOT)
        res["files_scanned"] += 1
        banks, problems = page_banks(path)
        for p in problems:
            res["problems"].append({"file": rel, "problem": p})
        if banks:
            res["files_with_banks"] += 1
        if any(b.startswith("TEST_YOURSELF") for b, _ in banks):
            res["ty_pages"] += 1
        for bank, entries in banks:
            ty = bank.startswith("TEST_YOURSELF")
            res["ty_banks" if ty else "quiz_banks"] += 1
            res["ty_questions" if ty else "questions"] += len(entries)
            for loc, q in entries:
                fields = question_fields(q)
                if fields is None:
                    res["problems"].append({"file": rel, "problem": "%s %s: unrecognised question shape" % (bank, loc)})
                    continue
                for field, text in fields:
                    res["strings"] += 1
                    for sev, det, frag in scan_text(text):
                        rec = {"file": rel, "bank": bank, "index": loc, "field": field,
                               "text": text, "match": frag, "detector": det,
                               "stem": q.get("q", "")[:160]}
                        (res["hits"] if sev == "hard" else res["review"]).append(rec)
                        by_file.setdefault(rel, []).append((sev, rec))

    if not quiet:
        for rel in sorted(by_file):
            recs = [r for sev, r in by_file[rel] if sev == "hard" or review]
            if not recs:
                continue
            print("\n%s" % rel)
            for r in recs:
                tag = r["detector"] if r["detector"] != "review" else "review"
                print("  %-12s %-22s %-14s \"%s\"\n       %s"
                      % (r["index"], r["field"], tag, r["match"], r["text"][:150]))
        for p in res["problems"]:
            print("UNREADABLE  %s: %s" % (p["file"], p["problem"]))
    return res


def main(argv):
    review = "--review" in argv
    include_frozen = "--include-frozen" in argv
    json_out = None
    args = []
    it = iter(argv)
    for a in it:
        if a == "--json":
            json_out = next(it, None)
        elif a not in ("--review", "--include-frozen"):
            args.append(a)
    roots, frozen = resolve_roots(args, include_frozen)
    res = scan(roots, review=review)

    hard = res["hits"]
    rx_n = sum(1 for h in hard if h["detector"] == "rx")
    files = len({h["file"] for h in hard})
    print("\n%d html file(s) scanned, %d holding questions: %d quiz bank(s) / %d question(s); "
          "TEST_YOURSELF on %d page(s), %d section(s) / %d question(s); %d string(s) checked"
          % (res["files_scanned"], res["files_with_banks"], res["quiz_banks"], res["questions"],
             res["ty_pages"], res["ty_banks"], res["ty_questions"], res["strings"]))
    if frozen:
        print("skipped %d frozen Semester 1 folder(s) (check_exam_standard.FROZEN)" % len(frozen))
    print("UNREADABLE (not checked): %d" % len(res["problems"]))
    print("%d citation(s) in %d file(s)  [source phrases (RX): %d, lecturer names: %d]"
          % (len(hard), files, rx_n, len(hard) - rx_n))
    print("%d pronoun candidate(s) for human review%s"
          % (len(res["review"]), "" if review else " -- list them with --review"))
    missing = unclassified_calendar_names()
    if missing:
        print("NOTE: calendar lecturers not yet classified in _lecturers.py: %s" % ", ".join(missing))
    if json_out:
        res["frozen_skipped"] = frozen
        with open(json_out, "w", encoding="utf-8") as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % json_out)
    return 1 if (hard or res["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
