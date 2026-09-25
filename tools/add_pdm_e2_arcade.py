#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Exam 2 Arcade decks -- Lectures 7, 8 and 9.

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

FLASK_ICON = ('<path d="M9 3h6"/><path d="M10 3v6L4.5 18.5A1.5 1.5 0 0 0 5.8 21h12.4a1.5 1.5 0 0 0 1.3-2.5L14 9V3"/>'
              '<path d="M7.5 15h9"/>')

CARDS = json.load(open(os.path.join(HERE, "pdm_e2_cards.json"), encoding="utf-8"))
DECKS = [
 ("pdm-ecg", "Electrocardiography &mdash; Basics", "accent1", HEART_ICON,
  [tuple(c) for c in CARDS["pdm-ecg"]]),
 ("pdm-cardiac-imaging", "Cardiac Imaging &amp; Vascular Studies", "accent3", SCAN_ICON,
  [tuple(c) for c in CARDS["pdm-cardiac-imaging"]]),
 # Lecture 9 (added 2026-09-25): written from the slides and the L9 pools; the
 # recording was still being transcribed. US spelling, full terms.
 ("pdm-cardiac-biomarkers-lipids", "Cardiac Biomarkers &amp; Lipids", "accent2", FLASK_ICON,
  [tuple(c) for c in CARDS["pdm-cardiac-biomarkers-lipids"]]),
]

if __name__ == "__main__":
    apply("PDME2", DECKS, "pdm-1", "Principles of Diagnostic Medicine I", "exam2", "Exam 2")
