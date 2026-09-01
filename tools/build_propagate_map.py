#!/usr/bin/env python3
"""Build an old->new text map from a commit (or the working tree) that fixed
self-containment, so the same rewrites can be carried into files that were
missed -- master forms sampled from the same question pool, most often.

  python3 tools/build_propagate_map.py <out.json> <rev> [path ...]
  python3 tools/build_propagate_map.py <out.json> WORKING [path ...]

Only pairs whose OLD text actually cites a source are kept, so unrelated
edits in the same commit never propagate.
"""
import io, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX


def load(blob):
    m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n', blob or "", re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def show(rev, path):
    r = subprocess.run(["git", "show", "%s:%s" % (rev, path)],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def main():
    out, rev = sys.argv[1], sys.argv[2]
    paths = sys.argv[3:]
    if rev.endswith("..WORKING"):
        # Old text from a pre-cleanup revision, new text from the CURRENT tree.
        # Never take the new side from the cleanup commit itself: a later
        # commit often repairs it (the Pharmacology pass stranded verbs and
        # they were fixed afterwards), and a snapshot would carry the broken
        # intermediate forward.
        before, after = rev[:-len("..WORKING")], None
        changed = subprocess.run(["git", "ls-tree", "-r", "--name-only", before],
                                 capture_output=True, text=True).stdout.split("\n")
    elif rev == "WORKING":
        before, after = "HEAD", None
        changed = subprocess.run(["git", "diff", "--name-only"],
                                 capture_output=True, text=True).stdout.split("\n")
    else:
        before, after = rev + "^", rev
        changed = subprocess.run(["git", "show", "--name-only", "--pretty=format:", rev],
                                 capture_output=True, text=True).stdout.split("\n")
    changed = [c for c in changed if c.endswith(".html") and
               (not paths or any(c.startswith(p) for p in paths))]
    pairs = {}
    for f in changed:
        o = load(show(before, f))
        try:
            n = load(io.open(f, encoding="utf8").read()) if after is None else load(show(after, f))
        except FileNotFoundError:
            continue
        if not o or not n:
            continue
        # Pair the before/after questions by their OPTION SET, never by
        # position.  A commit that rebuilt a master reorders and replaces
        # questions at unchanged length, and zipping positionally then
        # harvests pairs that map one question's stem onto another's -- which
        # silently rewrites a question into a different one.
        idx = {}
        for b in n:
            idx.setdefault(frozenset(x[0] for x in b["opts"]), []).append(b)
        matched = []
        for a in o:
            k = frozenset(x[0] for x in a["opts"])
            if len(idx.get(k, [])) == 1:          # unambiguous match only
                matched.append((a, idx[k][0]))
        for a, b in matched:
            if a["q"] != b["q"] and RX.search(a["q"]):
                pairs[a["q"]] = b["q"]
            # Pair options by their TEXT, not position: answer-position
            # rotation reorders them, and zipping positionally then pairs one
            # option's explanation with another's -- turning a refutation into
            # "Correct. ...".
            byopt = {}
            for y in b["opts"]:
                byopt.setdefault(y[0], []).append(y)
            for x in a["opts"]:
                cand = byopt.get(x[0], [])
                if len(cand) != 1:
                    continue
                y = cand[0]
                if len(x) > 1 and len(y) > 1 and x[1] != y[1] and RX.search(x[1]):
                    pairs[x[1]] = y[1]
    json.dump(pairs, io.open(out, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print("%s: %d file(s) -> %d old->new pair(s) (paired by option set)"
          % (rev, len(changed), len(pairs)))


if __name__ == "__main__":
    main()
