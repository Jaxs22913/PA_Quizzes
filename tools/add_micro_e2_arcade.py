#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Microbiology Exam 2 Arcade decks -- Lectures 7 and 8.

Cards derived from the question pools (see add_pdm_e2_arcade.py for why, and
for the check that derivation makes possible). Microbiology had no Exam 2
group entry before this.

ATOMIC FACTS ONLY. Idempotent: fenced between markers, re-runnable.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from _arcade_add import apply

SHIELD_ICON = ('<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>'
               '<path d="M9 12l2 2 4-4"/>')
DISH_ICON = ('<circle cx="12" cy="12" r="8.5"/><path d="M6 9h12"/>'
             '<circle cx="9.5" cy="13" r="1"/><circle cx="14" cy="14.5" r="1"/>'
             '<circle cx="13" cy="11" r="1"/>')

C = json.load(open(os.path.join(HERE, "micro_e2_cards.json"), encoding="utf-8"))
DECKS = [
 ("micro-immunity-disorders", "Disorders in Immunity", "accent2", SHIELD_ICON,
  [tuple(x) for x in C["micro-immunity-disorders"]]),
 ("micro-diagnosing-infections", "Diagnosing Infections", "accent4", DISH_ICON,
  [tuple(x) for x in C["micro-diagnosing-infections"]]),
]
if __name__ == "__main__":
    apply("MICROE2", DECKS, "microbiology", "Microbiology", "exam2", "Exam 2")
