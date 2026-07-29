#!/usr/bin/env python3
"""Remove iCloud Drive conflict copies from the repo.

This repo lives under ~/Documents, which has iCloud Desktop & Documents sync
enabled. When a build rewrites hundreds of files at once, iCloud loses the race
and keeps both versions, leaving copies named "<name> 2.js", "<name> 3.html".

They have bitten twice: 121 chunk files in one commit, and 179 files that would
have shipped 145 junk pages in another. Nothing here legitimately has a space in
its filename, so they are easy to spot -- but a copy is only deleted once it is
confirmed byte-identical to a surviving original.

    python3 tools/clean_sync_dupes.py          # report only
    python3 tools/clean_sync_dupes.py --apply  # delete the verified copies
"""
import hashlib, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules"}
DUPE = re.compile(r"^(?P<base>.+) (?P<n>\d+)(?P<ext>\.[A-Za-z0-9]+)$")


def digest(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def scan():
    identical, differing, orphaned = [], [], []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            m = DUPE.match(name)
            if not m:
                continue
            copy = os.path.join(root, name)
            original = os.path.join(root, m.group("base") + m.group("ext"))
            if not os.path.exists(original):
                orphaned.append(copy)
            elif digest(copy) == digest(original):
                identical.append(copy)
            else:
                differing.append(copy)
    return identical, differing, orphaned


def main(apply=False):
    identical, differing, orphaned = scan()
    rel = lambda p: os.path.relpath(p, REPO)

    print(f"identical to their original : {len(identical)}")
    print(f"DIFFER from their original  : {len(differing)}")
    print(f"no original present         : {len(orphaned)}")

    for p in differing:
        print("  differs, left alone:", rel(p))
    for p in orphaned:
        print("  no original, left alone:", rel(p))

    if not identical:
        print("nothing to delete")
        return 0
    if not apply:
        for p in identical[:8]:
            print("  would delete:", rel(p))
        if len(identical) > 8:
            print(f"  ... and {len(identical) - 8} more")
        print("\nre-run with --apply to delete them")
        return 0

    for p in identical:
        os.remove(p)
    print(f"deleted {len(identical)} verified duplicate(s)")
    if differing or orphaned:
        print("left the ones above in place -- look at those by hand")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
