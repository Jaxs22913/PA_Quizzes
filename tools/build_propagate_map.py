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
    if rev == "WORKING":
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
        n = load(io.open(f, encoding="utf8").read()) if after is None else load(show(after, f))
        if not o or not n or len(o) != len(n):
            continue
        for a, b in zip(o, n):
            if a["q"] != b["q"] and RX.search(a["q"]):
                pairs[a["q"]] = b["q"]
            for x, y in zip(a["opts"], b["opts"]):
                if len(x) > 1 and len(y) > 1 and x[1] != y[1] and RX.search(x[1]):
                    pairs[x[1]] = y[1]
                if x[0] != y[0] and RX.search(x[0]):
                    pairs[x[0]] = y[0]
    json.dump(pairs, io.open(out, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print("%s: %d file(s) -> %d old->new pair(s)" % (rev, len(changed), len(pairs)))


if __name__ == "__main__":
    main()
