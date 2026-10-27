#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 14 pool into 2 x 30.

Gram-Negative Bacilli of Medical Importance (Dr. Webster, 23 October 2026, 1-4 pm; the first lecture of Exam 3).
Pool A (tools/micro_l14_pool_a.py: endotoxin, the scheme and the aerobic nonenteric bacilli, slides 3-42) + pool B
(tools/micro_l14_pool_b.py: the enterics, Yersinia pestis, Pasteurella and Haemophilus, slides 43-101).

THE SYLLABUS GIVES TWO NUMBERED OBJECTIVES, and objective 1 ("compare and contrast the morphology, medium,
laboratory tests, biochemical reactions, diseases, clinical manifestations, methods of treatment, and prevention")
is nearly the whole deck. So, as in Lectures 10 and 13, the objective tag is coarse and the real coverage axis is
the ORGANISM GROUP in each question's topic field. Every set carries both objectives (objective 2 = transmission,
reservoir or source, at least MIN_IO2 per set) and every organism group weighted 2 or more. The syllabus appendix
lists eighteen organisms for this lecture (slides 3-4 reproduce it); every one is a topic below or inside one.

WEIGHTS ARE MINUTES SPOKEN (audio pass, 27 October 2026; transcript_emphasis_measurement). The recording is a
classmate's Notability export, three parts (46:13 + 45:19 + 32:12 = 2:03:43), one Whisper transcript only (no
Notability transcript to compare). Minutes per organism group, stories and outbreak tallies taken out: endotoxin 10,
sorting 3, Pseudomonas aeruginosa 14, its relatives 4, Brucella 3.5, Francisella 2, Bordetella 8, Legionella 8 (5 of
them outbreak stories), the enteric family, media and antigens 9, Escherichia coli and its four pathotypes 17,
other coliforms 7 (4 of them Serratia stories), Proteus and relatives 3.5, Salmonella 9 (2 Typhoid Mary), Shigella 5
(3 a laboratory story), enteric yersinias 1, Yersinia pestis 12 (5 outbreaks and history), Pasteurella 1,
Haemophilus 4; scaled to 60. Her one signpost: "There are four different strains of E. coli that you need to know.
Hint, hint, hint, hint." [1:04:18], so the four pathotypes get 14 of the 60 and EVERY set carries each pathotype
(MUST_EACH). She said "I'm not going to be testing on which antibiotics" [26:25], matching the pool's rule. The
slide 18 star ("cystic fibrosis***", which she repeated as "very, very, very common") stays in MUST_EACH.

Four options. Length bias by selection; answer position by ROTATION per set. Set 1 is TEXT-ONLY, so it stays in
Group Study (build_group_quizzes.py drops a quiz holding any picture); Set 2 carries N_IMG picture questions.
Carries the house 60-character explanation guard, the "Correct" opener contract that
check_answer_key_consistency.py reads, and guards for the points the pool deliberately does not test (pool A
header).
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l14_pool_a import POOL_A
from micro_l14_pool_b import POOL_B
from _option_order import ordered_kind

POOL = POOL_A + POOL_B
random.seed(20261023)
NOPT = 4
MIN_IO2 = 6
N_IMG = 4          # picture questions in Set 2 (Set 1 has none)
FOLDER = "Microbiology Exam 3"

# MINUTES SPOKEN per organism group (header), scaled to 60 questions (both sets together)
TARGET = {
    "Endotoxin": 4, "Classification": 2, "Pseudomonas aeruginosa": 5, "Pseudomonas relatives": 2,
    "Brucella": 2, "Francisella": 1, "Bordetella": 4, "Legionella": 2,
    "Enteric features": 3, "Escherichia coli": 2, "ETEC": 3, "EIEC": 3, "EPEC": 3, "EHEC": 5,
    "Other coliforms": 2, "Proteus & relatives": 2, "Salmonella": 3, "Shigella": 2, "Enteric Yersinia": 1,
    "Yersinia pestis": 5, "Pasteurella": 1, "Haemophilus": 3,
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert ids, "stem not found: " + p
    return ids


# near-twins that give each other away or share their options: at most N per set
CLUSTERS = [
    (1, stem("When is endotoxin released") + stem("Why can antibiotic therapy")),
    (2, stem("Which three properties") + stem("In the scheme for Gram-negative pathogens")
        + stem("Which Gram-negative rods belong to the aerobic group")),
    (1, stem("Which pigment gives") + stem("The colonies on this plate")),
    (1, stem("Which metabolic profile fits Pseudomonas") + stem("Which description fits Burkholderia")),
    (2, stem("In which hosts is Pseudomonas aeruginosa") + stem("Burkholderia cepacia is a particular problem")
        + stem("Why might a Pseudomonas aeruginosa vaccine")),
    (1, stem("How is melioidosis") + stem("Which organism causes melioidosis")),
    (2, stem("Which opportunist survives") + stem("Which opportunist forms biofilms")
        + stem("Why is Pseudomonas aeruginosa a frequent contaminant")),
    (1, stem("How do humans usually acquire brucellosis") + stem("Which animals carry Brucella")),
    (1, stem("Why is brucellosis called undulant") + stem("Tularemia is also known")),
    (2, stem("Which form of vaccine is available for brucellosis") + stem("Which vaccines give temporary protection")
        + stem("Which kind of vaccine prevents Haemophilus") + stem("What does the acellular pertussis vaccine")),
    (1, stem("Which test is used to diagnose brucellosis") + stem("How is plague diagnosed")
        + stem("How is enteroinvasive Escherichia coli diagnosed")),
    (1, stem("What does Bordetella pertussis bind") + stem("Why does mucus build up")),
    (1, stem("Why is pertussis incidence highest") + stem("What does the age pattern")),
    (1, stem("How is Bordetella pertussis transmitted") + stem("What is the reservoir of Bordetella pertussis")),
    (1, stem("With which organisms does Legionella") + stem("How is legionellosis transmitted")),
    (2, stem("In which hosts is Pseudomonas aeruginosa") + stem("Which people are most prone to Legionnaires")
        + stem("Serratia marcescens pneumonia is typical") + stem("Which patients are at risk of septicemia")),
    (1, stem("Which traits do ALL members") + stem("What divides the Enterobacteriaceae")),
    (1, stem("What makes MacConkey's") + stem("What does eosin methylene blue")),
    (1, stem("Which surface antigen of the enterics") + stem("Which surface antigen do ALL")
        + stem("What do the O157 and H7")),
    (1, stem("In toxigenic diarrheal disease") + stem("The diagram shows enteric bacteria invading")),
    (1, stem("Which enteric is a true pathogen") + stem("Which non-lactose-fermenting enterics are TRUE")),
    (1, stem("Which pair of toxins") + stem("How do the toxins of enterotoxigenic")),
    (1, stem("Enterotoxigenic Escherichia coli is the leading cause")
        + stem("Enteropathogenic Escherichia coli is the leading cause")),
    (1, stem("Which infection does enteroinvasive") + stem("Which pair of findings marks enteroinvasive")),
    (2, stem("How does enteroinvasive Escherichia coli damage") + stem("How does enteropathogenic Escherichia coli damage")
        + stem("How do the toxins of enterotoxigenic") + stem("How does the Shiga toxin")),
    (1, stem("Which complication of enterohemorrhagic") + stem("Why is antibiotic therapy approached")),
    (1, stem("What is the reservoir of Escherichia coli O157") + stem("Which foods transmit")),
    (1, stem("The chromogenic agar shown") + stem("Why do Escherichia coli O157:H7 colonies")),
    (1, stem("Which coliform has a large capsule") + stem("The capsule stain shows")),
    (1, stem("Which enteric produces the red pigment") + stem("Serratia marcescens pneumonia")),
    (1, stem("Which finding on agar is diagnostic") + stem("Which genus produces the wavelike")),
    (1, stem("Who are the hosts of Salmonella typhi") + stem("How is Salmonella typhi usually acquired")),
    (2, stem("Which sources spread the animal salmonelloses") + stem("Salmonella cholerae-suis")
        + stem("How do the salmonelloses other than typhoid")),
    (1, stem("How is Salmonella typhi usually acquired") + stem("How is Shigella transmitted")),
    (1, stem("Which condition can Yersinia enterocolitica") + stem("How does Yersinia pseudotuberculosis")),
    (1, stem("Which staining feature does Yersinia pestis") + stem("The tiny Gram-negative rods among")),
    (1, stem("How does an infected flea") + stem("What makes a plague-infected flea")),
    (2, stem("What is the bubo") + stem("Which form of plague is highly contagious") + stem("Why is septicemic plague")),
    (1, stem("What distinguishes sylvatic") + stem("Where in the United States")),
    (1, stem("How is Pasteurella multocida usually acquired") + stem("Which patients are at risk of septicemia")),
    # audio-pass pathotype items
    (1, stem("Which Escherichia coli pathotype damages the intestine without") + stem("How does enteroinvasive Escherichia coli damage")),
    (1, stem("Which Escherichia coli pathotype produces Shiga") + stem("How does the Shiga toxin")),
    (1, stem("Which part of the bowel does enteroinvasive") + stem("Which infection does enteroinvasive")),
    (1, stem("Uptake of which vitamin") + stem("How does enteropathogenic Escherichia coli damage")),
    (2, stem("Which Haemophilus species causes chancroid") + stem("How is the acute conjunctivitis")
        + stem("Which disease was Haemophilus influenzae")),
]

# EACH: every set carries one of the group. ANY: the pair of sets carries it at least once.
MUST_EACH = [
    # the deck's own emphasis: slide 18 stars "cystic fibrosis***"
    stem("In which hosts is Pseudomonas aeruginosa") + stem("Burkholderia cepacia is a particular problem")
    + stem("Why might a Pseudomonas aeruginosa vaccine"),
    # the scheme the whole lecture hangs on (slides 12-13, Table 20.1)
    stem("Which three properties") + stem("In the scheme for Gram-negative pathogens")
    + stem("Which Gram-negative rods belong to the aerobic group"),
    # Haemophilus influenzae itself, a syllabus organism: chocolate agar, the misnomer, the Hib vaccine
    stem("Why is Haemophilus grown on chocolate agar") + stem("Which disease was Haemophilus influenzae")
    + stem("Which kind of vaccine prevents Haemophilus"),
] + [
    # "four different strains of E. coli that you need to know. Hint, hint, hint, hint." [1:04:18]
    [i for i, q in enumerate(POOL) if q["topic"] == t] for t in ("ETEC", "EIEC", "EPEC", "EHEC")
]
# The slides' core facts that a random draw could leave out, then (audio pass) what the recording dwelt on.
MUST_ANY = [
    stem("How does an infected flea") + stem("What makes a plague-infected flea"),        # plague's vector (IO2)
    stem("What is the bubo"),                                                          # the classic sign
    stem("Which stage of pertussis"),                                                  # the whoop
    stem("What does the acellular pertussis vaccine") + stem("Why is pertussis incidence highest")
        + stem("What does the age pattern"),                                           # vaccination
    stem("Which extraintestinal infection does Escherichia coli") + stem("In water testing"),
    stem("How is Pasteurella multocida usually acquired"),
    stem("How is Salmonella typhi usually acquired") + stem("Who are the hosts of Salmonella typhi"),
    # audio pass
    stem("Why can antibiotic therapy") + stem("When is endotoxin released"),   # "you feel a whole lot worse" [1:11]
    stem("How is legionellosis transmitted"),                                  # cooling towers, the fountain [47:29-53:27]
    stem("How do humans usually acquire brucellosis"),                         # raw milk, "pasteurization is a good thing" [33:34]
    stem("From which organ do some chronic carriers"),                         # Typhoid Mary [1:33:46]
    stem("Which infection is typical of Pseudomonas"),                         # swimmer's ear, contact lens care [25:14]
    stem("How is plague diagnosed"),                                           # "you have to diagnose it quickly" [1:53:30]
]

# The points the pool deliberately does not test (pool A header), asserted over the whole pool.
PCT = re.compile(r"\d+\s*(%|percent)|\bcases (a|per) year\b|\binfective dose\b", re.I)
ABX_ASK = re.compile(r"\b(which|what) (antibiotic|drug|antimicrobial)s?\b|\btreated with which\b", re.I)
DOSE = re.compile(r"\b\d+\s*(mg|milligrams?)\b", re.I)
for q in POOL:
    key = q["opts"][q["c"]][0]
    both = q["q"] + " " + key
    assert not PCT.search(both), ("percentage, case count or dose keyed", q["q"])
    assert not ABX_ASK.search(q["q"]), ("asks which antibiotic", q["q"])
    assert not DOSE.search(" ".join(o[0] + " " + o[1] for o in q["opts"])), ("a dose appears", q["q"])
    assert not re.search(r"oxidase[- ]positive|\bmotile\b", key, re.I) or q["topic"] != "Pseudomonas relatives", \
        ("slide 21's motile, oxidase-positive line keyed", q["q"])
    assert not (re.search(r"Serratia|Hafnia", both) and re.search(r"lactose|coliform", both)), \
        ("Serratia or Hafnia lactose status asked (slides 12/47 against 50/68)", q["q"])
    assert not (re.search(r"parainfluenzae", key) and re.search(r"meningitis", q["q"], re.I)), \
        ("slide 97's H. parainfluenzae meningitis keyed", q["q"])
    assert not re.search(r"\bWHO\b|World Health Organization|top 3 critical", both), ("WHO list keyed", q["q"])
    assert not ordered_kind([o[0] for o in q["opts"]]), ("numeric option set would be rotated", q["q"])


def lens(q): return [len(o[0]) for o in q["opts"]]


def longest_is_correct(q):
    s = sorted(((l, i) for i, l in enumerate(lens(q))), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= 8 and tl >= rn * 1.18


def uniquely_longest(q):
    L = lens(q); c = L[q["c"]]
    return c > max(L[:q["c"]] + L[q["c"] + 1:])


def uniquely_shortest(q):
    L = lens(q); c = L[q["c"]]
    return c < min(L[:q["c"]] + L[q["c"] + 1:])


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_IOS = set(q["io"] for q in POOL)
IO2_KEY = [io for io in ALL_IOS if io.startswith("2 ")][0]


def score(idx, set_no):
    qs = [POOL[i] for i in idx]
    top = Counter(q["topic"] for q in qs)
    s = 0.0
    for t, n in TARGET.items():
        d = abs(top.get(t, 0) - n / 2.0)
        s += max(0.0, d - 0.5) * 12       # within half a question of target is free
        if n >= 2 and top.get(t, 0) == 0:
            s += 40                        # every weighted group in every set
    ios = Counter(q["io"] for q in qs)
    s += max(0, MIN_IO2 - ios.get(IO2_KEY, 0)) * 15
    s += gameable_pct(qs) * 3.0
    longest = 100.0 * sum(map(uniquely_longest, qs)) / len(qs)
    shortest = 100.0 * sum(map(uniquely_shortest, qs)) / len(qs)
    s += max(0.0, longest - 30.0) + max(0.0, shortest - 35.0)
    pics = sum(1 for q in qs if q.get("img"))
    s += (pics * 200) if set_no == 1 else abs(pics - N_IMG) * 30
    ids = set(idx)
    for n, cl in CLUSTERS:
        s += max(0, len(ids & set(cl)) - n) * 30
    for g in MUST_EACH:
        if not ids & set(g):
            s += 50
    return s


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
        if not (0 <= q["c"] < NOPT): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        for j, o in enumerate(q["opts"]):
            if len(o[1]) < 60:
                bad.append((i, "explanation under 60 chars: %r" % o[1][:40]))
            opens = o[1].lstrip().lower().startswith("correct")
            if (j == q["c"]) != opens:
                bad.append((i, "the 'Correct' opener must mark exactly the key"))
        wrong = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if len(set(wrong)) == 1:
            bad.append((i, "every wrong choice shares one explanation"))
        mis = q.get("mis") or {}
        if set(mis) != set(o[0] for j, o in enumerate(q["opts"]) if j != q["c"]):
            bad.append((i, "`mis` must name exactly the three distractors"))
        if not q["q"].rstrip().endswith("?"):
            bad.append((i, "stem does not ask a question"))
        if q.get("img"):
            if not os.path.exists(os.path.join(os.path.dirname(HERE), FOLDER, q["img"])):
                bad.append((i, "image file missing: " + q["img"]))
            if not q.get("alt") or not q.get("slide"):
                bad.append((i, "picture question without alt or slide caption"))
    stems = [q["q"] for q in pool]
    for s in set(stems):
        if stems.count(s) > 1:
            bad.append((stems.index(s), "duplicate stem"))
    return bad


if __name__ == "__main__":
    print("pool:", len(POOL), " (A %d, B %d)" % (len(POOL_A), len(POOL_B)))
    probs = validate(POOL)
    print("schema problems:", probs or "none")
    assert not probs, "fix the pool before partitioning"
    for t in TARGET:
        assert any(q["topic"] == t for q in POOL), "no question for " + t
    extra = set(q["topic"] for q in POOL) - set(TARGET)
    assert not extra, extra
    print("objectives:", len(ALL_IOS), " pool per objective:",
          dict(sorted(Counter(q["io"].split(" ")[0] for q in POOL).items())))
    print("pool per group:", dict(Counter(q["topic"] for q in POOL)))
    print("pool gameable: %.0f%%   pool key uniquely longest: %.0f%%"
          % (gameable_pct(POOL), 100.0 * sum(map(uniquely_longest, POOL)) / len(POOL)))
    for q in POOL:
        if longest_is_correct(q):
            print("   gameable in pool:", q["q"][:90])

    def total(ch):
        return score(ch[:30], 1) + score(ch[30:], 2) + sum(50 for g in MUST_ANY if not set(ch) & set(g))

    best, idx = None, list(range(len(POOL)))
    for _ in range(400):
        random.shuffle(idx)
        ch = idx[:60]
        t = total(ch)
        if best is None or t < best[0]:
            best = (t, list(ch))
    cur_t, cur = best
    for _ in range(100000):
        out = [i for i in range(len(POOL)) if i not in set(cur)]
        k = random.randrange(60)
        cand = list(cur)
        if random.random() < 0.5 and out:
            cand[k] = random.choice(out)            # swap in an unused question
        else:
            j = random.randrange(60)                # move one across the sets
            cand[k], cand[j] = cand[j], cand[k]
        t = total(cand)
        if t <= cur_t:
            cur_t, cur = t, cand
    print("selection score: %.1f" % cur_t)

    ch = cur
    s1 = rotate([json.loads(json.dumps(POOL[i])) for i in ch[:30]])
    s2 = rotate([json.loads(json.dumps(POOL[i])) for i in ch[30:]])
    texts = [POOL[i]["opts"][POOL[i]["c"]][0] for i in ch]
    for q, want in zip(s1 + s2, texts):
        assert q["opts"][q["c"]][0] == want, "rotation moved an answer!"
        assert q["opts"][q["c"]][1].startswith("Correct"), "key lost its Correct opener"
    print("rotation check: every correct answer still points at its own text\n")

    assert not set(ch[:30]) & set(ch[30:]), "a question landed in both sets"
    assert not any(q.get("img") for q in s1), "a picture question reached Set 1"
    for g in MUST_EACH:
        assert set(ch[:30]) & set(g) and set(ch[30:]) & set(g), "a set misses: " + POOL[g[0]]["q"]
    for g in MUST_ANY:
        assert set(ch) & set(g), "a flagged item is in neither set: " + POOL[g[0]]["q"]
    for name, s, part in (("SET 1", s1, ch[:30]), ("SET 2", s2, ch[30:])):
        assert set(q["io"] for q in s) == ALL_IOS, "%s misses an objective" % name
        assert sum(1 for q in s if q["io"] == IO2_KEY) >= MIN_IO2, "%s has too few objective-2 items" % name
        top = Counter(q["topic"] for q in s)
        for t, n in TARGET.items():
            if n >= 2:
                assert top.get(t, 0) >= 1, "%s has no %s question" % (name, t)
        for n, cl in CLUSTERS:
            assert len(set(part) & set(cl)) <= n, "%s carries too many of a twin cluster" % name
        pos = Counter(q["c"] for q in s)
        assert max(pos.values()) <= 9, "%s answer positions skewed %s" % (name, pos)
        assert gameable_pct(s) < 10, "%s length-gameable %.0f%%" % (name, gameable_pct(s))
        print("   per group:", ", ".join("%s %d" % (t, top.get(t, 0)) for t in TARGET))
        print("%s  n=%d  positions A/B/C/D %s  key uniquely longest %.0f%%  uniquely shortest %.0f%%"
              "  gameable %.0f%%  objective 2: %d  pictures: %d"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 100.0 * sum(map(uniquely_longest, s)) / len(s),
                 100.0 * sum(map(uniquely_shortest, s)) / len(s),
                 gameable_pct(s), sum(1 for q in s if q["io"] == IO2_KEY),
                 sum(1 for q in s if q.get("img"))))
    assert sum(1 for q in s2 if q.get("img")) == N_IMG, "Set 2 should carry %d pictures" % N_IMG

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l14_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l14_sets.json")
