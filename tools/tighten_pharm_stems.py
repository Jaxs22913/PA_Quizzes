#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strip lecture-preamble from the Pharmacology I stems.

48% of the pharm stems asked "what does the lecture say about X" rather than
just asking X. No exam question is phrased that way and it pads every stem.

A NAIVE regex pass was tried first and produced garbage -- "Which uses is for
propranolol", "How describes the nicotinic receptor". The problem is that
deleting the subject leaves the verb stranded. These rules instead rewrite the
whole clause into a grammatical shape, and anything that does not match a
template is left ALONE for a human rather than mangled.
"""
import re

# (pattern, replacement) -- each produces a complete, grammatical question.
TEMPLATES = [
 # attributions: pure deletion, always safe
 (r",?\s*(?:per|according to|in|from)\s+the\s+lectures?\b", ""),
 (r"^(?:According to|Per|In)\s+the\s+lectures?,\s*", ""),

 # "Which X does the lecture list/give/name for Y?"  ->  "What X does Y have?"
 (r"^Which (.+?) does the lecture (?:list|give|name|identify|specify)\s+for (.+?)\?$",
  r"What \1 does \2 have?"),
 # "Which X does the lecture list/give ...?"  ->  "What X ...?"
 (r"^Which (.+?) does the lecture (?:list|give|name|identify|specify)\s+(.+?)\?$",
  r"Which \1 \2?"),
 # pairing verbs
 (r"^Which (.+?) does the lecture (?:pair|link) with (.+?)\?$", r"Which \1 goes with \2?"),
 (r"^Which (.+?) does the lecture (?:attribute|assign) to (.+?)\?$", r"Which \1 belongs to \2?"),
 (r"^Which (.+?) does the lecture (?:direct|position|recommend) (?:to|for) (.+?)\?$",
  r"Which \1 is used for \2?"),
 # describe / define
 (r"^How does the lecture describe (.+?)\?$", r"How is \1 described?"),
 (r"^What does the lecture (?:call|define) (.+?)\?$", r"What is \1 called?"),
 (r"^Where does the lecture place (.+?)\?$", r"Where are \1 found?"),
 # say / state
 (r"^What does the lecture say about (.+?)\?$", r"What is true of \1?"),
 (r"^What does the lecture say (?:happens )?when (.+?)\?$", r"What happens when \1?"),
 (r"^What does the lecture say (.+?)\?$", r"What \1?"),
 # warn
 (r"^What does the lecture warn (?:about|happens if) (.+?)\?$", r"What is the risk of \1?"),
 (r"^What does the lecture warn (.+?)\?$", r"What \1?"),
 # give as
 (r"^What does the lecture give as (.+?)\?$", r"What is \1?"),
 (r"^(.+?)\. What does the lecture give as (.+?)\?$", r"\1. What is \2?"),
 (r"^(.+?)\. What does the lecture direct\?$", r"\1. What is the next step?"),
 # why / how many
 (r"^Why does the lecture (?:counsel|advise) caution with (.+?)\?$", r"Why is caution advised with \1?"),
 (r"^Why does the lecture prefer (.+?)\?$", r"Why is \1 preferred?"),
 (r"^How many (.+?) does the lecture give for (.+?)\?$", r"How many \1 does \2 have?"),
 # remaining "does the lecture <verb>" shapes, rewritten rather than deleted
 (r"^Which (.+?) does the lecture (?:say|note) (.+?)\?$", r"Which \1 \2?"),
 (r"^Which (.+?) does the lecture attach to (.+?)\?$", r"Which \1 belongs to \2?"),
 (r"^What (.+?) does the lecture give (?:for|to) (.+?)\?$", r"What \1 does \2 have?"),
 (r"^What (.+?) does the lecture give as (.+?)\?$", r"What \1 is \2?"),
 (r"^Which (.+?) the lecture lists\?$", r"Which \1?"),
 (r"^(.+?) the lecture lists\?$", r"\1?"),
]

TIDY = [(r"\s{2,}", " "), (r"\s+([?,.;:])", r"\1"), (r"^([a-z])", lambda m: m.group(1).upper())]


def tighten(stem):
    out = stem
    for pat, rep in TEMPLATES:
        new = re.sub(pat, rep, out, flags=re.I)
        if new != out:
            out = new
            if "lectur" not in out.lower():
                break
    for pat, rep in TIDY:
        out = re.sub(pat, rep, out)
    return out.strip()
