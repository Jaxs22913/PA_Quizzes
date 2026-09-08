# -*- coding: utf-8 -*-
"""Attach the authored lead-in question to stems that shipped without one.

Called by both partitioners as questions are loaded, so the lead-in lands in
exactly one place and the pool sources stay untouched. Editing the pools
directly was the obvious alternative and was rejected: 288 of the 364 stems are
written as multi-line string concatenations, so there is no single literal to
replace and the surgery would have been done blind.

A stem is only ever appended to -- never rewritten. That matters because the
review-missed feature keys documents on the stem text
([[review_missed_questions]]), and rewriting Pharmacology stems once orphaned
286 of 670 live documents. Appending still changes the key, so records written
against these questions between their first publication and this fix will not
match; that is one day's worth, and the alternative was leaving 364 questions
with no question in them.
"""
import re
from _cmse3_leadins import LEADINS
from _cmse3_leadin_fp import FP

_used = set()


IMPERATIVE = re.compile(r"(?i)^\s*(select|choose|identify|describe|rank|place|"
                        r"order|list|predict|state|give|match|arrange|name|"
                        r"calculate|estimate|determine|explain|classify|"
                        r"interpret|indicate|specify)\b")


def _has_leadin(t):
    """Does this stem already ask the student something?

    Kept identical to tools/check_leadin_present.py. Three shapes count:
    an explicit question mark; a COMPLETION stem, which does not end in a full
    stop because the options finish the sentence; or an opening imperative that
    names the task. Anything else is a complete sentence that asks nothing.

    An earlier version also treated the words what/how/when/where ANYWHERE in
    the stem as a lead-in. That is far too loose for a clinical vignette --
    "a mass that rises when she swallows" tripped it -- and it is unnecessary,
    because a real question ends in a question mark.
    """
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).strip()
    if not t:
        return True
    if "?" in t:                      # an explicit question
        return True
    if not t.endswith("."):           # completion stem: the options finish it
        return True
    if t.endswith("..."):             # ditto, ellipsis form
        return True
    return bool(IMPERATIVE.match(t))  # "Describe...", "Rank...", "List..."


def attach(module, index, q):
    """Return q with its lead-in appended, if one was authored for it."""
    key = (module, index)
    if key not in LEADINS:
        # Nothing authored: the stem must already ask something, or it is a
        # stem written after this fix that nobody has reviewed.
        assert _has_leadin(q["q"]), \
            "%s[%d] has no lead-in and none is authored: %r" % (module, index, q["q"][:70])
        return q

    assert not _has_leadin(q["q"]), \
        "%s[%d] already asks a question -- a lead-in would duplicate it" % (module, index)
    seen = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", q["q"])).strip()[:46]
    assert seen == FP[key], (
        "%s[%d] is not the question the lead-in was written for.\n"
        "  expected: %r\n  found:    %r\n"
        "The pool has been reordered or edited. Re-read the options and "
        "re-author the lead-in; do not just regenerate the fingerprints."
        % (module, index, FP[key], seen))

    q = dict(q)
    stem = q["q"].rstrip()
    q["q"] = stem + (" " if not stem.endswith(("</p>", ">")) else "") + LEADINS[key]
    _used.add(key)
    return q


def assert_all_used(modules):
    """Every lead-in authored for the given modules must have been applied."""
    want = {k for k in LEADINS if k[0] in modules}
    missing = want - _used
    assert not missing, "lead-ins never applied: %s" % sorted(missing)
