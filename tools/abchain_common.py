# -*- coding: utf-8 -*-
"""Shared step builder for the Acid-Base Case Chain mode (Arcade + homepage, 2026-10-29).

A case is a patient, a pinned set of blood values (every value with its normal range) and an ordered chain of
steps. The ARITHMETIC steps (pH, primary disorder, compensation, Winter formula, anion gap, chloride pattern,
potassium shift, curve shift, saline type) are generated here from the case's own numbers, so every number in an
explanation or a walk-through is computed, not typed. The CLINICAL steps (cause, next step) are written by hand in
the case files (tools/abchain_pdm_e4.py, tools/abchain_cms_e6.py).

The keys computed here are re-derived INDEPENDENTLY by tools/check_acid_base_cases.py from the shipped JSON; this
module also asserts each case's declared intent (`expect`) against what the numbers give, so a typo in a value
fails the build instead of shipping a wrong key.

Course rules (slides only; each set is scoped to its own deck):
  PDM I Lecture 19 (Finck), "Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx":
    pH 7.35-7.45 (s18-19); PaCO2 35-45 (s11, s21, s54); bicarbonate 22-26, sodium 135-148, chloride 98-106,
    potassium 3.6-5.2 (s54); anion gap Na - (Cl + HCO3), normal 9-15 (s46); compensation by DIRECTION only
    (s27-28, s30-31, s33, s50-53); albumin correction is NAMED but never calculated (s48; the lecturer, 1:22:14:
    "just know that it needs to be corrected"). No Winter formula, no ratios, no delta-delta, no osmolar gap.
  CMS I Lecture 34 (Finck), "PAJ5500 CMSI Acid Base MBF 2026sc.pptx":
    pH 7.35-7.45, acidemia/alkalemia (s3, s5); PaCO2 36-44, bicarbonate 22-26 (s5-6); unsustainable below 6.7 or
    above 7.6 (s8); compensation never returns the pH to normal (s19); renal for respiratory, respiratory for
    metabolic (s20); acute/chronic ratios (s59, GIVEN in the prompt with the 40/24 midpoints, as the L34 build
    does); metabolic alkalosis carbon dioxide rarely above 55 (s38); urine chloride and the saline types (s37,
    s41-43); anion gap 9-15 (s47); chloride pattern (s52); Winter formula, and ONLY its "higher than expected =
    added respiratory acidosis" direction (s58). The "below the range" mirror rule is NOT on the slides and is
    never keyed or stated; no case has a carbon dioxide below its Winter range.
Sodium, chloride and potassium ranges for CMS are standard laboratory scaffolding (the CMS deck gives none), the
same ranges the shipped L34 quizzes use. Albumin's 3.5-5.0 g/dL is scaffolding too.
"""
import math

PDM_DECK = "Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx"
CMS_DECK = "PAJ5500 CMSI Acid Base MBF 2026sc.pptx"

COURSES = {
    "pdm": dict(
        deck=PDM_DECK, ph=(7.35, 7.45), pco2=(35, 45), hco3=(22, 26), na=(135, 148), cl=(98, 106),
        k=(3.6, 5.2), ag=(9, 15), alb=(3.5, 5.0), po2_text="greater than 80", po2=(80, None),
        acid="Acidosis", alk="Alkalosis", acid_adj="acidosis", alk_adj="alkalosis",
        extreme="Incompatible with life"),
    "cms": dict(
        deck=CMS_DECK, ph=(7.35, 7.45), pco2=(36, 44), hco3=(22, 26), na=(135, 145), cl=(98, 106),
        k=(3.5, 5.0), ag=(9, 15), alb=(3.5, 5.0), po2_text="80 to 100", po2=(80, 100),
        acid="Acidemia", alk="Alkalemia", acid_adj="acidemia", alk_adj="alkalemia",
        extreme="Unsustainable pH"),
}

LABEL = {
    "ph": "pH", "pco2": "PaCO2 (arterial carbon dioxide)", "hco3": "Bicarbonate", "po2": "PaO2 (arterial oxygen)",
    "na": "Sodium", "cl": "Chloride", "k": "Potassium", "alb": "Albumin",
}
UNIT = {"ph": "", "pco2": "mm Hg", "hco3": "mEq/L", "po2": "mm Hg", "na": "mEq/L", "cl": "mEq/L", "k": "mEq/L",
        "alb": "g/dL"}
ORDER = ["ph", "pco2", "hco3", "po2", "na", "cl", "k", "alb"]

ACID, ALK = "acid", "alk"
RACID, RALK, MACID, MALK = "Respiratory acidosis", "Respiratory alkalosis", "Metabolic acidosis", "Metabolic alkalosis"


def f(x, nd=2):
    """Number for prose: 26, 25.5, 46.75, never 26.0."""
    if isinstance(x, str):
        return x
    r = round(x, nd)
    if abs(r - round(r)) < 1e-9:
        return str(int(round(r)))
    return (("%." + str(nd) + "f") % r).rstrip("0").rstrip(".") if nd else str(r)


def fph(x):
    return "%.2f" % x


def rng(t):
    lo, hi = t
    return "%s to %s" % (f(lo), f(hi))


def cite(cfg, slides):
    s = sorted(set(slides))
    word = "Slide" if len(s) == 1 else "Slides"
    return "%s, %s %s" % (cfg["deck"], word, ", ".join(str(n) for n in s))


def hh(hco3, pco2):
    """Henderson-Hasselbalch: an internal realism check only, never taught or keyed."""
    return 6.1 + math.log10(hco3 / (0.03 * pco2))


def status(v, t):
    lo, hi = t
    if lo is not None and v < lo:
        return "low"
    if hi is not None and v > hi:
        return "high"
    return "normal"


# ---------------------------------------------------------------- the numbers

class Ctx:
    """Everything the generators need, computed once per case."""

    def __init__(self, course, case):
        self.course = course
        self.cfg = COURSES[course]
        self.c = case
        L = case["labs"]
        self.L = L
        self.ph, self.p, self.h = L["ph"], L["pco2"], L["hco3"]
        cfg = self.cfg
        self.dir = ACID if self.ph < cfg["ph"][0] else ALK if self.ph > cfg["ph"][1] else None
        assert self.dir, "%s: pH %s is inside the normal range; every case needs acidemia or alkalemia" % (
            case["id"], self.ph)
        ps, hs = status(self.p, cfg["pco2"]), status(self.h, cfg["hco3"])
        self.ps, self.hs = ps, hs
        cands = []
        if self.dir == ACID:
            if ps == "high":
                cands.append(RACID)
            if hs == "low":
                cands.append(MACID)
        else:
            if ps == "low":
                cands.append(RALK)
            if hs == "high":
                cands.append(MALK)
        assert len(cands) == 1, "%s: primary disorder is not unique from the numbers: %s" % (case["id"], cands)
        self.primary = cands[0]
        self.resp = self.primary in (RACID, RALK)
        if "na" in L and "cl" in L:
            self.ag = L["na"] - (L["cl"] + self.h)
        else:
            self.ag = None

    # small phrase helpers
    def pdesc(self):
        lo, hi = self.cfg["pco2"]
        return {"low": "below %s" % f(lo), "high": "above %s" % f(hi), "normal": "inside %s to %s" % (f(lo), f(hi))}[
            self.ps]

    def hdesc(self):
        lo, hi = self.cfg["hco3"]
        return {"low": "below %s" % f(lo), "high": "above %s" % f(hi), "normal": "inside %s to %s" % (f(lo), f(hi))}[
            self.hs]

    def phword(self):
        return self.cfg["acid_adj"] if self.dir == ACID else self.cfg["alk_adj"]


# ---------------------------------------------------------------- generators
# Each returns (options, key_text, walk_lines, slides); options = [(text, explanation)].

def step_ph(x):
    cfg, ph = x.cfg, fph(x.ph)
    lo, hi = cfg["ph"]
    pdm = x.course == "pdm"
    A, K = cfg["acid"], cfg["alk"]
    if x.dir == ACID:
        key, other = A, K
        side, word, push = "below %s" % f(lo), cfg["acid_adj"], "down"
    else:
        key, other = K, A
        side, word, push = "above %s" % f(hi), cfg["alk_adj"], "up"
    opts = []
    opts.append((key, "Correct. The pH of %s is %s, outside the normal %s to %s, so this is %s. The next step is to find "
                 "which value, carbon dioxide or bicarbonate, is pushing the pH %s." % (ph, side, f(lo), f(hi), word, push)))
    if x.dir == ACID:
        opts.append((other, "%s means a pH above %s. This pH is %s, below %s, so the blood is on the acid side. Tell: "
                     "below the normal range is %s, above it is %s; read the direction first."
                     % (other, f(hi), ph, f(lo), cfg["acid_adj"], cfg["alk_adj"])))
    else:
        opts.append((other, "%s means a pH below %s. This pH is %s, above %s, so the blood is on the alkaline side. "
                     "Tell: above the normal range is %s, below it is %s; read the direction first."
                     % (other, f(lo), ph, f(hi), cfg["alk_adj"], cfg["acid_adj"])))
    if pdm:
        opts.append(("Normal pH", "A normal arterial pH is %s to %s, and %s is %s it, so the pH is abnormal: %s. "
                     "Tell: the pH is read against its own range before carbon dioxide or bicarbonate."
                     % (f(lo), f(hi), ph, "below" if x.dir == ACID else "above", word)))
        opts.append((cfg["extreme"], "Only a narrow pH range, 6.9 to 7.8, is compatible with life. A pH of %s is "
                     "abnormal but inside that range, so it is %s to be explained, not an unsurvivable value. Tell: this "
                     "label marks the extremes of pH, not its direction." % (ph, word)))
        slides = [17, 18, 19]
    else:
        opts.append(("Normal pH", "A normal arterial pH is %s to %s, and %s is %s it. Compensation never returns the pH "
                     "to normal, so a compensated disorder still shows an abnormal pH. Tell: compare the pH with its "
                     "range first." % (f(lo), f(hi), ph, "below" if x.dir == ACID else "above")))
        opts.append((cfg["extreme"], "A pH is unsustainable below 6.7 or above 7.6. A pH of %s is abnormal but inside "
                     "those limits, so it is %s to be explained, not an unsustainable value. Tell: unsustainable "
                     "describes how far the pH has moved, not which way." % (ph, word)))
        slides = [3, 5, 8, 19]
    walk = ["Compare the pH with its normal range, %s to %s." % (f(lo), f(hi)),
            "%s is %s." % (ph, side),
            "So the blood shows %s." % word]
    return opts, key, walk, slides


def _other_value_sentence(x):
    """For the primary-step key: what the non-primary value is doing."""
    p, h = f(x.p), f(x.h)
    if x.primary == MACID:
        if x.ps == "low":
            tail = ("; whether that response is enough is the next check" if any(
                (st[0] if isinstance(st, tuple) else st) == "winter_calc" for st in x.c["steps"]) else "")
            return ("The carbon dioxide of %s is low too, but a low carbon dioxide would raise the pH, so it did not "
                    "cause the %s; it is the lungs responding%s." % (p, x.phword(), tail))
        tail = ("; whether the lungs responded enough is the next check" if any(
            (st[0] if isinstance(st, tuple) else st) == "winter_calc" for st in x.c["steps"]) else "")
        return "The carbon dioxide of %s is %s, so it did not cause the %s%s." % (p, x.pdesc(), x.phword(), tail)
    if x.primary == MALK:
        if x.ps == "high":
            return ("The carbon dioxide of %s is high too, but a high carbon dioxide would lower the pH, so it did not "
                    "cause the %s." % (p, x.phword()))
        return "The carbon dioxide of %s is %s, so it did not cause the %s." % (p, x.pdesc(), x.phword())
    if x.primary == RACID:
        if x.hs == "high":
            return ("The bicarbonate of %s is high, which would raise the pH, so it is not the cause; it is the "
                    "kidneys compensating." % h)
        return "The bicarbonate of %s is still %s, so it did not cause the %s." % (h, x.hdesc(), x.phword())
    if x.hs == "low":
        return ("The bicarbonate of %s is low, which would lower the pH, so it is not the cause; it is the kidneys "
                "compensating." % h)
    return "The bicarbonate of %s is still %s, so it did not cause the %s." % (h, x.hdesc(), x.phword())


def step_primary(x):
    cfg = x.cfg
    plo, phi = cfg["pco2"]
    hlo, hhi = cfg["hco3"]
    ph, p, h = fph(x.ph), f(x.p), f(x.h)
    word = x.phword()
    expl = {}
    if x.primary == RACID:
        expl[RACID] = ("Correct. The pH of %s is low, and the carbon dioxide of %s is above %s: retained carbon dioxide "
                       "lowers the pH, so the problem is respiratory. %s" % (ph, p, f(phi), _other_value_sentence(x)))
    elif x.primary == RALK:
        expl[RALK] = ("Correct. The pH of %s is high, and the carbon dioxide of %s is below %s: breathing off carbon "
                      "dioxide raises the pH, so the problem is respiratory. %s" % (ph, p, f(plo), _other_value_sentence(x)))
    elif x.primary == MACID:
        expl[MACID] = ("Correct. The pH of %s is low, and the bicarbonate of %s is below %s: a low bicarbonate lowers "
                       "the pH, so the problem is metabolic. %s" % (ph, h, f(hlo), _other_value_sentence(x)))
    else:
        expl[MALK] = ("Correct. The pH of %s is high, and the bicarbonate of %s is above %s: a high bicarbonate raises "
                      "the pH, so the problem is metabolic. %s" % (ph, h, f(hhi), _other_value_sentence(x)))
    # wrong choices.  Never state a bare threshold rule ("needs a carbon dioxide above 40"): a later CMS step can
    # find an added respiratory or metabolic component, so each wrong choice says only that the value did not move
    # the pH the way it went (slide 60: concurrent disturbances may push pH in the same or opposite direction).
    pfx = {"high": "a high carbon dioxide lowers the pH", "low": "a low carbon dioxide raises the pH",
           "normal": "a normal carbon dioxide does not move the pH"}[x.ps]
    hfx = {"high": "a high bicarbonate raises the pH", "low": "a low bicarbonate lowers the pH",
           "normal": "a normal bicarbonate does not move the pH"}[x.hs]
    pstate = "%s, %s" % (x.ps, x.pdesc()) if x.ps != "normal" else "normal, %s" % x.pdesc()
    hstate = "%s, %s" % (x.hs, x.hdesc()) if x.hs != "normal" else "normal, %s" % x.hdesc()
    later = ""
    if x.course == "cms":
        later = (" Whether the lungs add a problem of their own is a later check." if not x.resp
                 else " Whether the kidneys add a problem of their own is a later check.")
    moved = "lower" if x.dir == ACID else "raise"
    if x.dir == ACID:
        cause = "the high carbon dioxide of %s" % p if x.primary == RACID else "the low bicarbonate of %s" % h
        if x.primary != RACID:
            expl[RACID] = ("The carbon dioxide of %s is %s, and %s, so it did not %s this pH; %s did.%s Tell: in a "
                           "primary respiratory acidosis carbon dioxide rises as the pH falls."
                           % (p, pstate, pfx, moved, cause, later))
        if x.primary != MACID:
            expl[MACID] = ("The bicarbonate of %s is %s, and %s, so it did not %s this pH; %s did.%s Tell: in a "
                           "primary metabolic acidosis bicarbonate falls with the pH."
                           % (h, hstate, hfx, moved, cause, later))
        lowp = ("The carbon dioxide of %s is low, but a low carbon dioxide raises the pH, so it does not explain this "
                "%s; the bicarbonate does." % (p, word) if x.ps == "low"
                else "Its carbon dioxide of %s is not low either." % p)
        expl[RALK] = ("A respiratory alkalosis on its own raises the pH above %s, and this pH is %s, %s. %s Tell: the "
                      "pH sets the direction before anything else." % (f(cfg["ph"][1]), ph, word, lowp))
        highh = ("The bicarbonate of %s is high, but a high bicarbonate raises the pH, so it does not explain this "
                 "%s; the carbon dioxide does." % (h, word) if x.hs == "high"
                 else "Its bicarbonate of %s is not high either." % h)
        expl[MALK] = ("A metabolic alkalosis on its own raises the pH above %s, and this pH is %s, %s. %s Tell: in a "
                      "primary metabolic alkalosis bicarbonate and pH both rise." % (f(cfg["ph"][1]), ph, word, highh))
    else:
        cause = "the low carbon dioxide of %s" % p if x.primary == RALK else "the high bicarbonate of %s" % h
        if x.primary != RALK:
            expl[RALK] = ("The carbon dioxide of %s is %s, and %s, so it did not %s this pH; %s did.%s Tell: in a "
                          "primary respiratory alkalosis carbon dioxide falls as the pH rises."
                          % (p, pstate, pfx, moved, cause, later))
        if x.primary != MALK:
            expl[MALK] = ("The bicarbonate of %s is %s, and %s, so it did not %s this pH; %s did.%s Tell: in a "
                          "primary metabolic alkalosis bicarbonate rises with the pH."
                          % (h, hstate, hfx, moved, cause, later))
        highp = ("The carbon dioxide of %s is high, but a high carbon dioxide pulls the pH down, so it does not "
                 "explain this %s; the bicarbonate does." % (p, word) if x.ps == "high"
                 else "Its carbon dioxide of %s is not high either." % p)
        expl[RACID] = ("A respiratory acidosis on its own lowers the pH below %s, and this pH is %s, %s. %s Tell: the "
                       "primary disorder is the value that moves the pH the way it went." % (f(cfg["ph"][0]), ph, word,
                                                                                            highp))
        lowh = ("The bicarbonate of %s is low, but a low bicarbonate lowers the pH, so it does not explain this "
                "%s; the carbon dioxide does." % (h, word) if x.hs == "low"
                else "Its bicarbonate of %s is not low either." % h)
        expl[MACID] = ("A metabolic acidosis on its own lowers the pH below %s, and this pH is %s, %s. %s Tell: in a "
                       "primary metabolic acidosis bicarbonate and pH both fall." % (f(cfg["ph"][0]), ph, word, lowh))
    opts = [(k, expl[k]) for k in (RACID, RALK, MACID, MALK)]
    pmove = {"high": "a high carbon dioxide lowers the pH", "low": "a low carbon dioxide raises the pH",
             "normal": "a normal carbon dioxide is not the primary change"}[x.ps]
    hmove = {"high": "a high bicarbonate raises the pH", "low": "a low bicarbonate lowers the pH",
             "normal": "a normal bicarbonate is not the primary change"}[x.hs]
    match = "carbon dioxide" if x.resp else "bicarbonate"
    walk = ["pH %s: %s." % (ph, word),
            "Carbon dioxide %s (normal %s): %s, and %s." % (p, rng(cfg["pco2"]), x.ps, pmove),
            "Bicarbonate %s (normal %s): %s, and %s." % (h, rng(cfg["hco3"]), x.hs, hmove),
            "The value that moves the pH the way it actually went is the %s, so the primary disorder is %s."
            % (match, x.primary.lower())]
    slides = [27, 30, 31, 33, 50, 51, 52, 53] if x.course == "pdm" else [20, 21, 29, 36, 45, 61, 63]
    return opts, x.primary, walk, slides


# PDM compensation, by direction only (slides 27-28, 30-31, 33, 50-53).
NONE = "No compensation yet"
KUP, KDOWN = "Kidneys raising bicarbonate", "Kidneys lowering bicarbonate"
LDOWN, LUP = "Lungs lowering carbon dioxide", "Lungs raising carbon dioxide"


def step_comp_pdm(x):
    cfg = x.cfg
    p, h = f(x.p), f(x.h)
    plo, phi = cfg["pco2"]
    hlo, hhi = cfg["hco3"]
    pr = x.primary
    if pr == RACID:
        key = KUP if x.hs == "high" else NONE
        assert x.hs in ("high", "normal"), x.c["id"]
        good, wrongdir, wrongsys = KUP, KDOWN, LDOWN
    elif pr == RALK:
        key = KDOWN if x.hs == "low" else NONE
        assert x.hs in ("low", "normal"), x.c["id"]
        good, wrongdir, wrongsys = KDOWN, KUP, LUP
    elif pr == MACID:
        key = LDOWN if x.ps == "low" else NONE
        assert x.ps in ("low", "normal"), x.c["id"]
        good, wrongdir, wrongsys = LDOWN, LUP, KUP
    else:
        key = LUP if x.ps == "high" else NONE
        assert x.ps in ("high", "normal"), x.c["id"]
        good, wrongdir, wrongsys = LUP, LDOWN, KDOWN
    E = {}
    # the compensating value and its words
    if x.resp:
        val, vname, vrange, vst = h, "bicarbonate", rng(cfg["hco3"]), x.hs
    else:
        val, vname, vrange, vst = p, "carbon dioxide", rng(cfg["pco2"]), x.ps
    if key == NONE:
        if pr == RACID:
            E[NONE] = ("Correct. The bicarbonate of %s is still inside %s, so the kidneys have not changed it yet. High "
                       "carbon dioxide, low pH and a normal bicarbonate is the acute pattern; renal compensation takes "
                       "days to build." % (h, vrange))
        elif pr == RALK:
            E[NONE] = ("Correct. The bicarbonate of %s is still inside %s: low carbon dioxide, high pH and a normal "
                       "bicarbonate are the findings of respiratory alkalosis before the kidneys respond, which takes "
                       "days." % (h, vrange))
        elif pr == MACID:
            E[NONE] = ("Correct. The carbon dioxide of %s is still inside %s, the expected finding in metabolic acidosis "
                       "before the lungs respond." % (p, vrange))
        else:
            E[NONE] = ("Correct. The carbon dioxide of %s is still inside %s, the expected finding in metabolic "
                       "alkalosis before the lungs respond." % (p, vrange))
    else:
        E[NONE] = ("The %s of %s is outside its normal %s, moved in the direction that pulls the pH back toward "
                   "normal, so compensation has begun. Tell: only a normal %s would mean none yet."
                   % (vname, val, vrange, vname))
    if key == KUP:
        E[KUP] = ("Correct. The bicarbonate of %s is above %s: the kidneys have reabsorbed more bicarbonate to offset "
                  "the retained carbon dioxide. That rise takes days, the chronic pattern of long-standing lung or "
                  "chest wall disease." % (h, f(hhi)))
    if key == KDOWN:
        E[KDOWN] = ("Correct. The bicarbonate of %s is below %s: the kidneys have reabsorbed less bicarbonate to offset "
                    "the low carbon dioxide. Renal compensation takes days, so this respiratory alkalosis is long "
                    "standing." % (h, f(hlo)))
    if key == LDOWN:
        E[LDOWN] = ("Correct. The carbon dioxide of %s is below %s: faster breathing is blowing off carbon dioxide to "
                    "offset the low bicarbonate. Respiratory compensation for a metabolic disorder works within "
                    "minutes to hours." % (p, f(plo)))
    if key == LUP:
        E[LUP] = ("Correct. The carbon dioxide of %s is above %s: slower breathing retains carbon dioxide to offset the "
                  "high bicarbonate. Respiratory compensation for a metabolic disorder works within minutes to hours."
                  % (p, f(phi)))
    if key != good:
        # the "good" direction is offered but this case has not compensated (or the other way round)
        if good in (KUP, KDOWN):
            E[good] = ("%s would show a %s bicarbonate. Here the bicarbonate is %s, still inside %s, the pattern "
                       "before the kidneys respond. Tell: renal compensation takes days to appear."
                       % (good, "raised" if good == KUP else "lowered", h, vrange))
        else:
            E[good] = ("%s would show a %s carbon dioxide. Here it is %s, still inside %s, the pattern before the "
                       "lungs respond. Tell: compensation is read from the value that is not the primary problem."
                       % (good, "lowered" if good == LDOWN else "raised", p, vrange))
    # wrong direction
    if x.resp:
        E[wrongdir] = ("%s would push the pH further the wrong way. In %s the kidneys offset the change by moving "
                       "bicarbonate the same way as carbon dioxide; here bicarbonate is %s, %s. Tell: compensation "
                       "pulls the pH back toward normal." % (wrongdir, pr.lower(), h, x.hdesc()))
        E[wrongsys] = ("The lungs are the source of this problem: the carbon dioxide of %s is %s because of a change in "
                       "ventilation. A respiratory disorder is compensated by the kidneys, through bicarbonate. "
                       "Tell: the system that compensates is the one that is not the cause."
                       % (p, "high" if pr == RACID else "low"))
    else:
        E[wrongdir] = ("%s would push the pH further the wrong way. In %s the lungs offset the change by moving carbon "
                       "dioxide the same way as bicarbonate; here carbon dioxide is %s, %s. Tell: compensation "
                       "pulls the pH back toward normal." % (wrongdir, pr.lower(), p, x.pdesc()))
        E[wrongsys] = ("The bicarbonate is where this problem lies: it is %s, %s. A metabolic disorder is compensated by "
                       "the lungs, through carbon dioxide, within minutes to hours. Tell: the system that compensates "
                       "is the one that is not the cause." % (h, x.hdesc()))
    opts = [(t, E[t]) for t in (NONE, good, wrongdir, wrongsys)]
    if x.resp:
        walk = ["Primary disorder: %s." % pr.lower(),
                "A respiratory disorder is compensated by the kidneys, which move bicarbonate the same way as carbon "
                "dioxide (up in acidosis, down in alkalosis), over days.",
                "Bicarbonate here: %s against %s, %s." % (h, vrange, vst),
                "So: %s." % key.lower()]
        slides = [27, 28, 30, 50, 51]
    else:
        walk = ["Primary disorder: %s." % pr.lower(),
                "A metabolic disorder is compensated by the lungs, which move carbon dioxide the same way as "
                "bicarbonate (down in acidosis, up in alkalosis), within minutes to hours.",
                "Carbon dioxide here: %s against %s, %s." % (p, vrange, vst),
                "So: %s." % key.lower()]
        slides = [31, 33, 52, 53]
    return opts, key, walk, slides


# CMS acute vs chronic respiratory (slide 59 ratios, given in the prompt; slide 22 timing).
def resp_preds(x):
    p = x.p
    if x.primary == RACID:
        d = p - 40
        return d, 24 + 1.0 * d / 10, 24 + 3.5 * d / 10
    d = 40 - p
    return d, 24 - 2.0 * d / 10, 24 - 5.0 * d / 10


def chronicity_of(x):
    d, a, c = resp_preds(x)
    h = x.h
    ok_a = abs(h - a) <= 1.5 and abs(h - c) >= 2.5
    ok_c = abs(h - c) <= 2.0 and abs(h - a) >= 2.5
    assert ok_a != ok_c, "%s: bicarbonate %s fits acute %s and chronic %s ambiguously" % (x.c["id"], h, a, c)
    assert abs(a - c) >= 3.5, "%s: acute and chronic predictions too close (%s vs %s)" % (x.c["id"], a, c)
    return "acute" if ok_a else "chronic"


def chron_prompt(x):
    if x.primary == RACID:
        return ("Is this acute or chronic? Bicarbonate rises about 1 mEq/L per 10 mm Hg rise in carbon dioxide when "
                "acute and about 3.5 when chronic, counting from midpoints of 40 mm Hg and 24 mEq/L.")
    return ("Is this acute or chronic? Bicarbonate falls about 2 mEq/L per 10 mm Hg fall in carbon dioxide when acute "
            "and about 5 when chronic, counting from midpoints of 40 mm Hg and 24 mEq/L.")


def step_chronicity(x):
    d, a, c = resp_preds(x)
    ch = chronicity_of(x)
    h, p = f(x.h), f(x.p)
    acid = x.primary == RACID
    name = "acidosis" if acid else "alkalosis"
    ACU, CHR = "Acute respiratory " + name, "Chronic respiratory " + name
    MIXA = "With an added metabolic alkalosis" if acid else "With an added metabolic acidosis"
    MIXB = "With an added metabolic acidosis" if acid else "With an added metabolic alkalosis"
    ar, cr = (1, 3.5) if acid else (2, 5)
    mv = "rose" if acid else "fell"
    ainc, cinc = ar * d / 10, cr * d / 10
    sign = "+" if acid else "-"
    A_ = "24 %s %s = %s" % (sign, f(ainc), f(a))
    C_ = "24 %s %s = %s" % (sign, f(cinc), f(c))
    E = {}
    if ch == "acute":
        key = ACU
        why = ("the kidneys have not yet raised it much; renal compensation begins 6 to 12 hours after onset and "
               "takes days to complete" if acid
               else "only the small acute fall has occurred, not the larger chronic one")
        E[ACU] = ("Correct. Carbon dioxide %s %s mm Hg (40 to %s). Acutely, bicarbonate moves about %s per 10, to "
                  "about %s; chronically about %s per 10, to about %s. The measured %s matches the acute value: %s."
                  % (mv, f(d), p, f(ar), A_, f(cr), C_, h, why))
        tell = ("complete renal compensation takes days" if acid
                else "the chronic rule predicts a much lower bicarbonate")
        E[CHR] = ("Chronic compensation would move bicarbonate about %s per 10 mm Hg, to about %s. The measured %s sits "
                  "near the acute %s instead. Tell: %s." % (f(cr), f(c), h, f(a), tell))
    else:
        key = CHR
        why = ("the kidneys have adjusted bicarbonate over days" if acid
               else "the kidneys have lowered bicarbonate, the chronic finding")
        E[CHR] = ("Correct. Carbon dioxide %s %s mm Hg (40 to %s). Chronic compensation predicts about %s per 10, so "
                  "%s; the acute rule gives only %s. The measured %s matches the chronic value: %s."
                  % (mv, f(d), p, f(cr), C_, A_, h, why))
        tell = ("a change this large takes days of renal work" if acid
                else "a bicarbonate this low is the chronic finding")
        E[ACU] = ("Acute compensation moves bicarbonate only about %s per 10 mm Hg, to about %s. The measured %s is "
                  "well past that and matches the chronic %s. Tell: %s." % (f(ar), f(a), h, f(c), tell))
    keyval = f(a) if ch == "acute" else f(c)
    up, down = ("push bicarbonate above", "hold bicarbonate below") if acid else ("keep bicarbonate above",
                                                                                  "pull bicarbonate below")
    E[MIXA] = ("%s would %s the %s prediction of about %s. The measured %s fits that prediction, so compensation "
               "explains it without a second disorder. Tell: call a mixed disorder only when compensation cannot "
               "account for the value." % (MIXA.replace("With an added", "An added"), up if acid else down, ch,
                                           keyval, h))
    E[MIXB] = ("%s would %s the %s prediction of about %s. The measured %s matches it. Tell: a value that fits the "
               "expected compensation is a simple disorder." % (MIXB.replace("With an added", "An added"),
                                                               down if acid else up, ch, keyval, h))
    opts = [(t, E[t]) for t in (ACU, CHR, MIXA, MIXB)]
    walk = ["Change in carbon dioxide from 40: %s %s mm Hg." % (p, "- 40 = " + f(d) if acid else "is " + f(d) + " below 40"),
            "Acute prediction: bicarbonate %s %s x %s/10 = %s." % ("24 +" if acid else "24 -", f(ar), f(d), f(a)),
            "Chronic prediction: bicarbonate %s %s x %s/10 = %s." % ("24 +" if acid else "24 -", f(cr), f(d), f(c)),
            "Measured bicarbonate: %s, which matches the %s prediction." % (h, ch),
            "So: %s." % key.lower()]
    slides = [22, 59, 60] if acid else [30, 32, 59, 60]
    return opts, key, walk, slides


# CMS Winter formula (slide 58).
def winter(x):
    k = 1.5 * x.h + 8
    return k, k - 2, k + 2


def step_winter_calc(x, pattern):
    h = x.h
    K, lo, hi = winter(x)
    R = lambda c: "%s to %s mm Hg" % (f(c - 2), f(c + 2))
    key = "%s to %s mm Hg" % (f(lo), f(hi))
    keyexp = ("Correct. Winter formula: expected carbon dioxide = 1.5 x %s + 8 = %s + 8 = %s, plus or minus 2, so %s "
              "to %s mm Hg. Only the measured bicarbonate goes into it." % (f(h), f(1.5 * h), f(K), f(lo), f(hi)))
    cand = {
        "normal": (36, "36 to 44 mm Hg",
                   "36 to 44 mm Hg is the normal range, the carbon dioxide you would expect with no acidosis at all. "
                   "With a bicarbonate of %s the lungs should pull carbon dioxide below normal: 1.5 x %s + 8 = %s, so %s "
                   "to %s. Tell: in metabolic acidosis the expected carbon dioxide is low, not normal."
                   % (f(h), f(h), f(K), f(lo), f(hi))),
        "nomult": (h + 8, R(h + 8),
                   "%s adds 8 to the bicarbonate without multiplying it by 1.5 (%s + 8 = %s). The formula is 1.5 x %s + "
                   "8 = %s, so %s to %s. Tell: multiply by 1.5 first, then add 8."
                   % (R(h + 8), f(h), f(h + 8), f(h), f(K), f(lo), f(hi))),
        "noplus": (1.5 * h, R(1.5 * h),
                   "%s multiplies by 1.5 but leaves out the 8 (1.5 x %s = %s). Adding it gives %s, so the expected range "
                   "is %s to %s. Tell: the formula has two parts, times 1.5 and plus 8."
                   % (R(1.5 * h), f(h), f(1.5 * h), f(K), f(lo), f(hi))),
        "minus": (1.5 * h - 8, R(1.5 * h - 8),
                  "%s subtracts the 8 instead of adding it (1.5 x %s - 8 = %s). The formula adds: 1.5 x %s + 8 = %s, so "
                  "%s to %s. Tell: the constant in the Winter formula is plus 8."
                  % (R(1.5 * h - 8), f(h), f(1.5 * h - 8), f(h), f(K), f(lo), f(hi))),
        "double": (2 * h + 8, R(2 * h + 8),
                   "%s multiplies the bicarbonate by 2 instead of 1.5 (2 x %s + 8 = %s). The multiplier is 1.5: 1.5 x %s "
                   "+ 8 = %s, so %s to %s. Tell: one and a half times the bicarbonate, plus 8."
                   % (R(2 * h + 8), f(h), f(2 * h + 8), f(h), f(K), f(lo), f(hi))),
    }
    names = {"A": ["minus", "nomult", "normal"], "B": ["nomult", "double", "normal"],
             "C": ["minus", "noplus", "normal"]}[pattern]
    rows = [(K, key, keyexp)] + [cand[n] for n in names]

    def span(row):
        c = row[0]
        return (36, 44) if row[1].startswith("36 to 44") else (c - 2, c + 2)
    rows.sort(key=lambda r: span(r)[0])
    for a, b in zip(rows, rows[1:]):
        assert span(a)[1] < span(b)[0], "%s: Winter options overlap: %s / %s" % (x.c["id"], a[1], b[1])
    opts = [(r[1], r[2]) for r in rows]
    walk = ["Winter formula: expected carbon dioxide = 1.5 x bicarbonate + 8, plus or minus 2.",
            "Bicarbonate = %s, so 1.5 x %s = %s." % (f(h), f(h), f(1.5 * h)),
            "%s + 8 = %s." % (f(1.5 * h), f(K)),
            "Range: %s - 2 = %s to %s + 2 = %s mm Hg." % (f(K), f(lo), f(K), f(hi))]
    return opts, key, walk, [58]


APPROP, ADDRA = "Appropriate respiratory compensation", "Added respiratory acidosis"
RENALC, PRALK = "Renal compensation for the acidosis", "Primary respiratory alkalosis"


def winter_read_of(x):
    K, lo, hi = winter(x)
    assert x.p >= lo, ("%s: carbon dioxide %s is below the Winter range %s-%s; the mirror rule is not on the slides, "
                       "so no case may need it" % (x.c["id"], x.p, lo, hi))
    return APPROP if x.p <= hi else ADDRA


def step_winter_read(x):
    K, lo, hi = winter(x)
    p, ph = f(x.p), fph(x.ph)
    r = "%s to %s" % (f(lo), f(hi))
    key = winter_read_of(x)
    in_normal = 36 <= x.p <= 44
    E = {}
    if key == APPROP:
        E[APPROP] = ("Correct. The measured carbon dioxide of %s sits inside the expected %s mm Hg, so the lungs are "
                     "compensating as predicted: a simple metabolic acidosis with appropriate respiratory "
                     "compensation." % (p, r))
        E[ADDRA] = ("Added respiratory acidosis shows as a carbon dioxide above the Winter range. Here %s sits inside "
                    "the expected %s, so the lungs are doing what is expected. Tell: inside the range means "
                    "appropriate compensation." % (p, r))
        E[PRALK] = ("A primary respiratory alkalosis would raise the pH, and this pH is %s, acidemic. The low carbon "
                    "dioxide of %s is the lungs compensating, inside the expected %s. Tell: a low carbon dioxide with a "
                    "low pH is compensation, not alkalosis." % (ph, p, r))
    else:
        E[ADDRA] = ("Correct. The measured carbon dioxide of %s is above the expected %s mm Hg. When carbon dioxide is "
                    "higher than the Winter formula predicts, metabolic acidosis is present together with respiratory "
                    "acidosis, and it can be a sign of impending respiratory failure.%s"
                    % (p, r, " A carbon dioxide inside the normal 36 to 44 is still too high in this acidosis."
                       if in_normal else ""))
        E[APPROP] = ("Appropriate compensation would put carbon dioxide inside %s mm Hg. The measured %s is above that "
                     "range%s. Tell: compare with the Winter range, not with the normal range."
                     % (r, p, ", even though it sits in the normal 36 to 44" if in_normal else ""))
        E[PRALK] = ("A primary respiratory alkalosis would raise the pH, and this pH is %s, acidemic. The carbon dioxide "
                    "of %s is %shigher than the expected %s, so the lungs are not overshooting into an alkalosis. Tell: "
                    "an acidemic pH points away from a primary alkalosis."
                    % (ph, p, "below normal but " if x.p < 36 else "", r))
    E[RENALC] = ("A metabolic acidosis is compensated by the lungs, through carbon dioxide; the kidneys compensate "
                 "respiratory disorders. The carbon dioxide of %s is the respiratory response, and it sits %s the "
                 "expected %s. Tell: metabolic problems get a respiratory response."
                 % (p, "inside" if key == APPROP else "above", r))
    opts = [(t, E[t]) for t in (APPROP, ADDRA, RENALC, PRALK)]
    walk = ["Expected carbon dioxide by the Winter formula: %s mm Hg." % r,
            "Measured carbon dioxide: %s." % p,
            "%s is %s the range." % (p, "inside" if key == APPROP else "above"),
            "So: %s." % key.lower()]
    slides = [20, 58]
    return opts, key, walk, slides


# CMS metabolic alkalosis: slide 38 (rarely above 55) with the slide 59 ratio given in the prompt.
EXPC, CONRA = "Expected respiratory compensation", "Concurrent respiratory acidosis"
RENALK, CONRALK = "Compensation back to a normal pH", "Concurrent respiratory alkalosis"
ALK_PROMPT = ("What does the carbon dioxide show? In metabolic alkalosis carbon dioxide rises about 0.75 mm Hg per "
              "1 mEq/L rise in bicarbonate, counting from midpoints of 40 mm Hg and 24 mEq/L.")


def alk_pred(x):
    dh = x.h - 24
    return dh, 0.75 * dh, 40 + 0.75 * dh


def alk_comp_of(x):
    dh, inc, pred = alk_pred(x)
    if x.p > 55:
        return CONRA
    assert 44 < x.p <= 55 and abs(x.p - pred) <= 3, (
        "%s: carbon dioxide %s is neither the expected %s nor above 55; not keyable from the slides"
        % (x.c["id"], x.p, pred))
    return EXPC


def step_alk_comp(x, tail=""):
    dh, inc, pred = alk_pred(x)
    p, h = f(x.p), f(x.h)
    key = alk_comp_of(x)
    E = {}
    if key == EXPC:
        E[EXPC] = ("Correct. Bicarbonate rose %s (24 to %s), and %s x 0.75 = %s, so carbon dioxide should be about 40 + "
                   "%s = %s. The measured %s fits that and stays under 55, the level compensation rarely exceeds. "
                   "The lungs retain carbon dioxide by decreasing ventilation, the expected compensation." % (f(dh), h, f(dh), f(inc), f(inc), f(pred), p))
        E[CONRA] = ("A concurrent respiratory acidosis is considered when carbon dioxide climbs above 55 mm Hg. The "
                    "measured %s is below that and matches the predicted %s. Tell: a modest rise is the lungs "
                    "compensating." % (p, f(pred)))
    else:
        E[CONRA] = ("Correct. Compensation for metabolic alkalosis rarely takes carbon dioxide above 55 mm Hg, and the "
                    "measured %s is above it; the 0.75 rule predicts only about %s (40 + %s x 0.75). A carbon dioxide "
                    "this high calls for considering a concurrent primary respiratory acidosis%s." % (p, f(pred), f(dh), tail))
        E[EXPC] = ("Compensation alone predicts about %s and rarely goes above 55 mm Hg; the measured %s is above both. "
                   "Tell: past 55, look for a second, respiratory, disorder." % (f(pred), p))
    E[RENALK] = ("Compensation never returns the pH to normal; only correcting the underlying disorder does. The pH "
                 "here is %s, still above 7.45. Tell: compensation does not return the pH to normal." % fph(x.ph))
    E[CONRALK] = ("A concurrent respiratory alkalosis would leave the carbon dioxide below the value expected from the "
                  "bicarbonate, about %s. The measured %s %s. Tell: with a metabolic alkalosis, the lungs compensate by "
                  "retaining carbon dioxide, so it goes up."
                  % (f(pred), p, "matches that prediction, so the lungs are compensating, not adding a separate "
                     "problem" if key == EXPC else "is above that prediction, not below it"))
    opts = [(t, E[t]) for t in (EXPC, CONRA, RENALK, CONRALK)]
    walk = ["Bicarbonate rise: %s - 24 = %s." % (h, f(dh)),
            "Expected carbon dioxide rise: %s x 0.75 = %s." % (f(dh), f(inc)),
            "Expected carbon dioxide: 40 + %s = %s mm Hg; compensation rarely goes above 55." % (f(inc), f(pred)),
            "Measured carbon dioxide: %s, which %s." % (p, "fits the expected value" if key == EXPC
                                                        else "is above 55"),
            "So: %s." % key.lower()]
    return opts, key, walk, [19, 20, 38, 59]


# Anion gap arithmetic (PDM slide 46, CMS slide 47).
def step_ag_calc(x, pattern):
    L = x.L
    na, cl, h, k, p = L["na"], L["cl"], x.h, L["k"], x.p
    assert abs(k - round(k)) < 1e-9, "%s: potassium must be a whole number in gap cases (option arithmetic)" % x.c["id"]
    ag = x.ag
    agl = x.cfg["ag"]
    cat = "elevated" if ag > agl[1] else "normal" if ag >= agl[0] else "decreased"
    lowalb = "alb" in L and L["alb"] < x.cfg["alb"][0]
    if lowalb:
        catx = "inside that range before any albumin correction" if cat == "normal" else "%s before any albumin correction" % cat
    else:
        catx = cat
    keyexp = ("Correct. Anion gap = sodium - (chloride + bicarbonate) = %s - (%s + %s) = %s - %s = %s. The normal gap is "
              "9 to 15, so this gap is %s." % (f(na), f(cl), f(h), f(na), f(cl + h), f(ag), catx))
    cand = {
        "nobicarb": (na - cl, "%s is sodium minus chloride only (%s - %s); the bicarbonate was left out. Both measured "
                     "anions come off the sodium: %s - (%s + %s) = %s. Tell: add chloride and bicarbonate first, then "
                     "subtract." % (f(na - cl), f(na), f(cl), f(na), f(cl), f(h), f(ag))),
        "plusbicarb": (na - cl + h, "%s adds the bicarbonate instead of subtracting it (%s - %s + %s). The gap takes "
                       "away chloride and bicarbonate together: %s - %s = %s. Tell: the parentheses hold chloride plus "
                       "bicarbonate." % (f(na - cl + h), f(na), f(cl), f(h), f(na), f(cl + h), f(ag))),
        "pluspot": (ag + k, "%s adds the potassium of %s to the sodium. The formula used here has no potassium: %s - (%s "
                    "+ %s) = %s. Tell: sodium, chloride and bicarbonate are the only three values."
                    % (f(ag + k), f(k), f(na), f(cl), f(h), f(ag))),
        "minuspot": (ag - k, "%s also subtracts the potassium of %s. Potassium is not part of this formula: %s - (%s + "
                     "%s) = %s. Tell: only chloride and bicarbonate are subtracted from the sodium."
                     % (f(ag - k), f(k), f(na), f(cl), f(h), f(ag))),
        "co2": (na - (cl + p), "%s uses the arterial carbon dioxide of %s mm Hg in place of the bicarbonate. The gap "
                "needs the bicarbonate, %s mEq/L: %s - (%s + %s) = %s. Tell: carbon dioxide pressure is a gas value, "
                "not one of the measured anions." % (f(na - (cl + p)), f(p), f(h), f(na), f(cl), f(h), f(ag))),
    }
    names = {"1": ["nobicarb", "plusbicarb", "pluspot"], "2": ["minuspot", "nobicarb", "pluspot"],
             "2c": ["co2", "nobicarb", "pluspot"], "3": ["co2", "minuspot", "nobicarb"]}[pattern]
    rows = [(ag, keyexp)] + [cand[n] for n in names]
    rows.sort(key=lambda r: r[0])
    vals = [r[0] for r in rows]
    assert len(set(vals)) == 4 and min(vals) > 0, "%s: gap options not distinct and positive: %s" % (x.c["id"], vals)
    opts = [(f(r[0]), r[1]) for r in rows]
    walk = ["Anion gap = sodium - (chloride + bicarbonate).",
            "Chloride + bicarbonate = %s + %s = %s." % (f(cl), f(h), f(cl + h)),
            "Sodium - %s = %s - %s = %s." % (f(cl + h), f(na), f(cl + h), f(ag)),
            ("Normal gap: 9 to 15; %s is %s." % (f(ag), catx.replace("that range", "it"))) if lowalb else
            "Normal gap: 9 to 15, so %s is %s." % (f(ag), cat)]
    return opts, f(ag), walk, ([45, 46] if x.course == "pdm" else [46, 47])


EGN, NGH = "Elevated anion gap, normochloremic", "Normal anion gap, hyperchloremic"
EGH, NGN = "Elevated anion gap, hyperchloremic", "Normal anion gap, normochloremic"


def ag_type_of(x):
    clst = status(x.L["cl"], x.cfg["cl"])
    if x.ag > 15:
        assert clst == "normal", "%s: elevated gap must come with a normal chloride (slide 52)" % x.c["id"]
        return EGN
    assert 9 <= x.ag <= 15 and clst == "high", "%s: normal gap must come with a high chloride (slide 52)" % x.c["id"]
    return NGH


def step_ag_type(x):
    ag, cl = f(x.ag), f(x.L["cl"])
    key = ag_type_of(x)
    E = {}
    if key == EGN:
        E[EGN] = ("Correct. The gap of %s is above 15, so the gap is elevated, and the chloride of %s is inside 98 to 106: "
                  "normochloremic, the pattern that goes with an elevated gap. The usual reason for an elevated gap is "
                  "added unmeasured anions." % (ag, cl))
        E[EGH] = ("The gap of %s is elevated, but the chloride of %s is normal, not high. An elevated anion gap acidosis "
                  "is normochloremic; a high chloride goes with a normal gap. Tell: read the gap and the chloride "
                  "separately." % (ag, cl))
        E[NGH] = ("A normal gap is 9 to 15, and this gap is %s. The chloride of %s is also normal, not high. Tell: a gap "
                  "above 15 is elevated." % (ag, cl))
        E[NGN] = ("The chloride of %s is normal, but the gap of %s is above 15, so it is not a normal gap. Tell: the gap "
                  "itself decides elevated versus normal." % (cl, ag))
    else:
        E[NGH] = ("Correct. The gap of %s is inside 9 to 15, so the gap is normal, and the chloride of %s is above 106: "
                  "hyperchloremic. A normal anion gap metabolic acidosis is the hyperchloremic type." % (ag, cl))
        E[EGN] = ("An elevated gap is above 15; this gap is %s, inside 9 to 15. The chloride of %s is high, not normal. "
                  "Tell: a high chloride with a normal gap is the hyperchloremic pattern." % (ag, cl))
        E[EGH] = ("The chloride of %s is high, but the gap of %s is inside 9 to 15, so it is not elevated. Tell: work out "
                  "the gap before naming the type." % (cl, ag))
        E[NGN] = ("The gap of %s is normal, but the chloride of %s is above 106, so this is hyperchloremic, not "
                  "normochloremic. Tell: a normal gap acidosis carries a high chloride." % (ag, cl))
    opts = [(t, E[t]) for t in (EGN, NGH, EGH, NGN)]
    walk = ["Anion gap %s against 9 to 15: %s." % (ag, "elevated" if key == EGN else "normal"),
            "Chloride %s against 98 to 106: %s." % (cl, "normal (normochloremic)" if key == EGN
                                                    else "high (hyperchloremic)"),
            "An elevated gap goes with a normal chloride; a normal gap goes with a high chloride.",
            "So: %s." % key.lower()]
    return opts, key, walk, [45, 47, 52]


# PDM reading of the gap, with the albumin rule (slides 45-48).
AGE, AGNm, AGD, AGALB = "Elevated anion gap", "Normal anion gap", "Decreased anion gap", "Correct for albumin first"


def ag_read_of(x):
    alb = x.L["alb"]
    if alb < x.cfg["alb"][0]:
        return AGALB
    assert alb >= 4.5, "%s: a 'normal' albumin must be at least 4.5 g/dL (slide 48's correction anchor)" % x.c["id"]
    if x.ag > 15:
        return AGE
    if x.ag >= 9:
        return AGNm
    return AGD


ALB_KEY = "Correct it for the low albumin first"
ALB_NORM, ALB_K, ALB_DEC = "Read it as normal as it stands", "Add the potassium before reading it", \
    "Read it as a decreased gap"


def ag_calc_prompt(x):
    if "alb" in x.L and x.L["alb"] < x.cfg["alb"][0]:
        return "Calculate the anion gap from the measured sodium, chloride and bicarbonate."
    return "Calculate the anion gap."


def ag_read_prompt(x):
    if ag_read_of(x) == AGALB:
        return "The calculated gap is %s and the albumin is %s g/dL. How should this gap be handled?" % (
            f(x.ag), "%.1f" % x.L["alb"])
    return "How should this anion gap be read?"


def step_ag_read(x):
    ag, alb = f(x.ag), "%.1f" % x.L["alb"]
    key = ag_read_of(x)
    cat = "elevated" if x.ag > 15 else "normal" if x.ag >= 9 else "decreased"
    if key == AGALB:
        assert 9 <= x.ag <= 15, "%s: the low-albumin case needs a gap that looks normal uncorrected" % x.c["id"]
        E = {
            ALB_KEY: ("Correct. The anion gap must be corrected when albumin is abnormal, and %s g/dL is well below "
                      "normal. Albumin is most of the normal gap, so a low albumin pulls the gap down and can hide a "
                      "real rise; the correction adds to the gap for each 1 g/dL of albumin below 4.5." % alb),
            ALB_NORM: ("%s sits inside 9 to 15, but with an albumin of %s g/dL that number understates the gap. A low "
                       "albumin must be corrected for first, and the correction can only raise the gap. Tell: check "
                       "the albumin before calling a gap normal." % (ag, alb)),
            ALB_K: ("The gap formula has no potassium: sodium - (chloride + bicarbonate). What changes the reading here "
                    "is the albumin of %s g/dL, which must be corrected for. Tell: albumin, not potassium, adjusts "
                    "the gap." % alb),
            ALB_DEC: ("A decreased gap is one below 9, and this gap is %s. A low albumin pulls the gap down, so the fix "
                      "is to correct it upward for the albumin, not to call it decreased. Tell: a gap inside 9 to 15 "
                      "is not decreased." % ag),
        }
        opts = [(t, E[t]) for t in (ALB_NORM, ALB_K, ALB_DEC, ALB_KEY)]
        walk = ["Check the albumin first: %s g/dL against 3.5 to 5.0 is low." % alb,
                "An abnormal albumin means the gap must be corrected before it is read; albumin is most of the normal "
                "gap.",
                "So the calculated gap of %s is not read as it stands: %s." % (ag, ALB_KEY.lower())]
        return opts, ALB_KEY, walk, [45, 46, 48]
    E = {}
    if key == AGE:
        E[AGE] = ("Correct. The gap of %s is above the normal 9 to 15, so it is elevated. An elevated gap usually means "
                  "added unmeasured anions, such as ketoacids or lactate. The albumin of %s g/dL is normal, so the gap "
                  "needs no correction." % (ag, alb))
        E[AGNm] = ("A normal gap is 9 to 15, and this gap is %s, above it, with a normal albumin of %s g/dL that "
                   "needs no correction. Tell: a gap above 15 is elevated." % (ag, alb))
    else:
        E[AGNm] = ("Correct. The gap of %s lies inside the normal 9 to 15, and the albumin of %s g/dL is normal, so the "
                   "gap can be read as it stands: it is not elevated." % (ag, alb))
        E[AGE] = ("An elevated gap is above 15, usually from added unmeasured anions such as ketoacids or lactate. This "
                  "gap is %s, inside 9 to 15. Tell: compare the calculated gap with 9 to 15." % ag)
    E[AGALB] = ("The gap needs correcting only when albumin is abnormal, and this albumin is %s g/dL, normal. So the "
                "gap of %s is read as it stands: %s. Tell: correct the gap only for an abnormal albumin."
                % (alb, ag, cat))
    E[AGD] = ("A decreased gap is below 9, usually from added unmeasured cations such as lithium. This gap is %s. Tell: "
              "only a gap below 9 is decreased." % ag)
    opts = [(t, E[t]) for t in (AGE, AGNm, AGD, AGALB)]
    walk = ["Check the albumin first: %s g/dL against 3.5 to 5.0 is normal." % alb,
            "Gap %s against 9 to 15: %s." % (ag, cat), "So: %s." % key.lower()]
    return opts, key, walk, [45, 46, 47, 48]


# Potassium shift (PDM slide 44, CMS slide 9).
KAO, KAI = "Acidosis moving potassium out of cells", "Acidosis moving potassium into cells"
KLI, KLO = "Alkalosis moving potassium into cells", "Alkalosis moving potassium out of cells"


def k_of(x):
    kst = status(x.L["k"], x.cfg["k"])
    if x.dir == ACID:
        assert kst == "high", "%s: potassium step needs a high potassium with acidemia" % x.c["id"]
        return KAO
    assert kst == "low", "%s: potassium step needs a low potassium with alkalemia" % x.c["id"]
    return KLI


def step_potassium(x):
    k, ph = f(x.L["k"], 1), fph(x.ph)
    lo, hi = x.cfg["k"]
    key = k_of(x)
    pdm = x.course == "pdm"
    E = {}
    if key == KAO:
        E[KAO] = ("Correct. The pH of %s is acidic and the potassium of %s is above %s. In acidosis %s, producing "
                  "hyperkalemia." % (ph, k, f(hi, 1), "potassium shifts into the extracellular space" if pdm else
                                     "hydrogen ions move into cells and potassium moves out into the blood"))
        E[KAI] = ("Potassium moving into cells would lower the blood level, and this potassium is %s, high. In acidosis "
                  "potassium moves out of cells. Tell: acidosis pushes potassium up, alkalosis pulls it down." % k)
        E[KLI] = ("This is an acidic pH of %s, not an alkalosis. Alkalosis moves potassium into cells and lowers it; "
                  "here potassium is %s, high. Tell: match the shift to the pH first." % (ph, k))
        E[KLO] = ("Alkalosis moves potassium into cells, not out, and this pH of %s is acidic anyway. The high "
                  "potassium of %s comes from the acidosis. Tell: acid sends potassium out of cells." % (ph, k))
    else:
        E[KLI] = ("Correct. The pH of %s is alkaline and the potassium of %s is below %s. In alkalosis %s, producing "
                  "hypokalemia." % (ph, k, f(lo, 1), "potassium shifts into the intracellular space" if pdm else
                                    "hydrogen ions move out of cells and potassium moves in"))
        E[KLO] = ("Potassium moving out of cells would raise the blood level, and this potassium is %s, low. In "
                  "alkalosis potassium moves into cells. Tell: alkalosis pulls potassium down." % k)
        E[KAO] = ("This pH of %s is alkaline, not acidic, and the potassium of %s is low, not high. Acidosis moves "
                  "potassium out of cells and raises it. Tell: match the shift to the pH first." % (ph, k))
        E[KAI] = ("The pH of %s is alkaline, so no acidosis is moving potassium anywhere; acidosis would move it out of "
                  "cells in any case. Here alkalosis has moved it in. Tell: alkalosis means potassium into cells." % ph)
    opts = [(t, E[t]) for t in (KAO, KAI, KLI, KLO)]
    walk = ["pH %s: %s." % (ph, x.phword()),
            "Potassium %s against %s to %s: %s." % (k, f(lo, 1), f(hi, 1), "high" if key == KAO else "low"),
            "Acidosis shifts potassium out of cells (hyperkalemia); alkalosis shifts it into cells (hypokalemia).",
            "So: %s." % key.lower()]
    return opts, key, walk, ([44] if pdm else [9, 30, 52] if key == KAO else [9, 30, 40])


# Oxygen-hemoglobin curve (PDM slide 39, CMS slides 10-11).
OR_, OL_ = "Right shift: oxygen released more easily", "Left shift: oxygen held more tightly"
ORX, OLX = "Right shift: oxygen held more tightly", "Left shift: oxygen released more easily"


def o2_of(x):
    return OR_ if x.dir == ACID else OL_


def step_o2(x):
    ph = fph(x.ph)
    key = o2_of(x)
    E = {}
    if key == OR_:
        E[OR_] = ("Correct. The pH of %s is acidic, and acidosis shifts the oxygen-hemoglobin dissociation curve to the "
                  "right: oxygen is released more easily from hemoglobin."
                  % ph)
        E[OL_] = ("A left shift, with oxygen held more tightly, is what alkalosis does. This pH of %s is acidic, which "
                  "shifts the curve right. Tell: a low pH shifts right and lets oxygen go." % ph)
        E[ORX] = ("A right shift lowers hemoglobin's hold on oxygen; it does not tighten it. Acidosis, like this pH of %s, "
                  "shifts the curve right so oxygen is released more easily. Tell: right shift means release." % ph)
        E[OLX] = ("A left shift tightens hemoglobin's hold, so oxygen is released less easily, and a left shift comes "
                  "from alkalosis, not this acidic pH of %s. Tell: acid shifts right." % ph)
    else:
        E[OL_] = ("Correct. The pH of %s is alkaline, and alkalosis shifts the curve to the left: hemoglobin binds "
                  "oxygen more tightly." % ph)
        E[OR_] = ("A right shift, with oxygen released more easily, is what acidosis does. This pH of %s is alkaline, "
                  "which shifts the curve left. Tell: a high pH shifts left and holds oxygen." % ph)
        E[OLX] = ("A left shift raises hemoglobin's hold on oxygen, so oxygen is released less easily, not more. "
                  "Alkalosis, like this pH of %s, shifts left. Tell: left shift means hold." % ph)
        E[ORX] = ("A right shift loosens hemoglobin's hold on oxygen, and it comes from acidosis, not this alkaline pH "
                  "of %s. Tell: alkalosis shifts left and holds oxygen tightly." % ph)
    opts = [(t, E[t]) for t in (OR_, OL_, ORX, OLX)]
    walk = ["pH %s: %s." % (ph, x.phword()),
            "Acidosis (low pH) shifts the curve right: oxygen is released more easily.",
            "Alkalosis (high pH) shifts the curve left: oxygen is held more tightly.",
            "So: %s." % key.lower()]
    return opts, key, walk, ([39] if x.course == "pdm" else [10, 11])


# CMS saline type (slides 37, 41).
SRC_, SUE = "Saline responsive, volume contracted", "Saline unresponsive, euvolemic or hypervolemic"
SRE, SUC = "Saline responsive, euvolemic or hypervolemic", "Saline unresponsive, volume contracted"


def saline_of(x):
    ucl, vol = x.c["urine_cl"], x.c["volume"]
    if ucl == "low":
        assert vol == "contracted", x.c["id"]
        return SRC_
    assert ucl == "high" and vol in ("euvolemic", "hypervolemic"), x.c["id"]
    return SUE


def step_saline(x):
    # volume_clue is a plain statement from the vignette ("he is volume depleted", "he is not dehydrated ..."):
    # the type is decided on the urine chloride (slide 41); slide 37 ties each type to its volume status
    key = saline_of(x)
    clue = x.c["volume_clue"]
    E = {}
    if key == SRC_:
        E[SRC_] = ("Correct. The urine chloride is low, which marks the saline-responsive type, and %s: saline-responsive "
                   "alkalosis is a sign of extracellular volume contraction. Saline-responsive is the more common type."
                   % clue)
        E[SUE] = ("The saline-unresponsive type has a high urine chloride, with an elevated bicarbonate and a normal or "
                  "high volume. Here the urine chloride is low and %s. Tell: a low urine chloride means saline "
                  "responsive." % clue)
        E[SRE] = ("Saline-responsive alkalosis is itself a sign of extracellular volume contraction, so it does not come "
                  "with euvolemia or hypervolemia, and here %s. Tell: responsive goes with a contracted volume." % clue)
        E[SUC] = ("A contracted volume is the saline-responsive picture, and the low urine chloride agrees. The "
                  "unresponsive type has a high urine chloride with a normal or high volume. Tell: low urine chloride "
                  "and a contracted volume travel together.")
    else:
        E[SUE] = ("Correct. The urine chloride is high, which marks the saline-unresponsive type, and %s: an elevated "
                  "bicarbonate with euvolemia or hypervolemia, not volume contraction." % clue)
        E[SRC_] = ("The saline-responsive type has a low urine chloride and a contracted volume. Here the urine chloride "
                   "is high and %s. Tell: a high urine chloride means saline unresponsive." % clue)
        E[SRE] = ("Saline-responsive alkalosis is a sign of volume contraction and carries a low urine chloride; this "
                  "urine chloride is high. Tell: a high urine chloride points to the unresponsive type.")
        E[SUC] = ("The unresponsive type comes with euvolemia or hypervolemia, not volume contraction, and %s. Tell: "
                  "volume contraction belongs to the responsive type." % clue)
    opts = [(t, E[t]) for t in (SRC_, SUE, SRE, SUC)]
    walk = ["Urine chloride separates the two types: lower (below 25 mEq/L) in saline responsive, higher (above 40 "
            "mEq/L) in saline unresponsive.",
            "Here the urine chloride is %s, so the type is saline %s." % (
                x.c["urine_cl"], "responsive" if key == SRC_ else "unresponsive"),
            "Volume, from the history: %s (%s)." % (clue, "contracted" if key == SRC_ else "not contracted"),
            "So: %s." % key.lower()]
    return opts, key, walk, [37, 41]


GEN = {
    "ph": ("pH", "What does the pH show?", step_ph),
    "primary": ("Primary disorder", "Which primary disorder explains the pH?", step_primary),
    "comp": ("Compensation", "How is the body compensating?", step_comp_pdm),
    "chronicity": ("Acute or chronic", None, step_chronicity),
    "winter_calc": ("Winter formula", "Use the Winter formula: what carbon dioxide range is expected?",
                    step_winter_calc),
    "winter_read": ("Compensation check", "Compare the measured carbon dioxide with that range. What does it show?",
                    step_winter_read),
    "alk_comp": ("Compensation check", ALK_PROMPT, step_alk_comp),
    "ag_calc": ("Anion gap", "Calculate the anion gap.", step_ag_calc),
    "ag_type": ("Type of acidosis", "What type of metabolic acidosis is this?", step_ag_type),
    "ag_read": ("Reading the gap", "How should this anion gap be read?", step_ag_read),
    "potassium": ("Potassium", "What best explains the potassium?", step_potassium),
    "o2": ("Oxygen delivery", "How does this pH change hemoglobin's hold on oxygen?", step_o2),
    "saline": ("Type of alkalosis", "Which type of metabolic alkalosis is this?", step_saline),
}
NUMERIC = {"winter_calc", "ag_calc"}


def computed_answers(x):
    """What the numbers say, for the case's declared `expect` to be checked against."""
    out = {"primary": x.primary}
    if x.course == "pdm":
        out["comp"] = step_comp_pdm(x)[1]
    elif x.resp:
        out["chronicity"] = chronicity_of(x)
    elif x.primary == MACID:
        out["winter"] = "appropriate" if winter_read_of(x) == APPROP else "added respiratory acidosis"
    else:
        out["alk_comp"] = "expected" if alk_comp_of(x) == EXPC else "concurrent respiratory acidosis"
    if x.ag is not None and x.primary == MACID:
        out["gap"] = "elevated" if x.ag > 15 else "normal" if x.ag >= 9 else "decreased"
    return out
