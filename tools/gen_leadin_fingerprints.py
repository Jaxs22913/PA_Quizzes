#!/usr/bin/env python3
"""Regenerate _cmse3_leadin_fp.py from the pools as they stand now.

Only run this after a DELIBERATE reorder of a pool. Running it to silence a
failing build would defeat the guard it exists to provide.
"""
import sys, os, importlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_leadins import LEADINS

lines = []
for mod in sorted({m for m, _ in LEADINS}):
    m = importlib.import_module(mod)
    P = [v for k, v in vars(m).items()
         if isinstance(v, list) and v and isinstance(v[0], dict) and "q" in v[0]][0]
    for (mm, i), _ in sorted(LEADINS.items()):
        if mm != mod:
            continue
        fp = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", P[i]["q"])).strip()[:46]
        lines.append('("%s", %d): %r,' % (mod, i, fp))
print("would write %d fingerprints" % len(lines))
