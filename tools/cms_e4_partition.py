#!/usr/bin/env python3
"""Partition a CMS I Exam 4 four-option pool into two 30s.

    python3 cms_e4_partition.py l20io     # Lecture 20 Hypertension, objective
    python3 cms_e4_partition.py l21io     # Lecture 21 Hypotension, objective (Set 1)
    python3 cms_e4_partition.py l21vig    # Lecture 21 Hypotension, vignettes (Set 2)
    python3 cms_e4_partition.py l22io | l22vig   # Atherosclerosis and Lipid Disorders
    python3 cms_e4_partition.py l25io | l25vig   # Heart Failure

Trimmed from cms_e3_partition.py. The Exam 3 driver carries three pieces of
machinery this one does not need: the lead-in attacher (Exam 4 pools are
authored with the lead-in in the stem), the length-fix tables, and the
five-to-four option drop remapping. Exam 4 is four-option from the start, so
none of that has anything to remap.

The scoring terms and the rotation are unchanged, including the deliberate
exclusion of the patient-stem term from objective sets -- Set 1 is recall by
design and carries no ages, so scoring it on patient stems is a flat penalty.

TWO PATHS (2026-09-24).
  l20io / l20vig -- the Hypertension build as shipped. Its code path is left
      exactly as it was so re-running it reproduces the committed sets.
  l21 / l22 / l25 -- Carter's three lectures. These go through the GUARDED path
      below, which restores every guard the earlier CMS vignette partitions
      carried (cms_l9_vig_partition.py, cms_e2l1_vig_partition.py) and adds the
      Carter scope guards:

      schema     four options, key authored first and opening "Correct", every
                 option explained, a slide citation on every question
      slot       every question tagged with one of the 16 fact slots
      io         every Set 1 question carries one of the lecture's VERBATIM
                 syllabus objectives (scope module IOS), and each set is scored
                 on covering all of them
      scope      no question cites an excluded slide (L25 slide 57, the 2026
                 poster); no dosing; no brand names; no mechanism-of-action
                 stems; the lecture's own banned patterns (scope module)
      acronyms   no bare acronym in a stem, option or explanation -- written
                 out, or ABBREV (full term) per the site policy; Carter: "no
                 acronyms in questions"
      spelling   US spelling (2026-09-23)
      depend     NO STEM MAY REFER TO ANOTHER QUESTION (both sets)
      vignette   Set 2 only: every stem opens on a patient; named findings carry
                 their description in parentheses (scope module NAMED); every
                 question carries an explicit lead= from the vocabulary, the
                 stem ends on a question, and a diagnosis lead can only be
                 labeled diagnosis -- a stem asking "most likely diagnosis"
                 labeled anything else fails, so the cap cannot be dodged
      dx cap     at most 6 diagnosis lead-ins per 30, BY CONSTRUCTION: the
                 search never makes a swap that breaks it, and the build fails
                 if the pool cannot supply enough non-diagnosis vignettes
      skew       no lead-in type above 40% of a set (asserted)

  Selection is swap-based LOCAL SEARCH (2026-08-26, cms_e2l1), not
  best-of-N shuffles, so the gameable term can actually be driven down.
  Length fixes come from cms_e4l<N>_lengthfix.FIXES, keyed by
  (module, index within module, option index) and applied before any guard.
"""
import sys, os, json, random, re, statistics, glob, importlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

WHICH = sys.argv[1] if len(sys.argv) > 1 else "l20io"
LEGACY = {
 "l20io": (["cms_e4l20_pool_a:QUESTIONS", "cms_e4l20_pool_b:QUESTIONS"],
           "cms_e4l20_sets.json"),
 "l20vig": (["cms_e4l20_vig_a:QUESTIONS", "cms_e4l20_vig_b:QUESTIONS"],
            "cms_e4l20_vig_sets.json"),
}
GUARDED = {
 # key: (lecture tag, is vignette set, seed)
 "l21io": ("l21", False, 20260924 + 211),
 "l21vig": ("l21", True, 20260924 + 212),
 "l22io": ("l22", False, 20260924 + 221),
 "l22vig": ("l22", True, 20260924 + 222),
 "l25io": ("l25", False, 20260924 + 251),
 "l25vig": ("l25", True, 20260924 + 252),
}
if WHICH not in LEGACY and WHICH not in GUARDED:
    sys.exit("unknown set %r -- use one of %s" % (WHICH, ", ".join(list(LEGACY) + list(GUARDED))))

PER_SET = 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= MARGIN_CHARS and tl >= rn * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


# ============================================================================
# LEGACY PATH -- Lecture 20 Hypertension, unchanged from the shipped version.
# ============================================================================
def legacy_main():
    mods, OUT_JSON = LEGACY[WHICH]
    POOL = []
    for spec in mods:
        m, attr = spec.split(":")
        for q in getattr(__import__(m), attr):
            # Pools author the correct answer FIRST and leave the key implicit.
            # Rotation below moves it regardless, so a missing key means 0.
            if "c" not in q:
                q = dict(q, c=0)
            POOL.append(q)

    random.seed(20260918)
    NOPT = len(POOL[0]["opts"]) if POOL else 4
    assert all(len(q["opts"]) == NOPT for q in POOL), \
        "the pool mixes option counts: %s" % sorted({len(q["opts"]) for q in POOL})

    PATIENT = re.compile(r"\b\d+-(year|month|week|day)-old\b|\bnewborn\b"
                         r"|\bin (his|her|their) (twenties|thirties|forties|fifties|sixties)\b", re.I)

    def is_patient(q):
        return bool(PATIENT.search(q["q"]))

    def slot_spread(qs):
        c = Counter(q.get("slot") for q in qs if q.get("slot"))
        return len(c), sum(max(0, n - 6) for n in c.values())

    def score(qs):
        pat = 100.0 * sum(is_patient(q) for q in qs) / len(qs)
        pat_term = max(0, 80 - pat) * 2.0 if WHICH.endswith("vig") else 0.0
        game = gameable_pct(qs)
        topics = Counter(q["topic"] for q in qs)
        lumpy = sum(max(0, n - 4) for n in topics.values())
        nslots, slot_lump = slot_spread(qs)
        return (pat_term + max(0, game - 13) * 1.5 + lumpy * 2.0
                + max(0, 10 - nslots) * 3.0 + slot_lump * 1.5)

    def rotate(qs):
        targets = [i % NOPT for i in range(len(qs))]
        random.shuffle(targets)
        for q, t in zip(qs, targets):
            k = (t - q["c"]) % NOPT
            q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
            q["c"] = t
        return qs

    def validate(pool):
        bad = []
        for i, q in enumerate(pool):
            if len(q["opts"]) != NOPT:
                bad.append((i, "has %d options, set uses %d" % (len(q["opts"]), NOPT)))
            if not (0 <= q["c"] < NOPT): bad.append((i, "answer index out of range"))
            if not q.get("cite"): bad.append((i, "missing citation"))
            if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
            for j, o in enumerate(q["opts"]):
                if not o[1].strip(): bad.append((i, "option %d unexplained" % j))
                if j != q["c"] and re.match(r"correct\b", o[1].strip(), re.I):
                    bad.append((i, "wrong option opens with Correct"))
            if not re.match(r"correct\b", q["opts"][q["c"]][1].strip(), re.I):
                bad.append((i, "keyed option does not open with Correct"))
        return bad

    print("set: %s   pool: %d" % (WHICH, len(POOL)))
    print("schema problems:", validate(POOL) or "none")
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    best, idx = None, list(range(len(POOL)))
    for _ in range(40000):
        random.shuffle(idx)
        ch = idx[:PER_SET * 2]
        total = score([POOL[i] for i in ch[:PER_SET]]) + score([POOL[i] for i in ch[PER_SET:]])
        if best is None or total < best[0]:
            best = (total, list(ch))

    ch = best[1]
    s1 = rotate([POOL[i] for i in ch[:PER_SET]])
    s2 = rotate([POOL[i] for i in ch[PER_SET:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        L = [len(o[0]) for q in s for o in q["opts"]]
        pos = Counter(q["c"] for q in s)
        nslots, _ = slot_spread(s)
        print("%s  n=%d" % (name, len(s)))
        print("   positions A-%s: %s" % ("ABCD"[NOPT - 1],
              "/".join(str(pos.get(i, 0)) for i in range(NOPT))))
        print("   gameable %d%%   slots covered %d   patient stems %d%%"
              % (gameable_pct(s), nslots,
                 100 * sum(map(is_patient, s)) // len(s)))
        print("   option length median %d, max %d (reference 19 / 66)"
              % (statistics.median(L), max(L)))
        print()

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, OUT_JSON), "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)


# ============================================================================
# GUARDED PATH -- Carter's lectures 21, 22 and 25.
# ============================================================================
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")

# Vignette lead-in vocabulary. "test" covers initial, confirmatory and what a test
# shows; "avoid" is what must not be given; "complication" includes prognosis.
LEADS = ("diagnosis", "next step", "treatment", "test", "education", "avoid",
         "complication", "referral")
DX_CAP = int(30 * 0.20)          # 6 of 30 -- "there might be SOME" diagnosis questions
SKEW_CAP = 0.40

# A stem that asks for the diagnosis must be LABELLED diagnosis, whatever else
# it is; this is what stops the cap from being dodged by a generous label.
_ASKS_DX = re.compile(r"most likely (diagnosis|cause|explanation|type|mechanism of (his|her|the) "
                      r"(syncope|faint|episode))|which (diagnosis|condition|disorder) (is|best)"
                      r"|what is the (diagnosis|most likely)", re.I)

# Every stem opens on a patient. A describing word or three may sit between the
# article and the age ("A previously healthy 19-year-old").
_VIG = re.compile(r"^(A|An)\s+(?:[\w,-]+\s+){0,4}\d{1,3}[- ](?:year|month|week|day)s?[- ]old\b", re.I)

_DEP = re.compile(r"previous question|question above|as in the last|earlier question"
                  r"|preceding (question|case|vignette)|\b(?:the same|this same) (?:patient|man|woman|"
                  r"girl|boy|mother|father|child|infant|person|case)\b"
                  r"|\bthe patient (?:above|described above)\b|\babove patient\b", re.I)

# No dosing. mg/dL and mmol/L are laboratory units, not doses.
_DOSE = re.compile(r"\b\d+(?:\.\d+)?\s?(?:mg|mcg|micrograms?|milligrams?|grams?|g|units?|IU)\b(?!\s?/\s?(?:dL|L|d[Ll]))"
                   r"|\b(?:once|twice|three times) (?:daily|a day)\b|\bq\.?d\b|\bb\.?i\.?d\b", re.I)

# Generic names only. Brand names from the three decks and the usual suspects.
_BRAND = re.compile(r"\b(Lipitor|Crestor|Zocor|Pravachol|Livalo|Zetia|Vytorin|Repatha|Praluent|"
                    r"Leqvio|Nexletol|Nexlizet|Evkeeza|Juxtapid|Kynamro|Vascepa|Lovaza|Tricor|"
                    r"Trilipix|Lopid|Welchol|Niaspan|Questran|Colestid|Entresto|Farxiga|Jardiance|"
                    r"Invokana|Lasix|Bumex|Demadex|Coreg|Toprol|Lopressor|Aldactone|Inspra|Kerendia|"
                    r"Lanoxin|Corlanor|Verquvo|BiDil|Florinef|ProAmatine|Northera|Mestinon|Vasotec|"
                    r"Zestril|Cozaar|Diovan|Norvasc|Tenormin|Inderal|LifeVest|Tryngolza)\b")

# Mechanism-of-action STEMS (Carter: "no mechanism of action questions").
# Disease pathophysiology is not banned -- drug mechanism is.
_MOA = re.compile(r"mechanism of action|by what mechanism does|how does (?:the drug |this drug |the medication )?"
                  r"\w+(?: \w+)? work\b|which (?:enzyme|receptor|transporter|protein) does \w+ (?:inhibit|block)"
                  r"|what does \w+ inhibit|\bworks? by\b|\bacts? by\b", re.I)

# Acronyms: any word carrying two or more consecutive capitals must be followed
# at once by its full term in parentheses. Roman numerals are identifiers, not
# abbreviations, and so are the heart sounds.
_ACRO = re.compile(r"(?<![\w-])([A-Za-z0-9-]*[A-Z]{2,}[A-Za-z0-9-]*)(?![\w-])")
_ACRO_OK = re.compile(r"^(?:I{1,3}|IV|VI{0,3}|IX|X|S[1-4]|mmHg|QRS)$")

# US spelling (2026-09-23). Verbatim io/cite fields are exempt.
_UK = re.compile(r"\b\w*(?:aemi|oedem|oesoph|oestr|paediat|orthopaed|ischaem|haemo(?!philus)|haema|haemorrh|"
                 r"anaesth|foet)\w*\b|\b(?:tumour|colour|behaviour|favour|centre|litre|fibre|"
                 r"counsell\w*|labell\w*|modell\w*|travell\w*|ageing|programme|manoeuvres?|grey|"
                 r"whilst|amongst|analyze[ds]?|paralyze[ds]?|license|defense|practice[ds]?|"
                 r"recognis\w*|characteris\w*|organis\w*|summaris\w*|emphasis(?:e|ed|es|ing)|"
                 r"minimis\w*|maximis\w*|normalis\w*|stabilis\w*|prioritis\w*|optimis\w*|mobilis\w*|"
                 r"utilis\w*|sensitis\w*|hospitalis\w*|specialis\w*|visualis\w*|categoris\w*|"
                 r"standardis\w*|individualis\w*|randomis\w*|hypothesis(?:e|ed)|neutralis\w*|"
                 r"metabolis(?:e|ed|es|ing))\b", re.I)

SET1_LEAD_NOTE = None


def _texts(q):
    yield "stem", q["q"]
    for j, o in enumerate(q["opts"]):
        yield "option %d" % j, o[0]
        yield "explanation %d" % j, o[1]


def load_guarded(lec, vig):
    scope = importlib.import_module("cms_e4%s_scope" % lec)
    pat = "cms_e4%s_%s_*.py" % (lec, "vig" if vig else "pool")
    mods = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, pat)))
    assert mods, "no pools match %s" % pat
    try:
        fixes = importlib.import_module("cms_e4%s_lengthfix" % lec).FIXES
    except ImportError:
        fixes = {}
    pool, origin = [], []
    for m in mods:
        qs = importlib.import_module(m).QUESTIONS
        for i, q in enumerate(qs):
            q = json.loads(json.dumps(q))          # never mutate the module's list
            q.setdefault("c", 0)
            for j in range(4):
                if (m, i, j) in fixes:
                    q["opts"][j][0] = fixes[(m, i, j)]
            pool.append(q)
            origin.append((m, i))
    stale = [k for k in fixes if k[0] in mods and k[1] >= len(importlib.import_module(k[0]).QUESTIONS)]
    assert not stale, "length fixes point past the end of their pool: %r" % stale[:3]
    return scope, mods, pool, origin, len([k for k in fixes if k[0] in mods])


def guard_all(scope, pool, origin, vig):
    """Every guard is an assert: a guard that only prints gets ignored."""
    def where(i):
        return "%s[%d] %r" % (origin[i][0], origin[i][1], pool[i]["q"][:70])

    ios = list(scope.IOS)
    excluded = set(getattr(scope, "EXCLUDED_SLIDES", ()))
    banned = [re.compile(p, re.I) for p in getattr(scope, "SCOPE_BANNED", ())]
    named = dict(getattr(scope, "NAMED", {}))
    deck = scope.DECK

    errs = []
    seen_stems = Counter(q["q"].strip().lower() for q in pool)
    for i, q in enumerate(pool):
        # schema
        if len(q["opts"]) != 4: errs.append((where(i), "not four options"))
        if q["c"] != 0: errs.append((where(i), "key must be authored first (c=0)"))
        if len({o[0].strip().lower() for o in q["opts"]}) != 4: errs.append((where(i), "duplicate option"))
        if not re.match(r"correct\b", q["opts"][0][1].strip(), re.I):
            errs.append((where(i), "keyed explanation does not open 'Correct'"))
        for j, o in enumerate(q["opts"][1:], 1):
            if re.match(r"correct\b", o[1].strip(), re.I):
                errs.append((where(i), "distractor %d explanation opens 'Correct'" % j))
            if len(o[1].strip()) < 60:
                errs.append((where(i), "distractor %d explanation under 60 chars" % j))
        if seen_stems[q["q"].strip().lower()] > 1: errs.append((where(i), "duplicate stem"))
        # citation
        m = re.match(r"^(.*), Slides? (\d+)", q.get("cite", ""))
        if not m or m.group(1) != deck:
            errs.append((where(i), "cite must read '%s, Slide N', got %r" % (deck, q.get("cite"))))
        else:
            for n in re.findall(r"\d+", q["cite"][len(deck):]):
                if int(n) in excluded:
                    errs.append((where(i), "cites excluded slide %s" % n))
        # slot and io
        if q.get("slot") not in SLOTS: errs.append((where(i), "bad slot %r" % q.get("slot")))
        if q.get("io") not in ios: errs.append((where(i), "io is not a verbatim scope IO"))
        # scope, dosing, brands, acronyms, spelling
        for label, t in _texts(q):
            if _DOSE.search(t): errs.append((where(i), "dosing in %s: %r" % (label, _DOSE.search(t).group(0))))
            if _BRAND.search(t): errs.append((where(i), "brand name in %s: %r" % (label, _BRAND.search(t).group(0))))
            if _UK.search(t): errs.append((where(i), "UK spelling in %s: %r" % (label, _UK.search(t).group(0))))
            for b in banned:
                if b.search(t): errs.append((where(i), "scope-banned %r in %s" % (b.pattern, label)))
            for mm in _ACRO.finditer(t):
                tok = mm.group(1)
                if _ACRO_OK.match(tok):
                    continue
                if not t[mm.end():].startswith(" ("):
                    errs.append((where(i), "bare acronym %r in %s" % (tok, label)))
        if _MOA.search(q["q"]): errs.append((where(i), "mechanism-of-action stem"))
        if _DEP.search(q["q"]): errs.append((where(i), "stem refers to another question"))
        if not q["q"].rstrip().endswith("?"): errs.append((where(i), "stem does not end on a question"))
        if vig:
            if not _VIG.match(q["q"].strip()): errs.append((where(i), "vignette stem does not open on a patient"))
            lead = q.get("lead")
            if lead not in LEADS: errs.append((where(i), "missing or unknown lead %r" % lead))
            elif _ASKS_DX.search(q["q"]) and lead != "diagnosis":
                errs.append((where(i), "asks for the diagnosis but is labeled %r" % lead))
            low = q["q"].lower()
            for name, gloss in named.items():
                if name.lower() in low and gloss.lower() not in low:
                    errs.append((where(i), "named finding %r without its description (%r)" % (name, gloss)))
    assert not errs, "%d guard failure(s):\n  %s" % (len(errs), "\n  ".join("%s -- %s" % e for e in errs[:60]))
    return ios


def guarded_main():
    lec, vig, seed = GUARDED[WHICH]
    random.seed(seed)
    scope, mods, POOL, origin, nfix = load_guarded(lec, vig)
    ios = guard_all(scope, POOL, origin, vig)
    OUT_JSON = "cms_e4%s_%s.json" % (lec, "vig_sets" if vig else "sets")
    ALL_TOPICS = sorted(set(q["topic"] for q in POOL))
    pool_ios = sorted(set(q["io"] for q in POOL), key=ios.index)

    print("set: %s   pool: %d from %s   length fixes applied: %d" % (WHICH, len(POOL), ", ".join(mods), nfix))
    print("topics: %d   objectives in pool: %d of %d" % (len(ALL_TOPICS), len(pool_ios), len(ios)))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("slots in pool:", dict(Counter(q["slot"] for q in POOL).most_common()))
    if vig:
        print("pool lead-in mix:", dict(Counter(q["lead"] for q in POOL).most_common()))
    print("guards passed: schema, citation, slot, io, excluded slides, dosing, brand names, "
          "mechanism stems, acronyms, US spelling, no cross-question dependency%s"
          % (", vignette opening, lead vocabulary, diagnosis labeling, named-finding glosses" if vig else ""))

    dx_idx = [i for i, q in enumerate(POOL) if vig and q["lead"] == "diagnosis"]
    if vig:
        need_other = 2 * PER_SET - 2 * DX_CAP
        n_other = len(POOL) - len(dx_idx)
        assert n_other >= need_other, (
            "pool has only %d non-diagnosis vignettes but two sets need %d at the cap -- write "
            "more management/test/education stems rather than relaxing the cap" % (n_other, need_other))
    dxset = set(dx_idx)
    ntop = len(ALL_TOPICS)
    lump_at = max(3, -(-PER_SET // ntop) + 2)

    def score(idxs):
        s = [POOL[i] for i in idxs]
        tops = Counter(q["topic"] for q in s)
        slots = Counter(q["slot"] for q in s)
        missing_t = sum(1 for t in ALL_TOPICS if t not in tops) if ntop <= PER_SET else 0
        lumpy_t = sum(max(0, n - lump_at) for n in tops.values())
        lumpy_s = sum(max(0, n - 6) for n in slots.values())
        thin_s = max(0, 10 - len(slots))
        v = (gameable_pct(s) * 3.0 + missing_t * 6 + lumpy_t * 3 + lumpy_s * 1.5 + thin_s * 3)
        if vig:
            leads = Counter(q["lead"] for q in s)
            skew = sum(max(0, n - len(s) * SKEW_CAP) for n in leads.values())
            v += skew * 20 + max(0, 5 - len(leads)) * 10
            v += max(0, leads.get("diagnosis", 0) - DX_CAP) * 500
        else:
            ioc = Counter(q["io"] for q in s)
            v += sum(1 for io in pool_ios if io not in ioc) * 12
        return v

    # REQUIRED (optional, scope module): content the lecturer said WILL be on the
    # test, as (label, stem regex, key regex, minimum per form). Scored, then asserted.
    required = [(lab, re.compile(sr, re.I), re.compile(kr, re.I), n)
                for lab, sr, kr, n in getattr(scope, "REQUIRED", ())]
    req_hit = {lab: {i for i, q in enumerate(POOL) if srx.search(q["q"]) and krx.search(q["opts"][0][0])}
               for lab, srx, krx, n in required}
    for lab, srx, krx, n in required:
        assert len(req_hit[lab]) >= 2 * n, "pool has only %d %r questions for two forms" % (len(req_hit[lab]), lab)

    def req_short(idxs):
        return sum(max(0, n - sum(1 for i in idxs if i in req_hit[lab])) for lab, _, _, n in required)

    def total(sel):
        return (score(sel[:PER_SET]) + score(sel[PER_SET:])
                + 100 * (req_short(sel[:PER_SET]) + req_short(sel[PER_SET:])))

    def dx_ok(sel):
        return (sum(1 for i in sel[:PER_SET] if i in dxset) <= DX_CAP and
                sum(1 for i in sel[PER_SET:] if i in dxset) <= DX_CAP)

    idx = list(range(len(POOL)))
    best = None
    for _ in range(600):
        if vig:
            random.shuffle(dx_idx)
            other = [i for i in idx if i not in dxset]
            random.shuffle(other)
            k = min(DX_CAP, len(dx_idx) // 2)
            take_dx = dx_idx[:2 * k]
            take_ot = other[:2 * PER_SET - len(take_dx)]
            cand = take_dx[:k] + take_ot[:PER_SET - k] + take_dx[k:] + take_ot[PER_SET - k:]
        else:
            random.shuffle(idx)
            cand = idx[:2 * PER_SET]
        t = total(cand)
        if best is None or t < best[0]:
            best = (t, list(cand))
    cur_score, cur = best
    outside = [i for i in range(len(POOL)) if i not in set(cur)]
    for step in range(80000):
        if outside and random.random() < 0.7:
            a, b = random.randrange(2 * PER_SET), random.randrange(len(outside))
            cur[a], outside[b] = outside[b], cur[a]
            ok = dx_ok(cur) if vig else True
            t = total(cur) if ok else None
            if ok and t <= cur_score:
                cur_score = t
            else:
                cur[a], outside[b] = outside[b], cur[a]
        else:                                   # move a question between the two sets
            a, b = random.randrange(PER_SET), PER_SET + random.randrange(PER_SET)
            cur[a], cur[b] = cur[b], cur[a]
            ok = dx_ok(cur) if vig else True
            t = total(cur) if ok else None
            if ok and t <= cur_score:
                cur_score = t
            else:
                cur[a], cur[b] = cur[b], cur[a]
    print("local search settled at score %.1f" % cur_score)

    for lab, _, _, n in required:
        for part in (cur[:PER_SET], cur[PER_SET:]):
            assert sum(1 for i in part if i in req_hit[lab]) >= n, "a form lacks %r" % lab
        print("required %r: %d and %d per form (minimum %d)" % (lab, sum(1 for i in cur[:PER_SET] if i in req_hit[lab]),
              sum(1 for i in cur[PER_SET:] if i in req_hit[lab]), n))
    answer_text = {i: POOL[i]["opts"][0][0] for i in cur}
    sets = []
    for part in (cur[:PER_SET], cur[PER_SET:]):
        qs = [json.loads(json.dumps(POOL[i])) for i in part]
        targets = [i % 4 for i in range(len(qs))]
        random.shuffle(targets)
        for i, q, t in zip(part, qs, targets):
            k = (t - q["c"]) % 4
            q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
            q["c"] = t
            assert q["opts"][q["c"]][0] == answer_text[i], "rotation moved an answer!"
            assert re.match(r"correct\b", q["opts"][q["c"]][1], re.I)
        sets.append(qs)
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in zip(("SET 1", "SET 2"), sets):
        pos = Counter(q["c"] for q in s)
        L = [len(o[0]) for q in s for o in q["opts"]]
        print("%s  n=%d" % (name, len(s)))
        print("   positions A/B/C/D: %s" % "/".join(str(pos.get(i, 0)) for i in range(4)))
        print("   gameable %.1f%%   topics %d of %d   slots %d"
              % (gameable_pct(s), len(set(q["topic"] for q in s)), ntop, len(set(q["slot"] for q in s))))
        print("   option length median %d, max %d (reference 19 / 66)" % (statistics.median(L), max(L)))
        if vig:
            leads = Counter(q["lead"] for q in s)
            print("   lead-ins:", dict(leads.most_common()))
            top = max(leads.values())
            assert top <= len(s) * SKEW_CAP, "%s is %d/%d one lead-in type -- too skewed" % (name, top, len(s))
            assert leads.get("diagnosis", 0) <= DX_CAP, "%s over the diagnosis cap" % name
            assert all(_VIG.match(q["q"]) for q in s)
        else:
            ioc = Counter(q["io"] for q in s)
            print("   objectives covered: %d of %d in pool" % (len(ioc), len(pool_ios)))
        assert len(s) == PER_SET and max(pos.values()) <= 10, "%s positions skewed: %s" % (name, dict(pos))
        print()
    assert not set(q["q"] for q in sets[0]) & set(q["q"] for q in sets[1]), "a stem is in both sets"

    json.dump({"set1": sets[0], "set2": sets[1]}, open(os.path.join(HERE, OUT_JSON), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)


if __name__ == "__main__":
    if WHICH in LEGACY:
        legacy_main()
    else:
        guarded_main()
