#!/usr/bin/env python3
"""Build the CMS I Exam 7 study guide from per-lecture fragments.

    python3 tools/build_cms_e7_guide.py

Exam 7 (Respiratory Block Exam II, Lectures 39-45) is built by more than one builder, one or two lectures at a
time, so the guide is assembled rather than hand-edited:

  tools/cms_e7_guide/_head.html   page head + styles (the previous exam's shell, bronze palette)
  tools/cms_e7_guide/_tail.html   footer + scripts + condition-block styles
  tools/cms_e7_guide/lNN.html     one <section class="deck"> per lecture (l39.html, l40.html, ...)

Each fragment is a complete section: h2.deck-title, the verbatim io-box, the emphasis and slide-conflict
callouts, h3.sub subsections with ids "lNN-...", and its condition blocks. The section number is fixed by the
lecture (Lecture 39 is 1, 40 is 2 ... 45 is 7), so a fragment can be written before the lectures ahead of it
exist. The table of contents is generated from the fragments: every h3.sub with an id, and every .prof-flag
that carries id + data-toc (shown starred). See tools/cms_e7_README.md for adding a lecture.

After building, the page's dark palette is written (dark_tokens.apply, this page only). Then rebuild the Word copy, guide links and
Pip data as the README says.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "cms_e7_guide")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-exam-7-study-guide.html")
FIRST, LAST = 39, 45


def fragments():
    out = []
    for n in range(FIRST, LAST + 1):
        p = os.path.join(SRC, "l%d.html" % n)
        if os.path.exists(p):
            out.append((n, open(p, encoding="utf-8").read().strip()))
    return out


def toc(frags):
    rows = []
    for n, html in frags:
        m = re.search(r'<section class="deck" id="([^"]+)">\s*<h2 class="deck-title">(.*?)</h2>', html, re.S)
        assert m, "l%d.html must open with <section class=\"deck\" id=...><h2 class=\"deck-title\">" % n
        sec, title = m.group(1), m.group(2).strip()
        assert title.startswith("%d &middot;" % (n - FIRST + 1)), "l%d.html: section must be numbered %d" % (n, n - FIRST + 1)
        rows.append('  <a class="top-link" href="#%s">%s</a>' % (sec, title))
        for t in re.finditer(r'<h3 class="sub" id="([^"]+)">(.*?)</h3>|<div class="prof-flag" id="([^"]+)" data-toc="([^"]+)"', html, re.S):
            if t.group(1):
                assert t.group(1).startswith("l%d-" % n), "l%d.html: id %r must start with l%d-" % (n, t.group(1), n)
                rows.append('  <a class="sub-link" href="#%s">%s</a>' % (t.group(1), t.group(2).replace(" &middot; ", " ")))
            else:
                rows.append('  <a class="sub-link" href="#%s">&nbsp;&nbsp;&#9733; %s</a>' % (t.group(3), t.group(4)))
    return "\n".join(rows)


def header(frags):
    nums = [n for n, _ in frags]
    have = ", ".join(str(n) for n in nums)
    todo = [n for n in range(FIRST, LAST + 1) if n not in nums]
    more = ((" &middot; Lecture %d is added when it is built" % todo[0]) if len(todo) == 1 else
            (" &middot; Lectures %s are added as they are built" % ", ".join(str(n) for n in todo))) if todo else " &middot; <b>All seven lectures</b>"
    return ("""<header class="top">
  <h1>Clinical Medicine and Surgery I &middot; Exam 7 &mdash; Study Guide</h1>
  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028</p>
  <p>Respiratory Block Exam II (Lectures 39&ndash;45) &middot; Monday 16 November 2026 &middot; Lectures in this guide: %s%s &middot; Instructional Objectives verbatim</p>
  <p class="hdr-note">&#9733; Starred boxes and highlighted phrases carry each lecturer&rsquo;s emphasis from the lecture recording (our transcript cross-checked against Notability&rsquo;s, or the lecturer&rsquo;s own narration); every fact still comes from the slides</p>
  <div class="hdr-links"><a href="cms-exam-7-cram-sheet.html">Cram sheet</a><a href="cms-exam-7-clin-med-pro-guide.html">Clin Med Pro guide</a></div>
</header>
""" % (have, more))


def main():
    frags = fragments()
    assert frags, "no fragments in tools/cms_e7_guide/"
    head = open(os.path.join(SRC, "_head.html"), encoding="utf-8").read()
    tail = open(os.path.join(SRC, "_tail.html"), encoding="utf-8").read()
    body = (header(frags) + '\n<div class="layout wrap" data-readable>\n<nav class="toc">\n' + toc(frags)
            + '\n</nav>\n<main>\n\n' + "\n\n".join(h for _, h in frags) + "\n\n" + tail)
    page = head + body
    ids = re.findall(r'\sid="([^"]+)"', page)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    assert not dup, "duplicate ids: %s" % dup
    for href in re.findall(r'href="#([^"]+)"', page):
        assert href in ids, "dangling link #%s" % href
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(page)
    print("wrote %s  (lectures %s, %d bytes)" % (os.path.relpath(OUT, ROOT), [n for n, _ in frags], len(page)))
    # This page only: dark_tokens.py's own main() rewrites every stale page on the site.
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import dark_tokens
    s = open(OUT, encoding="utf-8").read()
    new = dark_tokens.apply(s, dark_tokens.classify(s))
    assert "data-dark=" in new, "dark_tokens could not read the page palette"
    open(OUT, "w", encoding="utf-8").write(new)
    print("dark tokens: written")
    print("next: python3 tools/apply_guide_additions.py && python3 tools/check_guide_additions_inline.py "
          "(a rebuild drops the added lines), then tools/build_guide_links.py")


if __name__ == "__main__":
    main()
