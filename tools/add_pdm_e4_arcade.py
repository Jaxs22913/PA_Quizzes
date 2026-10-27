#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Exam 4 Arcade decks -- Lectures 17 to 21 as they arrive.

The cards are written by the per-lecture builders in tools/pdm_e4/l<N>_cards.json, from each
lecture's question pools and guide fragment (atomic facts only, per [[arcade_content_policy]]).
Same shape as add_pdm_e3_arcade.py. Idempotent: fenced between markers, re-runnable.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _arcade_add import apply  # noqa: E402

FRAG = os.path.join(HERE, "pdm_e4")
# A pair of lungs on a film.
LUNGS_ICON = ('<rect x="3" y="3" width="18" height="18" rx="2"/>'
              '<path d="M12 6v6M12 12c-1.5 0-2-1-3.5-1S6 13 6 16c0 1.5 1 2 2 2 2 0 4-2 4-6"/>'
              '<path d="M12 12c1.5 0 2-1 3.5-1S18 13 18 16c0 1.5-1 2-2 2-2 0-4-2-4-6"/>')

# A volume-time curve: a steep rise to a plateau.
SPIRO_ICON = ('<path d="M3 3v18h18"/><path d="M6 17c1.5-6 3-9 6-10s5-1 8-1"/>')

SPEC = [
 (17, "pdm-pulmonary-imaging", "Pulmonary Imaging", "accent1", LUNGS_ICON),
 (20, "pdm-pulmonary-function", "Pulmonary Function Testing", "accent2", SPIRO_ICON),
]


def decks():
    out = []
    for n, did, name, colour, icon in SPEC:
        cards = json.load(open(os.path.join(FRAG, "l%d_cards.json" % n), encoding="utf-8"))
        # Optional Match pairs under "<deck>:match" (crisp term -> short definition); without them
        # Match falls back to the cards.
        assert set(cards) - {did + ":match"} == {did}, (n, list(cards))
        rows = [tuple(c) for c in cards[did]]
        assert all(len(c) == 2 and c[0].strip() and c[1].strip() for c in rows), did
        assert len({c[0] for c in rows}) == len(rows), "%s: repeated prompt" % did
        match = [tuple(m) for m in cards.get(did + ":match", [])]
        assert all(len(m) == 2 and m[0].strip() and m[1].strip() for m in match), did
        assert len({m[0] for m in match}) == len(match), "%s: repeated match term" % did
        out.append((did, name, colour, icon, rows, match) if match else (did, name, colour, icon, rows))
    return out


if __name__ == "__main__":
    apply("PDME4", decks(), "pdm-1", "Principles of Diagnostic Medicine I", "exam4", "Exam 4")
