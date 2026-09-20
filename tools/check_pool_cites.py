#!/usr/bin/env python3
"""Flag question pools whose text still cites the course.

WHY THIS EXISTS. On 2026-09-20 I re-rendered Pharmacology Lecture 2
(dermatology medications) to pick up a one-word stem fix. The render replaced
1,570 lines with 104 and reintroduced course references into a shipped quiz
that had been hand-cleaned during the 2026-08-31 self-contained pass.

The cause is a divergence nothing was watching: the SHIPPED HTML was cleaned by
hand, but the POOL it is generated from was not. So the pool and the page
disagree, and any re-render silently discards the cleanup. check_self_contained
reads the rendered pages, so it reports clean right up until the moment someone
regenerates one.

Run this BEFORE re-rendering any topic. A non-empty count for that topic's pool
means its shipped page is currently better than its source, and regenerating
will make it worse -- clean the pool first.

    python3 tools/check_pool_cites.py            # every pool, counts only
    python3 tools/check_pool_cites.py --detail   # with the offending text
"""
import glob, importlib.util, os, re, sys

# "in class" needs the negative lookahead: topical steroids are ranked by
# potency CLASS ("placed in class 1, superpotent"), which is not a citation.
CITES = re.compile(r"\b(the lecture|the deck|the slide|this course|"
                   r"in class(?!\s*\d)|the professor|the syllabus|the lecturer)\b", re.I)


def scan():
    found = {}
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           "*pool*.py"))):
        mod = os.path.basename(f)[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod, f)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        except Exception:
            continue
        hits = []
        for attr in dir(m):
            P = getattr(m, attr)
            if not (isinstance(P, list) and P and isinstance(P[0], dict) and "opts" in P[0]):
                continue
            for q in P:
                if CITES.search(q["q"]):
                    hits.append(("stem", q["q"]))
                for t, e in q["opts"]:
                    if CITES.search(t):
                        hits.append(("option", t))
                    if CITES.search(e):
                        hits.append(("explanation", e))
        if hits:
            found[mod] = hits
    return found


if __name__ == "__main__":
    detail = "--detail" in sys.argv
    found = scan()
    total = sum(len(v) for v in found.values())
    for mod in sorted(found, key=lambda k: -len(found[k])):
        print("%5d  %s" % (len(found[mod]), mod))
        if detail:
            for kind, text in found[mod][:6]:
                print("         %-12s %s" % (kind, text[:96]))
    print("\n%d reference(s) across %d pool(s); the shipped pages are cleaner than these."
          % (total, len(found)))
    sys.exit(0)
