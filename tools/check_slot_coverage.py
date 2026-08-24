#!/usr/bin/env python3
"""Measure which FACT SLOTS a CMS question pool actually covers.

The CMS instructional objective names nine things for every condition --
etiology, epidemiology, risk factors, clinical manifestations, differential
diagnosis, diagnostic testing, management, referrals, patient education and
prognosis. A pool can hit every TOPIC and still be lopsided across those, and
nothing else in the QA sweep would notice.

Measured 2026-08-19 across the 450 objective questions of the five dermatology
lectures, the pools were heavy on what-is-it and what-does-it-look-like and thin
on the back half of the objective: ESCALATION appeared once, referral three
times, gold standard four, prognosis four. That is the gap this tool exists to
make visible.

Classification: a question's own `slot="..."` wins. Otherwise the stem is
matched against the patterns below, first match in order. Explicit tags are
strongly preferred for new pools -- a stem like "which is the most appropriate
response?" cannot be classified from its wording, exactly as with the vignette
lead-in guard.

Usage:
  python3 tools/check_slot_coverage.py                 # every CMS lecture
  python3 tools/check_slot_coverage.py l4 l5           # named lectures
  python3 tools/check_slot_coverage.py --floors        # apply the floors, exit 1 on a miss
"""
import sys, os, re, importlib
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# The slots, in the order the objective names them. Patterns are tried in this
# order, so put the specific ones above the general ones.
SLOTS = OrderedDict([
 ("etiology",     r"which organism|what organism|causative|caused by|what kind of organism|"
                  r"mechanism|pathophysiolog|what underlies|presumed origin|how (is|are) .* inherited|"
                  r"which gene|what triggers|which trigger"),
 ("epidemiology", r"what proportion|how common|prevalence|what percentage|which age group|"
                  r"who gets|age distribution|which sex|more common in (men|women|males|females)|"
                  r"in whom does|which population"),
 ("risk factors", r"risk factor|predispos|which factors (are named|underlie)"),
 ("manifestation",r"hallmark|pathognomonic|classic (lesion|presentation|appearance)|defining feature|"
                  r"describe|appearance|what does .* look like|how does .* (present|appear|behave)|"
                  r"which lesion|characteristic (finding|physical)|where do|which site|distribution|"
                  r"how (soon|long|fast)|time course|natural history|which skin tone|on darker skin"),
 ("differential", r"separat|distinguish|differs? from|rather than|which feature separates|"
                  r"differential|which condition is|mistaken for|identical to"),
 ("initial test", r"initial test|first test|which test|diagnostic (test|tool|approach|testing)|"
                  r"how is .* diagnosed|establishes the diagnosis|which investigation|which imaging|"
                  r"required to confirm|which laborator"),
 ("gold standard",r"gold standard|definitive diagnosis|confirms the diagnosis|pathognomonic (test|finding)|"
                  r"which test confirms|considered pathognomonic"),
 ("test finding", r"what does .* show|which finding|which result|histolog|biopsy shows?|"
                  r"fluoresce|what colour|which pattern (is seen|does)"),
 ("first-line",   r"first.line|initial treatment|first treatment|most appropriate treatment|"
                  r"mainstay|treatment of choice|drug of choice|how is .* (treated|managed)"),
 ("escalation",   r"next (step|treatment|line)|has (not|failed)|not (improved|responded|resolved)|"
                  r"refractory|second.line|escalat|unresponsive|persist(s|ed) despite|"
                  r"despite (a |an )?(full |complete )?(course|trial)|when .* fails"),
 ("agent/regimen",r"which (drug|agent|antibiotic|antifungal|medication|class)|which oral|which topical|"
                  r"how long|duration|how often|what dose|schedule|course of"),
 ("avoid",        r"avoid|not recommended|contraindic|why is .* not|should not|must not|never (be|use)|"
                  r"specifically avoided|is prohibited"),
 ("education",    r"counsel|patient education|what should .* be told|advice|patient asks|"
                  r"how (would|should) you explain|prevent|prophylax"),
 ("referral",     r"refer(ral|red)?\b|consult|which specialist|which team|who should (see|manage)"),
 ("complication", r"complicat|sequela|what may follow|which risk|leads? to|progress(es|ion) to"),
 ("prognosis",    r"prognos|resolves?|self.limit|how long does .* last|what should .* expect|"
                  r"chance of cure|recurrence rate|outcome"),
])

# Minimum questions per slot in a Set 1 pool of ~70+. Deliberately modest: the
# point is that no slot is ABSENT, not that they are equal. Manifestation and
# differential will always dominate, and should.
FLOORS = {"etiology": 5, "epidemiology": 3, "risk factors": 3, "manifestation": 10,
          "differential": 5, "initial test": 5, "gold standard": 2, "test finding": 3,
          "first-line": 5, "escalation": 3, "agent/regimen": 3, "avoid": 3,
          "education": 3, "referral": 2, "complication": 2, "prognosis": 2}

# THE MAP IS DISCOVERED FROM DISK, NOT HAND-MAINTAINED.
#
# It used to be a literal list of module names, and it went stale exactly as you
# would expect: Lecture 9 grew pools E, F and G while the map still named only
# A to D, so this tool kept reporting Lecture 9's ORIGINAL slot counts -- it
# went on printing "avoid: 0" after a whole corrective pool had been written to
# fix precisely that. Lectures 4 and 6 had drifted the same way, and Lecture 1
# was not listed at all. A checker that silently reads a subset of the thing it
# is checking is worse than no checker, because it reports success.
#
# Titles stay here because they are not derivable from a filename.
TITLES = {
 "l1": "Lecture 1 - Clinical Reasoning and Problem Solving",
 "l2": "Lecture 2 - General Dermatology I",
 "l3": "Lecture 3 - Dermatology II",
 "l4": "Lecture 4 - Cutaneous Bacterial Infections",
 "l5": "Lecture 5 - Dermatological Infestations",
 "l6": "Lecture 6 - Cutaneous Viral and Fungal Infections",
 "l7": "Lecture 7 - Benign Skin Lesions",
 "l8": "Lecture 8 - Pigmented Skin Lesions",
 "l9": "Lecture 9 - Pre-Malignant and Malignant Cutaneous Lesions",
}


def _discover():
    import glob, os.path as _p
    here = _p.dirname(_p.abspath(__file__))
    found = {}
    for path in glob.glob(_p.join(here, "cms_l*_pool_*.py")):
        m = re.match(r"cms_(l\d+)_pool_([a-z])$", _p.basename(path)[:-3])
        if m:
            found.setdefault(m.group(1), []).append("cms_%s_pool_%s" % m.groups())
    out = OrderedDict()
    for key in sorted(found, key=lambda k: int(k[1:])):
        title = TITLES.get(key)
        assert title, ("pools exist for %s but it has no title here -- add one rather "
                       "than letting the lecture go unchecked" % key)
        out[key] = (title, sorted(found[key]))
    return out


LECTURES = _discover()
def load(mods):
    out = []
    for m in mods:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError:
            continue                      # a pool that does not exist yet is fine
        names = [k for k in dir(mod) if k.startswith("POOL_")]
        for n in names:
            out += getattr(mod, n)
    return out


def slot_of(q):
    if q.get("slot"):
        s = q["slot"]
        assert s in SLOTS, "unknown slot %r on: %s" % (s, q["q"][:60])
        return s
    for name, pat in SLOTS.items():
        if re.search(pat, q["q"], re.I):
            return name
    return "unclassified"


# LECTURES THAT THE DISEASE-SHAPED FLOORS DO NOT APPLY TO.
#
# Lecture 1 is Clinical Reasoning and Problem Solving -- sensitivity, pretest
# probability, the naturalistic approach. It has no organism, no first-line
# agent, no prognosis, because it is not about a disease. It only started
# appearing in this report when the lecture map switched from a hand-written
# list to disk discovery, and reporting "avoid: 0/3" against it would be
# demanding questions that cannot honestly be written. Its slot distribution is
# still PRINTED; it is just not failed against the floors.
NO_DISEASE_FLOORS = {"l1"}


def report(key, apply_floors):
    label, mods = LECTURES[key]
    if key in NO_DISEASE_FLOORS:
        apply_floors = False
    pool = load(mods)
    if not pool:
        return []
    c = Counter(slot_of(q) for q in pool)
    tagged = sum(1 for q in pool if q.get("slot"))
    print("\n%s  (n=%d, %d explicitly tagged)" % (label, len(pool), tagged))
    misses = []
    for name in SLOTS:
        n = c.get(name, 0)
        floor = FLOORS[name]
        bar = "#" * min(n, 40)
        flag = ""
        if n < floor:
            # apply_floors was accepted as a parameter but never consulted here,
            # so --floors and the exemption above both had no effect on what got
            # reported as a miss.
            flag = "   <-- under floor of %d" % floor if apply_floors else "   (floors n/a)"
            if apply_floors:
                misses.append((label, name, n, floor))
        print("   %-14s %3d  %-40s%s" % (name, n, bar, flag))
    if c.get("unclassified"):
        print("   %-14s %3d   (add slot=\"...\" to these)" % ("unclassified", c["unclassified"]))
    return misses


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply_floors = "--floors" in sys.argv
    keys = args or list(LECTURES)
    all_misses = []
    for k in keys:
        all_misses += report(k, apply_floors)
    print("\n" + "=" * 62)
    if not all_misses:
        print("every slot at or above its floor in every lecture checked")
        return 0
    print("SLOTS UNDER FLOOR: %d" % len(all_misses))
    for label, name, n, floor in all_misses:
        print("   %-42s %-14s %d/%d" % (label, name, n, floor))
    return 1 if apply_floors else 0


if __name__ == "__main__":
    sys.exit(main())
