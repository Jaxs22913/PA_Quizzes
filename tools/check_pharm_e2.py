#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fact-check the Pharmacology I Exam 2 reference data against its decks, and enforce the content rules.

Every row must cite a slide that exists and every `verify` substring must appear on that slide
(runs joined or spaced; smart quotes and dashes normalised). Also fails on: missing fields, an empty
verify list, milligram dosing (Dr. Wood: doses are not tested), letters used as references, words
naming the source ("the slide", "the deck", a professor), and British spellings.

    python3 tools/check_pharm_e2.py [L4 L5 L6 L7 L8]
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pharm_e2_lib as L

REQ = {"indications": ("drug", "text", "edu", "tier", "slide", "verify"),
       "sideeffects": ("drug", "text", "monitor", "system", "slide", "verify"),
       "contra": ("drug", "text", "tier", "slide", "verify"),
       "kcz": ("effect", "drugs", "what", "slide", "verify"),
       "chart": ("cells", "slide", "verify")}
TIERS = {"indications": {"DOC", "IND", "EDU", "MON"}, "contra": {"ABS", "AVOID", "BBW", "NAMED", "CAUT"}}
BAD_TEXT = [(re.compile(r"\b\d+(\.\d+)?\s*(mg|mcg|µg|g)\b(?!\s*/\s*(dl|ml|g|kg)\b)(?!\s+of\s+(salt|sodium))", re.I), "milligram dose (doses are not tested)"),
            (re.compile(r"\b(the|this) (slide|lecture|deck|textbook)\b|\bDr\.? Wood\b|\bProf(essor|\.)", re.I), "names the source"),
            (re.compile(r"\b(choice|answer|option)s? [A-H]\b", re.I), "letter reference"),
            (re.compile(r"\b(color|flavor|edema|anemia|hemoglobin|esophag|pediatric|fetus|estrogen)\w*", re.I), None)]
BRIT = re.compile(r"\b(colour|flavour|oedema|anaemia|haemoglobin|paediatric|foetus|oestrogen|litre|behaviour|centre|programme|tumour)\w*", re.I)


def plain(s):
    return re.sub(r"<[^>]+>", " ", s)


def strings(kind, r):
    out = []
    for k, v in r.items():
        if k in ("verify", "slide", "tier", "bbw", "also", "allow_dose"):
            continue
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, list):
            out += [x for x in v if isinstance(x, str)]
    return out


def check(lec):
    d = L.load(lec)
    if d is None:
        print("%-4s (no data file yet)" % lec); return 0
    if L.LECTURES[lec]["deck"] is None:
        print("%-4s data present but its deck is not registered" % lec); return 1
    fails, n, subs = [], 0, 0
    nslides = L.slide_count(lec)
    for kind, r in L.iter_rows(d):
        n += 1
        base = "indications" if kind == "indications" else kind
        req = REQ["kcz" if kind.startswith("kcz") else base]
        label = (r.get("drug") or r.get("effect") or (r.get("cells") or ["?"])[0])[:50]
        miss = [k for k in req if k not in r or r[k] in ("", None, [])]
        if miss:
            fails.append((kind, label, "missing field(s): " + ", ".join(miss))); continue
        if kind in TIERS and r["tier"] not in TIERS[kind]:
            fails.append((kind, label, "bad tier %r" % r["tier"]))
        s = r["slide"]
        if not isinstance(s, int) or not 1 <= s <= nslides:
            fails.append((kind, label, "slide %r not in deck (1-%d)" % (s, nslides))); continue
        body = L.slide_text(lec, s)
        if not body:
            fails.append((kind, label, "slide %d has no text" % s)); continue
        for v in r["verify"]:
            subs += 1
            if L.norm(v) not in body:
                fails.append((kind, label, "NOT ON SLIDE %d: %r" % (s, v)))
        for j, extra in enumerate(r.get("also", [])):     # a chart row that draws on more than one slide
            es = extra.get("slide")
            if not isinstance(es, int) or not 1 <= es <= nslides or not extra.get("verify"):
                fails.append((kind, label, "bad 'also' entry %d" % j)); continue
            eb = L.slide_text(lec, es)
            for v in extra["verify"]:
                subs += 1
                if L.norm(v) not in eb:
                    fails.append((kind, label, "NOT ON SLIDE %d (also): %r" % (es, v)))
        for t in strings(kind, r):
            pt = plain(t)
            for rx, why in BAD_TEXT:
                if why and rx.search(pt) and not (r.get("allow_dose") and "milligram" in why):
                    fails.append((kind, label, "%s: %r" % (why, rx.search(pt).group(0))))
            if BRIT.search(pt):
                fails.append((kind, label, "British spelling: %r" % BRIT.search(pt).group(0)))
    print("%-4s rows: %3d   substrings: %4d   %s" % (lec, n, subs, "OK" if not fails else "FAILED %d" % len(fails)))
    for kind, label, why in fails[:60]:
        print("    [%s] %s -- %s" % (kind, label, why))
    return 1 if fails else 0


if __name__ == "__main__":
    which = sys.argv[1:] or L.lectures_present()
    rc = 0
    for lec in which:
        rc |= check(lec)
    sys.exit(rc)
