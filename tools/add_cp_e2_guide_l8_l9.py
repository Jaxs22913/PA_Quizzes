#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Lecture 8 (Immunity) and Lecture 9 (Pulmonary) to the Clinical Pathophysiology I
Exam 2 study guide, in place.

build_cp_e2_guide.py made the page from Lectures 6-7, but the page has since been edited
by site-wide tools (guide additions, the truth pass, the "Also tested" fold), so it is
never rebuilt from scratch. This script splices the two new sections in instead, between
the Vascular section and the page footer, the same way add_pdm_guide_l10.py does.
Idempotent: re-running replaces what an earlier run inserted (marker comments
CPE2L8L9 / CPE2TOC89 / CPE2TY89).

Content (sections, TOC entries, Test-yourself banks) lives in cp_e2_guide_content.py.
Mechanism only (clin_path_exam_spec): the management words of build_cp_e2_guide.BANNED
are asserted absent.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cp_e2_guide_content as C
from build_cp_e2_guide import BANNED

ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "Clinical Pathophysiology I Exam 2")
GUIDE = os.path.join(DIR, "cp-exam-2-study-guide.html")

OLD_COVERS = ("<p>Covers Lecture 6, Cardiac Pathophysiology, and Lecture 7, Vascular Pathophysiology "
              "&middot; Lectures 8&ndash;10 are added as each is posted")
NEW_COVERS = ("<p>Covers Lecture 6, Cardiac Pathophysiology; Lecture 7, Vascular Pathophysiology; "
              "Lecture 8, Immunity; and Lecture 9, Pulmonary Pathophysiology &middot; Lecture 10 is added "
              "when it is posted")


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for tag in ("CPE2L8L9", "CPE2TOC89"):
        src = re.sub(r"<!--%s-->.*?<!--/%s-->\s*" % (tag, tag), "", src, flags=re.S)
    src = re.sub(r",\n<!--CPE2TY89-->.*?<!--/CPE2TY89-->", "", src, flags=re.S)

    body = C.IMMUNITY + C.PULMONARY
    low = re.sub(r"<[^>]+>", " ", body).lower()
    for w in BANNED:
        assert w not in low, "management wording in guide: " + w
    for s in re.findall(r'src="(cp-exam-2-[^"]+)"', body):
        assert os.path.exists(os.path.join(DIR, s)), "missing figure " + s

    # Sections go after the Vascular section, before the page footer.
    anchor = '<footer class="guide-foot">\n  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html"'
    assert src.count(anchor) == 1, "page footer anchor not found once"
    src = src.replace(anchor, "<!--CPE2L8L9-->" + body.strip("\n") + "\n<!--/CPE2L8L9-->\n\n" + anchor, 1)

    navend = src.index("</nav>")
    src = src[:navend] + "<!--CPE2TOC89-->\n" + C.TOC_L8_L9 + "<!--/CPE2TOC89-->\n" + src[navend:]

    # Test-yourself banks: appended as the last keys of the TEST_YOURSELF object.
    ty = {k: C.TEST_YOURSELF[k] for k in ("immunity", "pulmonary")}
    for key, qs in ty.items():
        pos = [q["correct"] for q in qs]
        assert all(len(q["choices"]) == 4 for q in qs), key
        assert sorted(pos) == [0, 0, 1, 1, 2, 2, 3, 3], (key, pos)
    start = src.index("var TEST_YOURSELF = {")
    tyend = start + re.search(r"\n *\};\n</script>", src[start:]).start()
    blob = json.dumps(ty, ensure_ascii=False, indent=1)[1:-1].strip("\n")
    src = src[:tyend] + ",\n<!--CPE2TY89-->\n" + blob + "\n<!--/CPE2TY89-->" + src[tyend:]

    if OLD_COVERS in src:
        src = src.replace(OLD_COVERS, NEW_COVERS, 1)
    assert NEW_COVERS in src, "header 'Covers' line not found"

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li", "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for m in re.finditer(r'href="#([a-z0-9-]+)"', src):
        assert 'id="%s"' % m.group(1) in src, "dangling TOC link " + m.group(1)
    brit = re.findall(r"(?i)\b\w*(?:haem|oedem|tumour|colour|centre|anaem|oesoph|isation|oris[ei]|ognis[ei]|analyse)\w*\b", body)
    brit = [w for w in brit if w.lower() not in ("haemophilus",)]
    assert not brit, "British spelling: %r" % sorted(set(brit))
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added sections 8 and 9: %d + %d subsections, %d figures, %d test-yourself questions"
          % (len(re.findall(r'<h3 class="sub" id="l8-', src)), len(re.findall(r'<h3 class="sub" id="l9-', src)),
             body.count('<figure class="fig">'), sum(len(v) for v in ty.values())))


if __name__ == "__main__":
    main()
