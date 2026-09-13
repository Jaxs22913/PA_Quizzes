#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove "the deck" from the PD2 pools.

The topic quizzes are clean because the partitioner fixed the 60 questions it
selected. The other half of each pool never went through that, so drawing the
master exams from the full pools surfaced 109 questions that cite their own
source -- which [[self_contained_questions]] forbids, and which reads as
nonsense to anyone who has not seen the slides.

222 of the 226 offending strings are the single word "deck" in a small set of
regular shapes, so they are rewritten by rule rather than by hand table. The
rules turn a statement ABOUT the source into a statement of the fact itself:
"The deck names the lower lid" becomes "It is the lower lid." Anything the rules
do not catch is reported for hand-editing rather than left in.
"""
import io, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

RULES = [
    # meta phrases that add nothing once removed
    (r",?\s*as the deck defines it\b", ""),
    (r",?\s*per the deck's review slide\b", ""),
    (r",?\s*as the deck (?:has|had) it\b", ""),
    (r"\s*\bin the deck's symptom list\b", ""),
    (r"\s*\bin the deck\b", ""),
    # possessive: "the deck's X" -> "the X"
    (r"\bthe deck's\b", "the"),
    (r"\bThe deck's\b", "The"),
    # "the deck <verb>s" -> impersonal statement of the fact
    (r"\bthe deck (?:names|specifies|gives|lists|asks for|uses|flags|raises|"
     r"attaches|pairs|treats|reads|calls|says|describes|defines|groups|counts)\b",
     "it is"),
    (r"\bThe deck (?:names|specifies|gives|lists|uses|flags|raises|attaches|"
     r"pairs|treats|reads|calls|says|describes|defines|groups|counts)\b",
     "It is"),
    (r"\bThe deck asks for\b", "What is asked for is"),
    (r"\bdoes the deck (?:use|ask for|give|name|say|read|define)\b", "is used"),
    (r"\bthe deck\b", "the material"),
    (r"\bThe deck\b", "The material"),
]

TIDY = [
    (r"\s{2,}", " "),
    (r"\s+([.,;?!])", r"\1"),
    (r"\bit is the\b\s+\.", "it is."),
    (r"^\s+", ""),
]


def fix(text):
    out = text
    for pat, rep in RULES:
        out = re.sub(pat, rep, out)
    for pat, rep in TIDY:
        out = re.sub(pat, rep, out)
    return out


def main():
    apply = "--apply" in sys.argv
    total = 0
    for f in sorted(glob.glob(os.path.join(HERE, "pd2_l*_pool_*.py"))):
        src = io.open(f, encoding="utf-8").read()
        # only touch the STRING LITERALS, never the module's own comments
        def repl(m):
            global _n
            body = m.group(1)
            if "deck" not in body.lower():
                return m.group(0)
            return '"' + fix(body) + '"'
        new, n = re.subn(r'"((?:[^"\\]|\\.)*)"', repl, src)
        changed = sum(1 for _ in re.finditer(r'"((?:[^"\\]|\\.)*)"', src)
                      if "deck" in _.group(1).lower())
        if changed:
            total += changed
            print("  %-24s %3d string(s)" % (os.path.basename(f), changed))
            if apply:
                io.open(f, "w", encoding="utf-8").write(new)
    print("%s %d string(s)" % ("rewrote" if apply else "WOULD rewrite", total))


if __name__ == "__main__":
    main()
