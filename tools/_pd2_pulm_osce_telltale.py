"""The tell-tale sign for each Pulmonary OSCE chart row: the one clue (or tight cluster) that makes it
the most likely diagnosis, from the slides (the Cardiac OSCE chart's yellow "Tell-tale sign" box).

TELLTALE[name] = (sign, cite)
  sign  in plain words, the key words in <b>
  cite  the slide(s) it comes from, in the batches' shorthand (cite() in the builder spells it out)

Written with each row in its batch module (_pulm_osce_batch_*.py) and merged here.
"""
from _pd2_pulm_osce_data import _load

TELLTALE = _load("TELLTALE")
