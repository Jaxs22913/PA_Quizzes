#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert the Lecture 10 memory aid (the wall-building crew) into the PDM I Exam 2 study guide.

Jaxon, 2026-09-30, "do it how we usually do": teach a multi-part system as ONE connected
analogy where every player has a role (memory_aid_systems; the CMS lipoprotein 'garbage
system' is the precedent). The anchor is the lecturer's own brick-and-mortar picture
(platelets = bricks, clotting factors = mortar; recording part 1, ~12:05). It is labeled a
memory aid, lists where it breaks, and every role cites the deck slide that states the fact.

The fragment lives in tools/pdm_l10_memaid.html. This script APPENDS it as section 10.0 (before
10.1) plus a table-of-contents link, and is idempotent: both insertions are fenced in comment
markers and stripped before they are re-inserted. Re-run it after anything that regenerates
section 10 (tools/add_pdm_guide_l10.py strips and re-adds the whole section, which would
remove this fence), then rebuild the Word copy.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDE = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 2", "pdm-exam-2-study-guide.html")
FRAG = os.path.join(ROOT, "tools", "pdm_l10_memaid.html")

CSS = """<style>
  /* Memory-aid box, same look as the CMS lipoprotein garbage system: a story to hang deck facts
     on, visually distinct from .pearl/.callout and from the professor-emphasis marks. */
  .memaid{border:2px dashed #3f6e8c;border-radius:10px;padding:14px 16px 8px;margin:18px 0 16px;
          background:#eef5f9;position:relative;}
  .memaid-label{position:absolute;top:-12px;left:14px;background:#dcecf5;color:#234a63;
          font-size:.72rem;font-weight:800;letter-spacing:.4px;padding:2px 10px;border-radius:8px;
          border:1px solid #3f6e8c;text-transform:uppercase;}
  .memaid table{font-size:.86rem;}
  .memaid .breaks{background:#fff;border:1px solid #c6d9e6;border-radius:8px;padding:8px 12px;margin:10px 0 8px;}
  .memaid .breaks li{font-size:.86rem;}
  :root[data-theme="dark"] .memaid{background:#16232c;border-color:#5f93b5;}
  :root[data-theme="dark"] .memaid-label{background:#1f3443;color:#cfe4f2;border-color:#5f93b5;}
  :root[data-theme="dark"] .memaid .breaks{background:#101a21;border-color:#2c4354;}
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]) .memaid{background:#16232c;border-color:#5f93b5;}
    :root:not([data-theme="light"]) .memaid-label{background:#1f3443;color:#cfe4f2;border-color:#5f93b5;}
    :root:not([data-theme="light"]) .memaid .breaks{background:#101a21;border-color:#2c4354;}
  }
</style>
"""
TOC = '  <a href="#co-memaid">10.0 The wall-building crew (memory aid)</a>\n'


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for tag in ("PDMMEMAID10", "PDMMEMAIDTOC10"):
        src = re.sub(r"<!--%s-->.*?<!--/%s-->\s*" % (tag, tag), "", src, flags=re.S)
    frag = open(FRAG, encoding="utf-8").read().strip()
    anchor = '<h3 class="sub" id="co-define">'
    assert src.count(anchor) == 1
    src = src.replace(anchor, "<!--PDMMEMAID10-->" + CSS + "  " + frag + "\n<!--/PDMMEMAID10-->\n\n  " + anchor, 1)
    toc_anchor = '<a href="#co-define">'
    assert src.count(toc_anchor) == 1
    src = src.replace(toc_anchor, "<!--PDMMEMAIDTOC10-->" + TOC + "<!--/PDMMEMAIDTOC10-->  " + toc_anchor, 1)
    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li", "style"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert not re.findall(r"(?i)\b\w*(?:haem|oedem|tumour|colour|centre|anaem|oesoph)\w*\b", frag)
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("inserted section 10.0 memory aid (%d chars) and its TOC link" % len(frag))


if __name__ == "__main__":
    main()
