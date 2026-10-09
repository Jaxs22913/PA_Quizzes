#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Exam 3 Arcade decks -- Lectures 11 to 16 (electrocardiography).

The cards are written by the per-lecture builders in tools/pdm_e3/l<N>_cards.json,
from each lecture's question pools and guide fragment (atomic facts only, per
[[arcade_content_policy]]; where deck and truth disagree the card states the
truth, matching the quizzes and the guide). Same shape as add_pdm_e2_arcade.py.
Idempotent: fenced between markers, re-runnable.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _arcade_add import apply  # noqa: E402

FRAG = os.path.join(HERE, "pdm_e3")
# A single beat on a baseline, a monitor, a heart, a lightning bolt, an axis, a pill.
BEAT_ICON = '<path d="M2 12h5l2-5 3 10 2-7 1.5 2H22"/>'
WAVE_ICON = ('<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M5 12h3l1.5-3 2 6 1.5-3H19"/>'
             '<path d="M9 21h6"/>')
HEART_ICON = ('<path d="M12 20s-7-4.5-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.5-7 9-7 9z"/>'
              '<path d="M3 12h4l2-3 2 6 2-4 1.5 2H21"/>')
BOLT_ICON = '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>'
AXIS_ICON = ('<circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/><path d="M12 12l5 5"/>')
PILL_ICON = ('<rect x="3" y="9" width="18" height="6" rx="3" transform="rotate(-35 12 12)"/>'
             '<path d="M10 8.5l5 7"/>')

SPEC = [
 (11, "pdm-rhythm-analysis-sinus", "Rhythm Analysis &amp; Sinus Rhythms", "accent1", BEAT_ICON),
 (12, "pdm-ectopy-supraventricular", "Ectopy, Escape &amp; Supraventricular Rhythms", "accent2", WAVE_ICON),
 (13, "pdm-ventricular-heart-blocks", "Ventricular Dysrhythmias &amp; Heart Blocks", "accent3", BOLT_ICON),
 (14, "pdm-axis-bbb-enlargement", "Axis, Bundle Branch Blocks &amp; Enlargement", "accent1", AXIS_ICON),
 (15, "pdm-ischemia-infarction", "Ischemia, Injury &amp; Infarction", "accent2", HEART_ICON),
 (16, "pdm-pericarditis-electrolytes-drugs", "Pericarditis, Electrolytes &amp; Drug Effects", "accent3", PILL_ICON),
]


def decks():
    out = []
    for n, did, name, colour, icon in SPEC:
        cards = json.load(open(os.path.join(FRAG, "l%d_cards.json" % n), encoding="utf-8"))
        assert list(cards) == [did], (n, list(cards))
        rows = [tuple(c) for c in cards[did]]
        assert all(len(c) == 2 and c[0].strip() and c[1].strip() for c in rows), did
        assert len({c[0] for c in rows}) == len(rows), "%s: repeated prompt" % did
        out.append((did, name, colour, icon, rows))
    return out


if __name__ == "__main__":
    apply("PDME3", decks(), "pdm-1", "Principles of Diagnostic Medicine I", "exam3", "Exam 3")
