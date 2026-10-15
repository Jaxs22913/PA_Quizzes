#!/usr/bin/env python3
"""Numeric / ordered answer options: detect them and sort them (WRITER.md, Writing rule 8).

Why this exists (2026-10-15): the question-writing rules say options that are values, ages,
durations, counts, stages or grades are listed in ASCENDING order and are NOT shuffled, with the key
sitting where its value falls. Every pool is permuted by a seeded partition script that knows nothing
about this, so a numeric option set came out in random order. This module is the one place that
decides "are these options numeric?" and "what is the sorted order?", so the deterministic checker
(check_item_quality.py) and any build step agree.

    ordered_kind(options) -> "numeric" | None
        "numeric" when EVERY option reduces to the same template once its number is replaced by a
        placeholder, e.g. "5 mm", "10 mm" / "<5 mg/dL", "5-10 mg/dL", ">10 mg/dL" / "Stage 2",
        "Stage 3" / "Three", "Four" (number words one..twenty) / "35%", "50%". Units, percent signs,
        comparison words (<, >, at least, about ...) and ranges are tolerated; a different unit
        ("2 weeks" next to "3 days") or any option with no number gives None.
    option_values(options) -> [(low, high), ...] or None     # the sort key per option
    order_options(q) -> a COPY of the page-shaped question {opts:[[text, expl, ...], ...], c: key}
        with numeric options sorted ascending (stable), the key index and every per-option
        explanation (and any `mis`) moving with their option. Anything non-numeric comes back
        unchanged.

Question shape is the page shape used everywhere in this repo: q["opts"] = [[text, explanation, ...]],
q["c"] = index of the key.
"""
import copy
import re

WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}
ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10}

_NUM = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?"
_WORD_RE = re.compile(r"\b(%s)\b" % "|".join(sorted(WORDS, key=len, reverse=True)), re.I)
_ROMAN_RE = re.compile(r"\b((?:stage|grade|class|level|phase|tier)\s+)(viii|vii|iii|vi|iv|ix|ii|x|v|i)\b", re.I)
_OPERATORS = re.compile(r"(?:[<>=~≤≥≈+]|\b(?:at least|at most|about|approximately|around|over|under|"
                        r"more than|less than|greater than|fewer than|up to|nearly|roughly)\b)", re.I)
_RANGE = re.compile(r"(?P<a>%s)\s*(?:-|–|—|to)\s*(?P<b>%s)" % (_NUM, _NUM), re.I)


def _to_float(s):
    return float(s.replace(",", ""))


def _template(text):
    """-> (template, (low, high)) or None. One number (or one range) per option."""
    t = re.sub(r"<[^>]+>", " ", text or "").strip().lower()
    t = t.replace("−", "-")
    # roman numerals after stage/grade/class become digits first
    t = _ROMAN_RE.sub(lambda m: "%s%d" % (m.group(1), ROMAN[m.group(2).lower()]), t)
    t = _OPERATORS.sub(" ", t)
    vals = []

    def rng(m):
        vals.append((_to_float(m.group("a")), _to_float(m.group("b"))))
        return " # "
    t = _RANGE.sub(rng, t)

    def one(m):
        v = _to_float(m.group(0))
        vals.append((v, v))
        return " # "
    t = re.sub(_NUM, one, t)

    def word(m):
        v = float(WORDS[m.group(1).lower()])
        vals.append((v, v))
        return " # "
    t = _WORD_RE.sub(word, t)
    if len(vals) != 1:
        return None
    # unit/words: plural-insensitive, punctuation-insensitive
    t = re.sub(r"[^\w#%/]+", " ", t)
    t = " ".join(re.sub(r"(?<=[a-z]{3})s$", "", w) for w in t.split())
    return t, vals[0]


def option_values(options):
    out, tmpl = [], None
    for o in options:
        r = _template(o)
        if r is None:
            return None
        if tmpl is None:
            tmpl = r[0]
        elif r[0] != tmpl:
            return None
        out.append(r[1])
    return out if len(out) >= 2 else None


def ordered_kind(options):
    """'numeric' when every option is a number of the same unit, else None."""
    return "numeric" if option_values(options) is not None else None


def is_monotonic(options):
    """True when numeric options already run ascending or descending (ties allowed)."""
    v = option_values(options)
    if v is None:
        return True
    asc = all(v[i] <= v[i + 1] for i in range(len(v) - 1))
    desc = all(v[i] >= v[i + 1] for i in range(len(v) - 1))
    return asc or desc


def order_options(q):
    """Copy of q with numeric options sorted ascending; key and explanations travel with their option."""
    texts = [o[0] if isinstance(o, (list, tuple)) else o for o in q["opts"]]
    vals = option_values(texts)
    if vals is None:
        return q
    order = sorted(range(len(texts)), key=lambda i: (vals[i], i))
    out = copy.deepcopy(q)
    out["opts"] = [copy.deepcopy(q["opts"][i]) for i in order]
    out["c"] = order.index(q["c"])
    return out


if __name__ == "__main__":
    import json
    import sys
    print(__doc__)
    if len(sys.argv) > 1:
        print(json.dumps(order_options(json.loads(sys.argv[1])), indent=1))
