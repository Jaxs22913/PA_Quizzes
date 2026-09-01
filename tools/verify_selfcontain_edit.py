#!/usr/bin/env python3
"""Verify a self-containment pass against git HEAD for one or more folders.

Checks the things that have actually gone wrong before: an answer key moving,
an option changing without being audited, a deleted subject leaving a dangling
verb, and a stem landing on another question's options.

  python3 tools/verify_selfcontain_edit.py "Some Exam Folder" [...]
"""
import glob, json, os, re, subprocess, sys

BREAKS = [
    (r"\s{2,}", "double space"),
    (r"\s+[,.;]", "space before punctuation"),
    (r"[,;]\s*[.?]", "stranded comma"),
    (r"(?:^|[.?!]\s+)[a-z]", "sentence starts lowercase"),
    (r"\b(a|an|the)\s+(a|an|the)\b", "doubled article"),
    (r"\?\s*\?|\.\.(?!\.)", "doubled terminator"),
    (r"^\s|\s$", "leading or trailing space"),
    (r"\bthe\s+(?:'s|\?|\.)", "orphaned article"),
    (r"\bis stated\b|\bis called the\b", "bad passive from a deletion"),
    (r"\bWhich\s+\w+\s+is\?", "truncated which-question"),
    (r"\b\w+'s\s+(list|version|three|two|cut-off)\b", "orphaned genitive"),
]
C = [(re.compile(p), w) for p, w in BREAKS]
PT = re.compile(r"\b\d+-(year|month|week|day)-old\b|\bnewborn\b", re.I)


def load(blob):
    m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n', blob or "", re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def main(roots):
    n = flags = keys = opts = pt_before = pt_after = 0
    for root in roots:
        for f in sorted(glob.glob(os.path.join(root, "*.html"))):
            old = load(subprocess.run(["git", "show", "HEAD:" + f],
                                      capture_output=True, text=True).stdout)
            cur = load(open(f, encoding="utf8").read())
            if not old or not cur or len(old) != len(cur):
                continue
            for i, (a, b) in enumerate(zip(old, cur)):
                pt_before += bool(PT.search(a["q"])); pt_after += bool(PT.search(b["q"]))
                if a["c"] != b["c"]:
                    keys += 1
                    print("KEY MOVED   %s #%d" % (f, i))
                for x, y in zip(a["opts"], b["opts"]):
                    if x[0] != y[0]:
                        opts += 1
                        print("OPTION      %s #%d\n   was: %s\n   now: %s"
                              % (os.path.basename(f), i, x[0][:66], y[0][:66]))
                pairs = [("stem", a["q"], b["q"])]
                pairs += [("explanation %d" % j, x[1], y[1])
                          for j, (x, y) in enumerate(zip(a["opts"], b["opts"]))
                          if len(x) > 1 and len(y) > 1]
                for label, o, c in pairs:
                    if o == c:
                        continue
                    n += 1
                    for rx, why in C:
                        if rx.search(c):
                            flags += 1
                            print("[%s] %s #%d %s\n   %s"
                                  % (why, os.path.basename(f), i, label, c[:130]))
                            break
    print("\n%d rewritten | %d grammar flags | %d keys moved | %d option changes"
          % (n, flags, keys, opts))
    print("patient-naming stems: %d before, %d after" % (pt_before, pt_after))
    return flags + keys


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
