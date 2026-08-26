#!/usr/bin/env python3
"""Partition the CMS I Exam 2 Lecture 1 VIGNETTE pool into two 30s.

This is SET 2 of the four exams [[cms_exam_spec]] requires per CMS topic.

WHAT PROF. JAQUITH SAID ABOUT HER EXAM (Exam 1 opening minute, and there is no
reason to think Exam 2 differs): questions are "pretty much all clinical
vignettes ... recognize conditions by the vignette", with "SOME diagnosis but
A LOT are next management plan / first line treatment / patient education", and
"way more non-pictures than pictures". Hence:

  DX_CAP -- diagnosis lead-ins are capped at 20 per cent of each set. Everything
  else is next-step, first-line, education, testing or prognosis. Without the
  cap the selector happily fills a set with "what is the most likely diagnosis",
  which is not the exam she described.

  _VIG -- every stem must open on a patient. A vignette set with a bare recall
  question in it is not a vignette set.

  _DEP -- NO STEM MAY REFER TO ANOTHER QUESTION. This guard exists because of a
  real bug a classmate reported on 25 August 2026: vignettes written as chains
  ("The same patient is not bothered by her lesion...") never worked, because
  the partitioner shuffles and the setup question lands somewhere else entirely.
  The topic tag had been quietly supplying the missing lesion until the tag was
  hidden. The pattern list below is deliberately wide -- the original guard
  matched only the phrasings that had been imagined, not the one actually
  written thirteen times.

Every question is authored with its correct answer first.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_e2l1_vig_a import VIG_A
from cms_e2l1_vig_b import VIG_B

POOL = VIG_A + VIG_B

try:
    from cms_e2l1_vig_lengthfix import FIXES
except ImportError:
    FIXES = {}
for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Guard 1: every stem opens on a patient -------------------------------
# Allow a describing word or two between the article and the age --
# "A healthy 28-year-old man" is every bit as much a vignette as "A 28-year-old
# man", and the first version of this guard rejected it.
_VIG = re.compile(r"^A[n]?\s+(?:\w+\s+){0,3}\d{1,3}[- ]?(?:year|month|day|week)s?[- ]old"
                  r"|^A\s+(?:public health team|newborn|neonate)", re.I)
_notvig = [q["q"][:60] for q in POOL if not _VIG.match(q["q"].strip())]
assert not _notvig, ("vignette stem does not open on a patient: %r" % _notvig[:3])

# ---- Guard 2: no stem may depend on another question ----------------------
# "that eye" is an INTERNAL back-reference within a stem that already
# introduced the eye, and is perfectly fine -- the first version of this guard
# flagged it. The cross-question idiom is "the same X" / "this same X", which
# is what actually shipped broken in the CMS Exam 1 vignettes. Guard 1 already
# guarantees each stem opens on its own patient with an age, so a stem cannot
# silently inherit one.
_DEP = re.compile(r"previous question|question above|as in the last|earlier question"
                  r"|\b(?:the same|this same) (?:patient|man|woman|girl|boy|mother|"
                  r"father|child|infant|neonate|lesion|nodule|plaque|rash|eye|lid)\b"
                  r"|\bthe patient (?:above|described above)\b", re.I)
_dep = [q["q"][:70] for q in POOL if _DEP.search(q["q"])]
assert not _dep, ("stem refers to another question -- the partitioner shuffles, so it "
                  "will not be adjacent and the student is left without the finding: "
                  "%r" % _dep[:3])

# ---- Guard 3: named findings carry their description ----------------------
# [[cms_exam_spec]]: "Where a term has a special name, put what it actually
# looks like beside it." A stem may use the name only if it explains it.
_NAMED = {"ciliary flush": "ring of redness",
          "consensual photophobia": "shone",
          "hutchinson": "tip of",
          "violaceous": "bluish"}
_bare = []
for q in POOL:
    low = q["q"].lower()
    for name, gloss in _NAMED.items():
        if name in low and gloss not in low:
            _bare.append((name, q["q"][:50]))
assert not _bare, ("a named finding appears in a stem without its description in "
                   "parentheses: %r" % _bare[:3])

SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]
    assert _q.get("lead"), "missing lead type on: %s" % _q["q"][:70]

# ---- Guard 4: enough non-diagnosis vignettes to honour the cap ------------
DX_CAP = int(30 * 0.20)                       # 6 of 30, matching "there might be SOME"
_dx = [i for i, q in enumerate(POOL) if q["lead"] == "diagnosis"]
_other = [i for i in range(len(POOL)) if i not in set(_dx)]
_need_other = 60 - 2 * DX_CAP
assert len(_other) >= _need_other, (
    "pool has only %d non-diagnosis vignettes but two sets need %d at the %d%% cap -- "
    "write more" % (len(_other), _need_other, 20))
assert len(_dx) >= 2 * DX_CAP, ("pool has only %d diagnosis vignettes but two sets can "
                                "take %d" % (len(_dx), 2 * DX_CAP))

random.seed(20260826 + 22)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (top_len, top_i), (runner, _) = lens[0], lens[1]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_TOPICS = set(q["topic"] for q in POOL)


def score(setqs):
    tops = Counter(q["topic"] for q in setqs)
    leads = Counter(q["lead"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    over_dx = max(0, leads.get("diagnosis", 0) - DX_CAP)
    lumpy_t = sum(max(0, n - 3) for n in tops.values())
    thin_leads = max(0, 5 - len(leads))          # want a genuine spread of lead types
    lumpy_s = sum(max(0, n - 6) for n in slots.values())
    return (over_dx * 200 + thin_leads * 20 + lumpy_t * 3 + lumpy_s * 2
            + gameable_pct(setqs) * 8.0)


def rotate_for_balance(qs):
    targets = [i % 4 for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
        q["c"] = t
    return qs


def validate(pool):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != 4: bad.append((i, "not 4 options"))
        if not (0 <= q["c"] <= 3): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != 4: bad.append((i, "duplicate option text"))
        for o in q["opts"]:
            if not o[1].strip(): bad.append((i, "option missing explanation"))
    return bad


if __name__ == "__main__":
    print("vignette pool:", len(POOL))
    print("schema problems:", validate(POOL) or "none")
    print("topics:", len(ALL_TOPICS), " lead types:", len(set(q["lead"] for q in POOL)))
    print("diagnosis leads: %d   other leads: %d   (cap is %d per set)"
          % (len(_dx), len(_other), DX_CAP))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("guards: every stem opens on a patient, no stem references another question, "
          "named findings glossed")
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    def total(sel):
        return score([POOL[i] for i in sel[:30]]) + score([POOL[i] for i in sel[30:]])

    idx = list(range(len(POOL)))
    best = None
    for _ in range(400):
        random.shuffle(idx)
        cand = idx[:60]
        t = total(cand)
        if best is None or t < best[0]:
            best = (t, list(cand))
    cur_score, cur = best
    outside = [i for i in range(len(POOL)) if i not in set(cur)]
    for _ in range(60000):
        a = random.randrange(60)
        b = random.randrange(len(outside))
        cur[a], outside[b] = outside[b], cur[a]
        t = total(cur)
        if t < cur_score:
            cur_score = t
        else:
            cur[a], outside[b] = outside[b], cur[a]
    print("local search settled at score %.1f" % cur_score)

    s1 = rotate_for_balance([POOL[i] for i in cur[:30]])
    s2 = rotate_for_balance([POOL[i] for i in cur[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        ndx = sum(1 for q in s if q["lead"] == "diagnosis")
        assert ndx <= DX_CAP, "%s has %d diagnosis questions, cap is %d" % (name, ndx, DX_CAP)
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions %s  gameable %.1f%%  topics %d  diagnosis %d/%d  leads %d"
              % (name, len(s), dict(sorted(pos.items())), gameable_pct(s),
                 len(set(q["topic"] for q in s)), ndx, DX_CAP,
                 len(set(q["lead"] for q in s))))

    with open(os.path.join(HERE, "cms_e2l1_vig_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": s1, "set2": s2}, fh, ensure_ascii=False, indent=1)
    print("\nwrote cms_e2l1_vig_sets.json")
