#!/usr/bin/env python3
"""Print the stepped @keyframes for the app-shell background drift (bg-drift, bg-drift-soft).

2026-10-26: the drift used to animate background-position on every display frame, which repaints the
whole window 60-120 times a second (about a full CPU core in a software-painting browser; Safari paints
backgrounds on the CPU). These keyframes follow the same path the old two-keyframe rule took with the
element's ease-in-out timing (0% -> 100% -> 0% across, 50% down), as 40 straight pieces, each moved in
steps(N), so the picture changes N times per piece and the browser skips every frame in between.

Choose N so one step changes a color by about one level of 255 or less (invisible):
  theme.css, guides.html, group-join.html, group-host.html  (pale palettes, 16 s)   steps(6)  -> 15 a second
  arcade.css bg-drift       (saturated 26 s mode-color drift)                         steps(16) -> about 25 a second
  arcade.css bg-drift-soft  (its pale 16 s seasonal tints)                            steps(6)

Usage: python3 tools/gen_bg_drift_keyframes.py STEPS [INDENT]   then paste between the @keyframes braces.
"""
import sys


def _bez(t, p1, p2):                 # 1-D cubic bezier with end points 0 and 1
    return 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3


def ease_in_out(x):                  # CSS ease-in-out = cubic-bezier(.42, 0, .58, 1)
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo + hi) / 2
        if _bez(m, .42, .58) < x:
            lo = m
        else:
            hi = m
    return _bez((lo + hi) / 2, 0, 1)


def keyframes(steps, seg=20, indent="  "):
    out = []
    for k in range(2 * seg + 1):
        off = 50.0 * k / seg
        if k == seg:
            x = 100.0
        elif k < seg:
            x = 100 * ease_in_out(k / seg)
        else:
            x = 100 * (1 - ease_in_out((k - seg) / seg))
        if k == 2 * seg:
            x = 0.0
        tf = "" if k == 2 * seg else " animation-timing-function: steps(%d, end);" % steps
        out.append("%s%s%% { background-position: %s%% 50%%;%s }" % (
            indent, ("%.1f" % off).rstrip("0").rstrip("."), ("%.2f" % x).rstrip("0").rstrip(".") or "0", tf))
    return "\n".join(out)


if __name__ == "__main__":
    print(keyframes(int(sys.argv[1]), indent=sys.argv[2] if len(sys.argv) > 2 else "  "))
