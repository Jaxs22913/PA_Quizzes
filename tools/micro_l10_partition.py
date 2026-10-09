#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 10 pool into 2 x 30.

Gram-Positive Bacilli of Medical Importance (Dr. Webster, 2 October 2026; the
deck file is named "Lecture 9 Dr. Webster ...", the calendar row and the
recording make it Lecture 10). Pool A (spore-formers, slides 4-49) + pool B
(non-spore-formers, slides 50-94).

THE SYLLABUS GIVES TWO NUMBERED OBJECTIVES, and objective 1 ("compare and
contrast the morphology, medium, laboratory tests, biochemical reactions,
diseases, clinical manifestations, methods of treatment, and prevention") is
nearly the whole deck. So, as in Lecture 8, the objective tag is coarse and the
real coverage axis is the ORGANISM, carried in each question's topic field.
Every set must carry both objectives (objective 2 = transmission, at least
MIN_IO2 per set) and every organism group the recording did not exclude.

ORGANISM WEIGHTS ARE MINUTES SPOKEN, measured from the timestamps of our own
transcript of both parts (46:25 + 43:40; the recording starts at slide 6, so the
scheme slides 4-5 carry no audio):
    Bacillus anthracis 11.7  botulism 8.7  tuberculosis 9.3  leprosy 7.6
    C. perfringens (wound + food) 7.2  Listeria 6.5  C. difficile 5.9
    diphtheria 4.8  genus/scheme/spores ~4  B. cereus 4.2  tetanus 3.8
    Cutibacterium 3.2  Actinomyces + Nocardia 3.2  mycobacteria general 2.2
    Lactobacillus 2.1
Not weighted, because she excluded them: Erysipelothrix (0.9 min, "not going
to worry too much about"), the non-tuberculous mycobacteria (2.1 min, "don't
worry about being tested"). TARGET below is that table scaled to 60 and
rounded, then split evenly across the two sets.

Four options. Length bias by selection; answer position by ROTATION. Carries
the house 60-character explanation guard, the "Correct" opener contract that
check_answer_key_consistency.py reads, and a guard that no question is keyed
on a percentage (her stated rule) or asks which antibiotic to use.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l10_pool_a import POOL_A
from micro_l10_pool_b import POOL_B

POOL = POOL_A + POOL_B
random.seed(20261002)
NOPT = 4
MIN_IO2 = 6

# minutes spoken, scaled to 60 questions (both sets together)
TARGET = {
    "Classification": 5, "Bacillus anthracis": 8, "Bacillus cereus": 3,
    "Clostridium perfringens": 5, "Clostridium tetani": 4, "Clostridium botulinum": 6,
    "Clostridioides difficile": 4, "Lactobacillus": 1, "Listeria": 4,
    "Corynebacterium": 4, "Cutibacterium": 2, "Mycobacteria": 2,
    "Tuberculosis": 6, "Leprosy": 4, "Actinomyces & Nocardia": 2,
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())

# near-twins that give each other away, or share their options: at most N per set
def stem(p): return [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
CLUSTERS = [
    (1, stem("Which pair of traits describes the genus")),
    (1, stem("Which spore positions distinguish") + stem("Judging by where the spores sit")),
    (1, stem("What does tetanospasmin block") + stem("What is the clinical result of tetanospasmin")),
    (1, stem("How does botulinum toxin cause paralysis") + stem("Which pattern of paralysis does botulism")),
    (1, stem("Why does human tetanus immune globulin") + stem("What does diphtheria antitoxin")),
    (1, stem("Which cell wall component do Corynebacterium") + stem("Which wall components make mycobacteria")),
    (1, stem("Which is a cause of a false-positive") + stem("Why can a patient with acquired immunodeficiency")),
    (1, stem("Abdominal actinomycosis") + stem("Cervicofacial actinomycosis") + stem("Uterine actinomycosis")),
    (2, stem("How does infant botulism arise") + stem("Which food is a classic source of infant")
        + stem("What syndrome does the infant shown")),
    (2, stem("What does protective antigen") + stem("At high levels, what does anthrax lethal")
        + stem("How does anthrax toxin produce")),
    (1, stem("How is cutaneous anthrax acquired") + stem("What is the lesion shown on this man's jaw")),
    (1, stem("What makes a Gram-positive bacillus 'regular'") + stem("What makes a Gram-positive bacillus 'irregular'")),
    (1, stem("Which form of leprosy produces shallow") + stem("Which condition produces the facial")),
    (1, stem("How does Clostridium perfringens food poisoning compare")
        + stem("In Clostridium perfringens gastroenteritis")),
]
for n, ids in CLUSTERS:
    assert len(ids) >= 2, ("cluster stem not found", ids)

# What she flagged out loud must be asked. EACH: every set carries one of the
# group. ANY: the pair of sets carries it at least once.
MUST_EACH = [
    # "you need to know: bacillus centrally located, Clostridium terminally" [1, 21:16]
    stem("Which spore positions distinguish") + stem("Judging by where the spores sit"),
    # "you need to know the different forms ... the most common, what's the deadliest" [1, 8:49; 12:34]
    stem("Which is the most common form of anthrax") + stem("Which form of anthrax is the most deadly"),
    # "how the different things work": the two clostridial neurotoxins
    stem("What does tetanospasmin block") + stem("How does botulinum toxin cause paralysis"),
    # the pseudomembrane, "very characteristic ... that you should know" [2, 13:48]
    stem("Which finding is characteristic of respiratory diphtheria") + stem("The gray-white membrane shown"),
]
MUST_ANY = [
    stem("Which is the most common form of anthrax"),
    stem("Which form of anthrax is the most deadly"),
    stem("What does tetanospasmin block"),
    stem("How does botulinum toxin cause paralysis"),
    stem("Which organism most commonly causes gas gangrene"),       # "the one I would want you to know"
    stem("How does a mixed infection help myonecrosis"),           # "underline this"
    stem("What syndrome does the infant shown"),                    # "remember floppy baby syndrome"
    stem("Into which three divisions is clinical tuberculosis"),    # "three different stages that you need to know"
    stem("What is the current name of Propionibacterium"),          # "you need to know the new name"
    stem("When does Actinomyces israelii cause disease"),           # "this is one that you should know"
]
for g in MUST_EACH + MUST_ANY:
    assert g, "a must-ask stem was not found"

# Her two scope rules, asserted over the whole pool.
PCT = re.compile(r"\d+\s*(%|percent)|\bmortality rate\b", re.I)
ABX_ASK = re.compile(r"\b(which|what) (antibiotic|drug)s? (is|are) (used|given|chosen|preferred)\b"
                     r"|\btreated with which\b", re.I)
for q in POOL:
    key = q["opts"][q["c"]][0]
    assert not PCT.search(q["q"]) and not PCT.search(key), ("percentage keyed", q["q"])
    assert not ABX_ASK.search(q["q"]), ("asks which antibiotic", q["q"])
    assert "Erysipelothrix" not in q["q"] and "Erysipelothrix" not in key, ("Erysipelothrix keyed", q["q"])


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


def score(idx):
    qs = [POOL[i] for i in idx]
    top = Counter(q["topic"] for q in qs)
    s = 0.0
    for t, n in TARGET.items():
        want = n / 2.0
        d = abs(top.get(t, 0) - want)
        s += max(0.0, d - 0.5) * 12       # within half a question of target is free
        if n >= 2 and top.get(t, 0) == 0:
            s += 40                        # every weighted organism in every set
    ios = Counter(q["io"] for q in qs)
    s += max(0, MIN_IO2 - ios.get(IO2_KEY, 0)) * 15
    s += gameable_pct(qs) * 3.0
    longest = 100.0 * sum(map(uniquely_longest, qs)) / len(qs)
    shortest = 100.0 * sum(map(uniquely_shortest, qs)) / len(qs)
    s += max(0.0, longest - 30.0) * 1.0 + max(0.0, shortest - 35.0) * 1.0
    pics = sum(1 for q in qs if q.get("img"))
    s += abs(pics - 4) * 4
    ids = set(idx)
    for n, cl in CLUSTERS:
        s += max(0, len(ids & set(cl)) - n) * 30
    for g in MUST_EACH:
        if not ids & set(g):
            s += 50
    return s


def must_any_penalty(ch):
    ids = set(ch)
    return sum(50 for g in MUST_ANY if not ids & set(g))


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
            if not o[1].strip(): bad.append((i, "option unexplained"))
            opens = o[1].lstrip().lower().startswith("correct")
            if (j == q["c"]) != opens:
                bad.append((i, "the 'Correct' opener must mark exactly the key"))
        wrong = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if len(set(wrong)) == 1:
            bad.append((i, "every wrong choice shares one explanation"))
        if q.get("img"):
            if not os.path.exists(os.path.join(os.path.dirname(HERE), "Microbiology Exam 2", q["img"])):
                bad.append((i, "image file missing: " + q["img"]))
            if not q.get("alt") or not q.get("slide"):
                bad.append((i, "picture question without alt or slide caption"))
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
          dict(Counter(q["io"].split(" ")[0] for q in POOL)))
    print("pool gameable: %.0f%%   pool key uniquely longest: %.0f%%"
          % (gameable_pct(POOL), 100.0 * sum(map(uniquely_longest, POOL)) / len(POOL)))
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    def total(ch):
        return score(ch[:30]) + score(ch[30:]) + must_any_penalty(ch)

    best, idx = None, list(range(len(POOL)))
    for _ in range(400):
        random.shuffle(idx)
        ch = idx[:60]
        t = total(ch)
        if best is None or t < best[0]:
            best = (t, list(ch))
    cur_t, cur = best
    for _ in range(80000):
        out = [i for i in range(len(POOL)) if i not in set(cur)]
        k = random.randrange(60)
        cand = list(cur)
        if random.random() < 0.5:
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
    for g in MUST_ANY:
        assert set(ch) & set(g), "a flagged item is in neither set: " + POOL[g[0]]["q"]
    for g in MUST_EACH:
        assert set(ch[:30]) & set(g) and set(ch[30:]) & set(g), "a set misses: " + POOL[g[0]]["q"]
    for name, s, part in (("SET 1", s1, ch[:30]), ("SET 2", s2, ch[30:])):
        assert set(q["io"] for q in s) == ALL_IOS, "%s misses an objective" % name
        top = Counter(q["topic"] for q in s)
        for t, n in TARGET.items():
            if n >= 2:
                assert top.get(t, 0) >= 1, "%s has no %s question" % (name, t)
        for n, cl in CLUSTERS:
            assert len(set(part) & set(cl)) <= n, "%s carries too many of a twin cluster" % name
        pos = Counter(q["c"] for q in s)
        assert max(pos.values()) <= 9, "%s answer positions skewed %s" % (name, pos)
        print("   per organism:", ", ".join("%s %d" % (t, top.get(t, 0)) for t in TARGET))
        print("%s  n=%d  positions A/B/C/D %s  key uniquely longest %.0f%%  uniquely shortest %.0f%%"
              "  gameable %.0f%%  objective 2: %d  pictures: %d"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 100.0 * sum(map(uniquely_longest, s)) / len(s),
                 100.0 * sum(map(uniquely_shortest, s)) / len(s),
                 gameable_pct(s), sum(1 for q in s if q["io"] == IO2_KEY),
                 sum(1 for q in s if q.get("img"))))

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l10_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l10_sets.json")
