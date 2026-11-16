# -*- coding: utf-8 -*-
"""Acid-Base Case Chain cases -- Clinical Medicine and Surgery I, Exam 7 (Lecture 45, Acid-Base Disorders II, Finck).

Deck: "PAJ5510 Acid Base Disorders II MBF2026sc.pptx" (64 slides; text and tables read with python-pptx; the picture
slides viewed: s25 nomogram, s27/s50 change-in-gap rules, s58 primary-process flowchart, s59 evaluation flowchart).
Visible slide content only; speaker notes are not used. Unlike the Exam 6 set (tools/abchain_cms_e6.py, built on the
shared generators in tools/abchain_common.py), this set has its OWN generators below, because Lecture 45 is about mixed
disorders: normal-pH cases, two processes at once, the albumin-corrected gap, the change in anion gap against the change
in bicarbonate, and the change in chloride. Every key here is re-derived independently by
tools/check_acid_base_cases.py (check_case_e7) from the shipped JSON.

RULES USED, exactly as the slides state them:
  pH 7.35-7.45, acidemia below / alkalemia above (s3, s10); unsustainable below 6.7 or above 7.6 (s12).
  Carbon dioxide 35-45 (s10; s6 prints 36-44; no case value sits between them), bicarbonate 22-26 (s6, s10).
  Primary process from the value that matches the pH (s10-11, s58); normal pH = no abnormality OR a mixed disorder
  (s58); compensation never fully corrects the pH and inadequate or excessive compensation points to a mixed disorder;
  never more than one primary respiratory disorder (s23, s4).
  Anion gap = sodium - (bicarbonate + chloride), normal 6-12 (s7, s47), raised above 12 (s44), decreased below 6
  (s48); it can be abnormal with normal electrolytes (s26). Albumin 3.5-5.5; correct the gap by adding 2.5 for each
  1 g/dL below 4.5 (s8). No case albumin sits between 4.5 and 5.5 or between 3.5 and 4.5 (the slide is silent there).
  Compensation table (s24): acute respiratory acidosis bicarbonate +1 per 10, chronic +3.5 per 10 (s33-35); metabolic
  alkalosis carbon dioxide +0.75 per 1. Baselines 40 mm Hg and 25 mEq/L, given in the prompt (s27/s50 use 25 as the
  accepted bicarbonate). Every keyed case reads the same with a 24 baseline (asserted below).
  Winter formula 1.5 x bicarbonate + 8, plus or minus 2: inside = metabolic acidosis only, above = concurrent
  respiratory acidosis, below = concurrent respiratory alkalosis (s49: Lecture 45 DOES state the "below" direction;
  the s28 rows say the same).
  Change in anion gap = gap - 10; change in bicarbonate = 25 - bicarbonate (s27, s50). Equal = metabolic acidosis
  only; gap change larger = concurrent metabolic alkalosis (only detectable with a high gap); gap change smaller =
  check the change in chloride; bicarbonate change = gap change + chloride change = increased-gap AND normal-gap
  acidosis (s50, s30). The deck gives no normal chloride: the prompt states 100 mEq/L as the baseline (the s30
  example's change of 10 for a chloride of 110). "Roughly equal" = within 2; every unequal case differs by 5 or more.
  Metabolic alkalosis: urine chloride below 25 saline responsive, above 40 saline unresponsive (s51); responsive =
  volume contraction, unresponsive split normotensive / hypertensive (s53).
  Mixed pairs and their slide examples (s28-30): sepsis/lactic (metabolic acidosis + respiratory alkalosis); severe
  pneumonia, pulmonary edema (+ respiratory acidosis); liver disease and diuretics (metabolic alkalosis + respiratory
  alkalosis); chronic lung disease on diuretics (+ respiratory acidosis); uremia with vomiting (metabolic acidosis +
  metabolic alkalosis); diarrhea and lactic acidosis, treatment of diabetic ketoacidosis (increased + normal gap).

NOT USED, on purpose: her board cases A-H and their labs (the s28-30 example VALUES are not reused either; every case
here has new numbers); her spoken 0.1 / 0.4 shortcuts (not on a slide; the slide's 3.5 is keyed); the 1.3 per 1 row
for metabolic acidosis (she used the Winter formula; questions use Winter only); the respiratory alkalosis ratios
(not taught aloud; no case needs them); the nomogram (s25, "academic ways I'm going to expect you to calculate it").
Exogenous alkali and hypoparathyroidism are never offered (s53 files them oddly; the guide does not key them).
"""
import math
from abchain_common import f, fph

COURSE = "cms45"
SET = dict(
    id="cms-e7",
    name="Acid-Base II Case Chains",
    course="Clinical Medicine and Surgery I",
    exam="Exam 7",
    scope="Lecture 45, Acid-Base Disorders II",
    intro=("Twenty-one patients, most with more than one process at once. Read the pH, match the carbon dioxide and "
           "bicarbonate to it, calculate and albumin-correct the anion gap, check compensation (Winter formula, the "
           "acute and chronic ratios), compare the change in anion gap with the change in bicarbonate, then name what "
           "fits the patient. Every value comes with its normal range."),
)
NUMERIC = {"ag_calc", "alb_corr", "winter_calc", "delta_calc"}

PH, PCO2, HCO3 = (7.35, 7.45), (35, 45), (22, 26)
AGN = (6, 12)
B_CO2, B_HCO3, AG0, CL0 = 40, 25, 10, 100

RACID, RALK, MACID, MALK = "Respiratory acidosis", "Respiratory alkalosis", "Metabolic acidosis", "Metabolic alkalosis"


def st(v, t):
    return "low" if v < t[0] else "high" if v > t[1] else "normal"


class X:
    def __init__(self, c):
        self.c = c
        L = c["labs"]
        self.L = L
        self.ph, self.p, self.h = L["ph"], L["pco2"], L["hco3"]
        hh = 6.1 + math.log10(self.h / (0.03 * self.p))
        assert abs(hh - self.ph) <= 0.02, "%s: pH %s vs Henderson-Hasselbalch %.3f" % (c["id"], self.ph, hh)
        self.dir = "acid" if self.ph < PH[0] else "alk" if self.ph > PH[1] else "normal"
        self.ps, self.hs = st(self.p, PCO2), st(self.h, HCO3)
        if "na" in L:
            self.ag = L["na"] - (L["cl"] + self.h)
            self.agc = self.ag + (2.5 * (4.5 - L["alb"]) if L.get("alb", 4.6) < 3.5 else 0)
            if "alb" in L:
                a = L["alb"]
                assert a < 3.5 or a >= 4.5, "%s: albumin %s sits in the slide's silent band" % (c["id"], a)
        else:
            self.ag = self.agc = None

    def lowalb(self):
        return self.L.get("alb", 4.6) < 3.5


def cands(x):
    """Disorders that match the pH from each value (s10-11, s58)."""
    out = []
    if x.dir == "acid":
        if x.ps == "high":
            out.append(RACID)
        if x.hs == "low":
            out.append(MACID)
    elif x.dir == "alk":
        if x.ps == "low":
            out.append(RALK)
        if x.hs == "high":
            out.append(MALK)
    return out


def proc_of(x):
    """The process each abnormal value points to, regardless of the pH (for normal-pH and two-process cases)."""
    r = {"high": RACID, "low": RALK}.get(x.ps)
    m = {"low": MACID, "high": MALK}.get(x.hs)
    return r, m


def pdesc(x):
    return {"low": "below 35", "high": "above 45", "normal": "inside 35 to 45"}[x.ps]


def hdesc(x):
    return {"low": "below 22", "high": "above 26", "normal": "inside 22 to 26"}[x.hs]


PSTR = "carbon dioxide"


# ------------------------------------------------------------------ pH (s3, s12, s23, s58)
A_, K_, N_, U_ = "Acidemia", "Alkalemia", "Normal pH", "Unsustainable pH"


def g_ph(x):
    ph = fph(x.ph)
    word = {"acid": "acidemia", "alk": "alkalemia", "normal": "a normal pH"}[x.dir]
    where = {"acid": "below 7.35", "alk": "above 7.45", "normal": "inside 7.35 to 7.45"}[x.dir]
    key = {"acid": A_, "alk": K_, "normal": N_}[x.dir]
    E = {}
    if x.dir == "normal":
        E[N_] = ("Correct. The pH of %s sits inside 7.35 to 7.45. A normal pH does not rule out an acid-base problem: an "
                 "acidosis and an alkalosis can pull against each other and leave the pH in the middle, so the carbon "
                 "dioxide and bicarbonate still have to be read." % ph)
    else:
        E[key] = ("Correct. The pH of %s is %s, so this is %s. Next, find which value, carbon dioxide or bicarbonate, "
                  "moved the pH that way." % (ph, where, word))
        E[N_] = ("A normal pH is 7.35 to 7.45, and %s is %s it. Compensation never brings the pH fully back to normal, "
                 "so an abnormal pH stays abnormal. Tell: compare the pH with its range first."
                 % (ph, "below" if x.dir == "acid" else "above"))
    for lab, w in ((A_, "below 7.35"), (K_, "above 7.45")):
        if lab != key:
            E[lab] = ("%s means a pH %s. This pH of %s is %s, so it is %s. Tell: below the range is acidemia, above it "
                      "is alkalemia." % (lab, w, ph, where, word))
    E[U_] = ("A pH below 6.7 or above 7.6 is unsustainable. A pH of %s is well inside those limits%s. Tell: "
             "unsustainable marks how far the pH has moved, not which way." % (
                 ph, "; it is %s, still to be explained" % word if x.dir != "normal" else ", and in fact normal"))
    walk = ["Compare the pH with its normal range, 7.35 to 7.45.", "%s is %s." % (ph, where),
            "So: %s." % word + (" A normal pH can still hide a mixed disorder, so keep reading." if x.dir == "normal"
                                 else "")]
    return [(t, E[t]) for t in (A_, K_, N_, U_)], key, walk, [3, 12, 23, 58]


# ------------------------------------------------------------------ primary (abnormal pH, one value matches)
def g_primary(x):
    cs = cands(x)
    assert len(cs) == 1, "%s: primary not unique %s" % (x.c["id"], cs)
    key = cs[0]
    ph, p, h = fph(x.ph), f(x.p), f(x.h)
    word = "acidemia" if x.dir == "acid" else "alkalemia"
    move = "lowers" if x.dir == "acid" else "raises"
    eff_p = {"high": "a high carbon dioxide lowers the pH", "low": "a low carbon dioxide raises the pH",
             "normal": "an in-range carbon dioxide shows no respiratory process on its own"}[x.ps]
    eff_h = {"high": "a high bicarbonate raises the pH", "low": "a low bicarbonate lowers the pH",
             "normal": "an in-range bicarbonate shows no metabolic process on its own"}[x.hs]
    E = {}
    if key in (MACID, MALK):
        if x.ps == "normal":
            other = ("The carbon dioxide of %s is %s, so by the ranges it is not what moved the pH; whether it is the "
                     "right carbon dioxide for this bicarbonate is checked next." % (p, pdesc(x)))
        else:
            other = ("The carbon dioxide of %s is %s, and %s, so it did not cause the %s; whether it is only "
                     "compensation is checked next." % (p, pdesc(x), eff_p, word))
        E[key] = ("Correct. The pH of %s is %s, and the bicarbonate of %s is %s: %s, so the primary process is "
                  "metabolic. %s" % (ph, word, h, hdesc(x), eff_h, other))
    else:
        other = "The bicarbonate of %s is %s, and %s, so it did not cause the %s." % (h, hdesc(x), eff_h, word)
        E[key] = ("Correct. The pH of %s is %s, and the carbon dioxide of %s is %s: %s, so the primary process is "
                  "respiratory. %s" % (ph, word, p, pdesc(x), eff_p, other))
    same = [d for d in ((RACID, MACID) if x.dir == "acid" else (RALK, MALK)) if d != key][0]
    if same in (RACID, RALK):
        E[same] = ("The carbon dioxide of %s is %s, so it is not the primary process behind this pH; the bicarbonate "
                   "of %s is. Whether the lungs add a problem of their own is a later check. Tell: the primary process "
                   "is the value that moves the pH the way it went." % (p, pdesc(x), h))
    else:
        E[same] = ("The bicarbonate of %s is %s, and %s, so it is not what %s this pH; the carbon dioxide of %s is. "
                   "Tell: the primary process is the value that moves the pH the way it went."
                   % (h, hdesc(x), eff_h, "lowered" if x.dir == "acid" else "raised", p))
    for d in ((RALK, MALK) if x.dir == "acid" else (RACID, MACID)):
        E[d] = ("%s %s the pH, so it cannot be the primary process behind %s at %s. A second process, if any, is "
                "found later from the expected compensation. Tell: name the primary from the value that matches the pH."
                % (d, "raises" if x.dir == "acid" else "lowers", word, ph))
    walk = ["pH %s: %s." % (ph, word),
            "Carbon dioxide %s (normal 35 to 45): %s%s." % (p, x.ps, "" if x.ps == "normal" else ", and " + eff_p),
            "Bicarbonate %s (normal 22 to 26): %s%s." % (h, x.hs, "" if x.hs == "normal" else ", and " + eff_h),
            "The value that %s the pH the way it went is the %s, so the primary process is %s."
            % (move, "bicarbonate" if key in (MACID, MALK) else "carbon dioxide", key.lower())]
    return [(t, E[t]) for t in (RACID, RALK, MACID, MALK)], key, walk, [10, 11, 58]


# ------------------------------------------------------------------ normal pH: what do the gases show? (s23, s26, s56, s58)
MIXED, NONE, FULLC, TWOR, GAPF = ("A mixed acid-base disorder", "No acid-base disorder",
                                  "A fully compensated simple disorder", "Two respiratory disorders canceling",
                                  "Check the anion gap before deciding")


def normal_read_of(x):
    assert x.dir == "normal"
    return MIXED if (x.ps != "normal" or x.hs != "normal") else GAPF


def g_normal_read(x):
    key = normal_read_of(x)
    ph, p, h = fph(x.ph), f(x.p), f(x.h)
    E = {}
    gas_ok = x.ps == "normal" and x.hs == "normal"
    E[FULLC] = ("Compensation never fully corrects the pH in a simple disorder; it only brings it closer to normal. So a "
                "normal pH of %s is never a simple disorder that compensated all the way. Tell: a normal pH with "
                "abnormal values means two processes pulling against each other." % ph) if not gas_ok else (
        "Here nothing is abnormal for compensation to have corrected: carbon dioxide %s and bicarbonate %s are both in "
        "range, and a compensated simple disorder would still leave the pH off. Tell: normal gases leave the anion gap "
        "to check." % (p, h))
    E[TWOR] = ("There can never be more than one primary respiratory disorder: a patient cannot breathe too fast and "
               "too slow at once. Only one process can come from the carbon dioxide; the other must be metabolic. "
               "Tell: one respiratory process at most, metabolic ones can stack.") if not gas_ok else (
        "Two respiratory disorders cannot coexist: a patient cannot breathe too fast and too slow at once. Here the "
        "carbon dioxide of %s is in range, so by the ranges there is no respiratory abnormality to pair. Tell: only one "
        "respiratory process is ever possible." % p)
    if key == MIXED:
        r, m = proc_of(x)
        bits = []
        if x.ps != "normal":
            bits.append("the carbon dioxide of %s is %s, which %s the pH" % (p, pdesc(x), "lowers" if x.ps == "high"
                                                                              else "raises"))
        if x.hs != "normal":
            bits.append("the bicarbonate of %s is %s, which %s the pH" % (h, hdesc(x), "raises" if x.hs == "high"
                                                                          else "lowers"))
        E[MIXED] = ("Correct. The pH of %s is normal, but %s. Each would move the pH a different way, a tug of war that "
                    "leaves it in the middle. Compensation never fully corrects the pH, so a normal pH with abnormal "
                    "values means a mixed disorder." % (ph, "; ".join(bits)))
        E[NONE] = ("A normal pH does not rule out an acid-base problem. Here the %s out of range, so something is "
                   "moving them. Tell: look at the pH, the carbon dioxide and the bicarbonate before calling it normal."
                   % ("carbon dioxide and bicarbonate are" if (x.ps != "normal" and x.hs != "normal") else
                      "values are"))
        E[GAPF] = ("The gap is always worth calculating, but it is not what decides this step: the %s already out of "
                   "range with a normal pH, which by itself shows a mixed disorder. Tell: abnormal gases with a "
                   "normal pH mean two processes." % ("carbon dioxide and bicarbonate are" if (x.ps != "normal" and
                                                                                               x.hs != "normal")
                                                       else "values are"))
        opts = [(t, E[t]) for t in (MIXED, NONE, FULLC, TWOR)]
        walk = ["pH %s: normal." % ph, "Carbon dioxide %s: %s." % (p, x.ps), "Bicarbonate %s: %s." % (h, x.hs),
                "Abnormal values with a normal pH: each pulls the pH a different way, and compensation alone never "
                "returns the pH fully to normal.", "So: a mixed acid-base disorder."]
    else:
        E[GAPF] = ("Correct. The pH of %s, the carbon dioxide of %s and the bicarbonate of %s are all in range, but the "
                   "anion gap can be abnormal even when the bicarbonate is normal, and a large gap is "
                   "never from a respiratory disorder alone. Calculate it before calling this normal." % (ph, p, h))
        E[NONE] = ("Normal gases are not the end of the check: the anion gap can be abnormal even when the bicarbonate "
                   "is within range, and a sick patient with normal-looking gases needs it. Tell: "
                   "calculate the gap even when everything looks normal.")
        E[MIXED] = ("A mixed disorder may well be present, but nothing shown yet proves it: pH, carbon dioxide and "
                    "bicarbonate are all inside their ranges. The anion gap is the value that can show it. Tell: "
                    "calculate the gap before naming any disorder.")
        opts = [(t, E[t]) for t in (GAPF, NONE, FULLC, TWOR)]
        walk = ["pH %s, carbon dioxide %s and bicarbonate %s: all inside their ranges." % (ph, p, h),
                "That looks normal, but the anion gap can be abnormal even when the bicarbonate is normal.",
                "So: check the anion gap before deciding."]
    return opts, key, walk, [23, 26, 56, 58]


# ------------------------------------------------------------------ two processes named from the gases (s4, s10-11, s28-30)
PAIRS = [(MACID, RALK), (MACID, RACID), (MALK, RALK), (MALK, RACID)]


def pair_label(m, r):
    return "%s and %s" % (m, r.lower())


def pair_of(x):
    r, m = proc_of(x)
    assert r and m, "%s: pair step needs both values abnormal" % x.c["id"]
    if x.dir != "normal":
        assert len(cands(x)) == 2, "%s: pair step with an abnormal pH needs both values to match it" % x.c["id"]
    return pair_label(m, r)


def g_pair(x):
    key = pair_of(x)
    r, m = proc_of(x)
    p, h, ph = f(x.p), f(x.h), fph(x.ph)
    rtxt = "the carbon dioxide of %s is %s: a %s" % (p, pdesc(x), r.lower())
    mtxt = "the bicarbonate of %s is %s: a %s" % (h, hdesc(x), m.lower())
    E = {}
    if x.dir == "normal":
        tail = "They pull the pH opposite ways, so it ends up normal."
    else:
        tail = "Both push the pH the same way, which is why the pH of %s is so far from normal." % ph
    E[key] = ("Correct. Read each value on its own: %s, and %s. One respiratory and one metabolic process can run "
              "together. %s" % (rtxt, mtxt, tail))
    for mm, rr in PAIRS:
        lab = pair_label(mm, rr)
        if lab == key:
            continue
        wrong = []
        if mm != m:
            wrong.append("a %s needs a %s bicarbonate, and this one is %s" % (mm.lower(), "low" if mm == MACID
                                                                            else "high", h))
        if rr != r:
            wrong.append("a %s needs a %s carbon dioxide, and this one is %s" % (rr.lower(), "high" if rr == RACID
                                                                               else "low", p))
        E[lab] = ("%s. Here %s, and %s. Tell: each value names its own process; read the direction of each."
                  % ("; ".join(wrong)[0].upper() + "; ".join(wrong)[1:], rtxt, mtxt))
    walk = ["Carbon dioxide %s (normal 35 to 45): %s, so %s." % (p, x.ps, r.lower()),
            "Bicarbonate %s (normal 22 to 26): %s, so %s." % (h, x.hs, m.lower()),
            "Only one respiratory process is possible at a time; a metabolic one can join it.",
            "So: %s." % key.lower()]
    return [(pair_label(a, b), E[pair_label(a, b)]) for a, b in PAIRS], key, walk, [4, 10, 11, 28, 29]


# ------------------------------------------------------------------ anion gap (s7, s26)
def g_ag_calc(x):
    L = x.L
    na, cl, h, k, p = L["na"], L["cl"], x.h, L["k"], x.p
    ag = x.ag
    keyexp = ("Correct. Anion gap = sodium - (bicarbonate + chloride) = %s - (%s + %s) = %s - %s = %s. The normal gap is "
              "6 to 12, about 10 on average%s." % (f(na), f(h), f(cl), f(na), f(h + cl), f(ag),
                                                  "; the albumin still has to be checked before it is read"
                                                  if x.lowalb() else ""))
    cand = [
        (na - cl, "%s is sodium minus chloride only (%s - %s); the bicarbonate was left out. Both measured anions come "
                  "off the sodium: %s - (%s + %s) = %s. Tell: add bicarbonate and chloride first, then subtract."
                  % (f(na - cl), f(na), f(cl), f(na), f(h), f(cl), f(ag))),
        (na - cl + h, "%s adds the bicarbonate instead of subtracting it (%s - %s + %s). The gap takes away bicarbonate "
                      "and chloride together: %s - %s = %s. Tell: the parentheses hold bicarbonate plus chloride."
                      % (f(na - cl + h), f(na), f(cl), f(h), f(na), f(h + cl), f(ag))),
        (ag + k, "%s adds the potassium of %s. The formula has no potassium: %s - (%s + %s) = %s. Tell: sodium, "
                 "bicarbonate and chloride are the only three values." % (f(ag + k), f(k), f(na), f(h), f(cl), f(ag))),
        (na - (cl + p), "%s uses the arterial carbon dioxide of %s mm Hg in place of the bicarbonate. The gap needs the "
                        "bicarbonate, %s mEq/L: %s - (%s + %s) = %s. Tell: carbon dioxide pressure is a gas value, not "
                        "a measured anion." % (f(na - (cl + p)), f(p), f(h), f(na), f(h), f(cl), f(ag))),
    ]
    rows = [(ag, keyexp)]
    for v, e in cand:
        if v > 0 and all(abs(v - r[0]) >= 1 for r in rows) and len(rows) < 4:
            rows.append((v, e))
    assert len(rows) == 4, x.c["id"]
    rows.sort(key=lambda r: r[0])
    walk = ["Anion gap = sodium - (bicarbonate + chloride).",
            "Bicarbonate + chloride = %s + %s = %s." % (f(h), f(cl), f(h + cl)),
            "%s - %s = %s." % (f(na), f(h + cl), f(ag)),
            "Normal gap: 6 to 12 (about 10)." + (" Albumin is low, so correct it before reading it." if x.lowalb()
                                                else "")]
    return [(f(r[0]), r[1]) for r in rows], f(ag), walk, [7, 26]


# ------------------------------------------------------------------ albumin correction (s8)
def g_alb_corr(x):
    alb, ag = x.L["alb"], x.ag
    below = 4.5 - alb
    corr = 2.5 * below
    c = ag + corr
    keyexp = ("Correct. Albumin %s g/dL is %s below 4.5, so add 2.5 x %s = %s: corrected gap = %s + %s = %s. A low "
              "albumin hides part of the gap, so the correction can only raise it."
              % (f(alb, 1), f(below, 1), f(below, 1), f(corr), f(ag), f(corr), f(c)))
    cand = [
        (ag - corr, "%s subtracts the correction (%s - %s). A low albumin pulls the gap down, so the correction adds "
                    "2.5 for each 1 g/dL below 4.5: %s + %s = %s. Tell: correcting for a low albumin raises the gap."
                    % (f(ag - corr), f(ag), f(corr), f(ag), f(corr), f(c))),
        (ag + below, "%s adds only the %s g/dL that albumin sits below 4.5, without the 2.5 multiplier. The correction is "
                     "2.5 x %s = %s, so %s. Tell: 2.5 for each 1 g/dL below 4.5."
                     % (f(ag + below), f(below, 1), f(below, 1), f(corr), f(c))),
        (ag + 2.5 * (5.5 - alb), "%s counts down from 5.5, the top of the albumin range. The correction counts from 4.5: "
                                 "2.5 x %s = %s, so %s. Tell: the anchor is 4.5 g/dL."
                                 % (f(ag + 2.5 * (5.5 - alb)), f(below, 1), f(corr), f(c))),
    ]
    rows = [(c, keyexp)] + cand
    vals = [r[0] for r in rows]
    assert len(set(vals)) == 4 and min(vals) > 0, (x.c["id"], vals)
    rows.sort(key=lambda r: r[0])
    walk = ["The gap must be corrected when albumin is abnormal: add 2.5 for each 1 g/dL below 4.5.",
            "Albumin %s: 4.5 - %s = %s below." % (f(alb, 1), f(alb, 1), f(below, 1)),
            "2.5 x %s = %s." % (f(below, 1), f(corr)),
            "Corrected gap = %s + %s = %s." % (f(ag), f(corr), f(c))]
    return [(f(r[0]), r[1]) for r in rows], f(c), walk, [8]


# ------------------------------------------------------------------ reading the gap (s7, s8, s44, s47, s48)
GE, GN, GD = "Elevated anion gap", "Normal anion gap", "Decreased anion gap"
GALBUP, GALBF = "Elevated only because of the low albumin", "Needs an albumin correction first"


def gap_cat(v):
    return GE if v > AGN[1] else GN if v >= AGN[0] else GD


def g_ag_read(x):
    v = x.agc
    key = gap_cat(v)
    assert key != GN or v <= 12 and not (12 < v), x.c["id"]
    alb = x.L["alb"]
    vs = f(v)
    E = {}
    if x.lowalb():
        src = "The corrected gap of %s" % vs
        E[GALBUP] = ("A low albumin lowers the gap, it never raises it: albumin is one of the unmeasured anions. The "
                     "measured %s became %s only after correcting for the albumin of %s g/dL, which uncovers a gap "
                     "that was hidden. Tell: low albumin hides a raised gap." % (f(x.ag), vs, f(alb, 1)))
        fourth = GALBUP
    else:
        src = "The gap of %s" % vs
        E[GALBF] = ("The gap is corrected only when albumin is abnormal, and this albumin of %s g/dL is not low. So the "
                    "gap of %s is read as it stands. Tell: correct the gap only for an abnormal albumin."
                    % (f(alb, 1), vs))
        fourth = GALBF
    if key == GE:
        E[GE] = ("Correct. %s is above the normal 6 to 12, so it is elevated: added unmeasured anions such as "
                 "ketoacids or lactate. A large gap points to a metabolic acidosis, never a respiratory disorder alone."
                 % src)
        E[GN] = ("A normal gap is 6 to 12, about 10 on average, and %s is above it.%s Tell: above 12 is elevated, "
                 "pointing to the increased-gap list."
                 % (src.lower().replace("the ", "this ", 1),
                    " The measured %s looked normal, but the corrected value is the one to read." % f(x.ag)
                    if x.lowalb() else ""))
        E[GD] = ("A decreased gap is below 6, most often from a low albumin that has not been corrected. %s is above 12. "
                 "Tell: only a gap below 6 is decreased." % src)
    elif key == GN:
        E[GN] = ("Correct. %s lies inside the normal 6 to 12. A metabolic acidosis with a normal gap is the USEDCAR "
                 "group, from bicarbonate loss or chloride retention." % src)
        E[GE] = ("An elevated gap is above 12. %s is inside 6 to 12. Tell: compare the gap with 6 to 12, about 10 on "
                 "average." % src)
        E[GD] = ("A decreased gap is below 6. %s is inside 6 to 12. Tell: only a gap below 6 is decreased." % src)
    opts = [(t, E[t]) for t in (GE, GN, GD, fourth)]
    walk = ["Albumin %s g/dL: %s." % (f(alb, 1), "low, so read the corrected gap" if x.lowalb()
                                       else "not low, so no correction"),
            "Gap to read: %s, against 6 to 12." % vs, "So: %s." % key.lower()]
    return opts, key, walk, [7, 8, 44, 47, 48]


# ------------------------------------------------------------------ Winter formula (s49)
def winter(h):
    k = 1.5 * h + 8
    return k, k - 2, k + 2


def g_winter_calc(x):
    h = x.h
    K, lo, hi = winter(h)
    R = lambda c: "%s to %s mm Hg" % (f(c - 2), f(c + 2))
    key = R(K)
    keyexp = ("Correct. Winter formula: expected carbon dioxide = 1.5 x %s + 8 = %s + 8 = %s, plus or minus 2, so %s to "
              "%s mm Hg. Only the measured bicarbonate goes into it." % (f(h), f(1.5 * h), f(K), f(lo), f(hi)))
    cand = [
        (1.5 * h - 8, "%s subtracts the 8 instead of adding it (1.5 x %s - 8 = %s). The formula adds: 1.5 x %s + 8 = %s, "
                      "so %s to %s. Tell: the constant is plus 8." % (R(1.5 * h - 8), f(h), f(1.5 * h - 8), f(h), f(K),
                                                                      f(lo), f(hi))),
        (h + 8, "%s adds 8 to the bicarbonate without multiplying by 1.5 (%s + 8 = %s). The formula is 1.5 x %s + 8 = %s, "
                "so %s to %s. Tell: multiply by 1.5 first, then add 8." % (R(h + 8), f(h), f(h + 8), f(h), f(K), f(lo),
                                                                         f(hi))),
        (2 * h + 8, "%s multiplies the bicarbonate by 2 instead of 1.5 (2 x %s + 8 = %s). The multiplier is 1.5: 1.5 x %s + 8 = "
                    "%s, so %s to %s. Tell: one and a half times the bicarbonate, plus 8." % (
                        R(2 * h + 8), f(h), f(2 * h + 8), f(h), f(K), f(lo), f(hi))),
        (1.5 * h, "%s multiplies by 1.5 but leaves out the 8 (1.5 x %s = %s). Adding it gives %s, so %s to %s. Tell: "
                  "the formula has two parts, times 1.5 and plus 8." % (R(1.5 * h), f(h), f(1.5 * h), f(K), f(lo),
                                                                       f(hi))),
        (1.5 * h + 16, "%s adds 16 instead of 8 (1.5 x %s + 16 = %s). The constant is 8: %s, so %s to %s. Tell: plus 8, "
                       "plus or minus 2." % (R(1.5 * h + 16), f(h), f(1.5 * h + 16), f(K), f(lo), f(hi))),
        (40, "%s centers on 40, the normal carbon dioxide, as if the lungs were not compensating at all. With a "
             "bicarbonate of %s the lungs should pull carbon dioxide far lower: 1.5 x %s + 8 = %s, so %s to %s. Tell: "
             "in metabolic acidosis the expected carbon dioxide is low." % (R(40), f(h), f(h), f(K), f(lo), f(hi))),
    ]
    rows = [(K, key, keyexp)]
    for c, e in cand:
        if c - 2 > 0 and all(abs(c - r[0]) > 4 for r in rows) and len(rows) < 4:
            rows.append((c, R(c), e))
    assert len(rows) == 4, x.c["id"]
    rows.sort(key=lambda r: r[0])
    walk = ["Winter formula: expected carbon dioxide = 1.5 x bicarbonate + 8, plus or minus 2.",
            "Bicarbonate %s: 1.5 x %s = %s." % (f(h), f(h), f(1.5 * h)), "%s + 8 = %s." % (f(1.5 * h), f(K)),
            "Range: %s to %s mm Hg." % (f(lo), f(hi))]
    return [(r[1], r[2]) for r in rows], key, walk, [49]


ONLY, CRA, CRL, RENC = ("Appropriate respiratory compensation", "Concurrent respiratory acidosis",
                        "Concurrent respiratory alkalosis", "Renal compensation for the acidosis")


def winter_read_of(x):
    K, lo, hi = winter(x.h)
    if x.p > hi:
        assert x.p - hi >= 1
        return CRA
    if x.p < lo:
        return CRL
    return ONLY


def g_winter_read(x):
    K, lo, hi = winter(x.h)
    key = winter_read_of(x)
    p, r = f(x.p), "%s to %s" % (f(lo), f(hi))
    where = {"ONLY": "inside", "CRA": "above", "CRL": "below"}[{ONLY: "ONLY", CRA: "CRA", CRL: "CRL"}[key]]
    innorm = 35 <= x.p <= 45
    E = {}
    E[ONLY] = ("Appropriate respiratory compensation means the carbon dioxide sits inside the expected %s mm Hg. The measured %s is "
               "%s it, so the lungs are not simply compensating. Tell: outside the Winter range means a second, "
               "respiratory, process." % (r, p, where)) if key != ONLY else (
        "Correct. The measured carbon dioxide of %s sits inside the expected %s mm Hg, so the lungs are compensating "
        "as predicted; there is no concurrent respiratory disorder. Other metabolic processes are a separate check."
        % (p, r))
    if key == CRA:
        E[CRA] = ("Correct. The measured carbon dioxide of %s is above the expected %s mm Hg: the lungs are holding on to "
                  "more carbon dioxide than compensation needs, a concurrent respiratory acidosis.%s"
                  % (p, r, " A carbon dioxide inside the normal 35 to 45 is still too high for this acidosis."
                     if innorm else ""))
    else:
        E[CRA] = ("A concurrent respiratory acidosis shows as a carbon dioxide above the Winter range. The measured %s is "
                  "%s the expected %s. Tell: above the range is respiratory acidosis, below it respiratory alkalosis."
                  % (p, where, r))
    if key == CRL:
        E[CRL] = ("Correct. The measured carbon dioxide of %s is below the expected %s mm Hg: the lungs are blowing off "
                  "more than compensation needs, a concurrent respiratory alkalosis." % (p, r))
    else:
        E[CRL] = ("A concurrent respiratory alkalosis shows as a carbon dioxide below the Winter range. The measured %s "
                  "is %s the expected %s. Tell: below the range is respiratory alkalosis, above it respiratory acidosis."
                  % (p, where, r))
    E[RENC] = ("A metabolic acidosis is compensated by the lungs, through carbon dioxide; the kidneys compensate "
               "respiratory disorders. The carbon dioxide of %s is the respiratory side, and it sits %s the expected %s. "
               "Tell: a metabolic problem gets a respiratory response." % (p, where, r))
    walk = ["Expected carbon dioxide by the Winter formula: %s mm Hg." % r, "Measured carbon dioxide: %s." % p,
            "%s is %s the range: inside = appropriate compensation, no respiratory disorder; above = concurrent respiratory acidosis; below = "
            "concurrent respiratory alkalosis." % (p, where), "So: %s." % key.lower()]
    return [(t, E[t]) for t in (ONLY, CRA, CRL, RENC)], key, walk, [28, 49]


# ------------------------------------------------------------------ change in anion gap (s27, s50)
def g_delta_calc(x):
    v = x.agc
    d = v - AG0
    keyexp = ("Correct. Change in anion gap = calculated gap - 10, the accepted normal: %s - 10 = %s. It is compared "
              "next with the fall in bicarbonate from 25.%s" % (f(v), f(d), " The corrected gap is the one to use, because the albumin is low." if x.lowalb() else ""))
    cand = [
        (v - 12, "%s subtracts 12, the top of the normal range. The accepted normal for this calculation is 10: %s - 10 "
                 "= %s. Tell: change in gap = calculated gap - 10, not - 12." % (f(v - 12), f(v), f(d))),
        (v - 6, "%s subtracts 6, the bottom of the normal range. The accepted normal for this calculation is 10: %s - 10 "
                "= %s. Tell: change in gap = gap - 10." % (f(v - 6), f(v), f(d))),
        (v, "%s is the gap itself, not its change. Subtract the accepted normal of 10: %s - 10 = %s. Tell: the change is "
            "how far the gap rose above its accepted normal of 10." % (f(v), f(v), f(d))),
    ]
    if x.lowalb():
        cand.insert(0, (x.ag - AG0, "%s starts from the measured gap of %s, before the albumin correction. The corrected "
                                    "gap is %s, so %s - 10 = %s. Tell: correct for albumin first, then take the change."
                                    % (f(x.ag - AG0), f(x.ag), f(v), f(v), f(d))))
    rows = [(d, keyexp)]
    for c, e in cand:
        if c > 0 and all(abs(c - r[0]) >= 1 for r in rows) and len(rows) < 4:
            rows.append((c, e))
    assert len(rows) == 4, x.c["id"]
    rows.sort(key=lambda r: r[0])
    walk = ["Change in anion gap = calculated gap - 10 (the accepted normal).",
            "Gap%s: %s." % (" (corrected for albumin)" if x.lowalb() else "", f(v)), "%s - 10 = %s." % (f(v), f(d))]
    return [(f(r[0]), r[1]) for r in rows], f(d), walk, [27, 50]


DONLY, DMALK, DCL, DRALK = ("No second metabolic process", "Concurrent metabolic alkalosis",
                            "Check the change in chloride", "Decreased anion gap acidosis")


def deltas(x):
    return x.agc - AG0, B_HCO3 - x.h


def delta_read_of(x):
    da, dh = deltas(x)
    assert x.agc > 12, "%s: the change in gap is only read with a raised gap" % x.c["id"]
    if abs(da - dh) <= 2:
        return DONLY
    if da - dh >= 5:
        return DMALK
    assert dh - da >= 5, "%s: change in gap %s vs bicarbonate %s is equivocal" % (x.c["id"], da, dh)
    return DCL


def g_delta_read(x):
    da, dh = deltas(x)
    key = delta_read_of(x)
    sa, sh = f(da), f(dh)
    cmp_ = "about equal to" if key == DONLY else "larger than" if key == DMALK else "smaller than"
    E = {}
    E[DONLY] = ("Correct. The gap rose %s (%s - 10) and the bicarbonate fell %s (25 - %s): about equal, so the added "
                "acid explains the whole fall in bicarbonate: no second metabolic process is hidden. Any respiratory "
                "process is judged from the carbon dioxide against the Winter range, not from this comparison." % (sa, f(x.agc), sh, f(x.h))) \
        if key == DONLY else (
        "No second metabolic process needs the two changes to be about equal. Here the gap change of %s is %s the "
        "bicarbonate change of %s. Tell: unequal changes mean a second metabolic process." % (sa, cmp_, sh))
    E[DMALK] = ("Correct. The gap rose %s but the bicarbonate fell only %s (25 - %s): more acid was added than the "
                "bicarbonate shows, so something is holding bicarbonate up, a concurrent metabolic alkalosis. It can only "
                "be seen this way because the gap is high." % (sa, sh, f(x.h))) if key == DMALK else (
        "A concurrent metabolic alkalosis shows as a gap change clearly larger (by more than about 2) than the "
        "bicarbonate change. Here %s is %s %s. Tell: a gap change clearly bigger means a hidden alkalosis." % (sa, cmp_, sh))
    E[DCL] = ("Correct. The bicarbonate fell %s (25 - %s), more than the gap rose (%s). The extra fall is not from the "
              "unmeasured anions, so check the change in chloride next." % (sh, f(x.h), sa)) if key == DCL else (
        "The chloride is checked when the gap change is clearly smaller (by more than about 2) than the bicarbonate "
        "change. Here %s is %s %s. Tell: "
        "check the chloride only when the bicarbonate fell clearly more than the gap rose." % (sa, cmp_, sh))
    E[DRALK] = ("A decreased gap is below 6, and this gap is %s, raised; the change in gap is compared with the change "
                "in bicarbonate only when the gap is raised. Here the gap change is %s against a bicarbonate change of "
                "%s. Tell: read this comparison for a second metabolic process." % (f(x.agc), sa, sh))
    walk = (["Use the albumin-corrected gap (%s), not the measured %s." % (f(x.agc), f(x.ag))] if x.lowalb() else []) + [
            "Change in anion gap = %s - 10 = %s." % (f(x.agc), sa),
            "Change in bicarbonate = 25 - %s = %s." % (f(x.h), sh),
            "Equal: no second metabolic process. Gap change larger: concurrent metabolic alkalosis (seen only with a high "
            "gap). Gap change smaller: check the change in chloride.", "%s is %s %s, so: %s." % (sa, cmp_, sh,
                                                                                               key.lower())]
    return [(t, E[t]) for t in (DONLY, DMALK, DCL, DRALK)], key, walk, [27, 30, 50]


CBOTH, CMALK, CONLY, CRAC = ("Increased-gap plus normal-gap acidosis", "Concurrent metabolic alkalosis",
                             "A single increased-gap acidosis", "Concurrent respiratory acidosis")


def chloride_read_of(x):
    da, dh = deltas(x)
    dc = x.L["cl"] - CL0
    assert dc > 0 and abs(dh - (da + dc)) <= 2, "%s: chloride does not account for the gap" % x.c["id"]
    return CBOTH


def g_chloride_read(x):
    key = chloride_read_of(x)
    da, dh = deltas(x)
    cl = x.L["cl"]
    dc = cl - CL0
    s = "%s + %s = %s" % (f(da), f(dc), f(da + dc))
    E = {
        CBOTH: ("Correct. Change in chloride = %s - 100 = %s. Gap change plus chloride change = %s, which matches the "
                "bicarbonate change of %s. So two acidoses run together: an increased-gap acidosis (the rise in the gap) "
                "and a normal-gap acidosis (the rise in chloride)." % (f(cl), f(dc), s, f(dh))),
        CMALK: ("A metabolic alkalosis would leave the bicarbonate change smaller than the gap change. Here the "
                "bicarbonate fell %s, more than the gap rose (%s), and the chloride rise makes up the difference: %s. "
                "Tell: the chloride check finds a second acidosis." % (f(dh), f(da), s)),
        CONLY: ("A single increased-gap acidosis needs the gap change alone to match the bicarbonate change. Here the gap "
                "change is %s against %s; only with the chloride change added (%s) does it match. Tell: a chloride rise "
                "adds a normal-gap acidosis." % (f(da), f(dh), s)),
        CRAC: ("The chloride check compares metabolic changes only; a respiratory acidosis is found from the carbon "
               "dioxide against the Winter range. Here the changes balance: %s, about equal to %s. Tell: the chloride names a "
               "normal-gap acidosis." % (s, f(dh))),
    }
    walk = ["Change in chloride = %s - 100 = %s." % (f(cl), f(dc)),
            "Change in gap + change in chloride = %s." % s,
            "Change in bicarbonate = %s." % f(dh),
            "When the bicarbonate change equals the gap change plus the chloride change, an increased-gap and a "
            "normal-gap metabolic acidosis are both present.", "So: %s." % key.lower()]
    return [(t, E[t]) for t in (CBOTH, CMALK, CONLY, CRAC)], key, walk, [30, 50]


# ------------------------------------------------------------------ acute vs chronic respiratory acidosis (s24, s33-35)
CA, CC, CPM, CPA = ("Acute respiratory acidosis alone", "Chronic respiratory acidosis alone", "Concurrent metabolic alkalosis",
                    "Concurrent metabolic acidosis")


def chron_preds(p, base=B_HCO3):
    d = p - B_CO2
    return d, base + 1.0 * d / 10, base + 3.5 * d / 10


def chron_of(x, base=B_HCO3):
    d, a, c = chron_preds(x.p, base)
    h = x.h
    if abs(h - a) <= 1.5:
        return CA
    if abs(h - c) <= 2:
        return CC
    if h - c >= 3:
        return CPM
    if a - h >= 3:
        return CPA
    raise AssertionError("%s: bicarbonate %s fits neither acute %s nor chronic %s" % (x.c["id"], h, a, c))


def chron_prompt(x):
    return ("Bicarbonate rises about 1 mEq/L per 10 mm Hg rise in carbon dioxide when acute and about 3.5 when chronic, "
            "counting from 40 mm Hg and 25 mEq/L. Compared with these predictions, what does the measured bicarbonate show?")


def g_chronicity(x):
    key = chron_of(x)
    assert key == chron_of(x, 24), "%s: chronicity changes with a 24 baseline" % x.c["id"]
    d, a, c = chron_preds(x.p)
    h, p = f(x.h), f(x.p)
    A = "25 + 1 x %s/10 = %s" % (f(d), f(a))
    C = "25 + 3.5 x %s/10 = %s" % (f(d), f(c))
    E = {}
    E[CA] = ("Correct. Carbon dioxide rose %s (40 to %s). Acute: %s; chronic: %s. The measured %s matches the acute "
             "value: the kidneys have not had the 24 to 48 hours they need." % (f(d), p, A, C, h)) if key == CA else (
        "Acute compensation predicts %s. The measured %s is %s. Tell: compare the bicarbonate with both predictions."
        % (A, h, "well above it" if x.h > a else "well below it"))
    E[CC] = ("Correct. Carbon dioxide rose %s (40 to %s). Chronic: %s; acute only %s. The measured %s matches the "
             "chronic value: after 24 to 48 hours the kidneys raise bicarbonate 3.5 per 10." % (f(d), p, C, A, h)) \
        if key == CC else (
        ("Chronic compensation needs 24 to 48 hours and would reach about %s; the measured %s matches the acute "
         "prediction of %s instead. Tell: a bicarbonate at the acute value means the kidneys have not caught up yet."
         % (f(c), h, f(a))) if key == CA else
        "Chronic compensation predicts %s. The measured %s is %s. Tell: compensation that overshoots or falls short "
        "points to a mixed disorder." % (C, h, "above even that" if x.h > c else "below it"))
    E[CPM] = ("Correct. Even full chronic compensation predicts only %s, and the measured bicarbonate is %s, higher "
              "than compensation explains. Excess bicarbonate means a concurrent metabolic alkalosis; compensation alone "
              "never brings the pH back to normal." % (C, h)) if key == CPM else (
        "A concurrent metabolic alkalosis would leave the bicarbonate clearly above what compensation predicts. The "
        "measured %s fits the %s prediction of %s instead. Tell: call a mixed disorder only when compensation cannot "
        "explain the value." % (h, "acute" if key == CA else "chronic", f(a) if key == CA else f(c)))
    E[CPA] = ("Correct. Even acute compensation predicts a bicarbonate of %s, and the measured %s is well below it: "
              "something is using up bicarbonate, a concurrent metabolic acidosis." % (f(a), h)) if key == CPA else (
        "A concurrent metabolic acidosis would leave the bicarbonate clearly below what compensation predicts. The "
        "measured %s %s. Tell: a bicarbonate that fits a prediction needs no second disorder." % (
            h, "fits the acute prediction of %s" % f(a) if key == CA else "fits the chronic prediction of %s" % f(c)
            if key == CC else "is above even the chronic prediction of %s" % f(c)))
    walk = ["Rise in carbon dioxide: %s - 40 = %s." % (p, f(d)), "Acute prediction: %s." % A,
            "Chronic prediction: %s." % C,
            "Measured bicarbonate %s: %s." % (h, {CA: "matches the acute prediction", CC: "matches the chronic one",
                                                   CPM: "above even the chronic prediction",
                                                   CPA: "below even the acute prediction"}[key]),
            "So: %s." % key.lower()]
    return [(t, E[t]) for t in (CA, CC, CPM, CPA)], key, walk, [23, 24, 33, 34, 35]


# ------------------------------------------------------------------ metabolic alkalosis compensation (s24, s29)
EXP, MRA, MRL, BACK = ("Expected respiratory compensation", "Concurrent respiratory acidosis",
                       "Concurrent respiratory alkalosis", "Compensation back to a normal pH")
ALK_PROMPT = ("In metabolic alkalosis carbon dioxide rises about 0.75 mm Hg per 1 mEq/L rise in bicarbonate, counting "
              "from 40 mm Hg and 25 mEq/L. What does the carbon dioxide show?")


def alk_pred(h, base=B_HCO3):
    dh = h - base
    return dh, B_CO2 + 0.75 * dh


def alk_of(x, base=B_HCO3):
    dh, pred = alk_pred(x.h, base)
    if abs(x.p - pred) <= 2:
        return EXP
    if x.p - pred >= 5:
        return MRA
    if pred - x.p >= 5:
        return MRL
    raise AssertionError("%s: carbon dioxide %s equivocal against %s" % (x.c["id"], x.p, pred))


def g_alk_comp(x):
    key = alk_of(x)
    assert key == alk_of(x, 24), "%s: alkalosis reading changes with a 24 baseline" % x.c["id"]
    dh, pred = alk_pred(x.h)
    p, h = f(x.p), f(x.h)
    calc = "bicarbonate rose %s (25 to %s); 0.75 x %s = %s, so carbon dioxide should be about 40 + %s = %s" % (
        f(dh), h, f(dh), f(0.75 * dh), f(0.75 * dh), f(pred))
    E = {}
    E[EXP] = ("Correct. The %s. The measured %s fits: the lungs retain carbon dioxide by breathing less, the expected "
              "compensation, and the pH stays high." % (calc, p)) if key == EXP else (
        "Expected compensation would put carbon dioxide near %s. The measured %s is %s off. Tell: a carbon dioxide far "
        "from the prediction means a second, respiratory, process." % (f(pred), p, f(abs(x.p - pred))))
    E[MRA] = ("Correct. The %s. The measured %s is well above that: more carbon dioxide than compensation needs, a "
              "concurrent respiratory acidosis." % (calc, p)) if key == MRA else (
        "A concurrent respiratory acidosis shows as a carbon dioxide clearly higher than predicted (about %s). The "
        "measured %s %s. Tell: higher than predicted is respiratory acidosis." % (
            f(pred), p, "is within 2 of that prediction, so it is not meaningfully higher" if key == EXP
            else "is lower than predicted, not higher"))
    E[MRL] = ("Correct. The %s. The measured %s has not risen as predicted: the lungs are blowing carbon dioxide off, a "
              "concurrent respiratory alkalosis, which keeps the pH higher than expected." % (calc, p)) \
        if key == MRL else (
        "A concurrent respiratory alkalosis shows as a carbon dioxide that does not rise as predicted (about %s). The "
        "measured %s %s. Tell: lower than predicted is respiratory alkalosis." % (
            f(pred), p, "is within 2 of that prediction, so it is not meaningfully below it" if key == EXP
            else "is higher than predicted, not lower"))
    E[BACK] = ("Compensation never fully corrects the pH; only fixing the underlying condition does. %s Tell: a normal "
               "pH beside abnormal values points to a mixed disorder." % (
                   "The pH here is %s, still above 7.45." % fph(x.ph) if x.dir == "alk" else
                   "This pH of %s is normal because a second process is pulling the other way." % fph(x.ph)))
    walk = ["Bicarbonate rise: %s - 25 = %s." % (h, f(dh)), "Expected carbon dioxide rise: 0.75 x %s = %s." % (
        f(dh), f(0.75 * dh)), "Expected carbon dioxide: 40 + %s = %s mm Hg." % (f(0.75 * dh), f(pred)),
            "Measured: %s, %s." % (p, {EXP: "close to the prediction", MRA: "higher than predicted",
                                        MRL: "lower than predicted"}[key]), "So: %s." % key.lower()]
    return [(t, E[t]) for t in (EXP, MRA, MRL, BACK)], key, walk, [23, 24, 29]


# ------------------------------------------------------------------ saline type (s51, s53)
SR, SUN, SUH, SRH = ("Saline responsive, volume contracted", "Saline unresponsive, normotensive",
                     "Saline unresponsive, hypertensive", "Saline responsive, hypertensive")


def saline_of(c):
    u, sbp = c["urine_cl"], c.get("sbp")
    if u < 25:
        return SR
    assert u > 40, c["id"]
    assert sbp is not None and (sbp >= 140 or sbp < 130), c["id"]
    return SUH if sbp >= 140 else SUN


def g_saline(x):
    c = x.c
    key = saline_of(c)
    u = f(c["urine_cl"])
    bp = c.get("bp_text", "")
    E = {}
    if key == SR:
        E[SR] = ("Correct. A urine chloride of %s mEq/L is below 25, the saline-responsive type, which goes with volume "
                 "contraction. %s" % (u, c["volume_clue"]))
        for t in (SUN, SUH):
            E[t] = ("The saline-unresponsive types have a high urine chloride, above 40 mEq/L. This urine chloride is %s, "
                    "below 25. Tell: a low urine chloride means saline responsive; blood pressure only splits the "
                    "unresponsive group." % u)
        E[SRH] = ("Blood pressure splits only the saline-unresponsive group into normotensive and hypertensive; the "
                  "saline-responsive type goes with volume contraction. Tell: responsive pairs with a contracted volume.")
    else:
        hyp = key == SUH
        E[key] = ("Correct. A urine chloride of %s mEq/L is above 40, the saline-unresponsive type, and the %s, so it is "
                  "the %s group." % (u, bp, "hypertensive" if hyp else "normotensive"))
        E[SR] = ("The saline-responsive type has a low urine chloride, below 25 mEq/L, with volume contraction. This urine "
                 "chloride is %s, above 40. Tell: a high urine chloride means saline unresponsive." % u)
        other = SUN if hyp else SUH
        E[other] = ("The urine chloride of %s does mark the unresponsive type, but the %s, so the %s group fits instead. "
                    "Tell: in the unresponsive type, the blood pressure decides." % (u, bp, "hypertensive" if hyp
                                                                                     else "normotensive"))
        E[SRH] = ("Saline responsive needs a urine chloride below 25 mEq/L; this one is %s. Blood pressure is used only "
                  "inside the unresponsive group. Tell: urine chloride first, then blood pressure." % u)
    walk = ["Urine chloride: below 25 mEq/L = saline responsive; above 40 = saline unresponsive.",
            "Here it is %s mEq/L: %s." % (u, "responsive" if key == SR else "unresponsive")]
    if key != SR:
        walk.append("Unresponsive is split by blood pressure: %s." % bp)
    walk.append("So: %s." % key.lower())
    return [(t, E[t]) for t in (SR, SUN, SUH, SRH)], key, walk, [51, 53]


# ------------------------------------------------------------------ potassium (s5)
KAO, KAI, KLI, KLO = ("Acidosis moving potassium out of cells", "Acidosis moving potassium into cells",
                      "Alkalosis moving potassium into cells", "Alkalosis moving potassium out of cells")


def g_potassium(x):
    k = x.L["k"]
    assert x.dir == "alk" and k < 3.5, x.c["id"]
    ks, ph = f(k, 1), fph(x.ph)
    key = KLI
    E = {KLI: ("Correct. The pH of %s is alkalemic and the potassium of %s is below 3.5. In alkalosis hydrogen ions shift "
               "out of cells and potassium shifts in, resulting in hypokalemia. Other losses can add to a low potassium, but "
               "this shift is the alkalosis's own effect." % (ph, ks)),
         KLO: ("Potassium moving out of cells would raise the blood level, and this potassium is %s, low. In alkalosis "
               "potassium moves into cells. Tell: alkalosis pulls potassium down." % ks),
         KAO: ("This pH of %s is alkalemic, not acidemic, and the potassium of %s is low, not high. Acidosis moves "
               "potassium out of cells and raises it. Tell: match the shift to the pH first." % (ph, ks)),
         KAI: ("The pH of %s is alkalemic and the values show no acidosis, and acidosis would move potassium out of "
               "cells anyway. Here "
               "alkalosis has moved it in. Tell: alkalosis means potassium into cells." % ph)}
    walk = ["pH %s: alkalemia." % ph, "Potassium %s against 3.5 to 5.0: low." % ks,
            "Alkalosis shifts potassium into cells (hypokalemia); acidosis shifts it out (hyperkalemia).",
            "So: alkalosis moving potassium into cells."]
    return [(t, E[t]) for t in (KAO, KAI, KLI, KLO)], key, walk, [5]


GEN = {
    "ph": ("pH", "What does the pH show?", g_ph),
    "primary": ("Primary process", "Which primary process explains the pH?", g_primary),
    "normal_read": ("Normal pH?", "The pH is normal. What do these values show?", g_normal_read),
    "pair": ("Two processes", "Read the carbon dioxide and bicarbonate on their own. Which two processes are present?",
             g_pair),
    "ag_calc": ("Anion gap", "Calculate the anion gap.", g_ag_calc),
    "alb_corr": ("Albumin correction", "Correct the anion gap for the albumin.", g_alb_corr),
    "ag_read": ("Reading the gap", "How should this anion gap be read?", g_ag_read),
    "winter_calc": ("Winter formula", "Use the Winter formula: what carbon dioxide range is expected?", g_winter_calc),
    "winter_read": ("Compensation check", "Compare the measured carbon dioxide with that range. What does it show?",
                    g_winter_read),
    "delta_calc": ("Change in gap", "Calculate the change in anion gap.", g_delta_calc),
    "delta_read": ("Gap against bicarbonate", "Compare the change in anion gap with the change in bicarbonate. What "
                                              "does it show?", g_delta_read),
    "chloride_read": ("Change in chloride", "Counting the change in chloride from 100 mEq/L, what does the chloride "
                                            "show?", g_chloride_read),
    "chronicity": ("Acute or chronic", None, g_chronicity),
    "alk_comp": ("Compensation check", ALK_PROMPT, g_alk_comp),
    "saline": ("Type of alkalosis", "Which type of metabolic alkalosis is this?", g_saline),
    "potassium": ("Potassium", "Which potassium shift fits this pH and this potassium?", g_potassium),
}


def raw_steps(case):
    """Called by tools/build_acid_base_chain.py; returns the step dicts in the shared shape."""
    x = X(case)
    out = []
    for kind in case["steps"]:
        if kind == "cause":
            d = case["cause"]
            opts = [(t, e) for (t, cat, e) in d["options"]]
            cats = [cat for (t, cat, e) in d["options"]]
            out.append(dict(kind=kind, label="What fits", prompt=d["prompt"], opts=opts, cats=cats, key=d["key"],
                            walk=d["walk"], slides=d["slides"]))
            continue
        label, prompt, gen = GEN[kind]
        if kind == "chronicity":
            prompt = chron_prompt(x)
        if kind == "normal_read" and normal_read_of(x) == GAPF:
            prompt = "The pH, carbon dioxide and bicarbonate are all normal. What is the right conclusion so far?"
        if kind == "delta_read":
            prompt = ("%sompare the change in anion gap with the change in bicarbonate (changes within about 2 of each "
                      "other count as equal). What does it show?" % ("Using the albumin-corrected gap, c" if x.lowalb()
                                                                     else "C"))
        if kind == "ag_calc" and x.lowalb():
            prompt = "Calculate the anion gap from the measured sodium, bicarbonate and chloride."
        opts, key, walk, slides = gen(x)
        out.append(dict(kind=kind, label=label, prompt=prompt, opts=opts, cats=None, key=key, walk=walk,
                        slides=slides))
    return out


def C(options, key, walk, slides, prompt="Which condition best fits this patient and these values?"):
    return dict(prompt=prompt, options=options, key=key, walk=walk, slides=slides)


# Cause tags: the set of processes the option stands for, joined with "+":
#   MAH increased-gap metabolic acidosis, MAN normal-gap metabolic acidosis, MALK metabolic alkalosis,
#   RAC respiratory acidosis, RAL respiratory alkalosis.  The validator re-derives the case's own set from the numbers
#   and checks the key's tag equals it (and no distractor's does), using its own map of option names to tags.

CASES = [

# ------------------------------------------------------------------ metabolic acidosis + respiratory alkalosis (s28)
dict(id="e7-01", who="71-year-old woman",
     vignette=("A 71-year-old woman is admitted to the intensive care unit with a severe urinary tract infection that has "
               "spread to her blood (sepsis). She is confused, warm and breathing fast. Her blood lactate is high. She "
               "has no kidney disease, no diarrhea or vomiting, no diabetes, and has taken no toxins."),
     labs=dict(ph=7.40, pco2=20, hco3=12, na=138, cl=104, k=4.2, alb=4.6),
     steps=["ph", "normal_read", "pair", "ag_calc", "ag_read", "winter_calc", "winter_read", "delta_read", "cause"],
     cause=C([
         ("Sepsis with lactic acidosis", "MAH+RAL",
          "Correct. Sepsis with lactic acidosis is the classic metabolic acidosis with respiratory alkalosis: lactate "
          "raises the gap (22) while her fast breathing drives the carbon dioxide below the Winter range. Her high "
          "lactate and infection fit."),
         ("Uremia with vomiting", "MAH+MALK",
          "Uremia with vomiting is the metabolic acidosis plus metabolic alkalosis pair, and she has no kidney disease "
          "or vomiting; her gap change matched her bicarbonate change. Tell: her second process is respiratory."),
         ("Diarrhea with lactic acidosis", "MAH+MAN",
          "Diarrhea with lactic acidosis is an increased-gap plus normal-gap pair, and she has no diarrhea; her chloride "
          "of 104 is normal. Tell: the low carbon dioxide below the Winter range is the second process."),
         ("Lactic acidosis alone", "MAH",
          "Lactic acidosis is one of her processes, but alone it would leave the carbon dioxide inside the Winter range "
          "and the pH low. Hers is 20, below 24 to 28, with a normal pH. Tell: two processes, not one."),
     ], "Sepsis with lactic acidosis",
       ["Processes found: an increased-gap metabolic acidosis (gap 22) and a respiratory alkalosis (carbon dioxide 20, "
        "below the Winter range of 24 to 28).",
        "Does the clinical picture fit? Sepsis with a high lactate, breathing fast.",
        "So: sepsis with lactic acidosis."], [28, 45, 49, 57]),
     summary="Normal pH hiding two processes: an increased-gap lactic acidosis and a respiratory alkalosis from sepsis "
             "(carbon dioxide below the Winter range); the gap change matched the bicarbonate change."),

dict(id="e7-02", who="58-year-old man",
     vignette=("A 58-year-old man in the intensive care unit has septic shock from a perforated bowel. He is cold, "
               "mottled and breathing very rapidly and deeply; his blood lactate is very high. He has no kidney disease, "
               "no diabetes, no vomiting or diarrhea, and has taken no toxins."),
     labs=dict(ph=7.32, pco2=12, hco3=6, na=140, cl=104, k=4.8, alb=4.6),
     steps=["ph", "primary", "ag_calc", "ag_read", "winter_calc", "winter_read", "delta_read", "cause"],
     cause=C([
         ("Sepsis with lactic acidosis", "MAH+RAL",
          "Correct. Septic shock gives a lactic acidosis (gap 30) and drives breathing beyond what compensation needs: "
          "his carbon dioxide of 12 is below the Winter range of 15 to 19, a concurrent respiratory alkalosis."),
         ("Lactic acidosis alone", "MAH",
          "Lactic acidosis alone would leave the carbon dioxide inside the Winter range, 15 to 19. His is 12, below it. "
          "Tell: below the range adds a respiratory alkalosis."),
         ("Severe pneumonia with lactic acidosis", "MAH+RAC",
          "Severe pneumonia with lactic acidosis pairs a metabolic acidosis with a respiratory acidosis, a carbon dioxide "
          "above the Winter range. His is below it, and his infection is in the bowel. Tell: below the range is "
          "alkalosis."),
         ("Diarrhea with lactic acidosis", "MAH+MAN",
          "Diarrhea with lactic acidosis would leave the bicarbonate change larger than the gap change; here they are "
          "equal (19 and 20), and he has no diarrhea. Tell: equal changes mean no second metabolic process."),
     ], "Sepsis with lactic acidosis",
       ["Processes found: increased-gap metabolic acidosis (gap 30; changes equal) and a concurrent respiratory alkalosis "
        "(12, below 15 to 19).",
        "Does the clinical picture fit? Septic shock, very high lactate, very fast breathing.",
        "So: sepsis with lactic acidosis."], [28, 45, 49, 57]),
     summary="Acidemic increased-gap lactic acidosis in septic shock with a concurrent respiratory alkalosis: the carbon "
             "dioxide is lower than the Winter formula predicts."),

# ------------------------------------------------------------------ metabolic acidosis + respiratory acidosis (s28)
dict(id="e7-03", who="66-year-old man",
     vignette=("A 66-year-old man has had three days of fever and cough from a severe pneumonia filling both lower lungs. "
               "He is drowsy and tiring, with shallow breathing. His blood lactate is high. He has no diarrhea, no "
               "vomiting, no kidney disease and no diabetes, and takes no sedatives."),
     labs=dict(ph=7.23, pco2=40, hco3=16, na=138, cl=102, k=4.6, alb=4.6),
     steps=["ph", "primary", "ag_calc", "ag_read", "winter_calc", "winter_read", "delta_calc", "delta_read", "cause"],
     cause=C([
         ("Severe pneumonia with lactic acidosis", "MAH+RAC",
          "Correct. Severe pneumonia is a listed cause of respiratory acidosis, and the lactate gives the increased-gap "
          "acidosis. His carbon dioxide of 40 looks normal but is above the Winter range of 30 to 34: he is tiring and "
          "retaining carbon dioxide."),
         ("Septic shock with lactic acidosis", "MAH+RAL",
          "Sepsis with lactic acidosis pairs the acidosis with a respiratory alkalosis, a carbon dioxide below the Winter "
          "range. His 40 is above 30 to 34. Tell: above the range is respiratory acidosis."),
         ("Lactic acidosis without lung failure", "MAH",
          "Lactic acidosis alone would bring the carbon dioxide down into the Winter range, 30 to 34. His is 40. Tell: a "
          "normal-looking carbon dioxide can still be too high for the acidosis."),
         ("Uremia with vomiting", "MAH+MALK",
          "Uremia with vomiting hides a metabolic alkalosis, shown by a gap change much larger than the bicarbonate "
          "change. His are equal (10 and 9), and he has no kidney disease or vomiting. Tell: equal changes, no "
          "alkalosis."),
     ], "Severe pneumonia with lactic acidosis",
       ["Processes found: increased-gap metabolic acidosis (gap 20) and a concurrent respiratory acidosis (40, above the "
        "Winter range of 30 to 34).",
        "Does the clinical picture fit? Severe pneumonia, high lactate, drowsy with shallow breathing.",
        "So: severe pneumonia with lactic acidosis."], [28, 32, 45, 49, 57]),
     summary="Increased-gap lactic acidosis with a concurrent respiratory acidosis: a normal carbon dioxide of 40 is too "
             "high for a bicarbonate of 16."),

dict(id="e7-04", who="74-year-old woman",
     vignette=("A 74-year-old woman with long-standing heart failure and poor nutrition has acute pulmonary edema: she is "
               "gasping, with crackles through both lungs, cold hands and a blood lactate that is raised. She has no "
               "diarrhea or vomiting, no diabetes, and has taken no toxins."),
     labs=dict(ph=7.25, pco2=42, hco3=18, na=130, cl=101, k=4.4, alb=2.1),
     steps=["ph", "primary", "ag_calc", "alb_corr", "ag_read", "winter_calc", "winter_read", "delta_read", "cause"],
     cause=C([
         ("Pulmonary edema with lactic acidosis", "MAH+RAC",
          "Correct. Pulmonary edema is a listed cause of respiratory acidosis, and poor perfusion gives the lactic "
          "acidosis. The gap is raised only once corrected (17), and the carbon dioxide of 42 is above the Winter range "
          "of 33 to 37."),
         ("Lactic acidosis without lung failure", "MAH",
          "Lactic acidosis alone would bring the carbon dioxide into the Winter range, 33 to 37. Hers is 42, inside the "
          "normal range but too high. Tell: compare with the Winter range, not with 35 to 45."),
         ("Diarrhea with lactic acidosis", "MAH+MAN",
          "Diarrhea adds a normal-gap acidosis with a high chloride; she has no diarrhea, her chloride of 101 is normal, "
          "and her gap change matches her bicarbonate change (7 and 7). Tell: her second process comes from the lungs."),
         ("Septic shock with lactic acidosis", "MAH+RAL",
          "Sepsis pairs lactic acidosis with a respiratory alkalosis, a carbon dioxide below the Winter range. Hers is 42, "
          "above 33 to 37, and nothing in her story points to infection. Tell: above the range is respiratory acidosis."),
     ], "Pulmonary edema with lactic acidosis",
       ["Processes found: increased-gap metabolic acidosis (corrected gap 17) and a concurrent respiratory acidosis "
        "(42, above 33 to 37).",
        "Does the clinical picture fit? Acute pulmonary edema with poor perfusion and a raised lactate.",
        "So: pulmonary edema with lactic acidosis."], [28, 32, 45, 49, 57]),
     summary="A gap that looked normal (11) is raised once corrected for an albumin of 2.1 (17); the normal carbon "
             "dioxide of 42 is above the Winter range, a concurrent respiratory acidosis from pulmonary edema."),

# ------------------------------------------------------------------ metabolic alkalosis + respiratory alkalosis (s29)
dict(id="e7-05", who="59-year-old man",
     vignette=("A 59-year-old man with alcohol-related cirrhosis and tense ascites has been taking a loop diuretic and "
               "spironolactone at higher doses for two weeks. He is breathing a little fast and is mildly confused. He "
               "has not been vomiting and takes no antacids or licorice."),
     labs=dict(ph=7.57, pco2=37, hco3=33, na=134, cl=90, k=3.2),
     steps=["ph", "primary", "alk_comp", "cause"],
     cause=C([
         ("Liver disease with diuretics", "MALK+RAL",
          "Correct. Liver disease with diuretics is the classic metabolic alkalosis with respiratory alkalosis: the "
          "diuretics raise the bicarbonate, and he is breathing a little fast, so the carbon dioxide of 37 has not risen "
          "to the predicted 46. Both push the pH higher than expected."),
         ("Chronic lung disease on diuretics", "MALK+RAC",
          "Chronic lung disease on diuretics pairs the alkalosis with a respiratory acidosis, a carbon dioxide above the "
          "predicted value. His 37 is below the predicted 46, and nothing in his story points to lung disease. Tell: lower than predicted is "
          "alkalosis."),
         ("Vomiting alone", "MALK",
          "A metabolic alkalosis alone would raise the carbon dioxide to about 46. His is 37, and he has not been "
          "vomiting. Tell: a carbon dioxide that does not rise means a respiratory alkalosis too."),
         ("Uremia with vomiting", "MAH+MALK",
          "Uremia with vomiting pairs a metabolic alkalosis with a metabolic acidosis, but he has not been vomiting, "
          "and his bicarbonate is high with a carbon dioxide below the prediction. Tell: his second process is "
          "respiratory, shown by the carbon dioxide."),
     ], "Liver disease with diuretics",
       ["Processes found: metabolic alkalosis (bicarbonate 33) and a concurrent respiratory alkalosis (carbon dioxide 37, "
        "below the predicted 46).",
        "Does the clinical picture fit? Cirrhosis on diuretics, breathing fast.",
        "So: liver disease with diuretics."], [29, 53]),
     summary="Metabolic alkalosis from diuretics with a concurrent respiratory alkalosis from liver disease: the carbon "
             "dioxide did not rise as predicted and the pH is higher than expected."),

dict(id="e7-06", who="28-year-old woman",
     vignette=("A 28-year-old woman on a trek at very high altitude has vomited repeatedly for two days with altitude "
               "sickness. She is short of breath at rest, breathing fast, and her lips and tongue are dry. She takes no "
               "diuretics or antacids. Her urine chloride is 10 mEq/L."),
     labs=dict(ph=7.57, pco2=34, hco3=30, na=138, cl=97, k=3.3),
     urine_cl=10, volume_clue="Two days of vomiting with a dry mouth fit a contracted volume.",
     steps=["ph", "pair", "alk_comp", "saline", "cause"],
     cause=C([
         ("High altitude with vomiting", "MALK+RAL",
          "Correct. High altitude drives hyperventilation, a respiratory alkalosis (carbon dioxide 34), and two days of "
          "vomiting lose gastric acid, a saline-responsive metabolic alkalosis (bicarbonate 30). Both raise the pH."),
         ("Vomiting alone", "MALK",
          "Vomiting alone would raise the carbon dioxide as the lungs compensate. Hers is 34, below normal, so a "
          "respiratory alkalosis is running too. Tell: a low carbon dioxide with a high bicarbonate is two processes."),
         ("High altitude alone", "RAL",
          "Altitude alone gives a respiratory alkalosis, and the kidneys would lower the bicarbonate. Hers is 30, high. "
          "Tell: a high bicarbonate in a respiratory alkalosis is a second, metabolic, process."),
         ("Chronic lung disease on diuretics", "MALK+RAC",
          "That pair is a metabolic alkalosis with a respiratory acidosis, a high carbon dioxide. Hers is low, and she "
          "takes no diuretics. Tell: a low carbon dioxide is respiratory alkalosis."),
     ], "High altitude with vomiting",
       ["Processes found: respiratory alkalosis (carbon dioxide 34) and metabolic alkalosis (bicarbonate 30), both "
        "raising the pH.",
        "Does the clinical picture fit? High altitude (hyperventilation) and two days of vomiting.",
        "So: high altitude with vomiting."], [39, 53, 57]),
     summary="Both values push the pH up: a respiratory alkalosis from altitude and a saline-responsive metabolic "
             "alkalosis from vomiting (urine chloride 10)."),

# ------------------------------------------------------------------ metabolic alkalosis + respiratory acidosis (s29)
dict(id="e7-07", who="70-year-old man",
     vignette=("A 70-year-old man with severe chronic obstructive pulmonary disease and long-standing carbon dioxide "
               "retention started a loop diuretic three weeks ago for leg swelling. He feels weak but no more breathless "
               "than usual. He has not been vomiting and takes no steroids."),
     labs=dict(ph=7.38, pco2=70, hco3=40, na=140, cl=92, k=3.4),
     steps=["ph", "normal_read", "pair", "alk_comp", "cause"],
     cause=C([
         ("Chronic lung disease on diuretics", "MALK+RAC",
          "Correct. Chronic obstructive pulmonary disease on diuretics is the classic metabolic alkalosis with "
          "respiratory acidosis: the diuretic raises bicarbonate, the lungs retain carbon dioxide far beyond the "
          "predicted 51, and the two pull the pH to normal."),
         ("Liver disease with diuretics", "MALK+RAL",
          "That pair has a respiratory alkalosis, a carbon dioxide lower than predicted. His 70 is far above the "
          "predicted 51, and nothing in his story points to liver disease. Tell: higher than predicted is respiratory acidosis."),
         ("Diuretic use without lung disease", "MALK",
          "A diuretic alkalosis alone would lift the carbon dioxide to about 51, not 70, and would leave the pH high. "
          "Tell: a normal pH with these values means two processes."),
         ("Chronic lung disease without diuretics", "RAC",
          "Respiratory acidosis alone would leave the pH low: compensation never brings it back to normal. His pH is "
          "7.38, held up by the diuretic alkalosis. Tell: a normal pH rules out a simple disorder."),
     ], "Chronic lung disease on diuretics",
       ["Processes found: metabolic alkalosis (bicarbonate 40) and respiratory acidosis (carbon dioxide 70, far above "
        "the predicted 51), pulling against each other.",
        "Does the clinical picture fit? Severe chronic obstructive pulmonary disease, newly on a loop diuretic.",
        "So: chronic lung disease on diuretics."], [29, 32, 53]),
     summary="Normal pH from a tug of war: a diuretic metabolic alkalosis against a respiratory acidosis in chronic "
             "obstructive pulmonary disease."),

dict(id="e7-08", who="57-year-old woman",
     vignette=("A 57-year-old woman with severe kyphoscoliosis has had shallow breathing and a raised carbon dioxide for "
               "years. For the past four days she has vomited after every meal. She looks dry, takes no diuretics or "
               "steroids, and has no kidney disease."),
     labs=dict(ph=7.42, pco2=66, hco3=41, na=139, cl=90, k=3.3),
     steps=["ph", "normal_read", "pair", "chronicity", "cause"],
     cause=C([
         ("Chest wall disease with vomiting", "MALK+RAC",
          "Correct. Kyphoscoliosis is a listed musculoskeletal cause of respiratory acidosis, chronic here, and four "
          "days of vomiting lose gastric acid, a metabolic alkalosis. Her bicarbonate of 41 sits above even the chronic "
          "prediction of 34.1."),
         ("Chest wall disease without vomiting", "RAC",
          "Chronic respiratory acidosis alone predicts a bicarbonate of about 34.1 and a low pH. Hers is 41 with a "
          "normal pH. Tell: a bicarbonate above the chronic prediction is a second process."),
         ("Vomiting without chest wall disease", "MALK",
          "Vomiting alone would raise the pH above 7.45 and lift the carbon dioxide only modestly. Her carbon dioxide "
          "is 66 and her pH normal. Tell: the lung process is real too."),
         ("Uremia with vomiting", "MAH+MALK",
          "Uremia with vomiting adds an increased-gap acidosis; her gap is 8, normal, and she has no kidney disease. Her "
          "acid side is respiratory. Tell: a high carbon dioxide names the acidosis."),
     ], "Chest wall disease with vomiting",
       ["Processes found: chronic respiratory acidosis (carbon dioxide 66) and metabolic alkalosis (bicarbonate 41, above "
        "the chronic prediction of 34.1).",
        "Does the clinical picture fit? Years of kyphoscoliosis and four days of vomiting.",
        "So: chest wall disease with vomiting."], [32, 34, 53, 57]),
     summary="Normal pH: chronic respiratory acidosis from kyphoscoliosis plus a metabolic alkalosis from vomiting, "
             "found because the bicarbonate overshoots the chronic prediction."),

# ------------------------------------------------------------------ metabolic acidosis + metabolic alkalosis (s30)
dict(id="e7-09", who="62-year-old man",
     vignette=("A 62-year-old man with end-stage kidney disease has missed a week of dialysis. He is nauseated, has "
               "vomited many times a day for four days, and looks dry and unwell. He has no diabetes, no diarrhea, and "
               "has taken no toxins."),
     labs=dict(ph=7.37, pco2=43, hco3=24, na=142, cl=96, k=4.9, alb=4.6),
     steps=["ph", "normal_read", "ag_calc", "ag_read", "delta_calc", "delta_read", "cause"],
     cause=C([
         ("Uremia with vomiting", "MAH+MALK",
          "Correct. Uremia gives the increased-gap acidosis (gap 22) and vomiting the metabolic alkalosis that holds the "
          "bicarbonate at 24: the gap rose 12 while the bicarbonate fell only 1. Treat both."),
         ("Uremia alone", "MAH",
          "Uremia alone would drop the bicarbonate by about as much as the gap rose, to about 13, with a low pH. His is "
          "24. Tell: a gap change larger than the bicarbonate change hides an alkalosis."),
         ("Vomiting alone", "MALK",
          "Vomiting alone would raise the bicarbonate and the pH, and would not raise the gap to 22. Tell: a gap of 22 "
          "is an increased-gap acidosis, whatever the pH."),
         ("Diarrhea with lactic acidosis", "MAH+MAN",
          "That pair leaves the bicarbonate change larger than the gap change, with a high chloride. His gap change is "
          "larger and his chloride is 96. Tell: gap change bigger means alkalosis, not a second acidosis."),
     ], "Uremia with vomiting",
       ["Processes found: increased-gap metabolic acidosis (gap 22) and metabolic alkalosis (gap change 12, bicarbonate "
        "change 1).",
        "Does the clinical picture fit? Missed dialysis and four days of vomiting.",
        "So: uremia with vomiting."], [30, 45, 50, 53, 57]),
     summary="pH, carbon dioxide and bicarbonate all normal, yet the gap of 22 shows a uremic acidosis, and the change "
             "in gap against bicarbonate shows the alkalosis of vomiting."),

dict(id="e7-10", who="19-year-old woman",
     vignette=("A 19-year-old woman with type 1 diabetes ran out of insulin three days ago. Since then she has vomited "
               "repeatedly. She is breathing deeply, her glucose is very high and her urine is strongly positive for "
               "ketones. She has no diarrhea and no kidney disease, and has taken no toxins."),
     labs=dict(ph=7.34, pco2=31, hco3=16, na=136, cl=92, k=5.4, alb=4.6),
     steps=["ph", "primary", "ag_calc", "ag_read", "winter_calc", "winter_read", "delta_calc", "delta_read", "cause"],
     cause=C([
         ("Diabetic ketoacidosis with vomiting", "MAH+MALK",
          "Correct. Diabetic ketoacidosis raises the gap to 28, and repeated vomiting adds a metabolic alkalosis: the gap "
          "rose 18 while the bicarbonate fell only 9. Her carbon dioxide is inside the Winter range."),
         ("Diabetic ketoacidosis without vomiting", "MAH",
          "Ketoacidosis alone would drop the bicarbonate by about as much as the gap rose (18), to about 7. Hers is 16. "
          "Tell: a gap change much larger than the bicarbonate change means a hidden alkalosis."),
         ("Septic shock with lactic acidosis", "MAH+RAL",
          "Sepsis with lactic acidosis is the pair with a respiratory alkalosis, a carbon dioxide below the Winter range. "
          "Hers, 31, is inside 30 to 34, "
          "and her ketones name the acid. Tell: inside the range means no respiratory process."),
         ("Diabetic ketoacidosis treated with saline", "MAH+MAN",
          "Treatment with saline adds a normal-gap acidosis, with the bicarbonate change larger than the gap change and "
          "a high chloride. Hers is the other way round, chloride 92, and nothing in her story describes saline or other treatment. Tell: gap change bigger "
          "means alkalosis."),
     ], "Diabetic ketoacidosis with vomiting",
       ["Processes found: increased-gap metabolic acidosis (gap 28) and metabolic alkalosis (gap change 18, bicarbonate "
        "change 9); carbon dioxide inside the Winter range.",
        "Does the clinical picture fit? No insulin, ketones, and repeated vomiting.",
        "So: diabetic ketoacidosis with vomiting."], [30, 45, 50, 53, 57]),
     summary="Diabetic ketoacidosis with appropriate respiratory compensation, plus a metabolic alkalosis from vomiting "
             "that only the change in gap against bicarbonate shows."),

dict(id="e7-11", who="52-year-old man",
     vignette=("A 52-year-old man who drinks heavily and eats little stopped drinking two days ago after a binge, and has "
               "vomited many times since. He is thin and poorly nourished. His glucose is normal, his urine shows "
               "ketones, and he has no kidney disease, no diarrhea, and has taken no toxins."),
     labs=dict(ph=7.37, pco2=43, hco3=24, na=136, cl=100, k=3.6, alb=2.5),
     steps=["ph", "normal_read", "ag_calc", "alb_corr", "ag_read", "delta_read", "cause"],
     cause=C([
         ("Alcoholic ketoacidosis with vomiting", "MAH+MALK",
          "Correct. Alcoholic ketoacidosis is an increased-gap cause, hidden here by the low albumin (12 corrects to "
          "17), and vomiting adds the metabolic alkalosis: the gap rose 7 while the bicarbonate fell only 1."),
         ("Vomiting without ketoacidosis", "MALK",
          "Vomiting alone would raise the pH and the bicarbonate, with no raised gap. His corrected gap is 17. Tell: "
          "correct the gap for albumin before calling it normal."),
         ("Alcoholic ketoacidosis without vomiting", "MAH",
          "Ketoacidosis alone would lower the bicarbonate by about as much as the gap rose (7), to about 18. His is 24. "
          "Tell: a gap change larger than the bicarbonate change hides an alkalosis."),
         ("Diarrhea with lactic acidosis", "MAH+MAN",
          "That pair has a bicarbonate change larger than the gap change with a high chloride; his chloride is 100 and "
          "he has no diarrhea. Tell: here the gap change is the larger one."),
     ], "Alcoholic ketoacidosis with vomiting",
       ["Processes found: increased-gap metabolic acidosis (corrected gap 17) and metabolic alkalosis (gap change 7, "
        "bicarbonate change 1).",
        "Does the clinical picture fit? Heavy drinking, little food, ketones, repeated vomiting.",
        "So: alcoholic ketoacidosis with vomiting."], [8, 30, 45, 50, 53, 57]),
     summary="Everything looks normal until the gap is corrected for an albumin of 2.5: a hidden alcoholic "
             "ketoacidosis, with vomiting holding the bicarbonate up."),

# ------------------------------------------------------------------ increased-gap + normal-gap acidosis (s30)
dict(id="e7-12", who="45-year-old woman",
     vignette=("A 45-year-old woman has had profuse watery diarrhea for five days. She is now confused, cold and "
               "mottled, with a very low blood pressure and a high blood lactate. She has no diabetes, no kidney disease "
               "and no vomiting, and has taken no toxins."),
     labs=dict(ph=7.22, pco2=20, hco3=8, na=136, cl=112, k=3.1, alb=4.6),
     steps=["ph", "primary", "ag_calc", "ag_read", "winter_calc", "winter_read", "delta_calc", "delta_read",
            "chloride_read", "cause"],
     cause=C([
         ("Diarrhea with lactic acidosis", "MAH+MAN",
          "Correct. Diarrhea loses bicarbonate (the normal-gap part, chloride 112) and shock adds lactate (the "
          "increased-gap part, gap 16); together they explain the bicarbonate fall of 17."),
         ("Lactic acidosis without diarrhea", "MAH",
          "Lactic acidosis alone would raise the gap by about as much as the bicarbonate fell (17). Her gap rose only "
          "6. Tell: a bicarbonate change bigger than the gap change needs the chloride check."),
         ("Diarrhea without lactic acidosis", "MAN",
          "Diarrhea alone gives a normal gap, 6 to 12. Hers is 16, raised. Tell: a raised gap with a high chloride is "
          "two acidoses."),
         ("Uremia with vomiting", "MAH+MALK",
          "Uremia with vomiting leaves the gap change larger than the bicarbonate change. Hers is smaller, and she has "
          "no kidney disease or vomiting. Tell: bicarbonate change bigger means a normal-gap acidosis too."),
     ], "Diarrhea with lactic acidosis",
       ["Processes found: increased-gap acidosis (gap 16) and normal-gap acidosis (chloride change 12; 6 + 12 = 18, "
        "about the bicarbonate change of 17); carbon dioxide inside the Winter range.",
        "Does the clinical picture fit? Five days of diarrhea, then shock with a high lactate.",
        "So: diarrhea with lactic acidosis."], [30, 45, 46, 50, 57]),
     summary="Two metabolic acidoses: lactic (raised gap) and diarrheal (high chloride), found because the bicarbonate "
             "fell more than the gap rose; respiratory compensation appropriate."),

dict(id="e7-13", who="23-year-old man",
     vignette=("A 23-year-old man with type 1 diabetes was admitted last night in diabetic ketoacidosis and has since "
               "received insulin and many liters of normal saline. His ketones are clearing and he feels better. He has "
               "no diarrhea, no vomiting and no kidney disease."),
     labs=dict(ph=7.29, pco2=26, hco3=12, na=136, cl=109, k=4.0, alb=4.6),
     steps=["ph", "primary", "ag_calc", "ag_read", "winter_calc", "winter_read", "delta_read", "chloride_read", "cause"],
     cause=C([
         ("Treated diabetic ketoacidosis", "MAH+MAN",
          "Correct. Treatment of diabetic ketoacidosis with saline is a classic example of increased-gap plus normal-gap "
          "acidosis: the clearing ketones leave a gap of 15, and the saline raises the chloride to 109."),
         ("Diabetic ketoacidosis with vomiting", "MAH+MALK",
          "Vomiting would add a metabolic alkalosis, with the gap change larger than the bicarbonate change. His gap "
          "change (5) is smaller than his bicarbonate change (13), and he is not vomiting. Tell: the chloride "
          "explains the rest."),
         ("Diarrhea alone", "MAN",
          "Diarrhea is a normal-gap cause, and he has none; his gap of 15 is also still above 12. Tell: a raised gap "
          "plus a chloride rise is two acidoses."),
         ("Sepsis with lactic acidosis", "MAH+RAL",
          "Sepsis with lactic acidosis is the pair with a respiratory alkalosis. His 26 is inside the Winter range of 24 "
          "to 28, so there is no respiratory alkalosis, and nothing in his story points to sepsis. Tell: the second "
          "process here is metabolic, in the chloride."),
     ], "Treated diabetic ketoacidosis",
       ["Processes found: increased-gap acidosis (gap 15) and normal-gap acidosis (chloride change 9; 5 + 9 = 14, about "
        "the bicarbonate change of 13).",
        "Does the clinical picture fit? Diabetic ketoacidosis treated overnight with large volumes of saline.",
        "So: treated diabetic ketoacidosis."], [30, 46, 50, 57]),
     summary="Clearing diabetic ketoacidosis treated with saline: a shrinking raised gap plus a saline-driven "
             "normal-gap (hyperchloremic) acidosis."),

# ------------------------------------------------------------------ respiratory acidosis: acute, chronic, mixed (s32-35)
dict(id="e7-14", who="34-year-old man",
     vignette=("A 34-year-old man is found unresponsive an hour after injecting heroin. His breathing is slow and "
               "shallow and his pupils are pinpoint. He has no lung disease, no vomiting, and no kidney disease."),
     labs=dict(ph=7.22, pco2=70, hco3=28),
     steps=["ph", "primary", "chronicity", "cause"],
     cause=C([
         ("Opioid overdose", "RAC",
          "Correct. Narcotics are respiratory depressants, a listed central cause of respiratory acidosis. One hour of "
          "slow, shallow breathing fits the acute picture: bicarbonate 28, the acute prediction."),
         ("Anxiety attack", "RAL",
          "An anxiety attack drives fast breathing and a low carbon dioxide, a respiratory alkalosis. His is 70 with slow "
          "breathing. Tell: a high carbon dioxide is hypoventilation."),
         ("Persistent vomiting", "MALK",
          "Persistent vomiting causes a metabolic alkalosis with a high pH; his pH is 7.22 and he has not vomited. Tell: the pH "
          "and carbon dioxide name a respiratory acidosis."),
         ("Severe diarrhea", "MAN",
          "Severe diarrhea causes a normal-gap metabolic acidosis with a low bicarbonate; his bicarbonate is 28. Tell: a high "
          "carbon dioxide with a low pH is respiratory."),
     ], "Opioid overdose",
       ["Respiratory acidosis causes include central nervous system depression from sedatives; narcotics are "
        "respiratory depressants.", "Heroin an hour ago, slow shallow breathing, pinpoint pupils.",
        "So: opioid overdose."], [32, 36]),
     summary="Acute respiratory acidosis from an opioid overdose: bicarbonate 28, the acute prediction (25 + 1 x 3)."),

dict(id="e7-15", who="68-year-old woman",
     vignette=("A 68-year-old woman with long-standing chronic obstructive pulmonary disease comes for a routine clinic "
               "visit. She feels at her usual baseline, has had no recent flare, and takes no diuretics or steroids. "
               "She has not vomited recently and has no kidney disease."),
     labs=dict(ph=7.34, pco2=64, hco3=33),
     steps=["ph", "primary", "chronicity", "cause"],
     cause=C([
         ("Chronic obstructive pulmonary disease", "RAC",
          "Correct. Chronic obstructive pulmonary disease is a listed lung-disease cause of respiratory acidosis, and "
          "her stable, long-standing course fits the chronic picture: bicarbonate 33, the chronic prediction."),
         ("Years of living at very high altitude", "RAL",
          "Years at very high altitude causes hyperventilation, a low carbon dioxide. Hers is 64. Tell: a high carbon dioxide is "
          "hypoventilation."),
         ("Primary aldosteronism (adrenal excess)", "MALK",
          "Primary aldosteronism causes a metabolic alkalosis with a high pH; hers is 7.34 and her bicarbonate matches "
          "the chronic compensation. Tell: a bicarbonate that fits compensation is not a second disorder."),
         ("Renal tubular acidosis from a medicine", "MAN",
          "Renal tubular acidosis lowers the bicarbonate; hers is high, 33. Tell: a high carbon dioxide with a low pH is "
          "respiratory."),
     ], "Chronic obstructive pulmonary disease",
       ["Respiratory acidosis causes include lung disease such as chronic obstructive pulmonary disease.",
        "Long-standing disease at her baseline; bicarbonate at the chronic prediction.",
        "So: chronic obstructive pulmonary disease."], [32, 34]),
     summary="Chronic respiratory acidosis: bicarbonate 33 matches 25 + 3.5 x 2.4 = 33.4, the kidneys' work over days."),

dict(id="e7-16", who="41-year-old man",
     vignette=("A 41-year-old man was crushed in a car crash. Several ribs are broken in two places, so part of his chest "
               "wall moves inward when he breathes in (flail chest). He is bleeding internally, with a very low blood "
               "pressure, cold skin and a high blood lactate. He has no lung or kidney disease and took no drugs."),
     labs=dict(ph=7.10, pco2=60, hco3=18, na=140, cl=105, k=4.5, alb=4.6),
     steps=["ph", "pair", "ag_calc", "ag_read", "winter_calc", "winter_read", "cause"],
     cause=C([
         ("Flail chest with lactic acidosis", "MAH+RAC",
          "Correct. Flail chest is a listed thoracic cage injury causing respiratory acidosis (carbon dioxide 60), and "
          "blood loss with shock gives the lactic acidosis (gap 17). Both lower the pH, to 7.10."),
         ("Flail chest without blood loss", "RAC",
          "A respiratory acidosis alone would leave the bicarbonate normal or high; his is 18 with a gap of 17. Tell: a "
          "low bicarbonate with a high carbon dioxide is two acidoses."),
         ("Lactic acidosis without lung failure", "MAH",
          "Lactic acidosis alone would bring the carbon dioxide down to the Winter range, 33 to 37. His is 60. Tell: "
          "above the range is a respiratory acidosis too."),
         ("Septic shock with lactic acidosis", "MAH+RAL",
          "Sepsis pairs lactic acidosis with a respiratory alkalosis, a low carbon dioxide. His is 60. Tell: a high "
          "carbon dioxide is respiratory acidosis."),
     ], "Flail chest with lactic acidosis",
       ["Processes found: respiratory acidosis (carbon dioxide 60, far above the Winter range of 33 to 37) and "
        "increased-gap metabolic acidosis (gap 17).",
        "Does the clinical picture fit? Flail chest plus bleeding with shock and a high lactate.",
        "So: flail chest with lactic acidosis."], [28, 32, 45, 49, 57]),
     summary="Acidosis on both sides: respiratory from a flail chest and lactic from shock, together dropping the pH to "
             "7.10."),

# ------------------------------------------------------------------ metabolic alkalosis, saline types (s51-53)
dict(id="e7-17", who="55-year-old woman",
     vignette=("A 55-year-old woman is four days out from bowel surgery, with a nasogastric tube on continuous suction "
               "draining large volumes of stomach fluid. She feels weak and her mouth is dry. She takes no diuretics and "
               "has no lung disease. Her urine chloride is 14 mEq/L."),
     labs=dict(ph=7.48, pco2=47, hco3=34, na=137, cl=92, k=3.0),
     urine_cl=14, volume_clue="Days of gastric suction with a dry mouth fit a contracted volume.",
     steps=["ph", "primary", "alk_comp", "saline", "potassium"],
     summary="Simple metabolic alkalosis from gastric suction with the expected rise in carbon dioxide; saline "
             "responsive (urine chloride 14), with potassium shifted into cells."),

dict(id="e7-18", who="46-year-old man",
     vignette=("A 46-year-old man has high blood pressure despite three medicines, plus muscle cramps and weakness. A scan "
               "shows a small adrenal mass. He eats no licorice, takes no diuretics or steroids, and has not vomited. His "
               "blood pressure is 168/98 mm Hg and his urine chloride is 70 mEq/L."),
     labs=dict(ph=7.48, pco2=45, hco3=32, na=144, cl=100, k=2.8),
     urine_cl=70, sbp=168, bp_text="blood pressure of 168/98 mm Hg is raised",
     steps=["ph", "primary", "alk_comp", "saline", "potassium", "cause"],
     cause=C([
         ("Primary aldosteronism", "MALK",
          "Correct. Primary aldosteronism is a hypertensive, saline-unresponsive cause of metabolic alkalosis; the "
          "adrenal mass, resistant hypertension and low potassium fit."),
         ("Licorice", "MALK",
          "Licorice gives the same hypertensive, saline-unresponsive picture, but he eats none, and he has an adrenal "
          "mass. Tell: the history decides between causes of one type."),
         ("Vomiting", "MALK",
          "Vomiting is a saline-responsive cause with a urine chloride below 25. His is 70, and he has not vomited. "
          "Tell: a high urine chloride rules out the responsive causes."),
         ("Severe potassium depletion", "MALK",
          "Severe potassium depletion is a normotensive saline-unresponsive cause. His blood pressure is 168/98. Tell: "
          "a raised blood pressure points to the hypertensive group."),
     ], "Primary aldosteronism",
       ["Saline unresponsive (urine chloride 70) and hypertensive (168/98): primary aldosteronism, exogenous "
        "mineralocorticoids or licorice.", "Adrenal mass; no licorice, no steroids.",
        "So: primary aldosteronism."], [53], prompt="Which cause best fits this patient?"),
     summary="Saline-unresponsive, hypertensive metabolic alkalosis from primary aldosteronism, with the expected "
             "compensation and hypokalemia."),

dict(id="e7-19", who="60-year-old woman",
     vignette=("A 60-year-old woman has profound weakness and her potassium is found to be severely depleted. Her blood "
               "pressure is 116/72 mm Hg. She has not vomited, takes no diuretics, steroids or licorice, and has no "
               "adrenal mass. Her urine chloride is 58 mEq/L."),
     labs=dict(ph=7.47, pco2=44, hco3=31, na=140, cl=99, k=2.2),
     urine_cl=58, sbp=116, bp_text="blood pressure of 116/72 mm Hg is normal",
     steps=["ph", "primary", "alk_comp", "saline", "cause"],
     cause=C([
         ("Severe potassium depletion", "MALK",
          "Correct. Severe potassium depletion is a listed normotensive, saline-unresponsive cause, and it fits her "
          "severely low potassium with a normal blood pressure."),
         ("Primary aldosteronism", "MALK",
          "Primary aldosteronism is saline unresponsive but hypertensive, and her blood pressure is 116/72 with no "
          "adrenal mass. Tell: a normal blood pressure points to the normotensive group."),
         ("Licorice eaten in large amounts", "MALK",
          "Licorice is a hypertensive cause, and she eats none and is normotensive. Tell: in the unresponsive type, "
          "blood pressure sorts the causes."),
         ("Vomiting with loss of stomach acid", "MALK",
          "Vomiting is saline responsive with a urine chloride below 25; hers is 58 and she has not vomited. Tell: a high "
          "urine chloride rules out the responsive causes."),
     ], "Severe potassium depletion",
       ["Saline unresponsive (urine chloride 58) and normotensive (116/72): severe potassium depletion is a listed "
        "cause, and her potassium is severely low.", "Severely depleted potassium; no vomiting, diuretics, steroids, licorice or adrenal mass.",
        "So: severe potassium depletion."], [53], prompt="Which cause best fits this patient?"),
     summary="Saline-unresponsive, normotensive metabolic alkalosis from severe potassium depletion."),

# ------------------------------------------------------------------ simple metabolic acidosis: albumin, normal gap
dict(id="e7-20", who="80-year-old woman",
     vignette=("An 80-year-old nursing-home resident who is frail and poorly nourished has pneumonia with low blood "
               "pressure and a high blood lactate. She is breathing deeply. She has no diarrhea, no vomiting, no kidney "
               "disease and no diabetes, and has taken no toxins."),
     labs=dict(ph=7.33, pco2=35, hco3=18, na=136, cl=106, k=4.3, alb=2.9),
     steps=["ph", "primary", "ag_calc", "alb_corr", "ag_read", "winter_calc", "winter_read", "delta_read", "cause"],
     cause=C([
         ("Lactic acidosis", "MAH",
          "Correct. Lactic acidosis from poor tissue perfusion is one of the big four increased-gap causes; her gap is "
          "raised only once corrected for the albumin (16), and her high lactate names the acid."),
         ("Diarrhea", "MAN",
          "Diarrhea is a normal-gap cause with a high chloride. Her corrected gap is 16 and her chloride 106, and she has "
          "no diarrhea. Tell: correct the gap before calling it normal."),
         ("Renal tubular acidosis", "MAN",
          "Renal tubular acidosis is a normal-gap cause; her corrected gap of 16 is raised. Tell: a gap that only looks "
          "normal because of a low albumin is a raised gap."),
         ("Vomiting", "MALK",
          "Vomiting causes a metabolic alkalosis; her pH is low and her gap change matches her bicarbonate change, so "
          "nothing is holding bicarbonate up. Tell: equal changes mean no alkalosis."),
     ], "Lactic acidosis",
       ["Increased-gap metabolic acidosis (corrected gap 16), appropriately compensated, changes equal.",
        "Does the clinical picture fit? Pneumonia with low blood pressure and a high lactate.",
        "So: lactic acidosis."], [45, 57], prompt="Which cause best fits this patient?"),
     summary="An increased-gap lactic acidosis that a low albumin (2.9) had hidden: 12 corrects to 16; compensation "
             "appropriate, no second metabolic process."),

dict(id="e7-21", who="30-year-old man",
     vignette=("A 30-year-old man has had severe watery diarrhea for four days after a trip abroad. He is weak and thirsty "
               "but alert, with warm hands. His glucose and kidney function are normal, he has no vomiting, and he has "
               "taken no toxins or medicines."),
     labs=dict(ph=7.31, pco2=29, hco3=14, na=138, cl=114, k=3.2, alb=4.6),
     steps=["ph", "primary", "ag_calc", "ag_read", "winter_calc", "winter_read", "cause"],
     cause=C([
         ("Diarrhea", "MAN",
          "Correct. Diarrhea is the common normal-gap cause: bicarbonate lost in the stool, a gap of 10 and a chloride "
          "of 114. Four days of watery diarrhea fit."),
         ("Lactic acidosis", "MAH",
          "Lactic acidosis is an increased-gap cause; his gap of 10 is normal, and he is warm and alert. Tell: a normal "
          "gap points to the USEDCAR list."),
         ("Uremia", "MAH",
          "Uremia raises the gap, and his kidney function is normal with a gap of 10. Tell: a normal gap is not uremia."),
         ("Vomiting", "MALK",
          "Vomiting causes a metabolic alkalosis; his pH is low with a low bicarbonate. Tell: match the cause to the "
          "process the numbers show."),
     ], "Diarrhea",
       ["Normal-gap metabolic acidosis (gap 10, chloride 114), appropriately compensated.",
        "The USEDCAR list: ureteral diversion, saline infusion, exogenous acid, diarrhea, carbonic anhydrase inhibitors, "
        "adrenal insufficiency, renal tubular acidosis.", "Four days of diarrhea.", "So: diarrhea."], [43, 46, 47],
       prompt="Which cause best fits this patient?"),
     summary="Simple normal-gap (hyperchloremic) metabolic acidosis from diarrhea, with appropriate respiratory "
             "compensation."),
]
