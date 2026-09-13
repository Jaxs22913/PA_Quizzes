#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert every five-option CMS question to four options.

Jaxon, 13 September 2026: "All should be 4 answer choices not 5." That reverses
the five-option rule taken from the 40 reference exemplars, which had applied to
CMS only. Every other class was already four.

WHICH DISTRACTOR GOES. These questions are well authored -- in most of them all
four distractors name a real alternative with a specific refutation, so there is
no throwaway option to delete and every removal costs something. That is
acceptable (three good distractors plus the key is still a sound question) but
it means the choice has to be made on merit rather than by position. Dropping
the last option would have been trivial to write and actively wrong: in "which
structure lies in front of the ear canal", the last option is `concha`, the most
confusable one in the set and therefore the best distractor in it.

So each distractor is scored on how much work it does, and the lowest scorer
goes:

  NEAR-MISS distractors are protected outright. A refutation that concedes
  something -- "Koebner phenomenon is ALSO present in this patient", "antibiotic
  exposure GENUINELY raises the risk BUT" -- marks the option a careful student
  actually hesitates over. Those are the most valuable distractors on the page
  and they are never the one removed.

  SPECIFIC refutations beat generic ones. "That is angle-closure glaucoma" names
  the thing the student was thinking of; "Not a recognised finding" does not.

  REDUNDANT distractors lose. Where two refutations make substantially the same
  point, one of them is not earning its place.

Ties break toward the later option, purely so the result is deterministic.

The key is ALWAYS opts[0] in these pools -- asserted, not assumed -- and is
never a candidate for removal. Position rotation happens downstream in the
partitioners, so nothing here needs to preserve answer balance.

    python3 tools/convert_cms_to_four_options.py --dry-run   # report only
    python3 tools/convert_cms_to_four_options.py             # rewrite the pools
"""
import ast, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Scope is found BY CONTENT, not by filename. Globbing for "*pool*" looked
# right and silently missed 482 questions in the cms_*_vig_*.py vignette files,
# which hold questions but are not called pools. Any tools file containing a
# five-option options-list is in scope; nothing else is touched.
SCOPE_PREFIXES = ("cms_", "cmsderm_", "cmsophtho_", "cmsent_")

# A refutation that concedes ground marks a near-miss -- the distractor a
# careful student genuinely weighs. Never remove one of these.
CONCESSIVE = re.compile(
    r"\b(also|genuinely|does occur|can occur|may occur|is true|true,|belongs|"
    r"partly|partially|in part|correct that|right that|reasonable|tempting|"
    r"would be right|is present|does happen|not wrong|closest|near)\b", re.I)

# Generic dismissals that teach nothing specific.
GENERIC = re.compile(
    r"^\s*(not a recognised|not recognised|not a real|no such|unrelated|"
    r"does not apply|not applicable|irrelevant|not described|not a feature|"
    r"nothing to do with|has no role|no role|not the|neither|none of)\b", re.I)

WORD = re.compile(r"[a-z]{4,}")
STOP = {"that", "this", "with", "from", "which", "would", "there", "their",
        "have", "does", "into", "than", "then", "they", "them", "when", "what",
        "were", "been", "being", "here", "these", "those", "only", "also",
        "because", "after", "before", "about", "other", "rather"}


def content(text):
    return {w for w in WORD.findall(text.lower()) if w not in STOP}


def keep_score(i, opts):
    """How much work distractor i does. Higher survives."""
    text, why = opts[i][0], opts[i][1]
    s = 0.0
    s += min(len(why), 160) / 20.0                      # specific > terse
    if CONCESSIVE.search(why):
        s += 1000.0                                     # near-miss: protected
    if GENERIC.match(why):
        s -= 6.0
    if re.search(r"\bthat is\b|\bthose are\b|\bis the\b|\bare the\b", why, re.I):
        s += 2.0                                        # names the alternative
    # Redundancy: overlap with the OTHER distractors' refutations.
    mine = content(why)
    if mine:
        overlap = 0.0
        for j in range(1, len(opts)):
            if j == i:
                continue
            other = content(opts[j][1])
            if other:
                overlap = max(overlap, len(mine & other) / len(mine | other))
        s -= overlap * 8.0
    return s


def choose_drop(q):
    opts = q["opts"]
    key = q.get("c", 0)
    assert key == 0, "key is not opts[0]; this converter assumes the pool convention"
    scored = [(keep_score(i, opts), -i, i) for i in range(1, len(opts))]
    scored.sort()                                       # lowest keep-score first
    return scored[0][2]


# ---------------------------------------------------------------- rewriting
#
# The pools are hand-written Python, with comments and formatting worth keeping,
# so they are edited as TEXT rather than re-serialised from parsed objects. The
# option to remove is located by its literal source span using ast positions,
# which is exact -- a regex over option text would misfire on the several
# questions that share option wording.

def option_spans(src, tree):
    """Source offsets of every option, per options-list, keyed by list position.

    The pools use two constructor styles -- dict(topic=..., opts=[...]) and a
    local Q("topic", "stem", [...], c, slide) helper -- so keying off the
    constructor would have to know about both, and about whichever style the
    next pool uses. The options list is found BY SHAPE instead: a list whose
    elements are all two-element lists of strings, and whose first element's
    second string begins "Correct". That shape is the convention this whole
    conversion rests on, and it is verified rather than assumed.
    """
    # ast col_offset is a UTF-8 BYTE offset, not a character offset. Building
    # the line table in characters drifted every span on a line containing an em
    # dash -- and the pools are full of them -- so the cut ran past the end of
    # the option and ate the brackets closing the list. Everything here is bytes.
    lines = src.splitlines(keepends=True)
    starts = [0]
    for ln in lines:
        starts.append(starts[-1] + len(ln))

    def off(node, end=False):
        ln = (node.end_lineno if end else node.lineno) - 1
        col = node.end_col_offset if end else node.col_offset
        return starts[ln] + col

    def is_pair(e):
        return (isinstance(e, (ast.List, ast.Tuple)) and len(e.elts) == 2
                and all(isinstance(x, ast.Constant) and isinstance(x.value, str)
                        for x in e.elts))

    out = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.List, ast.Tuple)):
            continue
        elts = node.elts
        if len(elts) < 4 or not all(is_pair(e) for e in elts):
            continue
        if not re.match(r"\s*correct\b", elts[0].elts[1].value, re.I):
            continue
        out[off(node)] = {
            "spans": [(off(e), off(e, True)) for e in elts],
            # The option TEXT comes from the AST too, so choosing what to drop
            # never has to import the pool. That matters: the shared style
            # helpers assert the option count on import, so importing a
            # five-option pool after the helper has been moved to four fails
            # before the converter can do anything about it.
            "opts": [[e.elts[0].value, e.elts[1].value] for e in elts],
        }
    return out


def load_questions(path):
    """Import the pool and return its question dicts in source order."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("cv_" + os.path.basename(path), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    qs = []
    for v in vars(m).values():
        if isinstance(v, list) and v and isinstance(v[0], dict) and "opts" in v[0]:
            qs.extend(v)
    return qs


def convert_file(path, dry=False):
    text = open(path, encoding="utf-8").read()
    tree = ast.parse(text)
    src = text.encode("utf-8")          # splice in BYTES -- see option_spans
    spans = option_spans(src, tree)
    before = [spans[o]["opts"] for o in sorted(spans)]

    # Walk dict nodes in source order and pair them with the imported questions.
    five = [spans[o] for o in sorted(spans) if len(spans[o]["spans"]) >= 5]
    if not five:
        return 0, []

    cuts, report, dropped_idx = [], [], []
    for rec in five:
        sp, opts = rec["spans"], rec["opts"]
        q = {"opts": opts, "c": 0, "q": ""}
        di = choose_drop(q)
        assert di != 0, "would remove the correct answer"
        a, b = sp[di]
        start = a
        # swallow the separating comma and any run of whitespace after it
        end = b
        while end < len(src) and src[end:end + 1] in (b" ", b"\t"):
            end += 1
        if end < len(src) and src[end:end + 1] == b",":
            end += 1
            while end < len(src) and src[end:end + 1] in (b" ", b"\t", b"\r", b"\n"):
                end += 1
        else:
            # Last option in the list: there is no comma after it, so step BACK
            # over the comma that preceded it instead. Leaving that comma is
            # legal Python but leaves a stray dangling separator in a hand-kept
            # source file.
            while start > 0 and src[start - 1:start] in (b" ", b"\t", b"\r", b"\n"):
                start -= 1
            if start > 0 and src[start - 1:start] == b",":
                start -= 1
        cuts.append((start, end))
        dropped_idx.append(di)
        report.append((opts[0][0][:56], opts[di][0][:56], opts[di][1][:60]))

    if not dry:
        for a, b in sorted(cuts, reverse=True):
            src = src[:a] + src[b:]
        out = src.decode("utf-8")
        # VERIFY BEFORE WRITING. A byte-offset slip does not always produce a
        # syntax error -- it can just as easily shave a character off a string
        # and leave the file importable but wrong. So parse it, re-import it,
        # and require that what survived is EXACTLY the original minus the one
        # option chosen. Anything else and the file is left untouched.
        ast.parse(out)
        tmp = path[:-3] + "__verify_tmp.py"   # must end .py or import fails
        open(tmp, "w", encoding="utf-8").write(out)
        try:
            after_spans = option_spans(out.encode("utf-8"), ast.parse(out))
            after = [after_spans[o]["opts"] for o in sorted(after_spans)]
            assert len(after) == len(before), "option-list count changed"
            load_questions(tmp)      # must still import cleanly under the helpers
            di_iter = iter(d for d in dropped_idx)
            for bq, aq in zip(before, after):
                if len(bq) < 5:
                    assert aq == bq, "a four-option question was modified"
                    continue
                d = next(di_iter)
                assert aq == [o for i, o in enumerate(bq) if i != d], (
                    "surviving options are not the original minus the dropped one")
                assert len(aq) == 4, "question did not end up with four options"
        finally:
            os.remove(tmp)
        open(path, "w", encoding="utf-8").write(out)
    return len(cuts), report


def main():
    dry = "--dry-run" in sys.argv
    paths = sorted(p for p in glob.glob(os.path.join(HERE, "*.py"))
                   if os.path.basename(p).startswith(SCOPE_PREFIXES))
    total, files = 0, 0
    samples = []
    for p in paths:
        n, rep = convert_file(p, dry)
        if n:
            files += 1
            total += n
            print("  %-26s %4d converted" % (os.path.basename(p), n))
            samples.extend(rep[:1])
    print("\n%s %d question(s) across %d pool file(s)"
          % ("WOULD convert" if dry else "converted", total, files))
    if dry:
        print("\nsample of what would be dropped:")
        for stem, opt, why in samples[:12]:
            print("  key: %s" % stem)
            print("     drop: %-54s | %s" % (opt, why))
    return 0


if __name__ == "__main__":
    sys.exit(main())
