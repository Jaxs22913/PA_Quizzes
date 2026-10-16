#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 13 pool into 2 x 30.

Miscellaneous Bacterial Agents of Disease (Dr. Fair, 16 October 2026; the PAJ5200.* deck names no lecturer,
the calendar row names Dr. Fair). One pool, tools/micro_l13_pool.py, written from the 70-slide deck.

THE SYLLABUS GIVES TWO NUMBERED OBJECTIVES, and objective 1 ("compare and contrast the morphology, medium,
laboratory tests, biochemical reactions, diseases, clinical manifestations, methods of treatment, and
prevention") is nearly the whole deck. So, as in Lectures 9 and 10, the objective tag is coarse and the real
coverage axis is the ORGANISM GROUP, carried in each question's topic field. Every set carries both objectives
(objective 2 = transmission, at least MIN_IO2 per set) and every organism group.

ORGANISM WEIGHTS ARE MINUTES SPOKEN (the 16 October 2026 recording, two parts, 49 + 10 minutes; Whisper and
Notability transcripts read), as Lectures 10 and 11 were. Dr. Fair signposts almost nothing, so time on
topic is the signal (transcript_emphasis_measurement): syphilis ~9.5 min, rickettsias ~6, dental disease ~6,
Lyme ~5, Vibrio cholerae ~4, seafood vibrios ~4, Helicobacter ~4, Campylobacter ~3, chlamydias ~3,
Coxiella/Bartonella ~2.5, relapsing fever ~2, spirochete features ~1.5, Leptospira ~1.2, mycoplasma ~1,
nonsyphilitic treponematoses ~0.8; his stories (Komodo dragons, about 5 minutes; the marriage-licence
blood test; the Weil-Felix trick) are not counted toward anything the slides lack. Scaled to 60, with
chlamydias held at 4 (the syllabus names Chlamydia and Chlamydophila). His two cues that point at slide
facts are carried by MUST_EACH / MUST_ANY below; "So remember that." (part 1, 43:40) is about who may name
a bacterium, not a slide fact, so it is not used. The syllabus appendix names Treponema pallidum, Borrelia,
Rickettsia, Ehrlichia, Anaplasma, Chlamydia, Chlamydophila, Helicobacter and the mycoplasmas; the deck
never names Anaplasma.

Four options. Length bias by selection; answer position by ROTATION per set. Set 1 is TEXT-ONLY, so it stays in
Group Study (build_group_quizzes.py drops a quiz holding any picture); Set 2 carries N_IMG picture questions.
Carries the house 60-character explanation guard, the "Correct" opener contract that
check_answer_key_consistency.py reads, and guards for the points the pool deliberately does not test.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l13_pool import POOL
from _option_order import ordered_kind

random.seed(20261016)
NOPT = 4
MIN_IO2 = 6
N_IMG = 3          # picture questions in Set 2 (Set 1 has none)

# SLIDE COUNTS per organism group, scaled to 60 questions (both sets together)
TARGET = {
    "Spirochete features": 2, "Syphilis": 10, "Nonsyphilitic treponematoses": 1, "Leptospira": 2,
    "Relapsing fever": 2, "Lyme disease": 6, "Vibrio cholerae": 4, "Seafood vibrios": 4,
    "Campylobacter": 3, "Helicobacter": 4, "Rickettsias": 7, "Coxiella & Bartonella": 3,
    "Chlamydias": 4, "Mycoplasma": 2, "Dental disease": 6,
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert ids, "stem not found: " + p
    return ids


# near-twins that give each other away or share their options: at most N per set
CLUSTERS = [
    (1, stem("How do spirochetes such as") + stem("In a spirochete, where do the endoflagella")),
    (2, stem("Which stage of syphilis begins") + stem("Weeks after a genital sore healed")
        + stem("Which feature belongs to secondary syphilis") + stem("In which stages of untreated syphilis")),
    (1, stem("Which lesions develop in tertiary") + stem("Which complications mark tertiary")
        + stem("This lesion appeared on the face")),
    (1, stem("Which pair of signs is classic for congenital") + stem("Teeth like these in a child")),
    (1, stem("How does a fetus acquire syphilis") + stem("By which routes is Treponema pallidum")),
    (1, stem("Which drug is named alongside doxycycline") + stem("Why might erythromycin or tetracycline")),
    (1, stem("Why is Treponema pallidum hard to culture") + stem("What do rickettsias need in order")),
    (1, stem("Weeks after a genital sore healed") + stem("A patient has this rash on both palms")),
    (1, stem("Which nonsyphilitic treponematosis is a superficial") + stem("Which treponematosis starts as")
        + stem("Which organism causes bejel")),
    (1, stem("How is leptospirosis mainly acquired") + stem("Which worker is at higher risk of leptospirosis")),
    (2, stem("Which shape identifies Leptospira") + stem("How do Borrelia cells differ")
        + stem("Which description fits Campylobacter") + stem("Which curviform genus is comma-shaped")),
    (1, stem("What drives the repeated cycles") + stem("In relapsing fever, what brings each bout")),
    (1, stem("In the Lyme disease tick cycle") + stem("How do newly hatched tick larvae")
        + stem("What role do humans play")),
    (1, stem("Which ticks transmit Lyme disease") + stem("Which vectors carry Rocky Mountain")),
    (1, stem("What is the bull's-eye rash") + stem("This rash appeared around the site")),
    (1, stem("What is the best prevention of Lyme") + stem("Which statement about Lyme disease vaccines")),
    (2, stem("What does cholera toxin cause") + stem("In cholera, which way do water")
        + stem("How does Vibrio cholerae infect")),
    (1, stem("Which part of cholera treatment") + stem("What is the best treatment option for seafood")
        + stem("What is the usual treatment for Campylobacter")),
    (1, stem("Which vibrio causes gastroenteritis from raw oysters")
        + stem("Which vibrio causes gastroenteritis from raw seafood")),
    (1, stem("Who is most at risk of infection with Campylobacter fetus")
        + stem("Which infections can Campylobacter fetus")),
    (1, stem("How does Helicobacter pylori survive") + stem("Helicobacter pylori's urease converts")
        + stem("Why does a gastric biopsy")),
    (1, stem("In which specimens was Helicobacter") + stem("For discovering which organism")),
    (1, stem("Which vector carries Rickettsia prowazekii") + stem("How is endemic typhus spread")
        + stem("Which vector transmits scrub typhus")),
    (1, stem("Which organism causes endemic (murine) typhus") + stem("Which organism causes Rocky Mountain")
        + stem("A camper who was bitten")),
    (1, stem("Which disease does Ehrlichia chaffeensis") + stem("How is human ehrlichiosis transmitted")),
    (2, stem("Which organism causes Q fever") + stem("How is Q fever usually acquired")
        + stem("Which group is at highest risk of Q fever") + stem("What does Q fever usually cause")),
    (2, stem("Which genus causes cat-scratch") + stem("How is trench fever spread")
        + stem("Which Bartonella disease occurs")),
    (1, stem("Which chlamydial form is the infectious") + stem("What does the chlamydial reticulate body")),
    (1, stem("Which Chlamydia trachomatis disease disfigures") + stem("Which chlamydial disease deforms")),
    (1, stem("Which organism causes ornithosis") + stem("How is ornithosis transmitted")),
    (1, stem("Why is penicillin not used against Mycoplasma") + stem("What do mycoplasmas require")
        + stem("Which description fits the shape of mycoplasmas")),
    (1, stem("Which bacterium is commonly found as dental plaque") + stem("How does dental plaque damage")),
    (1, stem("What is dental calculus") + stem("In the progression of dental disease")
        + stem("What is periodontitis") + stem("In periodontal disease, which bacteria")),
    (1, stem("What is the most common treatment for relapsing") + stem("Which drugs are most commonly used for Lyme")
        + stem("Why is tetracycline a treatment")),
]

# The points the pool deliberately does not test (see the pool header), asserted over the whole pool.
PCT = re.compile(r"\d+\s*(%|percent)|\bcases a year\b", re.I)
for q in POOL:
    key = q["opts"][q["c"]][0]
    assert not PCT.search(q["q"]) and not PCT.search(key), ("percentage or case count keyed", q["q"])
    assert not re.search(r"granulocytic", key, re.I), ("granulocytic ehrlichiosis keyed", q["q"])
    assert not re.search(r"Typhinia|Komodo|Montana", q["q"] + key, re.I), ("held point asked", q["q"])
    if q["topic"] == "Helicobacter":
        assert "spirochete" not in (q["q"] + key).lower(), ("Helicobacter-as-spirochete asked", q["q"])
    assert not ordered_kind([o[0] for o in q["opts"]]), ("numeric option set would be rotated", q["q"])


# His two cues that point at slide facts (16 October 2026, part 1; both in both transcripts):
#   "the Rickettsia take-home message is that they're very small, obligate intracellular parasites, and
#    they're primarily transmitted through arthropod bite." (41:53)  -> slides 43-44; every set carries a
#    rickettsia-feature item and a rickettsial arthropod-vector item
#   "The main thing, though, is that Rocky Mountain spotted fever looks exactly like measles." (42:54)
#    -> slide 50; the one measles item goes into one of the two sets
MUST_EACH = [
    stem("Which description fits Rickettsia") + stem("What do rickettsias need in order to be cultivated"),
    stem("Which vector carries Rickettsia prowazekii") + stem("How is endemic typhus spread")
        + stem("Which vectors carry Rocky Mountain") + stem("How is human ehrlichiosis transmitted")
        + stem("Which vector transmits scrub typhus"),
]
MUST_ANY = [stem("The early rash of Rocky Mountain spotted fever")]


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
            if not os.path.exists(os.path.join(os.path.dirname(HERE), "Microbiology Exam 2", q["img"])):
                bad.append((i, "image file missing: " + q["img"]))
            if not q.get("alt") or not q.get("slide"):
                bad.append((i, "picture question without alt or slide caption"))
    stems = [q["q"] for q in pool]
    for s in set(stems):
        if stems.count(s) > 1:
            bad.append((stems.index(s), "duplicate stem"))
    return bad


if __name__ == "__main__":
    print("pool:", len(POOL))
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

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l13_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l13_sets.json")
