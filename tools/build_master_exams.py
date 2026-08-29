#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 5 x 60 cumulative Master Exams for an exam block.

Per [[master_exam_sizing]]: five SEPARATE 60-question forms per exam, held back
until the whole block's content is in -- a "cumulative" exam assembled while
lectures are still arriving is not cumulative, it is a snapshot that silently
omits whatever had not been written yet. CMS Exam 1's last lecture (9,
Pre-malignant and Malignant Cutaneous Lesions) landed 24 August, which is what
unblocks this.

Questions are REUSED VERBATIM from the topic quizzes rather than re-authored, so
a master exam cannot drift from the material it is meant to summarise, and any
later correction to a topic quiz can be propagated by re-running this.

Design decisions worth stating:

  STRATIFIED, NOT RANDOM. Sampling 60 from a 1,020-question pool at random gives
  a form that over-weights whichever lecture happens to have the most questions.
  Each form instead draws proportionally from every lecture, so all five are
  genuinely cumulative and comparable to each other.

  NO QUESTION APPEARS IN TWO FORMS. With 1,020 available and 300 needed there is
  no reason to repeat, and a student working through all five should meet 300
  distinct questions rather than the same ones reshuffled.

  ANSWER POSITIONS REBALANCED per form, because the source quizzes were each
  balanced independently and concatenating them does not preserve that.

    python3 tools/build_master_exams.py "Clinical Medicine and Surgery I Exam 1"
    python3 tools/build_master_exams.py --list        # show what it would use
"""
import os, re, sys, json, random, hashlib
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

try:
    import json5
except ImportError:
    sys.exit("missing dependency: json5  (a silent parser failure once deleted "
             "five Group Study quizzes, so this refuses to run without it)")

FORMS = ["A", "B", "C", "D", "E"]
PER_FORM = 60

SKIP = ("guide", "cram", "chart", "osce", "master")


def lecture_of(filename):
    """Group a quiz file with its siblings: the objective and vignette sets of
    one lecture are one lecture, not four."""
    n = filename.replace(".html", "")
    for suf in ("-version-2", "-vignettes", "-quiz"):
        n = n.replace(suf, "")
    return n.strip("-")


def harvest(folder):
    d = os.path.join(ROOT, folder)
    per_lecture = defaultdict(list)
    seen = set()
    for f in sorted(os.listdir(d)):
        if not f.endswith(".html") or any(k in f for k in SKIP):
            continue
        s = open(os.path.join(d, f), encoding="utf-8").read()
        m = re.search(r"const QUESTIONS\s*=\s*(\[.*?\]);", s, re.S)
        if not m:
            continue
        for q in json5.loads(m.group(1)):
            key = hashlib.sha1(q["q"].strip().lower().encode()).hexdigest()
            if key in seen:                      # same stem in two files
                continue
            seen.add(key)
            per_lecture[lecture_of(f)].append(q)
    return per_lecture


def allocate(per_lecture, n_forms, per_form):
    """How many questions each lecture contributes to each form.

    Proportional to the lecture's share of the pool, with the rounding remainder
    handed to the largest lectures so the total lands exactly on per_form.
    """
    total = sum(len(v) for v in per_lecture.values())
    quota, exact = {}, {}
    for lec, qs in per_lecture.items():
        exact[lec] = per_form * len(qs) / total
        quota[lec] = int(exact[lec])
    short = per_form - sum(quota.values())
    for lec in sorted(exact, key=lambda l: -(exact[l] - quota[l]))[:short]:
        quota[lec] += 1
    # never ask a lecture for more than it can supply across all forms
    for lec, qs in per_lecture.items():
        cap = len(qs) // n_forms
        if quota[lec] > cap:
            quota[lec] = cap
    return quota


def rebalance_positions(form, rng):
    """Spread correct answers across A/B/C/D.

    The source quizzes were each balanced on their own; concatenating slices of
    them does not preserve that, and 'the answer is usually B' is exactly the
    tell this project already fixed once.
    """
    targets = [i % 4 for i in range(len(form))]
    rng.shuffle(targets)
    for q, t in zip(form, targets):
        k = (t - q["c"]) % 4
        if k:
            q["opts"] = q["opts"][-k:] + q["opts"][:-k]
        q["c"] = t
    return form


def build(folder, seed=20260824):
    per_lecture = harvest(folder)
    assert per_lecture, "no topic quizzes found in %s" % folder
    rng = random.Random(seed)
    pools = {lec: qs[:] for lec, qs in per_lecture.items()}
    for qs in pools.values():
        rng.shuffle(qs)
    quota = allocate(per_lecture, len(FORMS), PER_FORM)

    forms, cursor = [], defaultdict(int)
    for _ in FORMS:
        form = []
        for lec, n in sorted(quota.items()):
            take = pools[lec][cursor[lec]:cursor[lec] + n]
            cursor[lec] += len(take)
            form.extend(json.loads(json.dumps(take)))       # deep copy per form
        # top up from the largest remaining pool if rounding left us short
        while len(form) < PER_FORM:
            lec = max(pools, key=lambda l: len(pools[l]) - cursor[l])
            if cursor[lec] >= len(pools[lec]):
                break
            form.append(json.loads(json.dumps(pools[lec][cursor[lec]])))
            cursor[lec] += 1
        rng.shuffle(form)
        forms.append(rebalance_positions(form, rng))
    return per_lecture, quota, forms


def main():
    # The folder is read independently of the flags. Previously "--list" forced
    # the CMS folder no matter what was passed, so a dry run on any other block
    # silently previewed the wrong exam -- which is exactly the case --list
    # exists for.
    positional = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = positional[0] if positional else "Clinical Medicine and Surgery I Exam 1"
    per_lecture, quota, forms = build(folder)

    print("pool: %d unique questions across %d lectures"
          % (sum(len(v) for v in per_lecture.values()), len(per_lecture)))
    for lec in sorted(per_lecture):
        print("   %-42s %3d available   %2d per form" % (lec, len(per_lecture[lec]), quota[lec]))

    stems = [q["q"] for f in forms for q in f]
    print("\n%d forms x %d = %d questions; unique stems: %d"
          % (len(forms), PER_FORM, len(stems), len(set(stems))))
    assert len(set(stems)) == len(stems), "a question appears in more than one form"
    for name, f in zip(FORMS, forms):
        pos = Counter(q["c"] for q in f)
        assert len(f) == PER_FORM, "form %s has %d questions" % (name, len(f))
        print("   Form %s: %d questions, answer positions A/B/C/D %d/%d/%d/%d"
              % (name, len(f), pos[0], pos[1], pos[2], pos[3]))

    if "--list" in sys.argv:
        return
    out = os.path.join(ROOT, folder, "master-exams.json")
    json.dump({n: f for n, f in zip(FORMS, forms)}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False)
    print("\nwrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
