#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repair the urgency badge colour on the ophthalmology comparison chart.

The badge that says how fast a condition must be seen is coloured by class:
.u.emerg dark red, .u.sameday orange, .u.urg amber, .u.rout green. The builder
picks the class with

    urg_cls = ("emerg" if "EMERGENT" in urg else
               "sameday" if "SAME DAY" in urg else
               "urg" if urg.startswith("Urgent") or "URGENT" in urg else "rout")

-- an UPPERCASE test. Lectures 10-12 write "EMERGENT"; Lectures 13 and 14,
added later, write "Emergent" and "Same day" in title case, so all of those fell
through to the default and were rendered in the ROUTINE GREEN.

Twenty-one rows were affected, and every one of them made an emergency look
routine on the chart students use to triage: retinal detachment, both artery
occlusions, giant cell arteritis, retinoblastoma, open globe injury, globe
rupture, hyphema and the rest. One row went the other way, showing a "Routine"
badge in the urgent amber.

The comparison is now case-insensitive, so a lecture written in any case lands
in the right colour.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHART = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2",
                     "cms-ophtho-comparison-chart.html")
BUILDER = os.path.join(ROOT, "tools", "build_cms_ophtho_chart.py")

WANT = {"emergent": "emerg", "same day": "sameday",
        "urgent": "urg", "routine": "rout"}


def fix_builder():
    s = open(BUILDER, encoding="utf-8").read()
    old = ('        urg_cls = ("emerg" if "EMERGENT" in urg else\n'
           '                   "sameday" if "SAME DAY" in urg else\n'
           '                   "urg" if urg.startswith("Urgent") or "URGENT" in urg else "rout")')
    new = ('        # CASE-INSENSITIVE. The uppercase-only test this replaces sent every\n'
           '        # Lecture 13 and 14 row -- which write "Emergent" and "Same day" in\n'
           '        # title case -- to the "rout" default, colouring twenty-one\n'
           '        # emergencies in the routine green.\n'
           '        _u = urg.upper()\n'
           '        urg_cls = ("emerg" if "EMERGENT" in _u else\n'
           '                   "sameday" if "SAME DAY" in _u else\n'
           '                   "urg" if "URGENT" in _u else "rout")')
    assert s.count(old) == 1, "builder classifier not found -- already fixed?"
    open(BUILDER, "w", encoding="utf-8").write(s.replace(old, new))
    print("  build_cms_ophtho_chart.py: classifier made case-insensitive")


def fix_chart():
    s = open(CHART, encoding="utf-8").read()
    n = [0]

    def repl(m):
        cls, text = m.group(1), m.group(2)
        plain = re.sub(r"<[^>]+>", "", text)
        plain = re.sub(r"&[a-z]+;", " ", plain).strip().lower()
        want = None
        for key, c in WANT.items():
            if plain.startswith(key):
                want = c
                break
        if want and want != cls:
            n[0] += 1
            return '<span class="u %s">%s</span>' % (want, text)
        return m.group(0)

    s = re.sub(r'<span class="u ([a-z]+)">(.*?)</span>', repl, s, flags=re.S)
    open(CHART, "w", encoding="utf-8").write(s)
    print("  cms-ophtho-comparison-chart.html: %d badge colours corrected" % n[0])
    return n[0]


def verify():
    s = open(CHART, encoding="utf-8").read()
    bad = []
    for m in re.finditer(r'<span class="u ([a-z]+)">(.*?)</span>', s, re.S):
        plain = re.sub(r"&[a-z]+;", " ", re.sub(r"<[^>]+>", "", m.group(2))).strip().lower()
        for key, c in WANT.items():
            if plain.startswith(key) and c != m.group(1):
                bad.append((plain[:24], m.group(1), c))
    assert not bad, bad
    print("  verified: every badge's colour now matches its word")


if __name__ == "__main__":
    fix_builder()
    fix_chart()
    verify()
