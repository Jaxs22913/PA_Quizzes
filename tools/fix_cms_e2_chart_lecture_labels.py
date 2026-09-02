#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Correct the lecture label on 30 rows of the ophthalmology comparison chart.

The chart's Condition column carries a small lecture badge -- L10, L11, L12 --
so that a bare slide number identifies something, because the five decks number
their slides independently. The badge is derived from the row's deck field:

    lect = {"11. Neuro-Ophthalmology": "L11",
            "12. Acute Vision Loss": "L12"}.get(deck, "L10")

Lectures 13 and 14 were added to the chart later and never added to that map,
so every one of their rows fell through to the DEFAULT and was labelled L10.
Thirty rows told the reader to look in the Common Ophthalmological Disorders
deck for a slide that is in Chronic Vision Loss & Tumors or Ocular Trauma:

    Chronic vision loss   9 rows      L10 -> L13
    Refractive            3 rows      L10 -> L13
    Ocular tumors         4 rows      L10 -> L13
    Ocular trauma        14 rows      L10 -> L14

Found while checking the pictures swapped in by swap_cms_e2_better_photos.py:
the lid-laceration row cited "Slide 29" under a badge reading L10, and slide 29
of Lecture 10 is a subconjunctival haemorrhage.

Fixes the generator's map, the legend paragraph that still said "three decks",
and the rendered chart, which is not rebuilt from scratch here for the same
reason the guide is not.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHART = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2",
                     "cms-ophtho-comparison-chart.html")
BUILDER = os.path.join(ROOT, "tools", "build_cms_ophtho_chart.py")

# chart group -> correct lecture badge
GROUP_LECT = {
    "Chronic vision loss": "L13",
    "Refractive": "L13",
    "Ocular tumors": "L13",
    "Ocular trauma": "L14",
}

NEW_LEGEND = (
    "<b>The Slide column names the lecture.</b> This chart spans five decks &mdash;\n"
    "<b>L10</b> Common Ophthalmological Disorders, <b>L11</b> Neuro-Ophthalmology, <b>L12</b> Acute\n"
    "Vision Loss, <b>L13</b> Chronic Vision Loss &amp; Tumors and <b>L14</b> Ocular Trauma &mdash; so a\n"
    "bare slide number no longer identifies anything on its own. Pictures from every deck after the\n"
    "first are filed under an <i>l11-</i>, <i>l12-</i>, <i>l13-</i> or <i>l14-</i> filename for the same\n"
    "reason: the five decks number their slides independently, and without the prefix four figures\n"
    "resolved to the wrong Lecture 10 photographs.")


def fix_builder():
    s = open(BUILDER, encoding="utf-8").read()
    old = ('        lect = {"11. Neuro-Ophthalmology": "L11",\n'
           '                "12. Acute Vision Loss": "L12"}.get(deck, "L10")')
    new = ('        # Every deck must be listed. Lectures 13 and 14 were added to the\n'
           '        # chart without being added here, so all 30 of their rows fell\n'
           '        # through to the default and claimed to be Lecture 10 slides.\n'
           '        lect = {"11. Neuro-Ophthalmology": "L11",\n'
           '                "12. Acute Vision Loss": "L12",\n'
           '                "Chronic Vision Loss & Tumors": "L13",\n'
           '                "CMS I Ocular Trauma": "L14"}.get(deck, "L10")')
    assert s.count(old) == 1, "builder line not found -- has it already been fixed?"
    s = s.replace(old, new)

    old_legend = (
        "<b>The Slide column names the lecture.</b> This chart now spans three decks &mdash;\n"
        "<b>L10</b> Common Ophthalmological Disorders, <b>L11</b> Neuro-Ophthalmology and <b>L12</b> Acute\n"
        "Vision Loss &mdash; so a bare slide number no longer identifies anything on its own. Lecture 11 and\n"
        "12 pictures are filed under <i>l11-</i> and <i>l12-</i> filenames for the same reason: the three\n"
        "decks number their slides independently, and without the prefix four figures resolved to the wrong\n"
        "Lecture 10 photographs.")
    assert s.count(old_legend) == 1, "legend paragraph not found"
    s = s.replace(old_legend, NEW_LEGEND)
    open(BUILDER, "w", encoding="utf-8").write(s)
    print("  build_cms_ophtho_chart.py: deck map and legend corrected")


def fix_chart():
    s = open(CHART, encoding="utf-8").read()
    n = 0

    def one_row(m):
        nonlocal n
        want = GROUP_LECT.get(m.group(1))
        if not want or m.group(2) == want:
            return m.group(0)
        n += 1
        return m.group(0).replace('<b class="lect">%s</b>' % m.group(2),
                                  '<b class="lect">%s</b>' % want, 1)

    s = re.sub(r'<tr data-g="([^"]*)".*?<b class="lect">([^<]*)</b>', one_row, s, flags=re.S)
    # The legend paragraph named three decks and explained the l11-/l12-
    # filename prefixes; it is rewritten whole rather than patched, because
    # every sentence in it counted the decks.
    old_legend = (
        "<b>The Slide column names the lecture.</b> This chart now spans three decks &mdash;\n"
        "<b>L10</b> Common Ophthalmological Disorders, <b>L11</b> Neuro-Ophthalmology and <b>L12</b> Acute\n"
        "Vision Loss &mdash; so a bare slide number no longer identifies anything on its own. Lecture 11 and\n"
        "12 pictures are filed under <i>l11-</i> and <i>l12-</i> filenames for the same reason: the three\n"
        "decks number their slides independently, and without the prefix four figures resolved to the wrong\n"
        "Lecture 10 photographs.")
    assert s.count(old_legend) == 1, "legend paragraph not found in the chart"
    s = s.replace(old_legend, NEW_LEGEND)
    open(CHART, "w", encoding="utf-8").write(s)
    print("  cms-ophtho-comparison-chart.html: %d row badges corrected" % n)
    return n


def verify():
    s = open(CHART, encoding="utf-8").read()
    bad = []
    for m in re.finditer(r'<tr data-g="([^"]*)".*?<td class="nm"><b>(.*?)</b>.*?<b class="lect">([^<]*)</b>',
                         s, re.S):
        want = GROUP_LECT.get(m.group(1))
        if want and m.group(3) != want:
            bad.append((m.group(2), m.group(3), want))
    assert not bad, bad
    print("  verified: every row in a relabelled group now carries its own lecture")


if __name__ == "__main__":
    fix_builder()
    fix_chart()
    verify()
