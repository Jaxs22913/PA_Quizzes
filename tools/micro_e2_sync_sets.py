#!/usr/bin/env python3
"""Carry pool edits onto the SHIPPED Microbiology Exam 2 sets, without re-partitioning.

    python3 tools/micro_e2_sync_sets.py          # rewrite tools/micro_l{7..13}_sets.json from the pools
    python3 tools/micro_e2_sync_sets.py --check  # exit 1 if any sets file is out of step with its pool

Why not just re-run the partitions: a partition is a seeded search scored on option LENGTHS, so editing one
explanation or option can change which questions it selects, and Lecture 7's committed sets no longer match
what its partition produces at all (its pools were edited after partitioning). Re-partitioning would ship
questions the blind review never saw. Same rule as tools/cms_e5l26_apply_patch.py: the reviewed selection
stays the selection that ships.

For every shipped question: find its pool record by exact stem (or through MOVED, for a stem that was
reworded or a question that was replaced), then rebuild it from the pool with the key kept at the SAME
position (the pool authors every key at position 0; the shipped order is a rotation of it). Unchanged
records must reproduce the shipped question exactly, which is asserted, so a run can only change what the
pools changed. `mis` (the misconception each distractor stands for) is carried into the sets file, where
tools/blind_review.py reads it; the renderers strip it before writing the page.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

POOLS = {7: ["micro_l7_pool_a", "micro_l7_pool_b"], 8: ["micro_l8_pool_a"],
         9: ["micro_l9_pool_a", "micro_l9_pool_b", "micro_l9_pool_c"],
         10: ["micro_l10_pool_a", "micro_l10_pool_b"], 11: ["micro_l11_pool"],
         12: ["micro_l12_pool"], 13: ["micro_l13_pool"]}
KEYS = ("topic", "io", "q", "opts", "c", "cite", "img", "alt", "slide", "mis")

# Shipped stem -> pool stem, for the blind-review repairs of 2026-10-15 (reworded or replaced questions).
MOVED = {
    # Lecture 7
    "Which hypersensitivity type is chronic asthma?":
        "Allergic asthma begins with an immediate, IgE-mediated response. When it becomes chronic, the airway "
        "inflammation is mediated by T cells, their cytokines and eosinophil granules. Which hypersensitivity "
        "type is this chronic phase?",
    # Repaired, then still flagged by the re-review, so dropped and replaced (the middle stem is the repair).
    "Adenosine deaminase deficiency causes which kind of immunodeficiency?":
        "A child is born with both limbs of the lymphocyte system defective and has no adaptive immune "
        "response. Which condition is this?",
    "A congenital adenosine deaminase deficiency blocks both cell-mediated immunity and immunoglobulin "
    "production. Which kind of immunodeficiency is this?":
        "A child is born with both limbs of the lymphocyte system defective and has no adaptive immune "
        "response. Which condition is this?",
    "What is the current status of tumor infiltrating lymphocyte therapy?":
        "Tumor infiltrating lymphocyte therapy activates which cells and expands them to a therapeutic amount?",
    # Lecture 8
    "Which of these is a named common laboratory test?":
        "Which of these is a common biochemical test run on a cultivated specimen?",
    "Into which two categories do results fall?":
        "Into which two categories do the results of specimen analysis fall?",
    # Repaired, then still flagged by the re-review, so dropped and replaced; the first replacement was
    # flagged too and replaced again (the middle stems are the repair and the first replacement).
    "Why is testing for antibodies often preferred to testing for the microbe itself?":
        "What is restriction fragment length polymorphism analysis often called?",
    "Why is immunological testing, which uses specific antibodies to detect antigens, often preferred to "
    "testing for the microbe itself?":
        "What is restriction fragment length polymorphism analysis often called?",
    "Rapid point-of-care tests for viral infections may be based on what?":
        "What is restriction fragment length polymorphism analysis often called?",
    # Lecture 9
    "A freshly isolated organism is Gram stained as shown. Which genus fits this arrangement?":
        "A freshly isolated organism is Gram stained as shown: purple, Gram-positive spheres lie in long, "
        "winding chains. Which genus fits this arrangement?",
    "What type of hemolysis surrounds the colonies on this blood agar plate?":
        "What type of hemolysis surrounds the colonies on this blood agar plate, each colony sitting in a "
        "sharp, clear, colorless halo?",
    "What does the change in the medium around and beneath these colonies show?":
        "What does the change in the medium around and beneath these colonies show, where the red blood agar "
        "has turned greenish?",
    "Which streptococcal skin infection produces lesions like these around the mouth?":
        "Which streptococcal skin infection produces lesions like these around the mouth, superficial lesions "
        "that have broken and formed thick crusts?",
    # Dropped after the re-review and replaced by a different question
    "Which streptococcus is strictly a human parasite, inhabiting the throat, nasopharynx and occasionally the skin?":
        "Which of these organisms has humans as its only reservoir?",
    "Which feature is true of every staphylococcus?":
        "Why do staphylococci stain Gram-positive?",
    # Lecture 10
    "Judging by where the spores sit in the rods shown, which genus are they?":
        "Judging by where the spores sit in the rods shown, each spore at one end of its rod and swelling it, "
        "which genus are they?",
    "What is the lesion shown on this man's jaw and neck?":
        "What is the lesion shown on this man's jaw and neck, a single dry, black, crusted lesion sitting on "
        "reddened, swollen skin?",
    "What syndrome does the infant shown illustrate?":
        "An infant who has been fed honey hangs limp, head and limbs drooping, when held face down across an "
        "adult's hand, as shown. What syndrome does this illustrate?",
    "Which condition produces the facial lesions shown?":
        "Which condition produces the facial lesions shown, deep, thick nodules that badly disfigure the nose, "
        "brow and lips?",
    "What does the test shown check for?":
        "A health worker lightly touches a feather to a boy's skin while the boy looks away, as shown. What "
        "does this test check for?",
    # Lecture 11
    "In the stewardship cycle, what should be considered before antimicrobial drugs are used?":
        "In the stewardship cycle, what should be considered after a bacterial disease is diagnosed and before "
        "antimicrobial drugs are used?",
    "The ESKAPE pathogens top the lists of which kind of infection?":
        "Klebsiella pneumoniae is counted among the drug-resistant superbugs in which form?",
    "A patient has had three recurrences of Clostridioides difficile infection despite treatment. Which novel "
    "therapy is established for preventing further recurrence?":
        "A patient has had three recurrences of Clostridioides difficile infection despite treatment. Which "
        "novel therapy has been specifically researched as a treatment for this infection?",
    "What kind of genome can a bacteriophage carry?":                 # its "never both" was notes-only
        "Which is a potential benefit of phage therapy?",
    "Why is fecal microbiota transplant an alternative to another antibiotic course in recurrent "
    "Clostridioides difficile infection?":
        "Why is fecal microbiota transplant researched as a treatment for Clostridioides difficile infection, "
        "an indirect adverse effect of antibiotics?",
    # Lecture 12 (blind review 2026-10-16): dropped and replaced by an unused pool question
    "In the pyramid of associations, which explanation sits at the base?":       # level order not in slide text
        "A relative risk that is either very high or very low is less likely to be due to chance or bias. Which of Hill's criteria is this?",
    "This epidemic curve shows Shigella cases among staff and attendees at a music festival by day of onset. "
    "Which type of epidemic does it show?":                                       # no slide label ties it to Mixed
        "This epidemic curve follows diarrheal illness in city residents for several weeks after water main "
        "breaks, falling away after a boil-water order. Which type of epidemic does it show?",
    # Lecture 13 (blind review 2026-10-16): stem reworded so only the key fits
    "Which drug is named alongside doxycycline as the treatment for syphilis?":
        "Which drug is named with doxycycline as the treatment for syphilis, not as a less effective fallback?",
}


def pool_records(n):
    import importlib
    out = {}
    for mod in POOLS[n]:
        m = importlib.import_module(mod)
        for name, v in vars(m).items():
            if name.isupper() and isinstance(v, list) and v and isinstance(v[0], dict) and "q" in v[0]:
                for r in v:
                    assert r["q"] not in out, "duplicate pool stem: %r" % r["q"][:80]
                    out[r["q"]] = r
    return out


def check_mis(r):
    m = r.get("mis")
    if m is None:
        return
    texts = [o[0] for o in r["opts"]]
    wrong = {t for i, t in enumerate(texts) if i != r["c"]}
    assert isinstance(m, dict) and set(m) == wrong, "mis must name every distractor exactly: %r" % r["q"][:80]
    assert all(isinstance(v, str) and v.strip() for v in m.values()), r["q"][:80]


def rebuild(shipped, r):
    """The pool record r, rotated so its key sits where the shipped question's key sits."""
    assert r["c"] == 0, "pool key not authored at position 0: %r" % r["q"][:80]
    t = shipped["c"]
    opts = [list(o) for o in r["opts"]]
    opts = opts[-t:] + opts[:-t] if t else opts
    q = {k: r[k] for k in KEYS if k in r and k not in ("opts", "c")}
    q["opts"], q["c"] = opts, t
    assert q["opts"][q["c"]][0] == r["opts"][0][0], "rotation moved the key"
    check_mis(dict(r))
    order = [k for k in shipped if k in q] + [k for k in KEYS if k in q and k not in shipped]
    return {k: q[k] for k in order}                 # the shipped key order, so the page JSON does not churn


def main(check=False):
    changed, moved, stale = 0, 0, []
    for n in POOLS:
        path = os.path.join(HERE, "micro_l%d_sets.json" % n)
        sets = json.load(open(path, encoding="utf-8"))
        pool = pool_records(n)
        out = {}
        for key, qs in sets.items():
            new = []
            for s in qs:
                stem = s["q"] if s["q"] in pool else MOVED.get(s["q"])
                assert stem in pool, "L%d %s: no pool record for %r" % (n, key, s["q"][:80])
                q = rebuild(s, pool[stem])
                if stem != s["q"]:
                    moved += 1
                if q != s:
                    changed += 1
                    stale.append("L%d %s: %s" % (n, key, s["q"][:70]))
                new.append(q)
            out[key] = new
        if not check:
            json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("%d shipped question(s) differ from their pool record (%d through MOVED)" % (changed, moved))
    if check and stale:
        for s in stale:
            print("   " + s)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
