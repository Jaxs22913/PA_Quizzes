#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Microbiology Exam 2 Arcade decks -- Lectures 7 to 10.

Cards derived from the question pools (see add_pdm_e2_arcade.py for why, and
for the check that derivation makes possible). Microbiology had no Exam 2
group entry before this.

ATOMIC FACTS ONLY. Idempotent: fenced between markers, re-runnable.
Lectures 9 and 10 read their cards from tools/micro_e2/l9_cards.json and
l10_cards.json (one deck per lecture, keyed by deck id).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from _arcade_add import apply

SHIELD_ICON = ('<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>'
               '<path d="M9 12l2 2 4-4"/>')
COCCI_ICON = ('<circle cx="7" cy="8" r="2.5"/><circle cx="12" cy="7" r="2.5"/>'
              '<circle cx="9.5" cy="12" r="2.5"/><circle cx="15" cy="11.5" r="2.5"/>'
              '<circle cx="12.5" cy="16.5" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>')
ROD_ICON = ('<rect x="3" y="9.5" width="8" height="5" rx="2.5"/>'
            '<rect x="13" y="9.5" width="8" height="5" rx="2.5"/>'
            '<circle cx="17" cy="12" r="1.2"/>')
DISH_ICON = ('<circle cx="12" cy="12" r="8.5"/><path d="M6 9h12"/>'
             '<circle cx="9.5" cy="13" r="1"/><circle cx="14" cy="14.5" r="1"/>'
             '<circle cx="13" cy="11" r="1"/>')

C = json.load(open(os.path.join(HERE, "micro_e2_cards.json"), encoding="utf-8"))
for frag in ("l9_cards.json", "l10_cards.json"):
    C.update(json.load(open(os.path.join(HERE, "micro_e2", frag), encoding="utf-8")))
DECKS = [
 ("micro-immunity-disorders", "Disorders in Immunity", "accent2", SHIELD_ICON,
  [tuple(x) for x in C["micro-immunity-disorders"]]),
 ("micro-diagnosing-infections", "Diagnosing Infections", "accent4", DISH_ICON,
  [tuple(x) for x in C["micro-diagnosing-infections"]]),
 ("micro-cocci", "Cocci of Medical Importance", "accent1", COCCI_ICON,
  [tuple(x) for x in C["micro-cocci"]]),
 ("micro-gram-positive-bacilli", "Gram-Positive Bacilli", "accent3", ROD_ICON,
  [tuple(x) for x in C["micro-gram-positive-bacilli"]]),
]
if __name__ == "__main__":
    apply("MICROE2", DECKS, "microbiology", "Microbiology", "exam2", "Exam 2")
