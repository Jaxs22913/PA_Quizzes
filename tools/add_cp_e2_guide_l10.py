#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Lecture 10 (Pathophysiology of Blood Disorders) to the Clinical Pathophysiology I
Exam 2 study guide, in place -- the same splice add_cp_e2_guide_l8_l9.py does for 8 and 9.

The page is never rebuilt from scratch (site-wide tools edit it in place). Section 10 goes
after the Lecture 8-9 block, its TOC entries after theirs, its Test-yourself bank as the last
key of TEST_YOURSELF. Idempotent: marker comments CPE2L10 / CPE2TOC10 / CPE2TY10.
Content lives in cp_e2_guide_content.py (BLOOD, TOC_L10, TEST_YOURSELF["blood"]).
Re-run tools/apply_guide_additions.py afterwards (rebuilt text drops applied lines).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cp_e2_guide_content as C
from build_cp_e2_guide import BANNED

ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "Clinical Pathophysiology I Exam 2")
GUIDE = os.path.join(DIR, "cp-exam-2-study-guide.html")

OLD_COVERS = ("Lecture 8, Immunity; and Lecture 9, Pulmonary Pathophysiology &middot; Lecture 10 is added "
              "when it is posted")
NEW_COVERS = ("Lecture 8, Immunity; Lecture 9, Pulmonary Pathophysiology; and Lecture 10, Pathophysiology "
              "of Blood Disorders")


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for tag in ("CPE2L10", "CPE2TOC10"):
        src = re.sub(r"<!--%s-->.*?<!--/%s-->\s*" % (tag, tag), "", src, flags=re.S)
    src = re.sub(r",\n<!--CPE2TY10-->.*?<!--/CPE2TY10-->", "", src, flags=re.S)

    body = C.BLOOD
    low = re.sub(r"<[^>]+>", " ", body).lower()
    for w in BANNED:
        assert w not in low, "management wording in guide: " + w
    for s in re.findall(r'src="(cp-exam-2-[^"]+)"', body):
        assert os.path.exists(os.path.join(DIR, s)), "missing figure " + s

    anchor = "<!--/CPE2L8L9-->\n"
    assert src.count(anchor) == 1
    src = src.replace(anchor, anchor + "<!--CPE2L10-->" + body.strip("\n") + "\n<!--/CPE2L10-->\n", 1)

    anchor = "<!--/CPE2TOC89-->\n"
    assert src.count(anchor) == 1
    src = src.replace(anchor, anchor + "<!--CPE2TOC10-->\n" + C.TOC_L10 + "<!--/CPE2TOC10-->\n", 1)

    qs = C.TEST_YOURSELF["blood"]
    assert all(len(q["choices"]) == 4 for q in qs)
    assert sorted(q["correct"] for q in qs) == [0, 0, 1, 1, 2, 2, 3, 3]
    anchor = "\n<!--/CPE2TY89-->"
    assert src.count(anchor) == 1
    blob = json.dumps({"blood": qs}, ensure_ascii=False, indent=1)[1:-1].strip("\n")
    src = src.replace(anchor, anchor + ",\n<!--CPE2TY10-->\n" + blob + "\n<!--/CPE2TY10-->", 1)

    if OLD_COVERS in src:
        src = src.replace(OLD_COVERS, NEW_COVERS, 1)
    assert NEW_COVERS in src, "header 'Covers' line not found"

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li", "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for m in re.finditer(r'href="#([a-z0-9-]+)"', src):
        assert 'id="%s"' % m.group(1) in src, "dangling TOC link " + m.group(1)
    brit = re.findall(r"(?i)\b\w*(?:haem|oedem|tumour|colour|centre|anaem|oesoph|isation|oris[ei]|ognis[ei]|analyse)\w*\b", body)
    assert not brit, "British spelling: %r" % sorted(set(brit))
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 10: %d subsections, %d figures, %d test-yourself questions"
          % (len(re.findall(r'<h3 class="sub" id="l10-', src)), body.count('<figure class="fig">'), len(qs)))


if __name__ == "__main__":
    main()
