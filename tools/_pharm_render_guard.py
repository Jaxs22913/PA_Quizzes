#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refuse to let a Pharmacology I Exam 1 renderer overwrite a hand-edited page.

WHY THIS EXISTS. The Exam 1 topic pages and master forms were rewritten IN THE
HTML after they were rendered: f67bcc18 (short vignettes, tightened questions),
562f0dd1 (every stem rewritten), ea1f2ec4 and 08653980 (self-containment,
11 repaired explanations), plus the one-off appliers apply_pharm_stem_rewrite*.py,
apply_pharm_shortening.py, apply_pharm_expl_repair.py and add_stable_qids.py.
None of that went back into the sets / master-exams JSON. Measured 2026-09-24:
render(committed sets) differs from the shipped page in stems, option text or
explanations on every derm, cholinergic and adrenergic topic page, and the
master pages carry `qid` fields the JSON does not. Re-rendering one of them for a
one-word fix would silently revert all of it (it has happened: re-rendering
pharm_l2_derm once replaced 1,570 lines with 104 and put "the lecture" back).

WHAT IT DOES.
  guard(pairs, force)  pairs = [(page_path, questions_about_to_be_rendered), ...]
    1. copies each shipped question's `qid` onto the matching new question
       (matched by stem, then by option set), so class-pick history survives;
    2. compares the page's QUESTIONS literal with the new questions;
    3. if ANY page would change and force is False, prints what differs and
       exits 2 BEFORE anything is written.
Run the renderer with --force only after bringing the sets / JSON to the page's
text on purpose (the page is authoritative until then), and diff the result.
"""
import json
import os
import sys


def _span(html):
    marker = "const QUESTIONS = "
    i = html.find(marker)
    if i < 0:
        return None
    j = k = i + len(marker)
    depth, ins, esc = 0, False, False
    while True:
        ch = html[k]
        if ins:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                ins = False
        else:
            if ch == '"':
                ins = True
            elif ch in "[{":
                depth += 1
            elif ch in "]}":
                depth -= 1
                if depth == 0:
                    return j, k + 1
        k += 1


def shipped_questions(path):
    if not os.path.exists(path):
        return None
    html = open(path, encoding="utf-8").read()
    sp = _span(html)
    return json.loads(html[sp[0]:sp[1]]) if sp else None


def carry_qids(page_qs, new_qs):
    by_stem = {q["q"]: q["qid"] for q in page_qs if "qid" in q}
    by_opts = {frozenset(o[0] for o in q["opts"]): q["qid"] for q in page_qs if "qid" in q}
    for q in new_qs:
        if "qid" in q:
            continue
        qid = by_stem.get(q["q"]) or by_opts.get(frozenset(o[0] for o in q["opts"]))
        if qid:
            q["qid"] = qid
    return new_qs


def guard(pairs, force=False):
    problems = []
    for path, new_qs in pairs:
        page = shipped_questions(path)
        if page is None:
            continue
        carry_qids(page, new_qs)
        if page != new_qs:
            n = sum(1 for a, b in zip(page, new_qs) if a != b) + abs(len(page) - len(new_qs))
            problems.append((os.path.basename(path), n, len(page)))
    if problems and not force:
        sys.stderr.write(
            "REFUSING TO OVERWRITE hand-edited Pharmacology pages (see tools/_pharm_render_guard.py):\n")
        for name, n, total in problems:
            sys.stderr.write("  %-48s %d of %d questions differ from what would be rendered\n"
                             % (name, n, total))
        sys.stderr.write("Bring the sets/JSON to the page text first, or pass --force deliberately.\n")
        sys.exit(2)
    return problems
