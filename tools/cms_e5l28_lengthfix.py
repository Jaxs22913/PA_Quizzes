#!/usr/bin/env python3
"""Lecture 28 length fixes -- and a standalone before/after report.

    python3 cms_e4l25_lengthfix.py          # per-pool gameable%, raw and fixed

FIXES maps (module, index within that module's QUESTIONS, option index) to new
option TEXT. cms_e5_partition.py applies them before any guard runs. The key is
authored at option 0, so (m, i, 0) SHORTENS THE ANSWER -- the default remedy
(Jaxon, 2026-08-30: shorten the answer, never pad the distractors); the detail
it loses already sits in that option's own explanation. A fix on a distractor
is only for a key that is already minimal.

Most of this lecture's length control was done AT SOURCE (keys written short on
purpose, detail in the explanation), so this table only carries what the first
measurement still flagged.
"""
import glob, os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FIXES = {
}

M_CHARS, M_FRAC = 8, 0.18


def gameable(opts, c=0):
    s = sorted(((len(o[0]), i) for i, o in enumerate(opts)), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == c and tl - rn >= M_CHARS and tl >= rn * (1 + M_FRAC)


if __name__ == "__main__":
    mods = sorted(os.path.basename(p)[:-3] for pat in ("cms_e5l28_pool_*.py", "cms_e5l28_vig_*.py")
                  for p in glob.glob(os.path.join(HERE, pat)))
    tot_raw = tot_fix = tot_n = 0
    for m in mods:
        qs = importlib.import_module(m).QUESTIONS
        raw = fixed = 0
        flagged = []
        for i, q in enumerate(qs):
            opts = [list(o) for o in q["opts"]]
            r = gameable(opts)
            for j in range(4):
                if (m, i, j) in FIXES:
                    opts[j][0] = FIXES[(m, i, j)]
            f = gameable(opts)
            raw += r; fixed += f
            if f:
                flagged.append((i, q["q"][:60]))
        n = len(qs)
        tot_raw += raw; tot_fix += fixed; tot_n += n
        print("%-22s n=%3d   raw %5.1f%%   fixed %5.1f%%" % (m, n, 100.0 * raw / n, 100.0 * fixed / n))
        for i, s in flagged:
            print("      still gameable [%d] %s" % (i, s))
    if tot_n:
        print("%-22s n=%3d   raw %5.1f%%   fixed %5.1f%%" % ("ALL", tot_n, 100.0 * tot_raw / tot_n, 100.0 * tot_fix / tot_n))
