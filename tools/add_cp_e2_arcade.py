#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Clinical Pathophysiology I Exam 2 Arcade decks -- Lectures 6 and 7.

MECHANISM ONLY, matching the pools these are derived from: this course draws
its line against Clinical Medicine and Surgery at pathophysiology versus
management, so no card asks what is given or done.

Idempotent: fenced between markers, re-runnable.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from _arcade_add import apply

HEART_ICON = ('<path d="M12 20s-7-4.5-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.5-7 9-7 9z"/>')
VESSEL_ICON = ('<path d="M5 4c0 6 3 8 3 16"/><path d="M12 4c0 6-3 8-3 16"/>'
               '<path d="M19 4c0 6-3 8-3 16"/><path d="M4 12h16"/>')

C = json.load(open(os.path.join(HERE, "cp_e2_cards.json"), encoding="utf-8"))
DECKS = [
 ("cp-cardiac-pathophys", "Cardiac Pathophysiology", "accent1", HEART_ICON,
  [tuple(x) for x in C["cp-cardiac-pathophys"]]),
 ("cp-vascular-pathophys", "Vascular Pathophysiology", "accent3", VESSEL_ICON,
  [tuple(x) for x in C["cp-vascular-pathophys"]]),
]
if __name__ == "__main__":
    apply("CPE2", DECKS, "clin-path-1", "Clinical Pathophysiology I", "exam2", "Exam 2")
