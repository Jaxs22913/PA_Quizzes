#!/usr/bin/env python3
"""Unit tests for tools/_option_order.py (2026-10-15). Run: python3 tools/test_option_order.py
Plain asserts, no framework (matches tools/test_planner.js in spirit); exit 1 and a traceback on failure."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _option_order import ordered_kind, order_options, is_monotonic, option_values


def q(texts, c):
    return {"opts": [[t, "expl " + t, "mis " + t] for t in texts], "c": c, "q": "x"}


# --- ordered_kind: numeric with units, percents, ranges, operators, words, stages
assert ordered_kind(["5 mm", "10 mm", "2 mm", "7 mm"]) == "numeric"
assert ordered_kind(["35%", "50%", "20%", "65%"]) == "numeric"
assert ordered_kind(["<5 mg/dL", "5-10 mg/dL", ">10 mg/dL", "20 mg/dL"]) == "numeric"
assert ordered_kind(["Stage 3", "Stage 1", "Stage 4", "Stage 2"]) == "numeric"
assert ordered_kind(["Stage III", "Stage I", "Stage IV", "Stage II"]) == "numeric"
assert ordered_kind(["Three", "Two", "Four", "Five"]) == "numeric"
assert ordered_kind(["1,000 mL", "500 mL", "250 mL", "2,000 mL"]) == "numeric"
assert ordered_kind(["2 weeks", "1 week", "4 weeks", "3 weeks"]) == "numeric"      # plural-insensitive
assert ordered_kind(["Grade 2.5", "Grade 1.5"]) == "numeric"
# --- not numeric
assert ordered_kind(["2 weeks", "3 days", "1 week", "4 weeks"]) is None            # mixed units
assert ordered_kind(["5 mm", "Surgery", "7 mm", "9 mm"]) is None                   # one option has no number
assert ordered_kind(["Aspirin", "Heparin", "Warfarin", "Apixaban"]) is None
assert ordered_kind(["5 mm", "10 mm Hg", "2 mm", "7 mm"]) is None                  # different unit text
assert ordered_kind(["5 and 10 mm", "2 mm", "7 mm"]) is None                       # two numbers, not a range
assert ordered_kind(["7"]) is None                                                 # nothing to order

# --- order_options: sorted ascending, key + explanations + mis travel together
src = q(["10 mm", "2 mm", "7 mm", "5 mm"], 2)           # key is "7 mm"
out = order_options(src)
assert [o[0] for o in out["opts"]] == ["2 mm", "5 mm", "7 mm", "10 mm"], out["opts"]
assert out["c"] == 2 and out["opts"][out["c"]][0] == "7 mm"
assert all(o[1] == "expl " + o[0] and o[2] == "mis " + o[0] for o in out["opts"])
assert src["opts"][0][0] == "10 mm", "input must not be mutated"
# numeric word order, ranges sort by lower bound
assert [o[0] for o in order_options(q(["Four", "Two", "Three"], 0))["opts"]] == ["Two", "Three", "Four"]
assert [o[0] for o in order_options(q([">10 mg/dL", "<5 mg/dL", "5-10 mg/dL"], 1))["opts"]] == \
    ["<5 mg/dL", "5-10 mg/dL", ">10 mg/dL"]
# stable on ties; non-numeric comes back as the same object
tie = q(["5 mm", "5 mm", "6 mm"], 1)
assert order_options(tie)["c"] == 1
plain = q(["Aspirin", "Heparin"], 1)
assert order_options(plain) is plain
# key follows when it is the first option
assert order_options(q(["9%", "1%", "5%", "3%"], 0))["c"] == 3

# --- is_monotonic: ascending or descending passes, a shuffled set does not
assert is_monotonic(["2 mm", "5 mm", "7 mm"]) and is_monotonic(["7 mm", "5 mm", "2 mm"])
assert not is_monotonic(["5 mm", "2 mm", "7 mm"])
assert is_monotonic(["Aspirin", "Heparin"])                                        # not numeric: nothing to say
assert option_values(["5-10 mm", "11-20 mm"]) == [(5.0, 10.0), (11.0, 20.0)]
print("test_option_order: all assertions passed")
