#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Physical Diagnosis 2 Exam 2 Arcade deck -- Lecture 5.

PHYSICAL DIAGNOSIS ONLY: what you find and how you find it. Clin Path I owns
the mechanism of these diseases and CMS I owns their management, and the pool
these cards come from is guarded to that boundary.

Idempotent: fenced between markers, re-runnable.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from _arcade_add import apply

STETH_ICON = ('<path d="M6 3v5a4 4 0 0 0 8 0V3"/><path d="M10 12v3a5 5 0 0 0 5 5"/>'
              '<circle cx="18" cy="18" r="2.5"/><circle cx="6" cy="3" r="1"/>'
              '<circle cx="14" cy="3" r="1"/>')

C = json.load(open(os.path.join(HERE, "pd2_e2_cards.json"), encoding="utf-8"))
DECKS = [("pd2-cardiovascular-exam", "Cardiovascular &amp; Peripheral Vascular Exam",
          "accent2", STETH_ICON, [tuple(x) for x in C["pd2-cardiovascular-exam"]])]
if __name__ == "__main__":
    apply("PD2E2", DECKS, "physical-diagnosis-2", "Physical Diagnosis 2", "exam2", "Exam 2")
