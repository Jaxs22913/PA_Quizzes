#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 11 pool into 2 x 30.

Novel Antimicrobial Therapy (Dr. Fair, 9 October 2026; the deck names no lecturer, slide 30
credits "Photos: D. Fair", the calendar row names Dr. Fair, and the recording is hers). One pool,
tools/micro_l11_pool.py, written from the 34-slide deck.

The syllabus gives FOUR numbered objectives and every set carries all four. Within objective 1 the
coverage axis is the topic field (stewardship, resistance, susceptibility testing, empiric therapy,
prophylaxis, adverse effects).

TOPIC WEIGHTS ARE MINUTES SPOKEN (see TARGET), measured from the timestamps of our own transcript of
the 45:42 recording, scaled to 60 questions and split evenly across the two sets.

Four options. Length bias by selection; answer position by ROTATION. Carries the house 60-character
explanation guard and the "Correct" opener contract that check_answer_key_consistency.py reads. The
one picture question goes to SET 2 only: a quiz holding any picture question is dropped from Group
Study by build_group_quizzes.py, so Set 1 stays text-only (the Lecture 9 rule).
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l11_pool import POOL

random.seed(20261009)
NOPT = 4
N_IMG = 1          # picture questions in Set 2 (Set 1 has none)

# MINUTES SPOKEN in the 45:42 recording (timestamps of both transcripts), substance only: stewardship and the
# six facts 3.3, Fleming + resistance timeline + superbugs 3.7, disk diffusion + antibiogram 3.4, empiric 1.1,
# special circumstances 3.1, adverse effects 1.5, non-antibiotic options 2.4, phage biology 3.5, phage therapy
# 4.6, fecal transplant 6.2, herbs/spices/essential oils 3.2 (36 min). Not weighted: the parasitic-worm aside
# (34:45-40:39, about 6 min, almost none of it on the slide), the garden photos (about 2 min), the supervillain
# and acronym jokes. Scaled to 60 and rounded:
TARGET = {
    "Drivers & stewardship": 6, "Resistance & superbugs": 6, "Susceptibility testing": 6,
    "Empiric therapy": 2, "Prophylaxis": 5, "Adverse effects": 3,
    "Non-antibiotic options": 4, "Diet & plant oils": 5,
    "Phage biology": 6, "Phage therapy": 7, "Fecal microbiota transplant": 10,
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert ids, "stem not found: " + p
    return ids


# near-twins that give each other away (one explanation states the other's answer): at most N per set
CLUSTERS = [
    (1, stem("In antimicrobial stewardship, which step") + stem("In the stewardship cycle, what should")
        + stem("Which step closes the antimicrobial")),
    (1, stem("Clinically inappropriate antibiotic") + stem("Antimicrobial stewardship works mainly")),
    (2, stem("Antibiotics are effective against") + stem("Which statement about sore throats")
        + stem("Which statement about ear infections") + stem("A parent asks for an antibiotic")),
    (1, stem("In a disk diffusion (Kirby-Bauer) test, what") + stem("In these disk diffusion plates")),
    (1, stem("What is an antibiogram") + stem("What is a hospital antibiogram mainly")),
    (1, stem("Which is a limitation of an antibiogram") + stem("Which information does a standard antibiogram")),
    (2, stem("What defines empiric") + stem("What is empiric antibiotic therapy based")
        + stem("Which patients most commonly receive empiric")),
    (1, stem("Which patient fits the high-risk group") + stem("How has antibiotic prophylaxis before dental")),
    (1, stem("Which is a DIRECT adverse effect") + stem("Which is listed as an indirect adverse")
        + stem("An antibiotic does not clear")),
    (1, stem("Which non-antimicrobial option gives") + stem("What is convalescent plasma")),
    (1, stem("Lactobacillus and Saccharomyces") + stem("Which foods are a common natural source")),
    (1, stem("What kind of antibacterial activity have plant") + stem("What is still needed before plant")),
    (1, stem("According to one hypothesis about cooking") + stem("Which is one of the hypotheses for why herbs")),
    (1, stem("What is a bacteriophage") + stem("Which cells do bacteriophages attack")),
    (1, stem("Before phage therapy can be used") + stem("Which is a drawback of phage therapy")),
    (1, stem("Which regulatory hurdle") + stem("Which pathway can allow phage therapy")),
    (1, stem("How long has fecal therapy") + stem("'Yellow soup' from old Chinese")),
    (1, stem("Which infection is a stool donor screened") + stem("Which intestinal parasites are stool")),
    (1, stem("A patient has had three recurrences") + stem("Why is fecal microbiota transplant an alternative")),
    (1, stem("Penicillin, vancomycin and azithromycin") + stem("Roughly how many antibiotics")),
]

# what the recording flagged: EACH = every set carries one of the group; ANY = the pair carries it
MUST_EACH = [
    # "they're very, very specific ... and then once there are no more of that particular strain of
    # bacteria, they die off" [22:11]
    stem("What property makes bacteriophages a possible option") + stem("Why could phage therapy be more efficient"),
    # fecal transplant for (recurrent) Clostridioides difficile: her study, "recurring C diff" [34:09]
    stem("A patient has had three recurrences") + stem("Why is fecal microbiota transplant an alternative"),
]
MUST_ANY = [
    stem("What property makes bacteriophages a possible option"),
    stem("Why could phage therapy be more efficient"),
    # "remember that the diagnosis might be time consuming too" [25:02]
    stem("Before phage therapy can be used") + stem("Which is a drawback of phage therapy"),
]

PCT = re.compile(r"\d+\s*(%|percent)", re.I)
YEAR = re.compile(r"\b(19|20)\d\d\b")
for q in POOL:
    key = q["opts"][q["c"]][0]
    assert not PCT.search(q["q"]) and not PCT.search(key), ("percentage keyed", q["q"])
    # "Don't worry about dates" [24:04]: no question keys or asks for a year
    assert not YEAR.search(key) and not YEAR.search(q["q"]), ("a year asked", q["q"])


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


def score(idx, set_no):
    qs = [POOL[i] for i in idx]
    top = Counter(q["topic"] for q in qs)
    s = 0.0
    for t, n in TARGET.items():
        d = abs(top.get(t, 0) - n / 2.0)
        s += max(0.0, d - 0.5) * 12
        if n >= 2 and top.get(t, 0) == 0:
            s += 40
    ios = Counter(q["io"] for q in qs)
    s += sum(60 for io in ALL_IOS if not ios.get(io))
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
            opens = o[1].lstrip().lower().startswith("correct")
            if (j == q["c"]) != opens:
                bad.append((i, "the 'Correct' opener must mark exactly the key"))
        wrong = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if len(set(wrong)) == 1:
            bad.append((i, "every wrong choice shares one explanation"))
        if not q["q"].rstrip().endswith("?"):
            bad.append((i, "stem does not ask a question"))
        if q.get("img"):
            if not os.path.exists(os.path.join(os.path.dirname(HERE), "Microbiology Exam 2", q["img"])):
                bad.append((i, "image file missing: " + q["img"]))
            if not q.get("alt") or not q.get("slide"):
                bad.append((i, "picture question without alt or slide caption"))
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
    print("pool gameable: %.0f%%   pool key uniquely longest: %.0f%%"
          % (gameable_pct(POOL), 100.0 * sum(map(uniquely_longest, POOL)) / len(POOL)))

    def total(ch):
        return score(ch[:30], 1) + score(ch[30:], 2) + must_any_penalty(ch)

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
        if random.random() < 0.5 and out:
            cand[k] = random.choice(out)
        else:
            j = random.randrange(60)
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
        print("   per topic:", ", ".join("%s %d" % (t, top.get(t, 0)) for t in TARGET))
        print("%s  n=%d  positions A/B/C/D %s  key uniquely longest %.0f%%  uniquely shortest %.0f%%"
              "  gameable %.0f%%  objectives %s  pictures: %d"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 100.0 * sum(map(uniquely_longest, s)) / len(s),
                 100.0 * sum(map(uniquely_shortest, s)) / len(s),
                 gameable_pct(s), dict(sorted(Counter(q["io"][0] for q in s).items())),
                 sum(1 for q in s if q.get("img"))))

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l11_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l11_sets.json")
