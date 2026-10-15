#!/usr/bin/env python3
"""Lecture 32 length fixes -- and a standalone before/after report.

    python3 cms_e5l32_lengthfix.py          # per-pool gameable%, raw and fixed

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
 # Set 1 pools (2026-10-15): keys shortened, the detail stays in each key's explanation
 ("cms_e5l32_pool_a", 4, 0): "Blood jets or foreign bodies",
 ("cms_e5l32_pool_a", 14, 0): "Poor dentition",
 ("cms_e5l32_pool_a", 17, 0): "Microbes colonizing the endocardium",
 ("cms_e5l32_pool_a", 23, 0): "A major embolus or aneurysm rupture",
 ("cms_e5l32_pool_b", 7, 0): "Staphylococci from the skin",
 ("cms_e5l32_pool_b", 34, 0): "Three, from separate sites",
 ("cms_e5l32_pool_c", 11, 0): "Uncomplicated with rapid response",
 ("cms_e5l32_pool_c", 26, 0): "Ampicillin by injection",
 ("cms_e5l32_pool_c", 27, 0): "Azithromycin",
 ("cms_e5l32_pool_c", 31, 0): "Prior valve infection",
 ("cms_e5l32_pool_c", 38, 0): "Large peripheral artery emboli",
 ("cms_e5l32_pool_c", 42, 0): "Pneumococcus or Staphylococcus aureus",
 ("cms_e5l32_pool_c", 47, 0): "Central lines and prematurity",
 # Set 2 pools
 ("cms_e5l32_vig_a", 11, 0): "Septal perivalvular abscess",
 ("cms_e5l32_vig_a", 16, 0): "Libman-Sacks endocarditis",
 ("cms_e5l32_vig_c", 20, 0): "Cefazolin by injection",
 ("cms_e5l32_vig_c", 24, 0): "Clindamycin is dropped",
}

M_CHARS, M_FRAC = 8, 0.18


def gameable(opts, c=0):
    s = sorted(((len(o[0]), i) for i, o in enumerate(opts)), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == c and tl - rn >= M_CHARS and tl >= rn * (1 + M_FRAC)


if __name__ == "__main__":
    mods = sorted(os.path.basename(p)[:-3] for pat in ("cms_e5l32_pool_*.py", "cms_e5l32_vig_*.py")
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
