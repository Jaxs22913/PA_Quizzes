"""Typical age for each Pulmonary OSCE chart row (the Cardiac OSCE chart's "Typical age" line).

AGES[name] = (from_slides, cite, textbook)
  from_slides  what a deck says about age, in plain words ("" if no deck says)
  cite         the slide(s) it came from ("" if none)
  textbook     a standard-reference age, used ONLY where the decks give none;
               the page labels it "Textbook, not on the slides" so it is never
               mistaken for course content

Written with each row in its batch module (_pulm_osce_batch_*.py) and merged here.
"""
from _pd2_pulm_osce_data import _load

AGES = _load("AGES")
