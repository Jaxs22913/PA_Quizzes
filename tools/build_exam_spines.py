#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Give every exam accordion on the homepage a spine in its own colour.

Jaxon, 2026-09-02: "Every exam already owns a palette -- derm is teal, ophtho
is blue-violet -- but the homepage doesn't use any of it. A 3px left edge in
each block's own colour makes them read as distinct places instead of rows."

NO NEW HEXES ARE INVENTED, per [[site_design_tokens]]. The colour is each
exam's own `--indigo`, read out of its rendered quiz pages -- the mid-tone of
the four-slot quiz palette, and the one Jaxon was describing: Clinical Medicine
and Surgery I Exam 1 is #3f7d7a (teal), Exam 2 is #5566b5 (blue-violet).
`--navy` was tried first and rejected: those are header-gradient darks sitting
at lightness 0.17-0.33, which all read as near-black in a 3px line.

The dark-mode variant follows the transform the homepage already applies to its
tab hues -- measured across all seven of them at a mean of +0.057 lightness --
with a floor of 0.42 so the darkest palettes stay visible on a dark card.

The accordion's folder is resolved from its own first quiz link rather than
from a table kept here, so a new exam needs no edit to this file.

Writes a generated block into home.css between the two markers. Re-run after
adding an exam or changing an exam's palette.
"""
import colorsys, glob, os, re, sys
from collections import Counter
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
INDEX = os.path.join(ROOT, "index.html")
CSS = os.path.join(ROOT, "home.css")

BEGIN = "    /* --- BEGIN generated exam spines (tools/build_exam_spines.py) --- */"
END = "    /* --- END generated exam spines --- */"

DARK_LIFT = 0.057     # mean of the seven light->dark tab-hue pairs in home.css
DARK_FLOOR = 0.42     # below this a spine disappears against a dark card

SECTION = re.compile(r'<details class="exam-section" data-examid="([^"]+)"(.*?)</details>', re.S)
LINK = re.compile(r'href="([^"]+?)/[^"/]+\.html"')
INDIGO = re.compile(r'--indigo:\s*(#[0-9a-fA-F]{6})')


def hex_to_hls(h):
    h = h.lstrip("#")
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return colorsys.rgb_to_hls(r, g, b)


def hls_to_hex(hh, ll, ss):
    r, g, b = colorsys.hls_to_rgb(hh, max(0.0, min(1.0, ll)), ss)
    return "#%02x%02x%02x" % tuple(round(c * 255) for c in (r, g, b))


def folder_colour(folder):
    """The --indigo the folder's own quiz pages agree on."""
    found = []
    for f in glob.glob(glob.escape(folder) + "/*.html"):
        try:
            m = INDIGO.search(open(f, encoding="utf-8").read())
        except OSError:
            continue
        if m:
            found.append(m.group(1).lower())
    if not found:
        return None, 0, 0
    top, n = Counter(found).most_common(1)[0]
    return top, n, len(found)


def main():
    src = open(INDEX, encoding="utf-8").read()
    rows, unresolved = [], []
    for m in SECTION.finditer(src):
        examid, body = m.group(1), m.group(2)
        link = LINK.search(body)
        if not link:
            unresolved.append((examid, "no quiz link"))
            continue
        folder = unquote(link.group(1))
        if not os.path.isdir(folder):
            unresolved.append((examid, "folder %r not found" % folder))
            continue
        col, agree, total = folder_colour(folder)
        if not col:
            unresolved.append((examid, "no --indigo in %s" % folder))
            continue
        hh, ll, ss = hex_to_hls(col)
        dark = hls_to_hex(hh, max(ll + DARK_LIFT, DARK_FLOOR), ss)
        rows.append((examid, folder, col, dark, agree, total))

    rows.sort(key=lambda r: r[1])
    light = "\n".join('    .exam-section[data-examid="%s"] { --exam-spine: %s; }' % (r[0], r[2])
                      for r in rows)
    darkc = "\n".join(':root[data-theme="dark"] .exam-section[data-examid="%s"] { --exam-spine: %s; }'
                      % (r[0], r[3]) for r in rows)
    block = "\n".join([
        BEGIN,
        "    /* Each exam's own --indigo, lifted by %.3f lightness for dark mode" % DARK_LIFT,
        "       (floor %.2f) -- the same treatment the tab hues above get. */" % DARK_FLOOR,
        light,
        darkc,
        END,
    ])

    css = open(CSS, encoding="utf-8").read()
    if BEGIN in css and END in css:
        css = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block, css, flags=re.S)
    else:
        anchor = '.tab-btn[data-tab="physio"]'
        i = css.find(anchor)
        assert i > 0, "could not find the tab-hue block to sit next to"
        j = css.rfind("\n", 0, i)
        css = css[:j] + "\n" + block + "\n" + css[j:]
    open(CSS, "w", encoding="utf-8").write(css)

    for examid, folder, col, dark, agree, total in rows:
        flag = "" if agree == total else "   (%d/%d files agree)" % (agree, total)
        print("  %-30s %-44s %s -> %s%s" % (examid, folder[:44], col, dark, flag))
    if unresolved:
        print("\nno spine for %d section(s):" % len(unresolved))
        for examid, why in unresolved:
            print("  %-30s %s" % (examid, why))
    print("\n%d exam spines written to home.css" % len(rows))


if __name__ == "__main__":
    main()
