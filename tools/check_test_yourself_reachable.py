#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every TEST_YOURSELF bank in a guide must have a button that opens it.

Found 2026-09-11: the Clin Path Exam 1 guide carried a six-question
TEST_YOURSELF.ophthalmic bank that no button referenced, so it had been
unreachable since the day it shipped. Nothing failed -- the JavaScript was
valid, the page rendered, the object was simply never read. That is the
signature of this bug: it is invisible from the page and invisible from the
console, and only a cross-reference finds it.

Same shape as the orphaned Microbiology quizzes found on 2026-09-10: content
that was built correctly and then wired to nothing.

Scoped to the TEST_YOURSELF object literal by brace matching, NOT by a bare
`key: [` regex -- guides hold plenty of other object literals and a loose
pattern reports keys from all of them.
"""
import re, os, sys, glob


def banks(src):
    """Top-level keys of the TEST_YOURSELF object literal, or None if absent."""
    m = re.search(r"var\s+TEST_YOURSELF\s*=\s*\{", src)
    if not m:
        return None
    i = m.end() - 1
    depth, j, in_str, quote, esc = 0, i, False, "", False
    while j < len(src):
        c = src[j]
        if in_str:
            if esc:            esc = False
            elif c == "\\":    esc = True
            elif c == quote:   in_str = False
        elif c in "\"'":
            in_str, quote = True, c
        elif c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
            if depth == 0:
                break
        j += 1
    body = src[i:j + 1]
    # depth 1 == directly inside TEST_YOURSELF; anything deeper is a question object
    out, depth, k, in_str, quote, esc = [], 0, 0, False, "", False
    while k < len(body):
        c = body[k]
        if in_str:
            if esc:            esc = False
            elif c == "\\":    esc = True
            elif c == quote:   in_str = False
        elif c in "\"'":
            in_str, quote = True, c
        elif c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
        elif depth == 1:
            mm = re.match(r"\s*([A-Za-z_$][\w$]*)\s*:", body[k:])
            if mm:
                out.append(mm.group(1))
                k += mm.end() - 1
        k += 1
    return out


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    targets = sys.argv[1:] or sorted(set(glob.glob(os.path.join(root, "*", "*guide.html"))))
    bad, scanned = [], 0
    for f in targets:
        src = open(f, encoding="utf-8").read()
        found = banks(src)
        if found is None:
            continue
        scanned += 1
        used = set(re.findall(r"TEST_YOURSELF\.([A-Za-z_$][\w$]*)", src))
        used |= set(re.findall(r"TEST_YOURSELF\[\s*[\"']([^\"']+)[\"']", src))
        orphans = [b for b in found if b not in used]
        if orphans:
            bad.append((os.path.relpath(f, root), orphans))

    for f, o in bad:
        print("  UNREACHABLE  %-58s %s" % (f, ", ".join(o)))
    print("\n%d guide(s) with a TEST_YOURSELF bank; %d hold a bank no button opens"
          % (scanned, len(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
