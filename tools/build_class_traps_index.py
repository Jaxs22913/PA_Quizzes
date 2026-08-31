#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emit the static index class-traps.html joins live Firestore counts against.

The counts have to be live -- a trap page built from a snapshot is out of date
the moment anyone answers -- but the question TEXT never changes between builds,
so shipping it as a file beats reading 1,765 documents in the browser.

Keyed by the same `<quizslug>__<qid>` the pages write, so the join is exact
rather than fuzzy.
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = re.compile(r'const (?:QUESTIONS|DATA|QUIZ_DATA)\s*=\s*(\[.*?\]);\s*\n', re.S)


def fnv36(t):
    h = 2166136261
    for ch in t:
        h ^= ord(ch); h = (h * 16777619) & 0xFFFFFFFF
    if h == 0: return "0"
    d = "0123456789abcdefghijklmnopqrstuvwxyz"; out = ""
    while h: out = d[h % 36] + out; h //= 36
    return out


def slug_for(rel):
    return re.sub(r'[^a-z0-9]+', '-', rel.lower().replace(".html", "")).strip('-')


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def quiz_title(fn):
    b = re.sub(r'\.html$', '', fn)
    b = re.sub(r'-(?:version|v|set)-?(\d+)$', r' (set \1)', b)
    b = b.replace("-", " ").strip()
    return b[:1].upper() + b[1:]


def main():
    out = {}
    files = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*", "*.html"))):
        src = open(path, encoding="utf8", errors="ignore").read()
        if "showClassPicks" not in src:
            continue                      # only pages that record picks can have traps
        m = BLOCK.search(src)
        if not m:
            continue
        try:
            qs = json.loads(m.group(1))
        except Exception:
            continue
        folder = os.path.basename(os.path.dirname(path))
        fn = os.path.basename(path)
        rel = folder + "/" + fn
        slug = slug_for(rel)
        files.append(rel)
        for q in qs:
            if not isinstance(q, dict) or "q" not in q or q.get("c") is None:
                continue
            qid = slug + "__" + (q.get("qid") or fnv36(q["q"]))
            out[qid] = {
                "q": strip(q["q"]),
                "o": [strip(o[0]) for o in q.get("opts", [])],
                "c": q["c"],
                "h": rel,
                "t": quiz_title(fn),
                "e": folder,
            }
    # One file per quiz, not one big one. As a single index this is 865 KB, which
    # is a lot to download for a page that only ever needs the handful of quizzes
    # the class has actually answered. The page reads the live counts first, sees
    # which quizzes appear, and fetches only those shards -- the same split that
    # took Group Study from 5.8 MB to 38 KB on load.
    outdir = os.path.join(ROOT, "class-traps")
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    for stale in glob.glob(os.path.join(outdir, "*.json")):
        os.remove(stale)
    shards = {}
    for qid, v in out.items():
        shards.setdefault(qid.split("__", 1)[0], {})[qid] = v
    manifest = {}
    for slug, items in shards.items():
        json.dump(items, open(os.path.join(outdir, slug + ".json"), "w", encoding="utf8"),
                  ensure_ascii=False, separators=(",", ":"))
        any_item = next(iter(items.values()))
        manifest[slug] = {"n": len(items), "t": any_item["t"], "e": any_item["e"],
                          "h": any_item["h"]}
    json.dump(manifest, open(os.path.join(ROOT, "class-traps-manifest.json"), "w",
                             encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
    tot = sum(os.path.getsize(f) for f in glob.glob(os.path.join(outdir, "*.json")))
    print("wrote %d shards (%d questions, %.0f KB total, largest %.0f KB) + a %.1f KB manifest"
          % (len(shards), len(out), tot / 1024.0,
             max(os.path.getsize(f) for f in glob.glob(os.path.join(outdir, "*.json"))) / 1024.0,
             os.path.getsize(os.path.join(ROOT, "class-traps-manifest.json")) / 1024.0))
    for e in sorted(set(v["e"] for v in out.values())):
        print("   %-44s %d" % (e, sum(1 for v in out.values() if v["e"] == e)))


if __name__ == "__main__":
    main()
