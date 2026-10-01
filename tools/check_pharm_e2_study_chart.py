#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fact-check tools/pharm_e2_study_chart.json (Jaxon's filled "Pharmacology Drug Study Chart", Exam 2) against the decks.

One row per drug class, seven columns (class, generic names, mechanism of action, indications, contraindications,
adverse effects, special warning). Every row must:

  * cite slides that exist in its lecture's deck (Lectures 4-8 = Dr. Adam Wood's Ophthalmology, ENT, Antihypertensives,
    Lipids and Myocardial Ischemia decks) and use every slide it cites;
  * carry a verify proof [field, slide, substring(, lecture)] for EVERY cell (moa, indications, contraindications,
    adverse, warning) except a cell that is declared in "absent" and says "None listed." / "Not given ..." - the
    substring must appear on that slide (runs joined or spaced, smart quotes and dashes normalized; picture-only slides
    use the transcription in the file's own extra_text);
  * name generics that appear on the cited slides (3 or more, or fewer with the builder printing "Only N named in the
    lecture");
  * carry no milligram dose (Dr. Wood: doses are not tested; allow_dose is for the one 4 gram limit he told us to know),
    no abbreviation without its full term in the same cell, no British spelling, no words naming the source, no letter
    references;
  * flag any black box warning the slides do not mention with the sentence "FDA (Food and Drug Administration) boxed
    warning" and boxed_not_on_slides, exactly as the other Exam 2 reference pages do.

    python3 tools/check_pharm_e2_study_chart.py
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pharm_e2_lib as L

DATA = os.path.join(HERE, "pharm_e2_study_chart.json")
FIELDS = ("moa", "indications", "contraindications", "adverse", "warning")
KINDS = ("bbw", "special", "none")
ABSENT_OK = re.compile(r"^(None listed|Not given|None stressed)", re.I)
BOXED = "FDA (Food and Drug Administration) boxed warning"

DOSE = re.compile(r"\b\d+(\.\d+)?\s*(mg|mcg|µg|g)\b(?!\s*/\s*(dl|ml|g|kg)\b)", re.I)
SOURCE = re.compile(r"\b(the|this) (slide|deck|textbook)s?\b|\b(the|this) lecture\b|\bDr\.? Wood\b|\bProf(essor|\.)", re.I)
SOURCE_OK = re.compile(r"\b(not (stated|given|listed) in (the|this) lecture)\b", re.I)
LETTER = re.compile(r"\b(choice|answer|option)s? [A-H]\b", re.I)
BRIT = re.compile(r"\b(colour|flavour|oedema|anaemia|haemoglobin|paediatric|foetus|oestrogen|litre|behaviour|centre|programme|tumour|diarrhoea|haemorrhage|anaesthe|oesophag|ischaemi|haem[aeo])\w*", re.I)
TOKEN = re.compile(r"\b[A-Z]{2,}[A-Z0-9]*\b")
TOKEN_OK = {"QT", "ST", "II", "III", "IV", "NOT", "NEVER", "AND", "ONLY", "P450"}   # ST/QT are ECG labels (like QRS); P450 sits inside "cytochrome P450"; the rest is emphasis
STOPWORDS = {"with", "plus", "and", "the"}


def plain(s):
    return re.sub(r"<[^>]+>", " ", s)


def slide_body(lec, n, extra):
    body = L.slide_text(lec, n)
    e = extra.get("%s|%d" % (lec, n))
    if e:
        body = body + " " + L.norm(e) + " " + re.sub(r"\s+", "", L.norm(e))
    return body


def unexpanded(cell):
    bad = []
    for m in TOKEN.finditer(cell):
        t = m.group(0)
        if t in TOKEN_OK:
            continue
        if (t + " (") in cell or ("(" + t + ")") in cell or ("(" + t + ",") in cell or re.search(re.escape(t) + r"(-\w+)+ \(", cell):
            continue
        bad.append(t)
    return sorted(set(bad))


def check(verbose=True):
    d = json.load(open(DATA, encoding="utf-8"))
    extra = d.get("extra_text", {})
    rows = d["rows"]
    fails, subs = [], 0
    nslide = {l: L.slide_count(l) for l in L.LECTURES}
    per, short, bbw = {}, [], 0
    for i, r in enumerate(rows):
        lab = "%s #%d %s" % (r.get("lecture"), i + 1, (r.get("class") or "?")[:46])
        def F(msg):
            fails.append((lab, msg))
        lec = r.get("lecture")
        if lec not in L.LECTURES:
            F("bad lecture %r" % lec); continue
        per[lec] = per.get(lec, 0) + 1
        for k in ("class", "moa", "indications", "contraindications", "adverse", "warning", "warning_kind", "slides", "verify", "generics"):
            if r.get(k) in (None, "", []):
                F("missing/empty field %s" % k)
        if r.get("warning_kind") not in KINDS:
            F("bad warning_kind %r" % r.get("warning_kind"))
        gen = r.get("generics") or []
        if len(gen) < 3:
            short.append((lab, len(gen)))
        slides = r.get("slides") or []
        for s in slides:
            if not isinstance(s, int) or not 1 <= s <= nslide[lec]:
                F("slide %r not in %s deck (1-%d)" % (s, lec, nslide[lec]))
        # ---- verify proofs
        used, have = set(), {}
        cross = []
        for v in r.get("verify") or []:
            if not (isinstance(v, list) and len(v) in (3, 4)):
                F("bad verify entry %r" % (v,)); continue
            f, s, t = v[0], v[1], v[2]
            vl = v[3] if len(v) == 4 else lec
            if f not in FIELDS + ("class", "generics"):
                F("verify field %r unknown" % f)
            if vl not in L.LECTURES or not isinstance(s, int) or not 1 <= s <= nslide[vl]:
                F("verify slide %r not in %s deck" % (s, vl)); continue
            subs += 1
            if L.norm(t) not in slide_body(vl, s, extra):
                F("NOT ON %s SLIDE %d [%s]: %r" % (vl, s, f, t))
            have[f] = have.get(f, 0) + 1
            if vl == lec:
                used.add(s)
                if s not in slides:
                    F("verify cites slide %d but it is not in the row's slides list" % s)
            else:
                cross.append((vl, s))
        for s in slides:
            if s not in used and not any(True for _ in ()):
                F("slide %d listed but no verify entry uses it" % s)
        absent = set(r.get("absent") or [])
        for f in FIELDS:
            txt = r.get(f) or ""
            if f == "warning" and r.get("warning_kind") == "none":
                if not ABSENT_OK.match(txt):
                    F("warning_kind none but the cell does not say None stressed")
                continue
            if f in absent:
                if not ABSENT_OK.match(txt):
                    F("%s is declared absent but does not start None listed / Not given" % f)
            elif not have.get(f) and not (f == "warning" and r.get("warning_kind") == "bbw" and r.get("boxed_not_on_slides")):
                F("cell %s has no verify proof" % f)
        # ---- generics on the cited slides
        texts = " ".join(slide_body(lec, s, extra) for s in slides) + " " + " ".join(slide_body(vl, s, extra) for vl, s in cross)
        for g in gen:
            parts = g.split("|")
            disp, aliases = parts[0], parts[1:]
            need = aliases or [w for w in re.findall(r"[A-Za-z][A-Za-z\-]{4,}", L.norm(disp)) if w not in STOPWORDS]
            for w in need:
                if L.norm(w) not in texts:
                    F("generic %r: %r is not on the cited slides" % (disp, w))
        # ---- warning bookkeeping
        wk = r.get("warning_kind")
        if wk == "bbw":
            bbw += 1
            if not r.get("boxed_not_on_slides") or BOXED not in r.get("warning", ""):
                F("bbw row must set boxed_not_on_slides and say %r" % BOXED)
        elif BOXED in r.get("warning", "") or "boxed warning" in r.get("warning", "").lower():
            F("mentions a boxed warning but warning_kind is not bbw")
        # ---- content rules on every cell
        cells = [("class", r.get("class", "")), ("generics", ", ".join(g.split("|")[0] for g in gen)), ("generics_note", r.get("generics_note", ""))] + [(f, r.get(f, "")) for f in FIELDS]
        for f, txt in cells:
            pt = plain(txt)
            words = len(pt.split())
            if f in FIELDS and words > 62:
                F("%s has %d words (limit about 60 for a one-glance chart)" % (f, words))
            m = DOSE.search(pt)
            if m and not r.get("allow_dose"):
                F("%s: milligram dose %r (doses are not tested)" % (f, m.group(0)))
            if f != "generics_note":
                sm = SOURCE.search(SOURCE_OK.sub("", pt))
                if sm:
                    F("%s names the source: %r" % (f, sm.group(0)))
            if LETTER.search(pt):
                F("%s: letter reference" % f)
            if BRIT.search(pt):
                F("%s: British spelling %r" % (f, BRIT.search(pt).group(0)))
            ub = unexpanded(pt)
            if ub and f != "generics":
                F("%s: abbreviation without its full term %s" % (f, ub))
    if verbose:
        print("rows: %d  %s   proofs: %d   black box rows: %d   classes with fewer than 3 generics: %d"
              % (len(rows), " ".join("%s=%d" % (k, per[k]) for k in sorted(per)), subs, bbw, len(short)))
        for lab, n in short:
            print("    only %d generic(s): %s" % (n, lab))
        print("OK" if not fails else "FAILED %d" % len(fails))
        for lab, why in fails[:80]:
            print("    [%s] %s" % (lab, why))
    return not fails, d


if __name__ == "__main__":
    sys.exit(0 if check()[0] else 1)
