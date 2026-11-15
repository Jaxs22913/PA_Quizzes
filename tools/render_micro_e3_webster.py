#!/usr/bin/env python3
"""Render the two Webster Review master exams for Microbiology Exam 3 from their pools.

Built 2026-11-14 from Professor Webster's own Exam 3 review (13 November 2026, the tail of the Lecture 18
recording; page micro-exam-3-webster-review.html). Every question is new and written for one review item
(tools/micro_e3_webster_pool_l{14,17,18}.py): each of her items gets one question in each exam, the two on
different facts, and the Know-cold items carry extras (the four Escherichia coli types get four per exam).
Light-touch material carries none. Split per exam: 20 Lecture 14 / 20 Lecture 17 / 20 Lecture 18 (equal scheduled
hours). The parasites carry picture-identification items ("if I give you a picture, be able to recognize it").

Her review covered only the three lectures she taught (14, 17, 18); Dr. Fair's lectures are in the topic quizzes,
and the intro says so.

Questions are ordered by lecture and then by review item. Numeric option sets are sorted ascending
(tools/_option_order.py) and keep the key where the sort puts it; every other key is permuted per exam onto
balanced letters (15 each), no letter four in a row (seeded). The two exams are a true partition of the pool.
"""
import importlib.util, io, os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
import _option_order as OO

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 3")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
LECS = (14, 17, 18)
PAGE_FIELDS = ("topic", "io", "q", "opts", "c", "cite", "img", "alt")


def load(lec):
    p = os.path.join(HERE, "micro_e3_webster_pool_l%d.py" % lec)
    spec = importlib.util.spec_from_file_location("wpool%d" % lec, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.POOL


def item_key(q):
    return tuple(int(x) for x in q["item"].split("."))


def place(qs, seed):
    """Sort numeric sets; spread the other keys evenly over A-D, never four of one letter in a row."""
    qs = [OO.order_options(q) for q in qs]
    fixed = {i for i, q in enumerate(qs) if OO.option_values([o[0] for o in q["opts"]]) is not None}
    rng = random.Random(seed)
    for _ in range(5000):
        counts = Counter(qs[i]["c"] for i in fixed)
        free = [i for i in range(len(qs)) if i not in fixed]
        want = []
        for L in range(4):
            want += [L] * max(0, -(-len(qs) // 4) - counts[L])
        while len(want) < len(free):                 # numeric sets crowded one letter past its share
            want.append(min(range(4), key=lambda L: counts[L] + want.count(L)))
        rng.shuffle(want)
        letters = {i: qs[i]["c"] for i in fixed}
        letters.update(zip(free, want[:len(free)]))
        seq = [letters[i] for i in range(len(qs))]
        if all(not (seq[i] == seq[i + 1] == seq[i + 2] == seq[i + 3]) for i in range(len(seq) - 3)):
            break
    out = []
    for i, q in enumerate(qs):
        if i in fixed:
            out.append(q)
            continue
        opts = list(q["opts"])
        key = opts.pop(q["c"])
        rest = opts[:]
        rng.shuffle(rest)
        rest.insert(letters[i], key)
        out.append(dict(q, opts=rest, c=letters[i]))
    return out


INTRO = (
    "<p>Built from Professor Webster&rsquo;s own Exam 3 review at the end of the DNA Viruses lecture. "
    "Every question is new and written for one item of that review: each of her items gets a question in each "
    "exam, the two exams on different facts, and the items she put to the class as questions (<em>know cold</em>) "
    "get extra ones &mdash; the four <em>Escherichia coli</em> types most of all. She said a parasite picture may "
    "have to be identified, so the parasites include picture questions. What she said not to worry about is left "
    "out. Every fact comes from her slides, cited under each answer.</p>"
    "<p>Questions run in her order: the Gram-negative bacilli, the parasites, then the DNA viruses, 20 each, so the "
    "score breakdown matches the headings of the "
    "<a href=\"micro-exam-3-webster-review.html\">Webster review page</a>.</p>"
    "<p><b>Her review covered only her three lectures.</b> Dr. Fair&rsquo;s lectures (Fungi, Food Safety, RNA "
    "Viruses) are not in these exams; they are in their own topic quizzes.</p>")
CHIPS = ["Gram-Negative Bacilli", "Parasites", "DNA Viruses"]

if __name__ == "__main__":
    pool = [q for lec in LECS for q in load(lec)]
    stems = [q["q"] for q in pool]
    assert len(stems) == len(set(stems)), "duplicate stem in the pool"
    imgs = [q["img"] for q in pool if q.get("img")]
    assert len(imgs) == len(set(imgs)), "a picture is used twice"
    for n, form, fname in ((1, "A", "micro-exam-3-webster-review-master-exam-1.html"),
                           (2, "B", "micro-exam-3-webster-review-master-exam-2.html")):
        sel = [q for q in pool if q["form"] == form]
        for lec in LECS:
            k = sum(q["lecture"] == lec for q in sel)
            assert k == 20, "form %s lecture %d has %d questions" % (form, lec, k)
        qs = sorted(sel, key=lambda q: (LECS.index(q["lecture"]), item_key(q), q["tier"] != "cold"))
        qs = place([{f: q[f] for f in PAGE_FIELDS if f in q} for q in qs], seed=20261114 + n)
        html = render(
            title="Webster Review Master Exam %d &mdash; Microbiology Exam 3" % n,
            h1="Webster Review Master Exam %d &mdash; Exam 3" % n,
            sub="Microbiology &middot; Exam 3 &middot; Lectures 14, 17 and 18 &middot; Exam %d of 2" % n,
            pill="%d questions" % len(qs),
            chips=CHIPS,
            intro=INTRO,
            questions=qs,
            already_converted=True,
            **PALETTE)
        p = os.path.join(OUT, fname)
        io.open(p, "w", encoding="utf-8").write(html)
        print("wrote %s  %d questions  keys %s" % (fname, len(qs),
              dict(sorted(Counter("ABCD"[q["c"]] for q in qs).items()))))
    assert {q["q"] for q in pool if q["form"] == "A"}.isdisjoint({q["q"] for q in pool if q["form"] == "B"})
    print("partition: %d total == %d unique stems" % (len(pool), len(set(stems))))
