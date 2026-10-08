#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Give every Semester 2+ quiz question a permanent id, so editing a stem no longer
throws away its history.

    python3 tools/add_stable_qids.py            # add missing ids (run after any quiz render)
    python3 tools/add_stable_qids.py --check    # exit 1 if any in-scope question has no id

The problem. answer_picks (the class's response counts) is keyed
`<quizslug>__<hash of the stem>`, computed in the page at read time. That is stable
only while the stem is. Rewriting the Pharmacology stems orphaned their history
silently: 286 of 670 live documents stopped joining to any question, and those
questions restarted at zero with nothing to show it.

The fix (2026-08-31, widened 2026-10-08). Each question carries a `qid` and the
page's qidFor() prefers it.
  - A question that has no id yet gets the CURRENT hash, which equals what the page
    computes today, so nothing that has been recorded is reset.
  - render.py does not know the ids (about 100 build scripts call it), so a re-render
    drops them. This tool puts them back from the last COMMITTED version of the
    page: a question whose options and key are unchanged keeps its old id even when
    its stem was reworded. Run it after any render, before committing;
    check_all.py fails a folder whose questions have no id.

Scope: pages rendered by tools/quiz-template (they carry data-dark-kind="quiz", which
Semester 1 pages never do), minus the frozen Semester 1 folders as a second guard.
Only `qid` fields are added; the tool asserts every stem, option and key is unchanged.
"""
import os, re, json, glob, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))


def fnv36(t):
    """Mirror of qidFor() in the quiz template: FNV-1a over UTF-16 code units
    (JavaScript's charCodeAt), base 36."""
    h = 2166136261
    data = t.encode("utf-16-le")
    for i in range(0, len(data), 2):
        h ^= data[i] | (data[i + 1] << 8)
        h = (h * 16777619) & 0xFFFFFFFF
    if h == 0:
        return "0"
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = ""
    while h:
        out = digits[h % 36] + out
        h //= 36
    return out


BLOCK = re.compile(r'(const (?:QUESTIONS|DATA|QUIZ_DATA)\s*=\s*)(\[.*?\])(;\s*\n)', re.S)


def dump_like(qs, original):
    """Re-serialise in the page's existing layout (one line from render.py, or indented
    from the older generators), so the only change in the file is the new ids."""
    m = re.match(r"\[\s*\n( +)\S", original)
    if m:
        return json.dumps(qs, ensure_ascii=False, indent=len(m.group(1)))
    return json.dumps(qs, ensure_ascii=False)


def frozen_folders():
    try:
        import check_exam_standard as ces
        return set(getattr(ces, "FROZEN", ()) or ())
    except Exception:
        return set()


def in_scope(path, src, frozen):
    folder = os.path.basename(os.path.dirname(path))
    if any(folder == f or folder.startswith(f) for f in frozen):
        return False
    return 'data-dark-kind="quiz"' in src or "showClassPicks" in src


def match_key(q):
    """What survives a stem rewording: the option texts and which one is correct."""
    opts = [o[0] if isinstance(o, list) else o for o in q.get("opts", [])]
    c = q.get("c")
    right = opts[c] if isinstance(c, int) and 0 <= c < len(opts) else None
    return (right, tuple(sorted(opts)))


def committed_ids(path):
    """{match_key: qid} and {stem: qid} from the version of this page in git HEAD."""
    rel = os.path.relpath(path, ROOT)
    try:
        old = subprocess.run(["git", "show", "HEAD:" + rel], cwd=ROOT, capture_output=True, check=True).stdout.decode("utf8")
    except Exception:
        return {}, {}
    m = BLOCK.search(old)
    if not m:
        return {}, {}
    try:
        qs = json.loads(m.group(2))
    except Exception:
        return {}, {}
    by_key, by_stem, seen = {}, {}, set()
    for q in qs:
        qid = q.get("qid") or fnv36(q.get("q", ""))
        k = match_key(q)
        if k in seen:            # two questions share options+key: matching on them would be ambiguous
            by_key.pop(k, None)
        else:
            by_key[k] = qid; seen.add(k)
        by_stem[q.get("q", "")] = qid
    return by_key, by_stem


def main(argv):
    check = "--check" in argv
    frozen = frozen_folders()
    files = sorted(glob.glob(os.path.join(ROOT, "*", "*.html")))
    pages = total = added = already = carried = 0
    missing, unparsable = [], []
    for path in files:
        src = open(path, encoding="utf8", errors="ignore").read()
        if not in_scope(path, src, frozen):
            continue
        m = BLOCK.search(src)
        if not m:
            continue
        try:
            qs = json.loads(m.group(2))
        except Exception:
            unparsable.append(os.path.relpath(path, ROOT))
            continue
        pages += 1
        need = [q for q in qs if not q.get("qid")]
        total += len(qs); already += len(qs) - len(need)
        if not need:
            continue
        if check:
            missing.append((os.path.relpath(path, ROOT), len(need)))
            continue
        before = [(q.get("q"), q.get("c"), [o[0] for o in q.get("opts", [])]) for q in qs]
        by_key, by_stem = committed_ids(path)
        for q in need:
            qid = by_stem.get(q.get("q", ""))
            if qid is None:
                qid = by_key.get(match_key(q))
                if qid is not None and qid != fnv36(q["q"]):
                    carried += 1
            q["qid"] = qid or fnv36(q["q"])
        after = [(q.get("q"), q.get("c"), [o[0] for o in q.get("opts", [])]) for q in qs]
        assert before == after, "%s: adding an id changed a stem, option or key" % path
        out = src[:m.start(2)] + dump_like(qs, m.group(2)) + src[m.end(2):]
        open(path, "w", encoding="utf8").write(out)
        added += len(need)
        print("  %-70s +%d" % (os.path.relpath(path, ROOT), len(need)))
    if unparsable:
        print("\nnot plain JSON, left alone (%d): %s" % (len(unparsable), ", ".join(unparsable[:5])))
    if check:
        if missing:
            print("%d page(s) have questions with no permanent id (run tools/add_stable_qids.py):" % len(missing))
            for p, n in missing[:20]:
                print("  %s: %d" % (p, n))
            return 1
        print("all %d questions on %d Semester 2+ quiz pages carry a permanent id" % (total, pages))
        return 0
    print("\n%d questions on %d Semester 2+ quiz pages; %d given an id (%d carried over a reworded stem), %d already had one"
          % (total, pages, added, carried, already))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
