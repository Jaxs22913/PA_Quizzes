#!/usr/bin/env python3
"""Deterministic item-quality flags from tools/question_writing/WRITER.md (2026-10-15).

Why this exists: the writing rules forbid things a machine can see -- duplicate or nested options,
"all of the above", an "a"/"an" that only fits the key, numeric options out of order -- and warn about
softer clues (absolutes only in distractors, the key echoing a distinctive stem word, near-duplicate
stems). check_exam_standard.py checks the SHAPE of a page (four options, length bias, positions); this checks
the content of each item. Judgement (is the key right? is a distractor defensible?) is the blind review,
tools/blind_review.py -- never this script.

    python3 tools/check_item_quality.py --folder "Clinical Medicine and Surgery I Exam 5"
    python3 tools/check_item_quality.py                       # every Semester 2 folder (the baseline table)
    python3 tools/check_item_quality.py --folder X --scope-only   # only files listed in scope.json
    python3 tools/check_item_quality.py --folder X --all          # exit 1 on any FAIL, in or out of scope

FAIL  two options identical after normalization; one option wholly containing another (the contained one
      longer than 3 words); "all/none of the above", "both A and B"; a lead-in ending in "an" (or "a") whose
      options do not all agree with it -- the key starts with a consonant (vowel) sound while a distractor
      does not match, or the reverse -- a grammatical clue; numeric options (tools/_option_order.py) not in ascending or descending order.
WARN  an absolute (always/never/only/all/none) in a distractor but not in the key; the key shares a
      distinctive stem word no distractor shares; near-duplicate stems on one page (word 5-gram Jaccard
      >= 0.6); a race/ethnicity word in a stem (review only: allowed when the deck ties it to the
      disease); a distractor of a SCOPED item with no `mis` (the misconception it stands for).

Exit 1 only on a FAIL in a file listed in scope.json (tools/question_writing/scope.json), unless --all.
Scope is empty today, so existing quizzes never fail; FAIL/WARN counts are still printed per folder.
Semester 1 folders are frozen and skipped. The last line is the summary and the exit status.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import blind_review as R  # noqa: E402  (question reader, scope, `mis` sources)
from _option_order import ordered_kind, is_monotonic  # noqa: E402

KINDS_FAIL = ["duplicate options", "option contains another", "all/none/both of the above",
              "a/an grammatical clue", "numeric options out of order"]
KINDS_WARN = ["absolute only in distractors", "key echoes a distinctive stem word", "near-duplicate stems",
              "race/ethnicity word in stem", "scoped distractor without mis"]
SHORT = {"duplicate options": "dup", "option contains another": "nest", "all/none/both of the above": "aota",
         "a/an grammatical clue": "a/an", "numeric options out of order": "order",
         "absolute only in distractors": "abs", "key echoes a distinctive stem word": "echo",
         "near-duplicate stems": "dupst", "race/ethnicity word in stem": "race", "scoped distractor without mis": "nomis"}
SHOW = 20

STOP = set("""the a an of and or to in on for with by is are was were be as at from that this these those it its
which what who whom not no than then into over under about after before during between both each most more less
other only also may can will should would could has have had their there they them his her he she when where while
because since if but so such any all one two three four first second per via vs does did do done
following likely best next step initial first-line common most commonly patient patients year old woman man
male female boy girl child adult presents presenting history comes brought reports complains evaluation
finding findings feature features characteristic reason explains result results term name type kind""".split())
ABSOLUTE = re.compile(r"\b(always|never|only|all|none)\b", re.I)
ALL_ABOVE = re.compile(r"\b(all|none|neither)\s+of\s+(the\s+)?(above|these|those)\b|\bboth\s+\(?[A-D]\)?\s+and\s+\(?[A-D]\)?\b|"
                       r"\b[A-D]\s+and\s+[A-D]\s+(only|are|both)\b|\ball\s+(the\s+)?above\b", re.I)
RACE = re.compile(r"\b(african[- ]american|caucasian|hispanic|latino|latina|latinx|asian|ashkenazi|native american|"
                  r"pacific islander|middle[- ]eastern|indigenous|ethnic\w*|racial\w*|race|jewish|"
                  r"(white|black)\s+(man|woman|male|female|patient|boy|girl|child|infant|adult|person|individual|"
                  r"farmer|worker))\b", re.I)


def n_opt(t):
    t = re.sub(r"<[^>]+>", " ", t or "").lower().replace("&nbsp;", " ")
    t = re.sub(r"(?<!\d)\.|\.(?!\d)", " ", t)
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s%/<>=.-]", " ", t)).strip()


def stem_words(t):
    return re.findall(r"[a-z][a-z-]+", re.sub(r"<[^>]+>", " ", t).lower())


def root(w):
    return re.sub(r"(ies|es|s)$", "", w) if len(w) > 5 else w


def contains_seq(big, small):
    n = len(small)
    return n > 0 and any(big[i:i + n] == small for i in range(len(big) - n + 1))


_VOWEL_EXC_CONSONANT = ("uni", "use", "usu", "ute", "uri", "uro", "ure", "eu", "one", "once", "ubiq")
_VOWEL_EXC_VOWEL = ("hour", "honest", "heir", "hono")


def starts_vowel_sound(text):
    t = re.sub(r"^[^A-Za-z0-9]+", "", re.sub(r"<[^>]+>", "", text or ""))
    if not t:
        return None
    first = t.split()[0]
    low = first.lower()
    if first.isupper() and 2 <= len(first.rstrip("s")) <= 5 and first.isalpha():       # acronym read letter by letter
        return first[0] in "AEFHILMNORSX"
    if low[0].isdigit():
        m = re.match(r"\d+", low)
        n = m.group(0)
        return n[0] in "8" or n in ("11", "18") or (n[0] == "1" and n[:2] == "18")
    if low.startswith(_VOWEL_EXC_VOWEL):
        return True
    if low.startswith(_VOWEL_EXC_CONSONANT):
        return False
    if low[0] == "x":
        return True
    return low[0] in "aeiou"


def grammar_clue(stem, opts, key):
    """The lead-in ends in "a"/"an" and the options do not all agree with it. Covers both shapes of the
    clue: the article fits ONLY the key (the key is the one grammatical answer), and the key is the one
    that does NOT fit while distractors do (a mismatch that singles it out)."""
    m = re.search(r"\b(an?)\s*[_.\u2026:?\s]*$", stem.strip(), re.I)
    if not m:
        return False
    want = m.group(1).lower() == "an"
    fits = [starts_vowel_sound(o[0]) == want for o in opts]
    return not all(fits) and any(fits)


def jaccard_grams(words, n=5):
    g = {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}
    return g


def check_question(q, scoped):
    """-> (fails, warns) lists of (kind, message)."""
    fails, warns = [], []
    texts = [o[0] for o in q.opts]
    ns = [n_opt(t) for t in texts]
    if len(set(ns)) != len(ns):
        fails.append((KINDS_FAIL[0], "identical after normalization"))
    else:
        for i in range(len(ns)):
            for j in range(len(ns)):
                if i != j:
                    a, b = ns[i].split(), ns[j].split()
                    if len(b) > 3 and contains_seq(a, b):
                        fails.append((KINDS_FAIL[1], "option %s contains option %s" % (R.LETTERS[i], R.LETTERS[j])))
    for i, t in enumerate(texts):
        if ALL_ABOVE.search(t):
            fails.append((KINDS_FAIL[2], "option %s: %r" % (R.LETTERS[i], t[:50])))
    if grammar_clue(q.stem, q.opts, q.key):
        fails.append((KINDS_FAIL[3], "lead-in ends %r and only the key fits" % q.stem.strip()[-12:]))
    if ordered_kind(texts) and not is_monotonic(texts):
        fails.append((KINDS_FAIL[4], "numeric options not ascending or descending: %s" % " | ".join(t[:14] for t in texts)))

    dist = [o[0] for i, o in enumerate(q.opts) if i != q.key]
    if any(ABSOLUTE.search(t) for t in dist) and not ABSOLUTE.search(q.key_text):
        warns.append((KINDS_WARN[0], "absolute in a distractor only: %s" % [t[:30] for t in dist if ABSOLUTE.search(t)][0]))
    stem_set = {root(w) for w in stem_words(q.stem) if w not in STOP and len(w) >= 5}
    keyw = {root(w) for w in stem_words(q.key_text)}
    distw = set()
    for t in dist:
        distw |= {root(w) for w in stem_words(t)}
    shared = sorted((stem_set & keyw) - distw)
    if shared:
        warns.append((KINDS_WARN[1], "key shares %s" % ", ".join(shared[:3])))
    race = RACE.search(re.sub(r"\bheart rac(?:e|ing)\b|\bpulse rac(?:e|ing)\b", " ", q.stem, flags=re.I))
    if race:
        warns.append((KINDS_WARN[3], "stem names race/ethnicity: %r" % race.group(0)))
    if scoped:
        miss = [R.LETTERS[i] for i, o in enumerate(q.opts) if i != q.key and not o[2]]
        if miss:
            warns.append((KINDS_WARN[4], "no mis on distractor(s) %s" % "".join(miss)))
    return fails, warns


def near_duplicates(qs):
    out = []
    grams = [jaccard_grams(stem_words(q.stem)) for q in qs]
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            a, b = grams[i], grams[j]
            if a and b and len(a & b) / len(a | b) >= 0.6:
                out.append((qs[i], qs[j]))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--folder", action="append", help="repo folder (repeatable); default every Semester 2 folder")
    ap.add_argument("--scope-only", action="store_true", help="only files listed in scope.json")
    ap.add_argument("--all", action="store_true", help="exit 1 on any FAIL, not just in scoped files")
    ap.add_argument("--scope", default=None)
    a = ap.parse_args(argv)
    if a.scope:
        R.SCOPE = a.scope
    folders = a.folder or R.s2_folders()
    globs = R.load_scope()
    unparse = []
    per_folder = collections.OrderedDict()
    firsts = {k: [] for k in KINDS_FAIL + KINDS_WARN}
    total_q = scoped_q = 0
    fail_scoped = fail_any = 0
    seen_pages = 0
    for f in folders:
        qs = R.attach_sources(R.load_folder(f, None, unparse)) if globs else R.load_folder(f, None, unparse)
        if a.scope_only:
            qs = [q for q in qs if R.in_scope(q.file, globs)]
        if not qs:
            continue
        counts = collections.Counter()
        by_file = collections.defaultdict(list)
        for q in qs:
            by_file[q.file].append(q)
        total_q += len(qs)
        for rel, fq in by_file.items():
            seen_pages += 1
            scoped = R.in_scope(rel, globs)
            if scoped:
                scoped_q += len(fq)
                if not fq[0].sourced:                       # scoped pages need `mis` from the pool/sets
                    R.attach_sources(fq)
            for q in fq:
                fails, warns = check_question(q, scoped)
                for kind, msg in fails + warns:
                    counts[kind] += 1
                    firsts[kind].append("%s | %s | %s" % (rel, q.stem[:50], msg))
                if fails:
                    fail_any += 1
                    if scoped:
                        fail_scoped += 1
            for x, y in near_duplicates(fq):
                counts[KINDS_WARN[2]] += 1
                firsts[KINDS_WARN[2]].append("%s | %s || %s" % (rel, x.stem[:40], y.stem[:40]))
        counts["_q"] = len(qs)
        per_folder[f] = counts
    for rel, err in unparse:
        print("UNPARSEABLE %s: %s -- NOT CHECKED" % (rel, err))
    tot = collections.Counter()
    for c in per_folder.values():
        tot.update(c)
    print("item quality: %d folder(s), %d page(s), %d question(s) read (%d in scope)" % (len(per_folder), seen_pages, total_q, scoped_q))
    print("%-46s %5s  %s" % ("folder", "Qs", " ".join("%5s" % SHORT[k] for k in KINDS_FAIL + KINDS_WARN)))
    print("%-46s %5s  FAIL: dup nest aota a/an order | warn: abs echo dupst race nomis" % ("", ""))
    for f, c in per_folder.items():
        print("%-46s %5d  %s" % (f[:46], c["_q"], " ".join("%5d" % c[k] for k in KINDS_FAIL + KINDS_WARN)))
    print("\nTotals (denominator %d questions):" % total_q)
    for kind in KINDS_FAIL:
        print("  FAIL %-34s %5d" % (kind, tot[kind]))
    for kind in KINDS_WARN:
        print("  warn %-34s %5d" % (kind, tot[kind]))
    for kind in KINDS_FAIL + KINDS_WARN:
        if firsts[kind]:
            print("\n%s %s: first %d of %d" % ("FAIL" if kind in KINDS_FAIL else "warn", kind, min(SHOW, len(firsts[kind])), len(firsts[kind])))
            for line in firsts[kind][:SHOW]:
                print("   " + line)
    n_fail = sum(tot[k] for k in KINDS_FAIL)
    n_warn = sum(tot[k] for k in KINDS_WARN)
    bad = (fail_any if a.all else fail_scoped) > 0 or bool(unparse)
    print("item quality: %s (exit %d): %d scoped question(s) with a FAIL%s; %d FAIL flag(s) and %d WARN flag(s) in all %d question(s)"
          % ("FAIL" if bad else "PASS", 1 if bad else 0, fail_scoped,
             ", %d overall (--all)" % fail_any if a.all else "", n_fail, n_warn, total_q))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
