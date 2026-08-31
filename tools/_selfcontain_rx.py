#!/usr/bin/env python3
"""The one detector for source attribution in question text.

A question must stand on its own: no reference to the lecture, the deck, the
slides, the syllabus, or the person who taught it.  Imported by the sweep and
by check_self_contained.py so both agree on what counts as a violation.
"""
import re

SAY = (r"say|says|said|state|states|stated|call|calls|called|name|names|named"
       r"|describe|describes|described|list|lists|listed|give|gives|gave"
       r"|flag|flags|flagged|stress|stresses|stressed|note|notes|noted"
       r"|emphasise|emphasises|emphasised|emphasize|emphasizes|emphasized"
       r"|mark|marks|marked|point|points|pointed|warn|warns|warned"
       r"|specify|specifies|specified|recommend|recommends|recommended"
       r"|prefer|prefers|preferred|teach|teaches|taught|single|singles|singled"
       r"|want|wants|wanted|ask|asks|asked|make|makes|made|treat|treats|treated"
       r"|show|shows|showed|use|uses|used|add|adds|added|put|puts|contrast"
       r"|contrasts|contrasted|define|defines|defined|rank|ranks|ranked"
       r"|cover|covers|covered|include|includes|included|offer|offers|offered")

PATTERNS = [
    r"\bthe (lecture|deck|slides?|syllabus|professor|lecturer|instructor|speaker)\b",
    r"\bspeaker notes?\b",
    r"\bthe notes\b",
    r"\b(professor|prof\.?|dr\.?)\s+[A-Z][a-z]+",
    r"\bin (the )?(lecture|class|the deck)\b",
    r"\bon the slide\b",
    r"\bthis (lecture|deck)\b",
    r"\b(according to|per) the (lecture|deck|slides?|syllabus|professor|notes)\b",
    r"\bcovered in (a |the )?(later|earlier|another) (course|lecture)\b",
    r"\bwas (taught|presented|shown)\b",
    r"\bin Lectures? \d",
]

RX = re.compile("|".join("(?:%s)" % p for p in PATTERNS), re.I)

# Pronoun + teaching verb catches "she flagged", "he said" — but also fires on
# patients ("he covers either eye", "she prefers"), so it feeds a review list
# for a human to judge rather than the pass/fail check.
REVIEW_RX = re.compile(r"\b(she|he|they)\s+(%s)\b" % SAY, re.I)


def review_hits(text):
    return [m.group(0) for m in REVIEW_RX.finditer(text or "")]


def hits(text):
    return [m.group(0) for m in RX.finditer(text or "")]


def flagged(text):
    return bool(RX.search(text or ""))
