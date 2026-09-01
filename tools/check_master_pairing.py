#!/usr/bin/env python3
"""Catch a master-exam question whose stem no longer belongs to its options.

Master forms are sampled from the topic quizzes and then shuffled, so for any
master question whose stem also exists in a topic quiz, the OPTION SET must
match that quiz's version -- order will differ, membership must not.

This exists because a text-keyed propagation once rewrote a master's stem
while leaving the old options behind, producing a question that read fine and
was answering something else entirely.

  python3 tools/check_master_pairing.py ["Some Exam Folder" ...]

About a dozen site-wide hits are genuine paraphrases of the same answer that
no substring rule can equate ("releases acetylcholine and blocks cholinesterase"
vs "releases acetylcholine and inhibits cholinesterase, acting as a
depolarizing neuromuscular blocker").  Treat this as a canary: read new hits,
do not expect zero.
"""
import glob, json, os, re, sys


def norm(t):
    """Compare answers on their content, not their wording.

    A master often rewords an option it inherited ("Right colic (hepatic)
    flexure" -> "The right colic (hepatic) flexure").  That is not a desync,
    so strip case, leading articles and punctuation before comparing.
    """
    t = re.sub(r"[^a-z0-9 ]+", " ", (t or "").lower())
    t = re.sub(r"^(the|a|an|it|its)\b", " ", t)
    return " ".join(t.split())


STOP = {"that", "this", "with", "from", "then", "than", "them", "they", "into",
        "which", "when", "what", "also", "such", "some", "only", "both", "each",
        "does", "have", "been", "were", "will", "used", "using", "there"}


def toks(t):
    """Content words, cut to a 5-character prefix so "allergic"/"allergy" and
    "lactam"/"lactams" count as the same idea."""
    return {w[:5] for w in norm(t).split() if len(w) > 3 and w not in STOP}


def overlap(a, b):
    """True when the two answers say the same thing.

    Masters routinely carry a long-form option where the topic quiz carries a
    condensed one ("No beta-lactam cross-reactivity; safe in true allergy" vs
    "No cross-reactivity with beta-lactams, so it can be used in truly
    penicillin-allergic patients"). Both are the same answer, so compare on
    shared content words rather than on wording.
    """
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    if na in nb or nb in na:
        return True
    ta, tb = toks(a), toks(b)
    if not ta or not tb:
        return False
    return len(ta & tb) / min(len(ta), len(tb)) >= 0.6


def load(path):
    m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n',
                  open(path, encoding="utf8").read(), re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def check(roots):
    bad = ok = orig = 0
    for root in roots:
        topic = {}
        for f in glob.glob(os.path.join(root, "*.html")):
            n = os.path.basename(f).lower()
            if "master" in n or any(k in n for k in ("guide", "cram", "chart")):
                continue
            for q in load(f) or []:
                if isinstance(q, dict) and "opts" in q:
                    topic.setdefault(q["q"], set()).add(q["opts"][q["c"]][0])
        for f in sorted(glob.glob(os.path.join(root, "*master*.html"))):
            for i, q in enumerate(load(f) or []):
                if not isinstance(q, dict) or "opts" not in q:
                    continue
                if q["q"] not in topic:
                    orig += 1
                    continue
                if any(overlap(q["opts"][q["c"]][0], t) for t in topic[q["q"]]):
                    ok += 1
                else:
                    bad += 1
                    print("\nMISPAIRED  %s  #%d" % (f, i))
                    print("  stem:    %s" % q["q"][:110])
                    print("  keyed to: %s" % q["opts"][q["c"]][0][:100])
                    print("  quizzes key this stem to: %s"
                          % " / ".join(sorted(topic[q["q"]])[:2])[:150])
    print("\nmatched %d | master-original %d | MISPAIRED %d" % (ok, orig, bad))
    return bad


if __name__ == "__main__":
    roots = sys.argv[1:] or [d for d in glob.glob("*") if os.path.isdir(d)
                             and not d.startswith(".")]
    sys.exit(1 if check(roots) else 0)
