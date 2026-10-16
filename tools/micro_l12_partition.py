#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 12 pool into 2 x 30.

Epidemiology (Dr. Webster, 16 October 2026; the deck's file name and the calendar row name Dr. Webster,
the title slide names no lecturer). One pool, tools/micro_l12_pool.py, written from the 76-slide deck.

The syllabus gives TEN numbered objectives and every set carries all ten. The topic field follows the
objectives (one topic per objective), so TARGET is the per-objective weight.

TOPIC WEIGHTS FROM THE RECORDING (16 October 2026: parts 1-3, about 74 minutes, are the lecture; part 4 is
her review for Exam 2, and only its closing minute, on this lecture, is used). Minutes on each objective (both transcripts): history and genomic epidemiology ~10, descriptive vs analytic with Snow ~9,
surveillance ~10, applications (Legionnaires', policy, social, environment, occupational) ~10, epidemic
terms, curves, R0 and herd immunity ~8, association and causation ~7, morbidity and mortality ~6, data
sources ~2.5, reportable diseases ~2.5, definition and uses ~3 (the recording starts after the opening
slides). Her closing list (part 4, 19:38-20:26) names: descriptive vs analytic, the history and its people,
the kinds of surveillance, the measures of morbidity and mortality, association and causation with Hill's
criteria, endemic/epidemic/pandemic/sporadic/herd immunity, and epidemiology as the evidence for policy.
Scaled to 60, split evenly across the two sets; MUST_EACH carries every item of that list into each set.

Four options. Length bias by selection; answer position by ROTATION (numeric option sets would be put back
in ascending order by tools/_option_order.py; this pool has none). Carries the house 60-character
explanation guard and the "Correct" opener contract that check_answer_key_consistency.py reads. Picture
questions go to SET 2 only: a quiz holding any picture question is dropped from Group Study by
build_group_quizzes.py, so Set 1 stays text-only (the Lecture 9 rule).
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l12_pool import POOL
from _option_order import order_options

random.seed(20261016)
NOPT = 4
N_IMG = 3          # picture questions in Set 2 (Set 1 has none): epidemic curves, flagged in the recording

# MINUTES SPOKEN per objective, scaled to 60 and nudged by her closing list (see the docstring).
TARGET = {
    "Definition & uses": 4,             # objective 2, slides 4-8 (~3 min; recording starts late)
    "History": 7,                       # objective 3, slides 9-12 and 69; "the people who are important"
    "Descriptive vs analytic": 8,       # objective 1, slides 31-42 and 70; "you need to know the basic components"
    "Data sources": 2,                  # objective 4, slide 18 (~2.5 min)
    "Surveillance": 7,                  # objective 5, slides 14-17, 19-20 (slide 25's list: not to memorize)
    "Reportable diseases": 3,           # objective 6, slides 21-22 (slide 23's list: "absolutely not")
    "Morbidity & mortality": 7,         # objective 7, slides 26-29 and 59; "know the difference" (incidence/prevalence)
    "Association & causation": 8,       # objective 8, slides 43-53; scenario association vs causation
    "Epidemic terms & herd immunity": 7, # objective 9, slides 54-60; curves "you should be able to identify"
    "Applications": 7,                  # objective 10, slides 61-68 and 71-76; evidence for policy
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert ids, "stem not found: " + p
    return ids


# near-twins that give each other away (one explanation states the other's answer): at most N per set
CLUSTERS = [
    (1, stem("Among the five W's of epidemiology, what does") + stem("Among the five W's of epidemiology, which one")),
    (2, stem("An epidemiologist describes who gets") + stem("Which use of epidemiological training develops")
        + stem("Evaluating vaccine and clinical trials")),
    (1, stem("Taken from its Greek roots") + stem("Epidemiology is described as a bridge")),
    (1, stem("Who first attempted to explain disease") + stem("Which 17th-century figure")),
    (1, stem("Who is called the father of modern vital") + stem("Who is called the father of field")),
    (1, stem("What is genomic epidemiology") + stem("Pathogens from cases in two different cities")),
    (1, stem("Which branch of epidemiology examines how") + stem("Which study design is typical of descriptive")
        + stem("Researchers compare past exposures")),
    (1, stem("Which three elements form the basic triad") + stem("Which three phenomena are assessed")),
    (1, stem("In the host-agent-environment triad, tobacco") + stem("In the host-agent-environment triad, which of these")),
    (2, stem("What is a map marking where") + stem("In John Snow's investigation of a London cholera")
        + stem("In John Snow's analytic study")),
    (1, stem("Water is collected from local streams") + stem("Air-quality ratings collected by sensors")),
    (2, stem("During a foodborne illness outbreak") + stem("Water is collected from local streams")
        + stem("A physician notifies the health department") + stem("Cigarette sales records")
        + stem("Air-quality ratings collected by sensors")),
    (1, stem("Which critical characteristic of surveillance allows") + stem("Which critical characteristic of surveillance gives")
        + stem("Why does timeliness matter")),
    (1, stem("Which type of surveillance uses staff") + stem("Which type of surveillance is the most common")),
    (1, stem("A prearranged group of providers") + stem("A surveillance system counts cases of diarrhea")),

    (1, stem("Which notifiable disease is reported by telephone") + stem("Which notifiable disease is reported as a total")
        + stem("Where is cancer reported")),
    (1, stem("What makes a disease reportable") + stem("Diseases are made notifiable because")),
    (1, stem("What does morbidity refer to") + stem("Morbidity in a population is measured")),
    (2, stem("Which measure counts only the new cases") + stem("A county counts residents newly diagnosed")
        + stem("A survey asks every adult")),
    (1, stem("Which mortality rate is used to compare") + stem("A health department reports the number of deaths")),
    (1, stem("How is the case fatality rate calculated") + stem("As testing of mild cases expands")),
    (2, stem("Rather than the cause of disease") + stem("In public health, interventions are most often")
        + stem("What does causation imply")),
    (2, stem("Which of Hill's criteria requires that exposure") + stem("Which of Hill's criteria is a dose-response")
        + stem("Three studies each find") + stem("Findings repeated in multiple studies")
        + stem("A relative risk that is either") + stem("Which of Hill's criteria asks that")
        + stem("An exposure leads to a single")),
    (1, stem("Which of Hill's criteria is a dose-response") + stem("Three studies each find")),
    (2, stem("Which term describes a disease found at chronically") + stem("Which term describes a disease that occurs at irregular")
        + stem("A county usually sees a few cases") + stem("What is a pandemic")),
    (1, stem("What is herd immunity") + stem("Besides vaccination, what else")),
    (1, stem("Guests at one banquet") + stem("This epidemic curve shows hepatitis A")),
    (1, stem("An infection spreads from person to person") + stem("This epidemic curve shows measles")),
    (1, stem("A single survey finds") + stem("What does causation imply")),
    (1, stem("Across many studies in different populations") + stem("Three studies each find")),
    (1, stem("Policy development rests on values") + stem("Epidemiological studies can bring about")),
    (1, stem("What is the first step in investigating") + stem("In an outbreak investigation, which step comes right after")),
    (2, stem("In the investigation of the 1976 Legionnaires'") + stem("Why did the health department's response")
        + stem("How was the bacterium behind")),
    (1, stem("In 1994, what change") + stem("Which measure was part of the population approach")),
    (2, stem("Social and behavioral epidemiology looks") + stem("A study compares illness among residents")
        + stem("Monitoring how often workers")),
]

# what the recording flags (L11 shape): EACH = every set carries one of the group; ANY = the pair carries it.
# Quotes are from the 16 October 2026 recording (part, m:ss); every one is in both transcripts.
MUST_EACH = [
    # "you need to know the basic components of descriptive epidemiology versus analytic" (2, 6:51)
    stem("Which three elements form the basic triad") + stem("Which three phenomena are assessed"),
    stem("In the person-place-time triad") + stem("In the host-agent-environment triad"),
    # "the history and the people who are important in history" (4, 19:44)
    stem("Who first attempted to explain disease") + stem("Which 17th-century figure")
        + stem("Who is called the father of modern vital") + stem("Who is called the father of field"),
    # "You need to know genomic epidemiology." (3, 24:46)
    stem("What is genomic epidemiology") + stem("Pathogens from cases in two different cities"),
    # "the different kinds of surveillances" (4, 19:52): two types in each set (the clusters cap each pair at one)
    stem("Which type of surveillance uses staff") + stem("Which type of surveillance is the most common"),
    stem("A prearranged group of providers") + stem("A surveillance system counts cases of diarrhea"),
    # "You should know the difference between incidence and prevalence." (1, 30:33)
    stem("Which measure counts only the new cases") + stem("A county counts residents newly diagnosed")
        + stem("A survey asks every adult"),
    stem("A new therapy keeps people") + stem("For a chronic disease such as osteoarthritis"),
    # association vs causation from a scenario (3, 11:10) and Hill's criteria (4, 19:52)
    stem("A single survey finds") + stem("Across many studies in different populations"),
    stem("Which of Hill's criteria is a dose-response") + stem("Three studies each find")
        + stem("A relative risk that is either") + stem("Across many studies in different populations"),
    # endemic, epidemic, pandemic, sporadic, herd immunity (4, 19:52)
    stem("Which term describes a disease found at chronically") + stem("Which term describes a disease that occurs at irregular")
        + stem("A county usually sees a few cases") + stem("What is a pandemic"),
    stem("What is herd immunity") + stem("Besides vaccination, what else"),
    # epidemic curves "you should be able to identify" (3, 13:47): a single-source and a spreading pattern
    stem("Guests at one banquet") + stem("This epidemic curve shows hepatitis A") + stem("This epidemic curve follows diarrheal"),
    stem("An infection spreads from person to person") + stem("An outbreak begins when food handlers")
        + stem("This epidemic curve shows measles"),
    # "epidemiology gives us the evidence for policy development" (4, 19:52)
    stem("Policy development rests on values") + stem("Epidemiological studies can bring about"),
]
MUST_ANY = []
# AFTER THE BLIND REVIEW (16 October 2026) the shipped sets were patched, not re-partitioned: two items were
# dropped from the pool and replaced in place through tools/micro_e2_sync_sets.py MOVED (Set 1: the pyramid
# base item -> the strength-of-association item; Set 2: the Shigella curve -> the diarrheal-illness curve).
# Re-running this script would reshuffle reviewed sets; use micro_e2_sync_sets.py for pool edits instead.

PCT = re.compile(r"\d+\s*(%|percent)", re.I)
YEAR = re.compile(r"\b(19|20)\d\d\b")
for q in POOL:
    key = q["opts"][q["c"]][0]
    assert not PCT.search(q["q"]) and not PCT.search(key), ("percentage keyed", q["q"])
    # no year is ever the key (a stem may name a decade or year for context)
    assert not YEAR.search(key), ("a year keyed", q["q"])


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
    return [order_options(q) for q in qs]


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
                 gameable_pct(s), dict(sorted(Counter(q["io"].split(" ")[0] for q in s).items())),
                 sum(1 for q in s if q.get("img"))))

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l12_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l12_sets.json")
