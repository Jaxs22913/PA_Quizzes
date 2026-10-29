#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate every Acid-Base Case Chain case against the slide rules, from the SHIPPED data (arcade-chain/*.json).

    python3 tools/check_acid_base_cases.py          # exit 1 on any failure, prints the failing tail

This is the point of the mode: the arithmetic is computable, so every keyed answer is recomputed here from the
case's own numbers and compared with the key the page will show. The rules are restated below, deliberately NOT
imported from the builder (tools/abchain_common.py), so a bug in one is caught by the other.

What a positive (a failure) looks like: "cms-03 s4 winter_read: key 'Appropriate respiratory compensation' but the
numbers give 'Added respiratory acidosis'". Every failure names the case, the step and both answers.

Recomputed per step (cut-offs from each set's own deck):
  ph          pH < 7.35 acidemia/acidosis, > 7.45 alkalemia/alkalosis (PDM s18-19; CMS s3, s5)
  primary     the value (carbon dioxide or bicarbonate) out of range in the direction that explains the pH, unique
              (PDM s27-33, s50-53; CMS s20-21, s29, s36, s45, s61, s63)
  comp        PDM: the non-primary value normal = none yet, moved the compensating way = that organ (s27-28, s50-53)
  chronicity  CMS: bicarbonate vs 24 + 1 or 3.5 per 10 (acidosis), 24 - 2 or 5 per 10 (alkalosis) (s59)
  winter_calc CMS: 1.5 x HCO3 + 8 +/- 2 (s58); options ascending, non-overlapping
  winter_read CMS: inside = appropriate, above = added respiratory acidosis; BELOW the range FAILS the case,
              because the mirror rule is not on the slides
  alk_comp    CMS: carbon dioxide above 55 = concurrent respiratory acidosis (s38); else must fit 40 + 0.75 x rise
  ag_calc     Na - (Cl + HCO3) (PDM s46, CMS s47); options ascending
  ag_type     CMS: gap > 15 with a normal chloride / 9-15 with a high chloride (s47, s52)
  ag_read     PDM: albumin below 3.5 -> correct first (s48); else elevated > 15, normal 9-15, decreased < 9
  potassium   acidosis -> out of cells, high; alkalosis -> into cells, low (PDM s44, CMS s9)
  o2          acidosis right shift / alkalosis left shift (PDM s39, CMS s10-11)
  saline      CMS: urine chloride low -> responsive (contracted); high -> unresponsive (s37, s41)
  cause/next  the keyed option's category must match the disorder the numbers give, using THIS file's own map of
              cause names to slide lists (PDM s22, s25-29, s32, s34; CMS s26-27, s33-34, s42-43, s55-56, s28/35/44)
Plus: every value shows its range and the ranges are the deck's; pH within the survivable limits; Henderson-
Hasselbalch realism within 0.02; four distinct options with exactly one key; key explanation opens "Correct.",
wrong ones carry a "Tell:"; cites name the right deck and real, non-excluded slides; no banned scope (Winter, ratios
or mnemonics in the PDM set; delta-delta, osmolar gap, the Winter mirror anywhere); no abbreviation outside the lab
labels; no reference to a lecture, slide or professor in student-facing text; key positions balanced; the arcade.js
CHAIN_SETS counts match the data.
"""
import glob, hashlib, json, math, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETS = {
    "pdm-e4": dict(course="pdm", deck="Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx", nslides=56,
                   excluded={1, 2, 55, 56}, life=(6.9, 7.8),
                   ranges=dict(ph=(7.35, 7.45), pco2=(35, 45), hco3=(22, 26), na=(135, 148), cl=(98, 106),
                               k=(3.6, 5.2), alb=(3.5, 5.0), po2=(80, None)),
                   acid="Acidosis", alk="Alkalosis"),
    "cms-e6": dict(course="cms", deck="PAJ5500 CMSI Acid Base MBF 2026sc.pptx", nslides=67,
                   excluded={1, 2, 64, 65, 66, 67}, life=(6.7, 7.6),
                   ranges=dict(ph=(7.35, 7.45), pco2=(36, 44), hco3=(22, 26), na=(135, 145), cl=(98, 106),
                               k=(3.5, 5.0), alb=(3.5, 5.0), po2=(80, 100)),
                   acid="Acidemia", alk="Alkalemia"),
}

# Cause names -> slide category, written from the decks, independent of the case files' own `cat` tags.
PDM_CAUSES = {
    "opioid overdose": "racid-acute", "anesthesia": "racid-acute", "anesthetic respiratory depression": "racid-acute",
    "barbiturate respiratory depression": "racid-acute", "head trauma": "racid-acute", "asthma": "racid-acute",
    "severe asthma attack": "racid-acute",
    "emphysema": "racid-chronic", "chronic bronchitis": "racid-chronic", "kyphoscoliosis": "racid-chronic",
    "anxiety": "ralk", "fever": "ralk", "pregnancy": "ralk", "severe pain": "ralk", "hypoxia": "ralk", "pulmonary emboli": "ralk", "hypoxia-driven hyperventilation": "ralk",
    "mechanical over-ventilation": "ralk",
    "diabetic ketoacidosis": "ma-acidgain", "lactic acidosis": "ma-acidgain", "renal failure": "ma-acidgain",
    "diarrhea": "ma-baseloss", "renal tubular acidosis": "ma-baseloss",
    "excess bicarbonate": "malk-basegain", "vomiting": "malk-acidloss", "nasogastric suction": "malk-acidloss",
}
CMS_CAUSES = {
    "methanol": "ma-elevated", "metformin": "ma-elevated", "uremia": "ma-elevated", "diabetic ketoacidosis": "ma-elevated",
    "isoniazid": "ma-elevated", "lactic acidosis": "ma-elevated", "ethylene glycol": "ma-elevated",
    "starvation": "ma-elevated", "salicylates": "ralk",       # salicylates only ever offered as a respiratory cause
    "ureteral diversion": "ma-normal", "saline infusion": "ma-normal", "diarrhea": "ma-normal",
    "carbonic anhydrase inhibitors": "ma-normal", "adrenal insufficiency": "ma-normal",
    "renal tubular acidosis": "ma-normal",
    "vomiting": "malk-resp", "diuretic therapy": "malk-resp", "nasogastric suction": "malk-resp",
    "primary aldosteronism": "malk-unresp-htn", "licorice": "malk-unresp-htn",
    "neuromuscular disorder": "racid-any", "central nervous system depression": "racid-acute",
    "thoracic trauma": "racid-acute", "chronic lung disease": "racid-chronic",
    "obesity hypoventilation syndrome": "racid-chronic",
    "psychogenic hyperventilation": "ralk", "hypoxia-driven hyperventilation": "ralk", "drug or toxin effect": "ralk",
    "pulmonary embolism": "ralk", "high altitude": "ralk", "pregnancy": "ralk", "hepatic failure": "ralk",
    "septicemia": "ralk", "mechanical hyperventilation": "ralk",
    "restore ventilation": "tx-ventilation", "careful oxygen titration": "tx-o2",
    "rapid carbon dioxide reduction": "tx-rapidco2", "isotonic saline infusion": "tx-saline",
    "treat the underlying cause": "tx-cause", "breathing into a paper bag": "tx-paperbag",
}

ABBR_OK = {"MUDPILES", "USEDCAR"}
SELF_REF = re.compile(r"(?i)\b(slides?|lectures?|lecturer|deck|professor|syllabus|finck|in class)\b")
BANNED_ALL = [r"(?i)delta[- ]delta", r"(?i)osmolar", r"(?i)added respiratory alkalosis",
              r"(?i)below (the|its) (winter|expected) range", r"(?i)lower than (the )?(winter|expected)"]
BANNED_PDM = [r"(?i)winter", r"(?i)\b0\.75\b", r"(?i)3\.5 per", r"MUDPILES", r"USEDCAR", r"(?i)urine chloride",
              r"(?i)saline", r"(?i)acidemi|alkalemi"]

fails = []
notes = []


def fail(where, msg):
    fails.append("%s: %s" % (where, msg))


def st(v, t):
    lo, hi = t
    if lo is not None and v < lo:
        return "low"
    if hi is not None and v > hi:
        return "high"
    return "normal"


def fmt(x):
    r = round(x, 2)
    return str(int(round(r))) if abs(r - round(r)) < 1e-9 else ("%.2f" % r).rstrip("0").rstrip(".")


def texts_of(case):
    yield "vignette", case["vignette"]
    yield "summary", case["summary"]
    for s in case["steps"]:
        yield s["id"] + " prompt", s["prompt"]
        for i, o in enumerate(s["options"]):
            yield "%s opt %s" % (s["id"], "ABCD"[i]), o["t"]
            yield "%s expl %s" % (s["id"], "ABCD"[i]), o["e"]
        for j, w in enumerate(s["walk"]):
            yield "%s walk %d" % (s["id"], j + 1), w


def check_case(sid, S, c):
    R = S["ranges"]
    W = c["id"]
    labs = {}
    for r in c["labs"]:
        k = r["k"]
        labs[k] = r["n"]
        lo, hi = R[k]
        want = ("greater than %s" % fmt(lo)) if hi is None else None
        if want is None:
            if k == "ph":
                want = "%.2f to %.2f" % (lo, hi)
            elif k in ("k", "alb"):
                want = "%.1f to %.1f" % (lo, hi)
            else:
                want = "%s to %s" % (fmt(lo), fmt(hi))
        if r.get("range") != want:
            fail(W, "%s range shown %r, deck says %r" % (k, r.get("range"), want))
        if r.get("v") in (None, ""):
            fail(W, "%s has no value" % k)
    for k in ("ph", "pco2", "hco3"):
        if k not in labs:
            fail(W, "missing %s" % k)
            return
    ph, p, h = labs["ph"], labs["pco2"], labs["hco3"]
    # every number in the vignette that is not an age or a duration needs a range: keep vignettes number-free
    for m in re.finditer(r"(?<!type )\b\d+(\.\d+)?\b", c["vignette"]):
        tail = c["vignette"][m.end():m.end() + 14]
        if not re.match(r"[- ](year|month|week|day|hour|minute|pack)", tail) and not re.match(r"\s*(years?|months?|weeks?|days?|hours?|minutes?)\b", tail):
            fail(W, "vignette number %r without a range (state it in the lab panel instead)" % m.group(0))
    hh = 6.1 + math.log10(h / (0.03 * p))
    if abs(hh - ph) > 0.02:
        fail(W, "pH %.2f does not fit carbon dioxide %s and bicarbonate %s (expected about %.2f)" % (ph, p, h, hh))
    lo, hi = R["ph"]
    if lo <= ph <= hi:
        fail(W, "pH %.2f is normal; every case needs acidemia or alkalemia" % ph)
        return
    if not (S["life"][0] < ph < S["life"][1]):
        fail(W, "pH %.2f outside the survivable limits %s" % (ph, S["life"]))
    acid = ph < lo
    ps, hs = st(p, R["pco2"]), st(h, R["hco3"])
    cand = []
    if acid:
        if ps == "high":
            cand.append("Respiratory acidosis")
        if hs == "low":
            cand.append("Metabolic acidosis")
    else:
        if ps == "low":
            cand.append("Respiratory alkalosis")
        if hs == "high":
            cand.append("Metabolic alkalosis")
    if len(cand) != 1:
        fail(W, "primary disorder not unique from the numbers: %s" % cand)
        return
    primary = cand[0]
    resp = primary.startswith("Respiratory")
    ag = labs["na"] - (labs["cl"] + h) if ("na" in labs and "cl" in labs) else None
    derived = dict(primary=primary)

    # acute/chronic for CMS respiratory
    chron = None
    if S["course"] == "cms" and resp:
        if primary == "Respiratory acidosis":
            d = p - 40
            a, ch = 24 + d / 10.0, 24 + 3.5 * d / 10.0
        else:
            d = 40 - p
            a, ch = 24 - 2 * d / 10.0, 24 - 5 * d / 10.0
        oka = abs(h - a) <= 1.5 and abs(h - ch) >= 2.5
        okc = abs(h - ch) <= 2.0 and abs(h - a) >= 2.5
        if oka == okc or abs(a - ch) < 3.5:
            fail(W, "bicarbonate %s does not clearly fit acute %.1f or chronic %.1f" % (h, a, ch))
        chron = "acute" if oka else "chronic"
    if S["course"] == "pdm" and primary == "Respiratory acidosis":
        chron = "acute" if hs == "normal" else "chronic"

    positions = []
    kinds_seen = []
    for s in c["steps"]:
        WS = "%s %s %s" % (W, s["id"], s["kind"])
        kinds_seen.append(s["kind"])
        opts = [o["t"] for o in s["options"]]
        if len(opts) != 4 or len(set(opts)) != 4:
            fail(WS, "needs four distinct options, has %s" % opts)
            continue
        if not isinstance(s.get("key"), int) or not 0 <= s["key"] < 4:
            fail(WS, "bad key index")
            continue
        key = opts[s["key"]]
        for i, o in enumerate(s["options"]):
            e = o["e"]
            if i == s["key"]:
                if not e.startswith("Correct."):
                    fail(WS, "key explanation does not open 'Correct.'")
            else:
                if e.startswith("Correct"):
                    fail(WS, "wrong option %s opens 'Correct'" % "ABCD"[i])
                if "Tell:" not in e:
                    fail(WS, "wrong option %s has no 'Tell:'" % "ABCD"[i])
            if len(e) < 90:
                fail(WS, "option %s explanation is thin (%d chars)" % ("ABCD"[i], len(e)))
        if not s.get("walk") or len(s["walk"]) < 2:
            fail(WS, "walk-through missing")
        m = re.match(r"^(.+?), Slides? ([\d, ]+)$", s.get("cite", ""))
        if not m or m.group(1) != S["deck"]:
            fail(WS, "cite %r does not name %s" % (s.get("cite"), S["deck"]))
        else:
            for n in [int(t) for t in m.group(2).split(",")]:
                if not 1 <= n <= S["nslides"] or n in S["excluded"]:
                    fail(WS, "cites slide %d (out of range or excluded)" % n)
        k = s["kind"]
        want = None
        if k == "ph":
            want = S["acid"] if acid else S["alk"]
        elif k == "primary":
            want = primary
        elif k == "comp":
            if S["course"] != "pdm":
                fail(WS, "direction-only compensation step belongs to the PDM set")
            other = hs if resp else ps
            if other == "normal":
                want = "No compensation yet"
            elif primary == "Respiratory acidosis" and other == "high":
                want = "Kidneys raising bicarbonate"
            elif primary == "Respiratory alkalosis" and other == "low":
                want = "Kidneys lowering bicarbonate"
            elif primary == "Metabolic acidosis" and other == "low":
                want = "Lungs lowering carbon dioxide"
            elif primary == "Metabolic alkalosis" and other == "high":
                want = "Lungs raising carbon dioxide"
            else:
                fail(WS, "compensating value moved the wrong way (a mixed disorder the deck does not teach)")
        elif k == "chronicity":
            want = ("Acute " if chron == "acute" else "Chronic ") + primary.lower()
        elif k == "winter_calc":
            kc = 1.5 * h + 8
            want = "%s to %s mm Hg" % (fmt(kc - 2), fmt(kc + 2))
            spans = []
            for t in opts:
                mm = re.match(r"^(-?[\d.]+) to (-?[\d.]+) mm Hg$", t)
                if not mm:
                    fail(WS, "option %r is not a range" % t)
                    break
                spans.append((float(mm.group(1)), float(mm.group(2))))
            if len(spans) == 4 and any(spans[i][1] >= spans[i + 1][0] for i in range(3)):
                fail(WS, "Winter options not ascending and non-overlapping: %s" % opts)
        elif k == "winter_read":
            lo_, hi_ = 1.5 * h + 6, 1.5 * h + 10
            if p < lo_:
                fail(WS, "carbon dioxide %s is BELOW the Winter range %s-%s: the mirror rule is not on the slides"
                     % (p, fmt(lo_), fmt(hi_)))
            want = "Appropriate respiratory compensation" if p <= hi_ else "Added respiratory acidosis"
            derived["winter"] = want
        elif k == "alk_comp":
            pred = 40 + 0.75 * (h - 24)
            if p > 55:
                want = "Concurrent respiratory acidosis"
            elif 44 < p and abs(p - pred) <= 3:
                want = "Expected respiratory compensation"
            else:
                fail(WS, "carbon dioxide %s is neither the expected %.1f nor above 55" % (p, pred))
        elif k == "ag_calc":
            if ag is None:
                fail(WS, "gap step without sodium and chloride")
                continue
            want = fmt(ag)
            vals = [float(t) for t in opts]
            if vals != sorted(vals):
                fail(WS, "gap options not ascending: %s" % opts)
        elif k == "ag_type":
            cls = st(labs["cl"], R["cl"])
            if ag > 15 and cls == "normal":
                want = "Elevated anion gap, normochloremic"
            elif 9 <= ag <= 15 and cls == "high":
                want = "Normal anion gap, hyperchloremic"
            else:
                fail(WS, "gap %s with chloride %s is not a pattern the slides describe" % (ag, labs["cl"]))
        elif k == "ag_read":
            alb = labs.get("alb")
            if alb is None:
                fail(WS, "gap reading step needs an albumin")
                continue
            if alb < R["alb"][0]:
                want = "Correct it for the low albumin first"
                if not 9 <= ag <= 15:
                    fail(WS, "low-albumin case needs a gap that looks normal uncorrected (got %s)" % ag)
                if any(t in ("Elevated anion gap", "Normal anion gap") for t in opts):
                    fail(WS, "low-albumin reading must not offer an elevated/normal label (both defensible)")
            else:
                want = "Elevated anion gap" if ag > 15 else "Normal anion gap" if ag >= 9 else "Decreased anion gap"
        elif k == "potassium":
            ks = st(labs["k"], R["k"])
            if acid and ks == "high":
                want = "Acidosis moving potassium out of cells"
            elif not acid and ks == "low":
                want = "Alkalosis moving potassium into cells"
            else:
                fail(WS, "potassium %s does not show the shift for this pH" % labs["k"])
        elif k == "o2":
            want = "Right shift: oxygen released more easily" if acid else "Left shift: oxygen held more tightly"
        elif k == "saline":
            u, vol = c.get("urine_cl"), c.get("volume")
            if u == "low" and vol == "contracted":
                want = "Saline responsive, volume contracted"
            elif u == "high" and vol in ("euvolemic", "hypervolemic"):
                want = "Saline unresponsive, euvolemic or hypervolemic"
            else:
                fail(WS, "urine chloride %r with volume %r is not a slide pattern" % (u, vol))
            if u and ("urine chloride is %s" % u) not in c["vignette"]:
                fail(WS, "vignette does not state the urine chloride as %r" % u)
        elif k in ("cause", "next"):
            cmap = PDM_CAUSES if S["course"] == "pdm" else CMS_CAUSES
            cats = []
            for o in s["options"]:
                mine = cmap.get(o["t"].lower())
                if mine is None:
                    fail(WS, "option %r is not in the validator's slide map" % o["t"])
                elif o.get("cat") != mine:
                    fail(WS, "option %r tagged %r, slide map says %r" % (o["t"], o.get("cat"), mine))
                cats.append(mine)
            kc = cats[s["key"]]
            if k == "next":
                if S["course"] != "cms":
                    fail(WS, "management steps belong to the CMS set only")
                if "tx-cause" in cats and cats.index("tx-cause") != s["key"]:
                    fail(WS, "'Treat the underlying cause' offered as a WRONG choice (always true on the slides)")
                if kc in ("tx-paperbag", "tx-rapidco2"):
                    fail(WS, "keyed a treatment the slides warn against")
                if primary == "Respiratory acidosis":
                    good = {"acute": "tx-ventilation", "chronic": "tx-o2"}[chron]
                elif primary == "Respiratory alkalosis":
                    good = "tx-cause"
                elif primary == "Metabolic alkalosis":
                    good = "tx-saline" if c.get("urine_cl") == "low" else "tx-cause"
                else:
                    good = "tx-cause"
                if kc != good:
                    fail(WS, "keyed treatment %r, the numbers call for %r" % (kc, good))
            else:
                ok = False
                if primary == "Respiratory acidosis":
                    ok = kc in ("racid-any", "racid-" + chron)
                elif primary == "Respiratory alkalosis":
                    ok = kc == "ralk"
                elif primary == "Metabolic acidosis":
                    g = ag
                    if S["course"] == "pdm" and labs.get("alb", 4.5) < R["alb"][0]:
                        g = ag + 2.5 * (4.5 - labs["alb"])    # slide 48's correction, used here only as a check
                    if S["course"] == "pdm":
                        ok = kc == ("ma-acidgain" if g > 15 else "ma-baseloss")
                    else:
                        ok = kc == ("ma-elevated" if g > 15 else "ma-normal")
                else:
                    if S["course"] == "pdm":
                        ok = kc in ("malk-acidloss", "malk-basegain")
                    else:
                        ok = kc == ("malk-resp" if c.get("urine_cl") == "low" else "malk-unresp-htn")
                if not ok:
                    fail(WS, "keyed cause %r (%s) does not fit %s from the numbers" % (key, kc, primary))
        else:
            fail(WS, "unknown step kind")
        if want is not None and key != want:
            fail(WS, "key %r but the numbers give %r" % (key, want))
        if k not in ("winter_calc", "ag_calc"):
            positions.append(s["key"])
            L = sorted(len(t) for t in opts)
            klen = len(key)
            if klen == L[-1] and klen - L[-2] >= 8 and klen >= 1.18 * L[-2]:
                notes.append("%s: key is the longest option by %d characters" % (WS, klen - L[-2]))
    # the chain must open with pH then primary, and metabolic acidosis cases must calculate the gap
    if kinds_seen[:2] != ["ph", "primary"]:
        fail(W, "chain must open pH -> primary, has %s" % kinds_seen[:2])
    if primary == "Metabolic acidosis" and "ag_calc" not in kinds_seen:
        fail(W, "metabolic acidosis case without the anion gap")
    if S["course"] == "cms" and primary == "Metabolic acidosis" and "winter_read" not in kinds_seen:
        fail(W, "CMS metabolic acidosis case without the Winter check")
    # text rules
    for where, t in texts_of(c):
        if SELF_REF.search(t):
            fail("%s %s" % (W, where), "refers to the course materials: %r" % SELF_REF.search(t).group(0))
        for rx in BANNED_ALL + (BANNED_PDM if S["course"] == "pdm" else []):
            if re.search(rx, t):
                fail("%s %s" % (W, where), "out-of-scope wording /%s/" % rx)
        for tok in re.findall(r"\b[A-Z]{2,}[A-Za-z0-9]*\b", t):
            if tok not in ABBR_OK:
                fail("%s %s" % (W, where), "abbreviation %r" % tok)
    return positions


def main():
    paths = sorted(glob.glob(os.path.join(ROOT, "arcade-chain", "*.json")))
    if not paths:
        print("check_acid_base_cases: no arcade-chain/*.json found")
        return 1
    reg = open(os.path.join(ROOT, "arcade.js"), encoding="utf-8").read()
    total_cases = total_steps = 0
    for path in paths:
        raw = open(path, encoding="utf-8").read()
        d = json.loads(raw)
        sid = d.get("id")
        S = SETS.get(sid)
        if not S:
            fail(os.path.basename(path), "unknown set id %r" % sid)
            continue
        if d.get("deck") != S["deck"]:
            fail(sid, "deck %r, expected %r" % (d.get("deck"), S["deck"]))
        ids = [c["id"] for c in d["cases"]]
        if len(set(ids)) != len(ids):
            fail(sid, "duplicate case ids")
        pos = []
        nsteps = 0
        for c in d["cases"]:
            pos += check_case(sid, S, c) or []
            nsteps += len(c["steps"])
        m = re.search(r'\{ id: "%s",[^}]*cases: (\d+), steps: (\d+), ver: "([0-9a-f]{10})" \}' % re.escape(sid), reg)
        if not m:
            fail(sid, "not registered in arcade.js CHAIN_SETS")
        elif m.group(3) != hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]:
            fail(sid, "arcade.js ver does not match the data file (re-run build_acid_base_chain.py)")
        elif (int(m.group(1)), int(m.group(2))) != (len(ids), nsteps):
            fail(sid, "arcade.js says %s cases / %s steps, data has %d / %d (re-run build_acid_base_chain.py)"
                 % (m.group(1), m.group(2), len(ids), nsteps))
        if pos:
            share = [pos.count(i) / float(len(pos)) for i in range(4)]
            if max(share) > 0.35:
                fail(sid, "key position skew A-D = %s" % ", ".join("%.0f%%" % (100 * x) for x in share))
            print("%-8s %2d cases, %3d steps, key positions A-D %s" % (
                sid, len(ids), nsteps, " ".join("%.0f%%" % (100 * x) for x in share)))
        total_cases += len(ids)
        total_steps += nsteps
    for n in notes:
        print("  note:", n)
    if fails:
        for f_ in fails[:60]:
            print("FAIL", f_)
        print("check_acid_base_cases: %d FAIL across %d cases / %d steps" % (len(fails), total_cases, total_steps))
        return 1
    print("check_acid_base_cases: all %d cases / %d steps verified against the slide rules (0 mismatches)"
          % (total_cases, total_steps))
    return 0


if __name__ == "__main__":
    sys.exit(main())
