#!/usr/bin/env python3
"""Lecture 29 length fixes -- and a standalone before/after report.

    python3 cms_e5l29_lengthfix.py          # per-pool gameable%, raw and fixed

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
    ("cms_e5l29_pool_a", 9, 0): "Intracranial hypertension",
    ("cms_e5l29_pool_a", 18, 0): "Unexplained once causes excluded",
    ("cms_e5l29_pool_a", 26, 0): "Surgical injury to the node",
    ("cms_e5l29_pool_a", 31, 0): "Irregular, with a variable rate",
    ("cms_e5l29_pool_b", 20, 0): "Intravenous rate control",
    ("cms_e5l29_pool_b", 22, 0): "High metabolic demand, normal heart",
    ("cms_e5l29_pool_b", 34, 0): "Ablation of the pathway",
    ("cms_e5l29_pool_b", 41, 0): "Neck pulsations",
    ("cms_e5l29_pool_b", 43, 0): "A beta blocker",
    ("cms_e5l29_pool_c", 0, 0): "250 to 300",
    ("cms_e5l29_pool_c", 16, 0): "Severe heart failure or infarction",
    ("cms_e5l29_pool_c", 33, 0): "When they trigger fibrillation",
    ("cms_e5l29_pool_c", 34, 0): "Atrial fibrillation or flutter",
    ("cms_e5l29_pool_c", 43, 0): "Check for heart disease",
    ("cms_e5l29_vig_a", 19, 0): "Pacemaker-defibrillator",
    ("cms_e5l29_vig_b", 21, 0): "An extra pathway causing fast rhythms",
    ("cms_e5l29_vig_b", 26, 0): "Pill-in-the-pocket beta blocker",
    ("cms_e5l29_vig_b", 28, 0): "Avoid her known triggers",
    ("cms_e5l29_vig_c", 22, 0): "Atrial bigeminy",
    ("cms_e5l29_vig_c", 27, 0): "Check for heart disease",
    ("cms_e5l29_pool_a", 20, 0): "Left untreated",
    ("cms_e5l29_pool_b", 16, 0): "A poor outlook",
    ("cms_e5l29_pool_c", 45, 0): "Well",
    ("cms_e5l29_vig_a", 10, 0): "Treat the bleeding",
    ("cms_e5l29_vig_b", 4, 0): "Hidden atrial activity",
    ("cms_e5l29_vig_c", 14, 0): "It is the first goal",
    ("cms_e5l29_vig_c", 16, 0): "Severe heart failure",
    ("cms_e5l29_pool_a", 4, 0): "Cyclic irregularity, normal P waves",
    ("cms_e5l29_pool_c", 3, 0): "Scarring after heart surgery",
    ("cms_e5l29_vig_b", 8, 0): "Treat the lung disease",
    ("cms_e5l29_vig_c", 10, 0): "May not be needed",
}

M_CHARS, M_FRAC = 8, 0.18


def gameable(opts, c=0):
    s = sorted(((len(o[0]), i) for i, o in enumerate(opts)), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == c and tl - rn >= M_CHARS and tl >= rn * (1 + M_FRAC)


if __name__ == "__main__":
    mods = sorted(os.path.basename(p)[:-3] for pat in ("cms_e5l29_pool_*.py", "cms_e5l29_vig_*.py")
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
