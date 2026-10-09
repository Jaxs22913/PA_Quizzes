#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 9 pool into 2 x 30.

Cocci of Medical Importance (Dr. Fair: the deck names no lecturer; the calendar row for
2026-10-02 names Dr. Fair, and the recording confirms a lecturer other than Dr. Webster --
"with Dr. Webster earlier, you had the gram-positive rods" [32:08] -- who will teach the class
again "next Friday" on what to do "when antibiotics don't work", the Lecture 11 Novel
Antimicrobial Therapy slot that is also Dr. Fair's).

Pools: micro_l9_pool_a (staphylococci), _b (streptococci and enterococci), _c (Gram-negative
cocci and coccobacilli, plus POOL_IMG, the picture questions).

WHAT THE SELECTION BALANCES, per set:
  * EVERY Appendix 2 organism of the syllabus (15 names; Branhamella and Moraxella are one
    organism, reclassified) appears at least once -- REQUIRED, asserted.
  * Sections by minutes spoken in the 59:37 recording: staphylococci ~16 min (26%),
    streptococci and enterococci ~26 min (43%), Gram-negatives ~18 min (31%, about five of
    them anecdote over rate maps). Targets 8 / 13 / 9 of 30.
  * Objective 2 (transmission) between 6 and 9 questions; the rest objective 1.
  * One question per near-duplicate fact group (DUPS below) per set.
  * Picture questions in SET 2 ONLY, exactly N_IMG of them. A quiz holding any picture question
    is dropped from Group Study by build_group_quizzes.py, so Set 1 stays text-only.
  * Length bias by selection (gameable %, and the key uniquely longest in at most ~30%).
Answer positions by ROTATION after selection, checked against the answer text.

Selector: swap-based local search from a seeded start (the CMS I Exam 2 / Micro L7 lesson:
best-of-N shuffles barely explore a constrained space). Seeded, so a re-run reproduces the
same sets.
"""
import sys, os, json, random, copy
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l9_pool_a import POOL_A
from micro_l9_pool_b import POOL_B
from micro_l9_pool_c import POOL_C, POOL_IMG

TEXT = POOL_A + POOL_B + POOL_C
IMGS = POOL_IMG
N_IMG = 6
NOPT = 4
random.seed(20261008)

REQUIRED_ORGS = ["aureus", "epidermidis", "hominis", "capitis", "saprophyticus", "pyogenes",
                 "agalactiae", "viridans", "pneumoniae", "enterococcus", "gonorrhoeae",
                 "meningitidis", "moraxella", "acinetobacter"]
TARGET = {"staph": 8, "strep": 13, "gneg": 9}

# Near-duplicate facts: stem prefixes; at most one per set from each group.
DUPS = {
    "clusters": ["How are staphylococcal cells arranged", "The Gram-stained smear shown comes from a pure culture"],
    "beta": ["What is beta hemolysis", "What type of hemolysis surrounds the colonies on this"],
    "alpha": ["What does the name viridans refer to", "What does the change in the medium around"],
    "camp": ["What does a positive CAMP test look like", "A beta-hemolytic streptococcus is streaked toward"],
    "lancet": ["What is the cell morphology of Streptococcus pneumoniae", "A sputum Gram stain is shown"],
    "gonostain": ["What gives a presumptive identification of gonorrhea", "A Gram stain of urethral pus is shown"],
    "impetigo": ["Which streptococcal skin infection forms a highly contagious crust", "Which streptococcal skin infection produces lesions like these"],
    "chains": ["A freshly isolated organism is Gram stained"],
    "catalase": ["Which test distinguishes staphylococci from streptococci", "A Gram-positive coccus bubbles vigorously",
                 "How do streptococci react in the catalase test"],
    "coagulase": ["Which enzyme, produced by 97% of human isolates", "After a positive catalase test"],
    "hominis": ["Where does Staphylococcus hominis live", "Why do the armpits and groin suit"],
    "sapro": ["Which staphylococcus infrequently lives", "Which infection may Staphylococcus saprophyticus"],
    "bacitracin": ["A beta-hemolytic streptococcus is bacitracin sensitive", "Which beta-hemolytic streptococci are bacitracin resistant"],
    "attach": ["What enhances the attachment of Neisseria", "Which gonococcal surface structures"],
    "endotoxin": ["Which of these is a virulence factor of Neisseria meningitidis", "What causes the hemorrhage and shock"],
    "msa": ["Staphylococcus aureus grows on a selective medium", "On which medium do streptococci grow poorly"],
    "tsst": ["What does toxic shock syndrome toxin induce", "In females, staphylococcal toxic shock"],
    "mprotein": ["What does M-protein contribute", "Which Streptococcus pyogenes surface antigen contributes most"],
    "gbsscreen": ["What is the preventive step against group B", "A pregnant woman is expected to deliver vaginally"],
    "humanonly": ["What is the reservoir of Streptococcus pyogenes", "Which streptococcus is strictly a human parasite"],
    "candle": ["How are the pathogenic Neisseria cultured", "What does a candle jar provide"],
    "military": ["Where has Acinetobacter baumannii become", "A 26-year-old soldier evacuated"],
    "viridansentry": ["How do viridans streptococci usually gain entrance", "A 62-year-old with pre-existing heart valve disease"],
}

# MUST: every set carries one question from each of these groups. They are the facts the
# lecturer HIGHLIGHTED in yellow on the slides (slides 3, 6, 17-18, 21, 23, 27/32, 38, 45, 57,
# 79) plus the one she flagged aloud ("this M protein, which you might also want to highlight").
MUST = {
    "gram (slide 3)": ["Why do staphylococci stain Gram-positive", "Gram-positive cells are described as physically strong",
                       "Which feature is true of every staphylococcus"],
    "catalase (slides 17-18, 21)": DUPS["catalase"],
    "hemolysis (slides 6, 23)": DUPS["beta"] + DUPS["alpha"] + ["Colonies of Staphylococcus aureus are grown on blood agar",
                                                               "Which of these is alpha hemolytic"],
    "coagulase": DUPS["coagulase"],
    "M-protein (audio)": DUPS["mprotein"],
    "humans only (slides 27, 32)": DUPS["humanonly"],
    "group B screening (slide 38)": DUPS["gbsscreen"],
    "viridans entry (slide 45)": DUPS["viridansentry"],
    "candle jar (slide 57)": DUPS["candle"],
    "Acinetobacter military (slide 79)": DUPS["military"],
    # Not highlighted, but the spine of each organism's story; without these a set can satisfy
    # every other constraint and still skip what the organism is known for.
    "S. aureus virulence": ["What does staphylokinase do", "How do the lipases", "Which Staphylococcus aureus toxin lyses",
                            "A newborn develops a bright red flush", "Staphylococcal food intoxication follows",
                            "What does toxic shock syndrome toxin induce", "In females, staphylococcal toxic shock"],
    "staphylococcal skin lesions": ["What is a carbuncle", "Which staphylococcal lesion is a boil"],
    "group B neonatal disease": ["Group B Streptococcus (Streptococcus agalactiae) is the most prevalent cause",
                                 "How does group B Streptococcus reach the newborn"],
    "group A sequelae": ["Which long-term complication of group A", "Which group A streptococcal sequela"],
    "streptococcal flowchart (slide 24)": DUPS["bacitracin"] + ["An alpha-hemolytic streptococcus is optochin sensitive"],
    "gonococcal presumptive diagnosis": DUPS["gonostain"],
    "meningococcal risk": ["Which setting raises the risk of meningococcal", "Which age groups carry a high risk"],
    # ~4.4 minutes of the recording, the second-largest single organism after group A
    "pneumococcus": ["What is the cell morphology of Streptococcus pneumoniae", "Streptococcus pneumoniae is capnophilic",
                     "Which media are required to culture Streptococcus pneumoniae", "Why may Streptococcus pneumoniae cultures die",
                     "What is the major virulence factor of Streptococcus pneumoniae", "What varies among the capsular types",
                     "Besides pneumococcal pneumonia", "How does Streptococcus pneumoniae reach the middle ear",
                     "How does pneumococcal pneumonia begin", "Pneumococcal infections are usually endogenous",
                     "Who is at greatest risk of Streptococcus pneumoniae", "Which pneumococcal vaccine is given",
                     "What problem now affects the traditional treatment of pneumococcal", "A sputum Gram stain is shown",
                     "An alpha-hemolytic streptococcus is optochin sensitive"],
    "pneumococcal capsule (slide 50)": ["What is the major virulence factor of Streptococcus pneumoniae",
                                        "What varies among the capsular types"],
}
MUST_MIN = {"S. aureus virulence": 2, "pneumococcus": 2}
MAX_WHERE = 4      # habitat stems ("Where does ... live?") are easy to over-select


def slide_of(q):
    return int(q["cite"].rsplit(" ", 1)[1])


def section(q):
    s = slide_of(q)
    return "staph" if s <= 20 else ("strep" if s <= 53 else "gneg")


def tag_dups(pool):
    for q in pool:
        q["_dup"] = None
    for g, prefixes in DUPS.items():
        for p in prefixes:
            hits = [q for q in pool if q["q"].startswith(p)]
            assert len(hits) == 1, "DUPS prefix %r matched %d questions" % (p, len(hits))
            hits[0]["_dup"] = g


def longest_is_correct(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= 8 and tl >= rn * 1.18


def uniquely_longest(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    return s[0][1] == q["c"] and s[0][0] > s[1][0]


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def must_missing(qs):
    stems = [q["q"] for q in qs]
    return [g for g, prefixes in MUST.items()
            if sum(1 for st in stems for p in prefixes if st.startswith(p)) < MUST_MIN.get(g, 1)]


def score(qs):
    orgs = Counter(o for q in qs for o in q["org"])
    must = len(must_missing(qs))
    where = max(0, sum(1 for q in qs if q["q"].startswith("Where")) - MAX_WHERE)
    missing = sum(1 for o in REQUIRED_ORGS if not orgs.get(o))
    sec = Counter(section(q) for q in qs)
    off = sum(abs(sec.get(k, 0) - v) for k, v in TARGET.items())
    io2 = sum(1 for q in qs if q["io"].startswith("2 "))
    io_pen = max(0, 6 - io2) + max(0, io2 - 9)
    dups = Counter(q["_dup"] for q in qs if q["_dup"])
    dup_pen = sum(n - 1 for n in dups.values() if n > 1)
    topics = Counter(q["topic"] for q in qs)
    lumpy = sum(max(0, n - 6) for n in topics.values())
    longest = 100.0 * sum(map(uniquely_longest, qs)) / len(qs)
    return (missing * 40 + must * 40 + dup_pen * 30 + off * 6 + io_pen * 8 + lumpy * 2 + where * 5
            + gameable_pct(qs) * 2.0 + max(0.0, longest - 30.0) * 1.0)


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
        if len(q["opts"]) != NOPT: bad.append((i, "not four options"))
        if q["c"] != 0: bad.append((i, "key not authored in position 0"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if not q.get("org"): bad.append((i, "missing org"))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        if not q["opts"][q["c"]][1].startswith("Correct"): bad.append((i, "key explanation must open with Correct"))
        for j, o in enumerate(q["opts"]):
            if len(o[1]) < 60:
                bad.append((i, "explanation under 60 chars: %r" % o[1][:50]))
            if j != q["c"] and o[1].startswith("Correct"):
                bad.append((i, "distractor explanation opens with Correct"))
        if len(set(o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"])) < NOPT - 1:
            bad.append((i, "two wrong choices share one explanation"))
        if "img" in q:
            p = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2", q["img"])
            if not os.path.exists(p): bad.append((i, "missing image " + q["img"]))
            if not q.get("alt") or not q.get("slide"): bad.append((i, "picture without alt/slide"))
    return bad


def search():
    n_text = len(TEXT)
    idx = list(range(n_text)); random.shuffle(idx)
    s1, s2 = idx[:30], idx[30:30 + 30 - N_IMG]
    rest = idx[30 + 30 - N_IMG:]
    im = list(range(len(IMGS))); random.shuffle(im)
    i2, irest = im[:N_IMG], im[N_IMG:]

    def total(s1, s2, i2):
        return score([TEXT[i] for i in s1]) + score([TEXT[i] for i in s2] + [IMGS[j] for j in i2])

    best = total(s1, s2, i2)
    for it in range(60000):
        move = random.random()
        a1, a2, ai, ar, airr = s1[:], s2[:], i2[:], rest[:], irest[:]
        if move < 0.4:                       # set1 <-> rest
            x, y = random.randrange(30), random.randrange(len(ar))
            a1[x], ar[y] = ar[y], a1[x]
        elif move < 0.75:                    # set2 text <-> rest
            x, y = random.randrange(len(a2)), random.randrange(len(ar))
            a2[x], ar[y] = ar[y], a2[x]
        elif move < 0.9:                     # set1 <-> set2
            x, y = random.randrange(30), random.randrange(len(a2))
            a1[x], a2[y] = a2[y], a1[x]
        else:                                # picture swap
            if not airr: continue
            x, y = random.randrange(len(ai)), random.randrange(len(airr))
            ai[x], airr[y] = airr[y], ai[x]
        t = total(a1, a2, ai)
        if t <= best:
            best, s1, s2, i2, rest, irest = t, a1, a2, ai, ar, airr
    return best, s1, s2, i2


def report(name, s):
    pos = Counter(q["c"] for q in s)
    orgs = Counter(o for q in s for o in q["org"])
    sec = Counter(section(q) for q in s)
    io2 = sum(1 for q in s if q["io"].startswith("2 "))
    print("%s  n=%d  positions A/B/C/D %s  gameable %.1f%%  uniquely-longest %.0f%%"
          % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)), gameable_pct(s),
             100.0 * sum(map(uniquely_longest, s)) / len(s)))
    print("      sections staph/strep/gneg %d/%d/%d  objective 2: %d  pictures: %d  organisms %d/%d"
          % (sec["staph"], sec["strep"], sec["gneg"], io2, sum(1 for q in s if "img" in q),
             sum(1 for o in REQUIRED_ORGS if orgs.get(o)), len(REQUIRED_ORGS)))
    missing = [o for o in REQUIRED_ORGS if not orgs.get(o)]
    assert not missing, "%s misses organisms %s" % (name, missing)
    mm = must_missing(s)
    assert not mm, "%s misses emphasized groups %s" % (name, mm)
    print("      emphasized groups %d/%d  habitat stems %d"
          % (len(MUST) - len(mm), len(MUST), sum(1 for q in s if q["q"].startswith("Where"))))
    d = Counter(q["_dup"] for q in s if q["_dup"])
    assert all(n == 1 for n in d.values()), "%s repeats a fact group: %s" % (name, d)


if __name__ == "__main__":
    pool = TEXT + IMGS
    print("pool: %d text + %d picture = %d" % (len(TEXT), len(IMGS), len(pool)))
    bad = validate(pool)
    print("schema problems:", bad or "none")
    assert not bad
    print("pool gameable: %.1f%%" % gameable_pct(pool))
    print("pool by section:", dict(Counter(section(q) for q in pool)),
          " objective 2:", sum(1 for q in pool if q["io"].startswith("2 ")))
    tag_dups(pool)
    for g, prefixes in MUST.items():
        for p in prefixes:
            assert sum(1 for q in pool if q["q"].startswith(p)) == 1, "MUST prefix %r" % p
    answer_text = {id(q): q["opts"][q["c"]][0] for q in pool}

    best, s1i, s2i, i2 = search()
    print("search score %.1f" % best)
    s1 = [TEXT[i] for i in s1i]
    s2 = [TEXT[i] for i in s2i] + [IMGS[j] for j in i2]
    # Lecture order: the picture questions fall among the text questions on their topic.
    s1 = sorted(s1, key=slide_of)
    s2 = sorted(s2, key=slide_of)
    assert not any("img" in q for q in s1), "a picture question reached Set 1"
    assert not set(map(id, s1)) & set(map(id, s2)), "a question is in both sets"
    s1, s2 = rotate(copy.deepcopy(s1)), rotate(copy.deepcopy(s2))
    for q in s1 + s2:
        orig = [p for p in pool if p["q"] == q["q"]][0]
        assert q["opts"][q["c"]][0] == answer_text[id(orig)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")
    report("SET 1", s1)
    report("SET 2", s2)

    def clean(qs):
        out = []
        for q in qs:
            d = {k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite")}
            for k in ("img", "alt", "slide"):
                if k in q: d[k] = q[k]
            out.append(d)
        return out
    json.dump({"set1": clean(s1), "set2": clean(s2)},
              open(os.path.join(HERE, "micro_l9_sets.json"), "w"), ensure_ascii=False, indent=1)
    print("\nwrote micro_l9_sets.json")
