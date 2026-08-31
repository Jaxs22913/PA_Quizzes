#!/usr/bin/env python3
"""Apply hand-written self-containment rewrites to CMS quiz files.

Input: a JSON file  { "<path>": { "<qid>": {"q": "...", "e": {"<opt idx>": "..."}} } }
Only stems and explanations may change.  Option TEXT and the answer key are
asserted byte-identical, so class-pick history and every answer stay valid.
"""
import io, sys, os, json, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX as SRC


def load(path):
    s = io.open(path, encoding="utf8").read()
    m = re.search(r'(const QUESTIONS\s*=\s*)(\[.*?\])(;\s*\n)', s, re.S)
    if not m:
        raise SystemExit("no QUESTIONS block in %s" % path)
    return s, m, json.loads(m.group(2))


def apply_file(path, edits, report):
    s, m, qs = load(path)
    by_qid = {}
    for i, q in enumerate(qs):
        by_qid.setdefault("#%d" % i, []).append(q)     # positional fallback
        if q.get("qid"):
            by_qid.setdefault(str(q["qid"]), []).append(q)
    n = 0
    for qid, e in edits.items():
        hits = by_qid.get(qid)
        if not hits:
            raise SystemExit("%s: qid %s not found" % (path, qid))
        if len(hits) > 1:
            raise SystemExit("%s: qid %s is ambiguous (%d)" % (path, qid, len(hits)))
        q = hits[0]
        before_opts = [o[0] for o in q["opts"]]
        before_key = q["c"]
        for i, txt in (e.get("o") or {}).items():           # option TEXT: audited, reported
            i = int(i)
            before_opts[i] = txt
            q["opts"][i][0] = txt; n += 1
        if "q" in e:
            q["q"] = e["q"]; n += 1
        for i, txt in (e.get("e") or {}).items():
            i = int(i)
            if len(q["opts"][i]) < 2:
                raise SystemExit("%s: qid %s opt %d has no explanation" % (path, qid, i))
            q["opts"][i][1] = txt; n += 1
        assert [o[0] for o in q["opts"]] == before_opts, "option text changed"
        assert q["c"] == before_key, "answer key changed"
    out = s[:m.start(2)] + json.dumps(qs, ensure_ascii=False, indent=2) + s[m.end(2):]
    io.open(path, "w", encoding="utf8").write(out)
    left = sum(1 for q in qs if SRC.search(q["q"])) + \
           sum(1 for q in qs for o in q["opts"] if len(o) > 1 and SRC.search(o[1]))
    report.append((path, n, left))
    return n, left


def main():
    edits = json.load(io.open(sys.argv[1], encoding="utf8"))
    report, tot = [], 0
    for path, e in edits.items():
        n, left = apply_file(path, e, report)
        tot += n
    for path, n, left in report:
        flag = "" if left == 0 else "   <-- %d attribution(s) still present" % left
        print("  %-58s %3d edit(s)%s" % (path.split("/")[-1][:58], n, flag))
    print("%d edits across %d file(s)" % (tot, len(report)))


if __name__ == "__main__":
    main()
