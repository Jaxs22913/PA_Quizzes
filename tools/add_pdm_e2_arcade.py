#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Exam 2 Arcade decks -- Lectures 7 and 8.

Cards are derived from the existing question pools rather than re-read from the
PPTs. The pools are already atomic (short stem, short key) and every one cites
its slide, so they are the same source at one remove -- and deriving from them
keeps the deck and the quizzes saying the same thing.

The derivation is not blind: the candidates were read before shipping, which is
how the truncated left-bundle-branch key was caught (it said "three" and listed
two). A card has to stand on its own without distractors, which makes that kind
of damage visible in a way the quiz format hides.

ATOMIC FACTS ONLY, per [[arcade_content_policy]].
Idempotent: fenced between markers, re-runnable.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _arcade_add import apply

HEART_ICON = ('<path d="M12 20s-7-4.5-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.5-7 9-7 9z"/>'
              '<path d="M3 12h4l2-3 2 6 2-4 1.5 2H21"/>')
SCAN_ICON = ('<path d="M3 8V5a2 2 0 0 1 2-2h3"/><path d="M16 3h3a2 2 0 0 1 2 2v3"/>'
             '<path d="M21 16v3a2 2 0 0 1-2 2h-3"/><path d="M8 21H5a2 2 0 0 1-2-2v-3"/>'
             '<circle cx="12" cy="12" r="3.5"/>')

CARDS = json.load(open(os.path.join(HERE, "pdm_e2_cards.json"), encoding="utf-8"))
DECKS = [
 ("pdm-ecg", "Electrocardiography &mdash; Basics", "accent1", HEART_ICON,
  [tuple(c) for c in CARDS["pdm-ecg"]]),
 ("pdm-cardiac-imaging", "Cardiac Imaging &amp; Vascular Studies", "accent3", SCAN_ICON,
  [tuple(c) for c in CARDS["pdm-cardiac-imaging"]]),
]

if __name__ == "__main__":
    apply("PDME2", DECKS, "pdm-1", "Principles of Diagnostic Medicine I", "exam2", "Exam 2")
