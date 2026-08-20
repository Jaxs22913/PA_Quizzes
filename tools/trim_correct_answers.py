#!/usr/bin/env python3
"""Move the tail of an over-long CORRECT answer into its own explanation.

WHY THIS EXISTS. Measured across nine pools on 2026-08-20: writing a question
naturally produces a correct answer that carries every qualifying clause while
the distractors stay to one. That is the length tell, and it lands at 20-80%
gameable depending on how compare-and-contrast the content is. The fix that
costs least is to TRIM the answer, not to pad three distractors -- one edit
instead of three, and nothing is lost because the trimmed clause moves into the
explanation the student reads immediately after answering.

Doing that by hand took 25 edits on one pool and 42 on another. This does the
mechanical part: split the correct option at its last major boundary, keep the
head as the option, and prepend the tail to the explanation.

IT IS NOT AUTOMATIC. It writes a proposal file for review and only applies what
you approve, because a bad split reads as a bad sentence and the student sees
the option before they see anything else.

  python3 tools/trim_correct_answers.py cms_l6_pool_d POOL_D            # propose
  python3 tools/trim_correct_answers.py cms_l6_pool_d POOL_D --apply    # write

Guarantees, asserted every run:
  * only the option at index q["c"] is ever touched
  * the trimmed option is never empty and never shorter than 24 characters
  * the resulting option stops being the uniquely-longest by a gameable margin,
    or the question is left alone and reported
  * no question ends up with two identical options
  * every correct explanation still starts with "Correct"
"""
import importlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
MIN_HEAD = 24

# Split points, most preferred first. A semicolon is the cleanest break; " and "
# is the loosest and is only used when nothing better exists.
SPLITS = ["; ", " — ", " — ", ", with ", ", and ", ", which ", ", so ", ", "]


def gameable(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rl, _) = lens[0], lens[1]
    return ti == q["c"] and (tl - rl) >= MARGIN_CHARS and tl >= rl * (1 + MARGIN_FRAC)


def runner_up(q):
    return sorted((len(o[0]) for i, o in enumerate(q["opts"]) if i != q["c"]), reverse=True)[0]


# A stem that asks two things ("What is X, and how is it treated?") FORCES a
# compound answer, and no amount of trimming fixes that -- cut the second clause
# and the option stops answering the question that was asked. Measured on CMS
# Lecture 6 pool D, 2026-08-20: 23 of 29 were gameable and the splitter's output
# was mostly unusable ("or there is ophthalmic", "For atypical, disseminated")
# precisely because the stems were two-part. The fix for those is at the STEM,
# not the option -- ask one thing, or give the distractors the same compound
# shape. So refuse them here rather than emit prose that dangles.
TWO_PART = re.compile(r",\s*(and|or)\s+(what|how|when|where|which|why|who)\b", re.I)


def propose(q):
    """Return (head, tail) or None if no acceptable split exists."""
    if TWO_PART.search(q["q"]):
        return None
    text = q["opts"][q["c"]][0]
    target = runner_up(q)
    best = None
    for sep in SPLITS:
        idx = text.rfind(sep)
        while idx > 0:
            head, tail = text[:idx], text[idx + len(sep):]
            if len(head) >= MIN_HEAD and tail:
                # good enough if the head no longer leads by a gameable margin
                if not ((len(head) - target) >= MARGIN_CHARS
                        and len(head) >= target * (1 + MARGIN_FRAC)):
                    return head.rstrip(" ,;—"), tail
                if best is None or len(head) < len(best[0]):
                    best = (head.rstrip(" ,;—"), tail)
            idx = text.rfind(sep, 0, idx)
    return best


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    modname, poolname = sys.argv[1], sys.argv[2]
    apply = "--apply" in sys.argv
    mod = importlib.import_module(modname)
    pool = getattr(mod, poolname)
    path = os.path.join(HERE, modname + ".py")
    src = open(path, encoding="utf-8").read()

    todo, skipped = [], []
    for q in pool:
        if not gameable(q):
            continue
        p = propose(q)
        if not p:
            why = "TWO-PART STEM" if TWO_PART.search(q["q"]) else "no clean split"
            skipped.append((why, q["q"][:66]))
            continue
        head, tail = p
        expl = q["opts"][q["c"]][1]
        assert expl.startswith("Correct"), "correct explanation must start with 'Correct'"
        # graft the tail on after the "Correct — ..." opener
        newexpl = expl.rstrip()
        if not newexpl.endswith("."):
            newexpl += "."
        tail_s = tail[0].upper() + tail[1:]
        if not tail_s.endswith("."):
            tail_s += "."
        newexpl = newexpl + " " + tail_s
        others = [o[0] for i, o in enumerate(q["opts"]) if i != q["c"]]
        assert head not in others, "trim would duplicate another option"
        todo.append((q, head, newexpl))

    print("%s.%s: %d questions, %d gameable, %d trimmable, %d unsplittable"
          % (modname, poolname, len(pool), sum(gameable(x) for x in pool), len(todo), len(skipped)))
    for why, name in skipped:
        print("   SKIP (%s): %s" % (why, name))
    for q, head, newexpl in todo:
        print("\n  Q: %s" % q["q"][:78])
        print("  -  %s" % q["opts"][q["c"]][0])
        print("  +  %s" % head)

    if not apply:
        print("\n(run again with --apply to write)")
        return

    n = 0
    for q, head, newexpl in todo:
        old_opt, old_expl = q["opts"][q["c"]][0], q["opts"][q["c"]][1]
        import json as _j
        a, b = _j.dumps(old_opt, ensure_ascii=False), _j.dumps(old_expl, ensure_ascii=False)
        # the source writes these as "..." literals; match on the raw text
        assert src.count(old_opt) >= 1, "option text not found in source: %r" % old_opt[:50]
        assert src.count(old_expl) >= 1, "explanation not found in source"
        src = src.replace(old_opt, head, 1)
        src = src.replace(old_expl, newexpl, 1)
        n += 1
    open(path, "w", encoding="utf-8").write(src)
    print("\napplied %d trims to %s" % (n, path))


if __name__ == "__main__":
    main()
