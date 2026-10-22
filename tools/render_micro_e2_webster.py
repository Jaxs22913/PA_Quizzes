#!/usr/bin/env python3
"""Render the two Webster Review quizzes for Microbiology Exam 2 from their pools.

Built 2026-10-21 from Professor Webster's own Exam 2 review (16 October 2026, the tail of the Lecture 12
recording; page micro-exam-2-webster-review.html). Every question is new and written for one review item
(tools/micro_e2_webster_pool_l{7,10,12}.py): each of her 33 items gets one question in each set, the
two on different facts, and the Know-cold items she drilled hardest carry seven extra per set. Light-touch
material and the Lecture 10 organisms she excluded carry none.

Her review covered only the three lectures she taught (7, 10, 12); Dr. Fair's lectures are in the topic
quizzes and the master exams, and the intro says so.

Questions are ordered by lecture and then by review item, so the score breakdown lines up with the review
page's headings. Numeric option sets are sorted ascending (tools/_option_order.py) and keep the key where
the sort puts it; every other key is permuted per set onto balanced letters, no letter more than three in
a row (seeded).
"""
import importlib.util, io, os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
import _option_order as OO

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
LECS = (7, 10, 12)
PAGE_FIELDS = ("topic", "io", "q", "opts", "c", "cite")


def load(lec):
    p = os.path.join(HERE, "micro_e2_webster_pool_l%d.py" % lec)
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
    "<p>Built from Professor Webster&rsquo;s own Exam 2 review at the end of the Epidemiology lecture. "
    "Every question is new and written for one item of that review: each of her items gets one question "
    "in each set, the two on different facts, and the items she put to the class as questions "
    "(<em>know cold</em>) get extra ones. What she said not to memorize, and the organisms she said not "
    "to worry about, are left out. Every fact comes from her slides, cited under each answer.</p>"
    "<p>Questions run in her order: Disorders in Immunity, then the Gram-positive bacilli organism by "
    "organism, then Epidemiology, so the score breakdown matches the headings of the "
    "<a href=\"micro-exam-2-webster-review.html\">Webster review page</a>.</p>"
    "<p><b>Her review covered only her three lectures.</b> Dr. Fair&rsquo;s lectures (Diagnosing "
    "Infections, Cocci, Novel Antimicrobial Therapy, Miscellaneous Bacterial Agents) are not in these "
    "sets; they are in their own topic quizzes and the five master exams.</p>")
CHIPS = ["Disorders in Immunity", "Gram-Positive Bacilli", "Epidemiology"]

if __name__ == "__main__":
    pool = [q for lec in LECS for q in load(lec)]
    for n, form, fname in ((1, "A", "micro-exam-2-webster-review-quiz.html"),
                           (2, "B", "micro-exam-2-webster-review-quiz-version-2.html")):
        qs = sorted((q for q in pool if q["form"] == form),
                    key=lambda q: (LECS.index(q["lecture"]), item_key(q), q["tier"] != "cold"))
        qs = place([{f: q[f] for f in PAGE_FIELDS} for q in qs], seed=20261021 + n)
        html = render(
            title="Webster Review Quiz %d &mdash; Microbiology Exam 2" % n,
            h1="Webster Review &mdash; Exam 2",
            sub="Microbiology &middot; Exam 2 &middot; Lectures 7, 10 and 12 &middot; Set %d" % n,
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
