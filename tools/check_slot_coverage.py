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

LECTURES = OrderedDict([
 ("l2", ("Lecture 2 - General Dermatology I",
         ["cms_l2_pool_a", "cms_l2_pool_b", "cms_l2_pool_c", "cms_l2_pool_d", "cms_l2_pool_e"])),
 ("l3", ("Lecture 3 - Dermatology II",
         ["cms_l3_pool_a", "cms_l3_pool_b", "cms_l3_pool_c", "cms_l3_pool_d"])),
 ("l4", ("Lecture 4 - Cutaneous Bacterial Infections",
         ["cms_l4_pool_a", "cms_l4_pool_b", "cms_l4_pool_c", "cms_l4_pool_d"])),
 ("l5", ("Lecture 5 - Dermatological Infestations",
         ["cms_l5_pool_a", "cms_l5_pool_b", "cms_l5_pool_c", "cms_l5_pool_d"])),
 ("l6", ("Lecture 6 - Cutaneous Viral and Fungal Infections",
         ["cms_l6_pool_a", "cms_l6_pool_b", "cms_l6_pool_c", "cms_l6_pool_d"])),
 ("l7", ("Lecture 7 - Benign Skin Lesions",
         ["cms_l7_pool_a", "cms_l7_pool_b", "cms_l7_pool_c", "cms_l7_pool_d"])),
 ("l8", ("Lecture 8 - Pigmented Skin Lesions",
         ["cms_l8_pool_a", "cms_l8_pool_b", "cms_l8_pool_c", "cms_l8_pool_d"])),
 ("l9", ("Lecture 9 - Pre-Malignant and Malignant Cutaneous Lesions",
         ["cms_l9_pool_a", "cms_l9_pool_b", "cms_l9_pool_c", "cms_l9_pool_d"])),
])


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


def report(key, apply_floors):
    label, mods = LECTURES[key]
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
            flag = "   <-- under floor of %d" % floor
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
